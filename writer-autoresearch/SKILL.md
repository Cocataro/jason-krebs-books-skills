---
name: writer-autoresearch
description: Continuous-improvement experiment loop for the Series Writer's drafting process. Systematically tunes prompt templates, humanization passes, tic deployment, voice-anchor depth, and model/effort settings to maximize rubric pass-rate AND voice-preservation simultaneously. Experiments run on sandbox outlines only (never ship-bound chapters). Only proven improvements merge into Daniel's production config. Owner: Daniel runs experiments; Margaret approves config merges; Board approves changes that affect voice-anchor or model selection.
---

# Writer Autoresearch

The AI-fingerprint audit catches bad prose at the gate. This skill optimizes Daniel's drafting process so less bad prose shows up at the gate in the first place.

Karpathy-style autoresearch for fiction. Modify one variable, generate a sandbox chapter, measure, keep improvements, revert failures. Never stops until interrupted.

See references:
- `experiment-design.md` — structuring a single experiment
- `voice-preservation-metric.md` — stylometric distance from the canonical Book 1 voice anchor
- `sandbox-outlines.md` — what to experiment on
- `variable-catalog.md` — what to tune, ranked by expected impact
- `multi-objective-gate.md` — balancing rubric pass-rate vs voice-preservation vs dev-edit acceptance

## The core principle

**Two metrics improve together or the variant reverts.**

- **Rubric pass-rate** — how well output passes the `ai-fingerprint-audit` rubric (D1–D10)
- **Voice-preservation** — stylometric distance from the canonical Book 1 voice anchor

Optimizing only for rubric produces chapters that game detectors but read badly. Optimizing only for voice produces chapters that hold tone but get AI-flagged. Both must hold.

## The loop

```
1. Current baseline:   (rubric_score, voice_score, dev_edit_score)
2. Propose variant:    change ONE variable (prompt template, humanization technique, tic strategy, etc.)
3. Run variant:        generate 3 sandbox chapters on throwaway outlines
4. Measure:            rubric + voice + (if samples allow) dev-edit-spot-check
5. Compare:            did variant improve ≥1 metric WITHOUT regressing any other?
6. Decision gate:
   - Both/all metrics improve → adopt variant as new baseline
   - Any metric regresses → revert
   - Ambiguous → run 3 more chapters; re-evaluate
7. Log to experiment journal
8. Loop
```

## Sandbox-only rule

