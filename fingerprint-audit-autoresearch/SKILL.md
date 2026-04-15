---
name: fingerprint-audit-autoresearch
description: Autonomous research loop that keeps the ai-fingerprint-audit skill calibrated and current. Quarterly scheduled research dispatch, continuous benchmarking against a labeled corpus, and incident-driven re-baselining. Every proposed rubric change goes through a precision/recall gate before it merges. Owner: Thomas (Line/Copy Editor) runs the loop; Margaret approves rubric changes; Board approves any change that moves a ship/no-ship threshold.
---

# Fingerprint Audit Autoresearch

AI detection is a moving target. Pangram updates. Claude/GPT/Gemini output patterns shift. BookTok readers catalog new tells monthly. The `ai-fingerprint-audit` rubric degrades silently if we don't maintain it.

This skill defines the autonomous research + benchmarking loop that keeps the audit current, with a hard gate: **no rubric change merges without passing a precision/recall test on a labeled corpus.**

See references:
- `benchmark-corpus.md` — how to build and maintain the labeled dataset
- `research-loop.md` — the quarterly research dispatch prompt + merge workflow
- `incident-replay.md` — what to do when a real-world flag happens
- `paperclip-trigger.md` — scheduling the loop via Paperclip's CronCreate

## Three-layer loop

### Layer 1 — Quarterly research dispatch (scheduled, cadence-driven)

**Cadence:** every 90 days, or sooner if a trigger fires (see Layer 3).

**Process:**
1. Paperclip scheduled trigger fires a research subagent (see `paperclip-trigger.md`).
2. Subagent pulls in:
   - New arXiv papers on AI-text detection published in the last 90 days
   - Pangram/GPTZero/Binoculars transparency reports + changelog
   - r/selfpublish, r/ChatGPT, BookTok community ban-list updates
   - New community-curated lists (GitHub: humanizer, anti-ai-slop-writing, etc.)
   - Any cozy-fantasy-specific incidents posted publicly in the last quarter
3. Subagent outputs a **proposed rubric diff** — which banned words to add, which thresholds to adjust, which new dimensions to test.
4. Thomas runs the proposed diff through the benchmark (Layer 2).
5. If benchmark passes: Margaret approves; skill updates; git commit + reimport.
6. If benchmark fails: diff archived, rationale noted, no change.

### Layer 2 — Continuous benchmarking (gate on every change)

Every proposed rubric change — from quarterly research OR incident replay OR ad-hoc — must pass a precision/recall test before merging.

**The labeled corpus:**
- ~50 chapters from 5 human cozy fantasy comps (positive class — "human")
- ~50 chapters of Claude/GPT output on cozy fantasy outlines (negative class — "AI-default")
- ~20 chapters of Claude/GPT output passed through a Daniel-equivalent humanization pass (middle class — "AI-drafted-human-edited" — this is our actual shipping category)
- Updated quarterly (swap 10% of samples)

See `benchmark-corpus.md` for construction details.

