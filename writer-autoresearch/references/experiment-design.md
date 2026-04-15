# Experiment Design — Per-Experiment Structure

## Pre-experiment checklist

- [ ] Variable to tune is selected from `variable-catalog.md`
- [ ] Only ONE variable changes (all other settings identical to baseline)
- [ ] Baseline config is current-production Daniel config (document it)
- [ ] Variant config differs by exactly one setting (document it)
- [ ] Sandbox outlines selected (3 outlines from `sandbox-outlines.md`)
- [ ] Experiment not running during active Book 1 drafting week
- [ ] Margaret aware the experiment is running (optional, but helpful for QA scheduling)

## Experiment spec template

```
EXPERIMENT: [short descriptive name, e.g., "voice-anchor-5000"]
DATE: [YYYY-MM-DD]
VARIABLE: [voice-anchor-depth / humanization-technique / prompt-template / ...]
HYPOTHESIS: [why we expect this to help, e.g., "Deeper voice anchor re-reading should lower Pangram scores while preserving voice"]

BASELINE CONFIG:
- Model: claude-opus-4-6
- Effort: high
- Prompt template: [current production template]
- Voice anchor depth: 2,000 words
- Humanization pass: post-self-edit, ~20% time
- Tic deployment strategy: 3+ per chapter, spread across scenes
- ... (all settings, explicitly)

VARIANT CONFIG:
- Model: claude-opus-4-6
- Effort: high
- Prompt template: [SAME as baseline]
- Voice anchor depth: 5,000 words   ← ONLY CHANGE
- Humanization pass: post-self-edit, ~20% time
- Tic deployment strategy: 3+ per chapter, spread across scenes
- ... (all other settings identical to baseline)

SANDBOX OUTLINES:
1. [Outline 1 name / source]
2. [Outline 2 name / source]
3. [Outline 3 name / source]

EXPECTED IMPACT:
- Rubric: Pangram -3 to -8% doc score; D7 paragraph-chaos +0.02
- Voice: distance from anchor -5 to -10%
- Time: drafting session +20 min (anchor re-read)
- Cost: +$0.02/chapter (extra tokens for anchor re-read)
```

## Run protocol

For each of baseline and variant:

1. **Start clean.** Daniel (in sandbox mode) loads the specified config.
2. **Generate 3 chapters** on the 3 sandbox outlines. One chapter per outline.
3. **Log each chapter** as a separate file with:
   - Full text
   - Config used (JSON snapshot)
   - Timestamp
   - Any notes Daniel adds during drafting
4. **Do not edit between drafts.** Raw output only. Consistent.
5. **Run all metrics** on each chapter:
   - In-house lint (D2–D9)
   - Pangram API call
   - GPTZero API call
   - Voice-preservation metric (see `voice-preservation-metric.md`)
6. **Store results** in `scores.json`:
   ```json
   {
     "chapter_id": "sandbox-outline-1-variant",
     "config": { ... },
     "rubric": {
       "pangram_doc": 0.04,
       "pangram_max_para": 0.18,
       "gptzero_verdict": "human",
       "gptzero_burstiness": 0.67,
       "d2_tier1_count": 0,
       "d2_tier2_count": 1,
       "d4_em_dash_per_1k": 2.1,
       "d5_not_x_y": 1,
       "d6_tricolons_per_1_5k": 1.2,
       "d7_paragraph_chaos": 0.68,
       "d8_copula_ratio": 0.04,
       "d9_participle_tails_per_1k": 2.1
     },
     "voice": {
       "stylometric_distance_to_anchor": 0.32,
       "sentence_length_variance_match": 0.94,
       "ttr_match_to_anchor": 0.91,
       "tic_deployment_count": 4
     }
   }
   ```

## Comparison + decision

Produce `comparison.md`:

```
# Experiment: voice-anchor-5000

## Rubric comparison

| Metric | Baseline mean | Variant mean | Δ | Verdict |
|---|---|---|---|---|
| Pangram doc | 8.2% | 4.1% | -4.1% | Improved |
| Pangram max-para | 24.0% | 17.2% | -6.8% | Improved |
| D2 Tier 1 | 1.0 | 0.3 | -0.7 | Improved |
| D4 em-dash/1k | 3.2 | 2.4 | -0.8 | Improved |
| D7 paragraph chaos | 0.52 | 0.71 | +0.19 | Improved |
| D8 copula ratio | 0.08 | 0.05 | -0.03 | Improved |

**Rubric overall: CLEAR IMPROVEMENT**

## Voice comparison

| Metric | Baseline mean | Variant mean | Δ | Verdict |
|---|---|---|---|---|
| Stylometric distance to anchor | 0.48 | 0.31 | -0.17 | Improved (closer to anchor) |
| Sentence length variance match | 0.78 | 0.92 | +0.14 | Improved |
| TTR match to anchor | 0.82 | 0.89 | +0.07 | Improved |
| Tic deployment count | 3.3 | 4.1 | +0.8 | Improved |

**Voice overall: CLEAR IMPROVEMENT**

## Cost comparison

| Metric | Baseline | Variant |
|---|---|---|
| Drafting session time | 3.2h | 3.4h |
| Tokens / chapter | 12,000 | 12,800 |
| API cost / chapter | $0.18 | $0.19 |

## Decision: ADOPT

Both metrics improved clearly. Time cost (+20min/session) is acceptable.
No regression on any dimension.
Adopting as new baseline. Updating Daniel's config.

Approval chain:
- [ ] Daniel: [signed]
- [ ] Margaret: [signed — voice-QA rating of variant samples 4.3 vs baseline 3.8]
- [ ] Board: [signed — voice anchor depth change requires approval]
```

## Decision rules

| Situation | Action |
|---|---|
| Both metrics improve, consistent across 3 chapters | Adopt |
| One metric improves, other stable within 5% | Adopt (no regression) |
| One metric improves, other regresses | Revert |
| Mixed across chapters (1 of 3 regresses) | Run 3 more; re-evaluate |
| Both metrics change within 5% (noise band) | Inconclusive — try a more aggressive variant or different variable |
| Variant breaks something unrelated (grammatical errors, incoherent output) | Revert immediately; document failure mode |

## When NOT to adopt even with positive metrics

- Variant is expensive (>2x cost) and improvement is <10%
- Variant introduces a fragility (only works with specific outline types)
- Variant's gain is in one dimension but Margaret's human read says "feels worse"
- Variant requires config that conflicts with other production requirements

## Archive

Every experiment, even inconclusive ones, lives in the Writer-Experiments directory permanently. Future experiments reference past ones to avoid re-running.

## Failure modes to watch for

### The "too good to be true" signal
If a variant drops Pangram doc score from 8% to 0.5% on all 3 chapters, something is wrong. Either:
- The variant is over-fitting (prompt-injection style)
- The sandbox outlines are too similar to training data
- Measurement error
Investigate before adopting.

### The "sandbox-production gap"
A variant that wins in sandbox but fails in production = sandbox bias. Sandbox outlines should be representative of Book 1–6 outline difficulty. If sandbox outlines are too simple, sandbox wins don't generalize.

### The "model update" drift
Claude Opus 4.6 in April may behave differently from Claude Opus 4.6 in October (post-model-update). Re-baseline every 2–3 months even without new experiments.

## Ship-bound chapter data

Every shipped chapter's rubric + voice scores ALSO get logged to the experiment journal (as passive data — not an experiment, but useful baseline drift signal). If production scores trend worse while sandbox scores hold stable: investigate the gap.