**No experiment runs on ship-bound Book 1 chapters.** Ever. Experiments run on:
- Book 2–6 warm-up chapters (Daniel drafts a scene he'd write for a later book — if it lands, he can use it; if it doesn't, it's discarded)
- Synthetic cozy fantasy outlines (see `sandbox-outlines.md`)
- Fan-fiction-style warm-up pieces Daniel writes for personal craft practice

Results from ship-bound chapters inform the loop (log them), but the loop's primary experiments use sandbox outlines to avoid polluting the production draft.

## One variable at a time

Change ONE variable per experiment. Not two. Not three.

If you change "prompt template" + "voice anchor depth" simultaneously and scores improve, you don't know which change caused the improvement. Controls matter.

Variables ranked by expected impact (tune in this order — see `variable-catalog.md`):
1. **Voice-anchor depth** — 500 words vs 2,000 vs 5,000 before each drafting session
2. **Humanization-pass technique** — which specific transformations applied
3. **Prompt template** — how the scene brief is framed
4. **Scene-composition depth** — how detailed the brief before drafting
5. **Model + effort** — Opus 4.6 high vs Opus medium vs Sonnet high
6. **Tic deployment strategy** — frequency, placement, variety
7. **Read-aloud cadence** — how often Daniel does a rhythm-check pass

## Minimum sample size per experiment

**3 sandbox chapters per variant.** Single-chapter results are noise. Three chapters per variant, compared against three baseline chapters on comparable outlines.

If results are within 5% on both metrics → inconclusive, re-run with 3 more chapters.
If results diverge >10% on either metric → clear signal, decide.

## The stats that matter

For each chapter measured:

**Rubric metrics** (from `ai-fingerprint-audit`):
- Pangram document score (%)
- Pangram max-paragraph score (%)
- GPTZero verdict + burstiness
- D2 Tier 1/2/3 banned vocab counts
- D3 unique openers / 100 sentences
- D4 em-dash per 1k
- D5 "not X — Y" count
- D6 tricolons per 1.5k
- D7 paragraph chaos ratio
- D8 copula ratio
- D9 participle tails per 1k

**Voice metrics** (from `voice-preservation-metric.md`):
- Stylometric distance from Book 1 voice anchor (lower = better)
- Sentence-length variance match (target ratio of Book 1's)
- Character-voice TTR differentiation (dialogue chapters only)
- Tic deployment count (target ≥3/chapter)

**Quality metrics** (human spot-check, every 5th experiment cycle):
- Margaret voice-QA 1–5 rating
- Dev-edit-equivalent structural pass rate (synthetic — Daniel audits against cozy rubric)

## Gate: all metrics non-regressive + ≥1 improvement

| Scenario | Decision |
|---|---|
| Rubric up, voice stable | Adopt |
| Rubric up, voice down | Revert — rubric-gaming risk |
| Voice up, rubric stable | Adopt |
| Voice up, rubric down | Revert — voice holding but AI-flagging more |
| Both improve | Adopt (ideal) |
| Both regress | Revert |
| Mixed across chapters | Run 3 more; re-evaluate |

## Research budget

- 3 sandbox chapters per variant × 2,500–3,500 words average × $0.015/1k (Opus) ≈ $0.12 per experiment in tokens (Claude Max covers this)
- Pangram API: ~$0.02 per experiment
- GPTZero API: included in monthly flat
- Human voice-QA: ~30 min of Margaret's time per 5th experiment
- **Total cost: negligible per experiment; Margaret's time is the bottleneck**

## Anti-failure modes

**Over-optimizing for detectors.** Daniel starts writing prose that games Pangram but reads badly. Mitigation: voice-preservation metric + Margaret's voice-QA every 5th cycle. If her rating drops below 4.0, halt and diagnose.

**Voice drift from baseline.** Each variant nudges voice away from canonical Book 1. Mitigation: stylometric distance threshold. If any variant increases distance by >10%, revert even if rubric improves.

**Spurious improvements.** 3-chapter minimum + 5% noise band. Don't adopt from one-chapter signals.

**Scope explosion.** One variable at a time. No simultaneous tuning.

**Experiment pollution into production.** Sandbox-only rule. Ship-bound chapters are off-limits for experiments.

**Config drift you can't reproduce.** Every experiment logs: exact prompt, exact model version, exact tool versions, exact chapter text, exact scores. Full reproducibility.

## Experiment journal

Every experiment logged at:
```
/Users/nicoleopcl/Desktop/Vaults/Jason Krebs Books/00-Meta/Writer-Experiments/YYYY-MM-DD-variable/
├── baseline/
│   ├── chapter-1.md
│   ├── chapter-2.md
│   ├── chapter-3.md
│   ├── config.json
│   └── scores.json
├── variant/
│   ├── chapter-1.md
│   ├── chapter-2.md
│   ├── chapter-3.md
│   ├── config.json
│   └── scores.json
├── comparison.md        # side-by-side analysis
└── decision.md          # adopt / revert / inconclusive + rationale
```

SQLite table logs the decisions:
```sql
CREATE TABLE IF NOT EXISTS writer_experiments (
  id INTEGER PRIMARY KEY,
  run_date TEXT DEFAULT (datetime('now')),
  variable TEXT,
  baseline_config TEXT,     -- JSON
  variant_config TEXT,      -- JSON
  baseline_rubric_score REAL,
  variant_rubric_score REAL,
  baseline_voice_distance REAL,
  variant_voice_distance REAL,
  decision TEXT,            -- adopt / revert / inconclusive
  adopted_in_production BOOLEAN DEFAULT 0,
  adopted_at TEXT,
  notes TEXT
);
```

## Cadence

- **Daniel runs 1 experiment per week** when between books or in a low-draft week.
- **Paused during active Book 1 drafting** — don't split focus.
- **Resume during revision cycles and between-book gaps.**
- **Book 2 onward:** can run continuously if Daniel has bandwidth.

## Adoption into production

When a variant is approved for adoption:

1. Update Daniel's agent config in Paperclip (adapterConfig.promptTemplate OR instructions bundle) via PATCH.
2. Update the relevant section of Daniel's AGENTS.md on disk + post to JAS-5.
3. Log adoption in SQLite.
4. **Production validation run**: next 3 ship-bound chapters are audited with extra attention to confirm the variant generalizes from sandbox to production.
5. If production scores regress unexpectedly: revert to previous config. Sandbox vs production differences matter; the experiment may have a bias we didn't catch.

## Margaret's veto

Margaret can override any adoption if:
- Voice-QA score drops below 4.0
- Output reads "AI-slick" to a trained human reader even if rubric passes
- Voice-preservation metric says improvement but her reading says drift

Her veto stops adoption. Daniel proposes a different variant.

## Board approval required for

- Changes to the voice anchor itself (e.g., swapping the canonical Book 1 passage for a different one)
- Model-family changes (Opus → Sonnet, or switching Claude → GPT/Gemini)
- Changes that affect the calibration of the voice-preservation metric

These are meta-changes to the pipeline, not just tuning.

## When to retire this loop

When Daniel's output reliably passes the rubric AND holds voice AND gets ≥4.5 Margaret voice-QA AND the detector landscape stops moving — maybe Book 4 or 5 of the series. Until then, keep running.

## Intersection with fingerprint-audit-autoresearch

Both loops run in parallel:
- **fingerprint-audit-autoresearch** improves the rubric (what we measure)
- **writer-autoresearch** improves Daniel's output (the thing we measure)

A rubric update might invalidate some of Daniel's prior adoption decisions. When the rubric changes materially, re-test current production config against the new rubric. If regressions: re-run experiments against the new rubric.

## First experiments to run (seed queue)

See `variable-catalog.md`. Priority list for Board approval:

1. Voice-anchor depth: 500 vs 2,000 vs 5,000 words
2. Humanization pass: before-or-after-self-edit
3. Prompt template: scene-brief-as-list vs scene-brief-as-narrative
4. Model: Opus 4.6 high vs Opus 4.6 medium (cost vs quality tradeoff)
5. Tic deployment: spread-evenly vs cluster-in-emotional-beats
6. Read-aloud pass: post-humanization vs post-self-edit

## Hard rules

- One variable per experiment. Not two.
- Three sandbox chapters minimum per variant.
- Both metrics (rubric + voice) must be non-regressive for adoption.
- Sandbox only. Ever.
- Every experiment logged. Every decision documented.
- Margaret has veto.
- Board approves meta-changes (voice anchor, model family, rubric calibration).
