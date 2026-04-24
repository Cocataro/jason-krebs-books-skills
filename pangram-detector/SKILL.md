---
name: pangram-detector
description: Run Pangram AI-detection (https://text.api.pangram.com/v3) on a manuscript chapter and produce a structured pass/fail report. Enforced ship-ready gate per Board SOP — no chapter ships without a clean Pangram pass. Thomas (line/copy editor) runs it as the QA step of his pass; Eleanor verifies; Margaret will not ship-ready without the verdict artifact. Daniel does NOT run this on his own output — that would be self-scoring. If Pangram flags passages beyond line/copy scope, Thomas kicks back to Daniel for targeted humanization.
---

# Pangram Detector — per-chapter ship-ready gate

Board SOP (2026-04-23): every chapter runs through Pangram AI-detection as part of the line/copy pass. Thomas owns the run. Eleanor verifies. Margaret will not mark ship-ready without a clean pass. Daniel does NOT run Pangram on his own drafts — QA runs the audit, not the author.

The goal is not "fool a detector." The goal is: ship a book that reads as genuinely-authored fiction to a top-tier public detector. If Pangram flags a passage, that passage needs craft work — not obfuscation.

## When to run

1. **First thing in Thomas's line/copy pass.** After Daniel applies Eleanor's dev-edit revisions to a chapter, Thomas starts his pass by running Pangram. The verdict informs the line/copy edits he makes.
2. **Retroactively** on Ch 1 and Ch 2 to establish the baseline and clear ship-ready retroactively.
3. **After any humanization pass.** Re-run until clean.

## Prerequisites

- `PANGRAM_API_KEY` env var populated from Paperclip secret store.
- Python 3.9+ with `requests` available in the runtime.
- Chapter file exists in `crossroads-manuscripts` repo at a canonical path (`Drafts/Book-{N}/Ch-{NN}-{Title-In-Hyphens}.md`).

## How to run

```
python skills/pangram-detector/scripts/run-pangram.py \
  --input crossroads-manuscripts/Drafts/Book-1/Ch-03-The-Blue-Fire.md \
  --output crossroads-manuscripts/Detector-Runs/Ch-03-$(date +%Y%m%d-%H%M).json
```

The script:
1. Reads the markdown file and strips YAML frontmatter.
2. Sends the body to `POST https://text.api.pangram.com/v3` with `x-api-key` auth.
3. Writes the raw Pangram JSON plus a derived `verdict` block to the output path.
4. Prints a one-line summary to stdout (`PASS` / `FAIL` / `WARN`) and exits with status 0/1/2.

If Pangram returns 401, rotate the key via Board. If 500 or timeout, retry after 60s; if still failing, flag in the issue comment and escalate.

## Thresholds (canonical pass/fail logic)

See `references/thresholds.md` for full spec. Summary:

| Verdict | Criteria |
|---|---|
| **PASS** | `prediction_short == "Human"` AND `fraction_ai < 0.10` AND no window labeled `AI-Generated` with `confidence: High` |
| **WARN** | `prediction_short == "AI-Assisted"` AND `fraction_ai < 0.10` AND no `AI-Generated/High` window — ship-ready allowed if Eleanor signs off on the AI-Assisted score |
| **FAIL** | `prediction_short in ["AI", "Mixed"]` OR `fraction_ai >= 0.10` OR any window labeled `AI-Generated` with `confidence: High` |

**A FAIL verdict blocks ship-ready.** Daniel humanizes flagged passages and re-runs until PASS or WARN. A WARN verdict requires Eleanor's explicit sign-off on the specific segments before Margaret can ship-ready.

## Humanization workflow when Pangram fails

Thomas decides at the flagged-window level whether the fix is line/copy-scope or author-scope:

- **Line/copy-scope (Thomas fixes in place):** sentence-rhythm, em-dash overuse, adverb pruning, breaking back-to-back tricolons, roughening smooth transitions with fragments or voice tics.
- **Author-scope (kick back to Daniel):** whole-paragraph abstraction problems, narrative-voice misalignment, passages where the specific fix requires knowing the character's interiority choices. Thomas posts a focused revision request on the chapter's draft issue, lists the Pangram-flagged windows + suggested craft lens, and waits for Daniel to push a revision before re-running Pangram.

Default to Thomas-scope unless the flagged content has structural problems.

Applying a fix:
1. **Rewrite in POV voice** — if the passage is narratively flat, rewrite through the POV character's sensory + temperamental lens (Briar: grudge-specific observation, spare, intrusive verbs).
2. **Roughen rhythm** — add a fragment, break a tricolon, vary sentence openers, drop a too-clean transition.
3. **Add sensory anchor** — specific concrete noun replaces the generic abstraction ("the fire" → "the fire that wanted to be looked at").
4. **Kill smoothness** — read aloud. Passage reads as too-smooth? Break it.

See `references/humanization-patterns.md` for craft-pattern catalog tuned to Briar-POV cozy fantasy.

## Output artifact

Every run writes a JSON file to `crossroads-manuscripts/Detector-Runs/Ch-{NN}-{YYYYMMDD-HHMM}.json`. Commit it. History of detector runs is how we learn what flags — do not delete.

File schema:

```json
{
  "chapter_file": "Drafts/Book-1/Ch-03-The-Blue-Fire.md",
  "chapter_sha": "ffe182c4...",
  "run_at": "2026-04-24T10:00:00Z",
  "pangram_raw": { ... full Pangram response ... },
  "verdict": {
    "status": "PASS|WARN|FAIL",
    "reasons": ["fraction_ai=0.03", "prediction=Human", "no high-confidence AI windows"],
    "flagged_windows": []
  },
  "ship_ready_gate": "CLEARED|BLOCKED"
}
```

## Eleanor's verification step

Eleanor reads the JSON artifact + the chapter source. Her job is to confirm:

- Thomas didn't skip passages (compare word count of Pangram input vs chapter body).
- Edits applied to flagged passages address the craft issue, not cosmetic score-chasing.
- WARN-level scores reflect real AI-assisted content, not misfire on voice.
- If Thomas kicked back to Daniel for author-scope humanization, Daniel's revision actually addresses the flagged windows rather than just touching up adjacent prose.

Eleanor posts a short verdict comment on the chapter's issue: `Pangram verdict ratified: PASS/WARN/FAIL. [notes]`.

## Margaret's ship-ready gate

Margaret will NOT mark any chapter ship-ready without:

1. Pangram JSON artifact committed to `Detector-Runs/` in the repo
2. Thomas's verdict comment posted with the JSON referenced
3. Eleanor's verification comment ratifying the verdict
4. Status in the verdict is PASS (or WARN with Eleanor explicit sign-off)

If any of the four are missing, ship-ready is blocked. No exceptions for launch deadlines.

## What this skill does NOT do

- Does not automatically humanize flagged passages. Craft work is Thomas (line/copy-scope) or Daniel (author-scope).
- Does not replace Thomas's fingerprint-audit / style-sheet work. Pangram is the external-detector layer; the fingerprint audit is the internal-quality layer. Both run in Thomas's pass.
- Does not substitute for Eleanor's dev-edit letter. Different pass, different purpose.
- Does not run on pre-revision drafts. Pangram gates Daniel's revision-complete handoff to Thomas — not the initial draft.
- Does not run on Daniel's agent. Daniel does not self-audit his own prose. QA runs the gate.