**The gate:**
| Metric | Current baseline | Required for merge |
|---|---|---|
| Precision on "human" class (don't reject real human prose) | 95%+ | No regression |
| Recall on "AI-default" class (catch raw AI output) | 90%+ | No regression |
| Precision on "AI-drafted-human-edited" (don't reject legitimate studio output) | 90%+ | No regression |
| Recall on "AI-drafted-human-edited" (catch studio output that slipped without humanization) | 80%+ | No regression |

**If all four are non-regressive AND at least one dimension improves:** merge.
**If any regress:** reject. Diff is archived with rationale.

### Layer 3 — Incident-driven updates

Triggers (any one fires a re-baseline):
- A shipped book gets publicly flagged by Pangram/GPTZero screenshot on BookTok/Reddit/Twitter
- An agent kicks back chapters with PASS rubric scores that Thomas/Margaret recognize as AI-slick on read
- A new detector launches or an existing one has a material update
- Pangram v2 / GPTZero v2 / new SOTA detector appears in benchmarks

**Process:**
1. Log incident in studio compliance note with full Pangram/GPTZero scores + screenshot + reader-community response.
2. Replay the flagged chapter through the current rubric — did it PASS or WATCH?
3. If PASS: run `incident-replay.md` to propose what rubric change would have caught it.
4. If WATCH: the rubric worked — the issue is we shipped despite a watch signal. Tighten ship rules, not rubric.
5. Run the proposed rubric change through Layer 2 benchmark.
6. On pass: merge urgently (within 48 hours of incident).
7. Re-run the calibration sprint within 14 days of incident.

## What gets researched each quarter

Subagent prompt for the quarterly dispatch (see `research-loop.md` for full version):

- New AI-detection papers (arXiv: search "AI-generated text detection" + "stylometry" + "burstiness" past 90 days)
- Pangram transparency reports and benchmark updates
- GPTZero component changes + new detector competitors launching
- r/selfpublish AI-tells threads from the last 90 days
- BookTok / r/romancebooks / r/fantasy specific AI-callout screenshots (catalog what patterns readers flagged)
- GitHub repositories: humanizer, anti-ai-slop, fingerprint-detection — any new forks or major updates
- Kindlepreneur / Jane Friedman / ALLi blog posts on AI detection in fiction
- Any newly published cozy fantasy that got publicly flagged

Output format: proposed diff to `banned-vocabulary.md` and `SKILL.md` with rationale per change, ready to pass through Layer 2 benchmark.

## The gate is hard

**No rubric change merges without benchmark pass.** Not even if the research looks obviously correct. Not even if Margaret wants to merge.

Reason: detector research is noisy. New papers claim 99% accuracy that falls apart in practice. Community ban-lists sometimes add words that aren't actually AI-tells. Without the benchmark gate, the rubric drifts and false-rejects Daniel's work or false-passes AI-default chapters.

## Exception: typography/unicode tells

Typography-level tells (unicode ellipsis, curly quotes inconsistency, stray arrow glyphs) can merge without benchmark — they're deterministic and have zero false-positive risk. Add via regex update directly.

## Owner chain

- **Thomas (Line/Copy Editor):** runs the loop, executes the benchmarks, surfaces diffs.
- **Margaret (Editor-in-Chief):** approves research dispatch, approves rubric diffs that pass benchmark.
- **Board (Nicole):** approves any change that moves a ship/no-ship threshold OR adds a new automated-FAIL dimension OR changes the calibration corpus.
- **CEO (Jason):** gets the quarterly research report as an issue comment; budget approval for any paid tool added.

## Cost

- Pangram API for benchmark re-runs: ~$1/quarter
- GPTZero API for benchmark re-runs: included in monthly flat
- Research subagent dispatch: a few dollars in LLM tokens per quarter
- **Total marginal cost:** <$10/quarter
- **Marginal value:** the rubric stays calibrated, which prevents the $500+ cost of a single BookTok-flagged book (refunds, reputation, rewrite cycle)

## Scheduling — Paperclip cron

See `paperclip-trigger.md` for the CronCreate payload. Quarterly schedule with auto-dispatch to Thomas. Add an additional trigger for incident-replay on demand (manually invoked by Board/Margaret).

## Output artifacts per cycle

1. **Research report** — quarterly issue on Paperclip, assigned to Margaret, summarizing what changed in the AI-detection landscape.
2. **Proposed rubric diff** — concrete git-style diff against current skill files.
3. **Benchmark results** — precision/recall numbers on the labeled corpus pre- and post-change.
4. **Merge or reject decision** — documented with rationale on the research issue.
5. **New calibration thresholds** if material changes warranted re-baseline.

All stored in the studio vault at `00-Meta/Fingerprint-Research-Log/YYYY-QN/`.

## Hard rules

- No change to the FAIL threshold without Board sign-off.
- No change to the labeled corpus without documented rationale.
- Every merged change traceable to a research source (paper, transparency report, community post).
- No "feels better" edits. The benchmark is the judge.
- Research subagent's rationale always archived — future quarters reference past decisions to avoid flip-flopping.

## When to retire this skill

When reliable AI/human-prose classification becomes a solved problem (accurate detectors + no false positives on literary voice), this skill becomes over-engineered. Not currently the case; watch for it in future.

## When to expand

- Additional genres beyond cozy fantasy (each genre has its own prose rhythm; separate baseline)
- Non-English publishing (different fingerprints entirely; needs new benchmark corpus)
- Audiobook production (ACX-specific tells around AI narration — separate audit)

Until then, cozy fantasy only.
