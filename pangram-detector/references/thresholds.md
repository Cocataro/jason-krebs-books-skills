# Pangram thresholds + verdict logic

Canonical pass/fail spec for Jason Krebs Books ship-ready gate. Applied by the `run-pangram.py` script; ratified by Eleanor; enforced by Margaret.

## Pangram response fields we use

From `POST /v3` response:

- `prediction_short` — one of `"Human"`, `"AI-Assisted"`, `"AI"`, `"Mixed"`
- `fraction_ai` — float 0.0–1.0, proportion of the text classified AI-generated
- `fraction_ai_assisted` — float 0.0–1.0, proportion AI-assisted
- `fraction_human` — float 0.0–1.0, proportion human
- `windows[]` — per-segment classifications with `label`, `ai_assistance_score`, `confidence`, `start_index`, `end_index`

## Verdict rules

### PASS (ship-ready cleared)

All of:
- `prediction_short == "Human"`
- `fraction_ai < 0.10`
- No window has `label == "AI-Generated"` with `confidence == "High"`

Rationale: a clean pass means the detector agrees this is human-written at the chapter level, with no high-confidence AI passages. Ship-ready cleared on the Pangram axis.

### WARN (requires Eleanor sign-off)

All of:
- `prediction_short == "AI-Assisted"` (not Human, not Mixed, not AI)
- `fraction_ai < 0.10`
- No window has `label == "AI-Generated"` with `confidence == "High"`

Rationale: AI-Assisted is technically accurate for any ghostwritten-with-AI fiction — but it's still a signal a public detector would emit. Shipping WARN-verdict chapters means the book is labeled "AI-Assisted" by any reader running the same detector. Eleanor must explicitly judge whether that's acceptable for this chapter, or whether the assisted segments can be humanized to get to PASS.

### FAIL (blocks ship-ready)

Any of:
- `prediction_short in ["AI", "Mixed"]`
- `fraction_ai >= 0.10`
- Any window has `label == "AI-Generated"` with `confidence == "High"`

Rationale: any one of these says the chapter has meaningful AI-generated content a detector will catch. Ship-ready blocked. Daniel humanizes flagged windows, commits, re-runs, repeats until PASS or WARN.

## Why these numbers

- **10% `fraction_ai` ceiling**: realistic upper bound for fiction that reads as human. Above 10%, detectors converge on "AI" verdict and reader-facing detector tools (GPTZero, Originality, Copyleaks) align.
- **"High" confidence cutoff on windows**: Pangram's confidence is calibrated; Medium/Low are noise-level for short segments. High-confidence AI windows are concrete craft failures.
- **Prediction-label tiering**: `"Human"` > `"AI-Assisted"` > `"Mixed"` > `"AI"`. The cliff between AI-Assisted and Mixed is the publish/don't-publish line for a pen-persona human-authored book.

## What we do NOT threshold on

- `fraction_ai_assisted` — too noisy, real editing triggers this signal. Not a pass/fail lever.
- `fraction_human` — derived; doesn't add info over the others.
- Low/Medium confidence windows — pattern-noise; doesn't warrant craft response.
- `num_*_segments` counts — superseded by fraction metrics.

## Iteration protocol when FAIL

1. Open the verdict JSON. Extract all windows with `label: "AI-Generated"` (any confidence).
2. For each flagged window, apply humanization per `references/humanization-patterns.md`.
3. Commit humanized chapter on the same branch (`daniel/ch-NN-draft1`) with a commit message like `Ch NN humanization pass N: address Pangram-flagged windows [list start/end indices]`.
4. Re-run `run-pangram.py`. New JSON artifact with new timestamp goes to `Detector-Runs/`.
5. Repeat until PASS or WARN.

If three humanization cycles don't move a chapter to PASS/WARN, escalate to Board: Eleanor + Daniel collaborate on dev-edit-scale rewrites of flagged sections, not cosmetic humanization.

## Retroactive application

Ch 1 + Ch 2 were ship-readied before this SOP existed. Retroactive run:

1. Run Pangram on the current ship-ready file.
2. If PASS: ratify ship-ready, proceed.
3. If WARN: Eleanor reviews, decides.
4. If FAIL: ship-ready is revoked. Chapter returns to revision cycle. Monday lead-magnet PDF may slip.

This is the correct tradeoff — we will not ship a detector-failing chapter to meet a launch window.
