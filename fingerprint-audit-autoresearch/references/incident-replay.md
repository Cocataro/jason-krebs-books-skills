# Incident Replay

When a shipped book gets publicly flagged (BookTok / Pangram screenshot / reader callout), the rubric either failed or was followed despite a WATCH signal. Replay the incident to learn from it.

## Trigger conditions

Any of the following triggers an incident replay:

1. **Pangram screenshot** of a paragraph from a shipped Jason Krebs book posted publicly
2. **GPTZero screenshot** (same)
3. **Reader-quoted pattern** — a post identifying specific prose tells in a shipped book
4. **Review citing "AI"** on Amazon/Goodreads with >3 engagement signals (votes, comments)
5. **Influencer BookTok post** (>10k followers) amplifying a flagging
6. **Refund-rate spike** >2× baseline in the week following a launch

Run the recovery playbook (in `ai-fingerprint-audit/references/recovery-playbook.md`) in parallel. Incident replay is the learning phase; recovery is the public-response phase.

## Replay process

### Step 1: Isolate the flagged content
- Pull the exact paragraph/chapter/text the reader flagged
- If it's a Pangram screenshot, extract the exact chunk they scored
- Save to `/Users/nicoleopcl/Desktop/Vaults/Jason Krebs Books/00-Meta/Fingerprint-Incidents/YYYY-MM-DD-[brief-name]/`

### Step 2: Replay the current rubric against the flagged content

Run:
1. In-house lint script — what D2–D9 scores did it produce?
2. Pangram — what was the original score at ship time (from the audit log)?
3. Pangram — re-score now (has Pangram updated?)
4. GPTZero — same two scores
5. Compare to the reader's screenshot Pangram score — do they match?

### Step 3: Classify the incident

| Classification | Meaning | Action |
|---|---|---|
| **True rubric failure** | Content PASSed audit at ship; would still PASS today; detector agrees with reader | Rubric has a gap. Research what pattern the reader flagged; propose new D-dimension or banned-word addition. |
| **Watch-ignored** | Content flagged WATCH at ship; was shipped anyway | Process failure, not rubric failure. Tighten ship rules: WATCH now = Margaret mandatory review before ship. |
| **Detector drift** | Original audit PASS; current Pangram FAIL; model updated | Detector is stricter now. Re-baseline thresholds. Consider running full corpus benchmark. |
| **False positive** | Audit PASS; detector PASS on re-run; reader is wrong | Document the incident; respond publicly via recovery playbook; no rubric change. |
| **Reader knowledge update** | Reader identified a pattern we don't measure | Research the specific pattern; propose new D-dimension. |
| **Prompt-leak / artifact** | Literal "Certainly! Here's..." or AI-prompt string in text | Process failure, not rubric failure. Tighten self-edit + lint pass to catch AI-prompt artifacts. Add regex to lint for common prompt patterns ("Certainly!", "Here is", "I'll rewrite", "Let me") as P0 FAIL. |

### Step 4: Propose the fix

Based on classification, produce a proposal:

**True rubric failure proposal template:**
```
Incident: [date + reader name/handle + platform]
Flagged content: [excerpt, 1-2 sentences]
Reader's claim: [what they said]
Pangram at-ship: [score]
Pangram current: [score]
GPTZero at-ship: [verdict]
GPTZero current: [verdict]
Our rubric classification: [True rubric failure]

Pattern analysis: [what specific tell did the reader identify?]

Proposed rubric change:
- [Add new banned phrase / new D-dimension / new regex check]
- Measurement: [how to detect automatically]
- Threshold: [PASS/WATCH/FAIL bands]

Benchmark plan:
- Run proposed change against class A/B/C corpus
- Expected: class B catches improve, class A preserved

Re-calibration needed: [yes/no]
```

### Step 5: Benchmark the fix

Run the proposed change through `benchmark-corpus.md`. Same gate as quarterly research: no regression on precision_A, recall_A, recall_B, recall_C.

### Step 6: Merge if benchmark passes

Urgent-track merge:
- Margaret approves
- Board reviews if threshold change
- Git commit + skill reimport within 48 hours of incident
- Changelog entry referencing the incident

### Step 7: Re-audit shipped titles

After the fix merges:
- Re-run the rubric on every currently-shipped Jason Krebs book
- Flag any chapter now failing the updated rubric
- Propose silent version-bump rewrite OR overt re-release per Board decision

### Step 8: Add incident to the permanent corpus

The flagged chapter/paragraph becomes a permanent class-B or class-C sample in the benchmark corpus. Never rotated out. Future rubric changes must continue to catch this specific pattern.

## Example replay (hypothetical)

**Scenario:** 2026-08-14, a reader on r/fantasy pastes 3 paragraphs from *The Crossroads Inn Book 2* into Pangram and posts screenshot showing 84% AI-probability. Comment thread gains 400 upvotes in 6 hours.

**Replay:**
1. Extract the 3 paragraphs.
2. Original audit score (from ai_audit_log): 12% document, max paragraph 19% — PASSed.
3. Pangram re-score today: 34% document, max paragraph 68%.
4. GPTZero: Mixed verdict (was Human at ship).
5. **Classification: Detector drift.** Pangram updated in July; our threshold didn't.

**Proposed fix:**
- Tighten D1 PASS band from <5% to <4% document.
- Re-calibrate all thresholds against current Pangram.
- Re-run corpus benchmark.
- If benchmark passes: merge, re-audit backlist, quiet rewrite of any now-failing chapters.

**Public response** (recovery playbook):
- Template A: "I take the concern seriously. The detector used has updated since this book shipped. I'm reviewing the flagged paragraphs and pushing an update."
- Execute rewrite within 7 days; re-release.

## Multiple incidents per quarter

If >1 incident fires in the same quarter:
- Pattern signal — something is systematically failing
- Pause new releases if 3+ incidents fire
- Accelerate re-calibration to immediate (don't wait for quarterly)
- Board review: is the humanization process broken, or is the rubric? Pause to diagnose.

## What NOT to do

- Don't blame Daniel. Incidents are process/rubric failures, not author failures.
- Don't silently tighten thresholds without benchmark. You'll cause false-reject cycles on Daniel's work.
- Don't delete the flagged content. Unpublish if needed, but preserve the artifact for the incident corpus.
- Don't argue with the reader publicly about detector accuracy. Follow the recovery playbook for public response; handle the rubric learning internally.

## Incident documentation

Every incident gets a permanent entry:

```
/Users/nicoleopcl/Desktop/Vaults/Jason Krebs Books/00-Meta/Fingerprint-Incidents/YYYY-MM-DD-short-name/
├── incident-report.md        # what happened, classification, fix
├── flagged-content.md        # the exact text flagged
├── pangram-scores.json       # at-ship and current
├── gptzero-scores.json       # at-ship and current
├── reader-post-screenshot.png # (if available + public)
├── proposed-diff.md          # proposed rubric change
├── benchmark-results.json    # before/after corpus scores
├── merge-decision.md         # merged? when? by whom?
└── recovery-response.md      # what public response was issued
```

Makes future incidents faster to classify (similar patterns reference past incidents).

## Learning loop

Every N incidents:
- Meta-review: what classifications dominate? (true rubric failure vs detector drift vs process)
- If mostly detector drift: too-loose thresholds; recalibrate aggressively
- If mostly rubric failure: coverage gap; invest in new detection dimensions
- If mostly process: humanization pass discipline is slipping; training intervention with Daniel

After every 3 incidents in a quarter, Board review mandatory. After every 5 incidents in a year, full pipeline audit.
