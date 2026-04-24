---
name: pangram-beating-research
description: Autonomous research loop for finding a prose-generation pipeline that produces Pangram-Human output. Iteratively tests approaches (multi-model chains, human-seed+AI fill, stylometric camouflage, heavy-edit passes) against the live Pangram /v3 detector. Maintains an experiment journal. Proposes SOP changes when a variant consistently scores Human. Never modifies ship-bound chapters directly — all experiments run on sandbox 500-word passages first, then full-chapter validation. Owner: Aria Patel (Research Engineer). Findings ratified by Margaret Krebs (EIC). Board approves any change that affects Daniel's drafting SOP.
---

# Pangram-Beating Research

Ch 1 and Ch 2 of *The Crossroads Inn* both scored 100% AI-Generated, High confidence on Pangram (2026-04-23). The current prose pipeline (Daniel drafts via Claude Opus + humanization rules + Thomas fingerprint audit) reliably produces detector-failing output. This skill is the continuous-improvement loop that finds a pipeline variant that beats Pangram, validates it on short passages, then on full chapters, then proposes SOP changes to Margaret + Board.

**Target:** prose that scores `prediction_short == "Human"`, `fraction_ai < 0.10`, zero high-confidence AI-Generated windows.

## The loop (Karpathy-style)

```
1. Current baseline approach → score on Pangram (500-word passage)
2. Propose variant: change ONE thing about the pipeline
3. Generate 3 passages via the variant, all ~500 words
4. Score all 3 on Pangram
5. Compare mean fraction_ai + prediction_short distribution
6. Decision gate:
   - Variant consistently scores Human/AI-Assisted (mean fraction_ai < 0.30, no prediction="AI") → promote to full-chapter test
   - Variant scores better than baseline but not passing → keep as candidate for stacking
   - Variant scores worse or equal → revert
7. Log result to experiment journal
8. Loop — pick next variable to tune
```

## Variables worth testing (ranked by expected impact)

See `references/variable-catalog.md`. Quick summary in order of likely impact:

1. **Generation approach** — multi-model chain vs. single-model vs. human-seed+AI fill vs. back-translation
2. **Prose seed style** — generic baseline vs. mimicking a specific human author's sentence-length distribution vs. fragment-heavy
3. **Post-generation edit pass** — aggressive human rewrite, stylometric camouflage overlay, voice-tic injection
4. **Chunking strategy** — generate paragraph-by-paragraph vs. scene-by-scene vs. whole-chapter
5. **Model choice** — Opus vs. Sonnet vs. GPT-4 vs. Gemini vs. mixed
6. **Prompt structure** — detailed outline-driven vs. free-style vs. voice-anchor-heavy
7. **Humanization rule set** — current Style-Guide rules vs. stripped-down vs. expanded catalog
8. **Sentence-level perturbation** — random fragment insertion, punctuation irregularity, rare-word substitution

Test one variable at a time. Multi-variable tests produce inconclusive results.

## Scoring harness

Reuse `skills/pangram-detector/scripts/run-pangram.py`. Input: text file (prose, no frontmatter). Output: JSON with `prediction_short`, `fraction_ai`, `fraction_ai_assisted`, `windows[]`, and computed verdict.

**Passage budget:** each 500-word passage burns 1 credit. Target ~30 credits/week for continuous research. Current balance: 589 credits (after 11 used for Ch 1/Ch 2 manual baseline).

**Validation cost:** full 3,000-word chapter = 3 credits. Promotion-gate testing needs 3 full chapters = 9-12 credits per variant.

## Experiment journal format

Every experiment produces a JSON entry in `research/pangram-experiments/YYYYMMDD-{slug}.json`:

```json
{
  "experiment_id": "20260424-multimodel-v1",
  "hypothesis": "Multi-model chain (Opus draft → Sonnet rewrite → GPT-4 polish) breaks single-model statistical signature enough to tip Pangram below fraction_ai=0.50.",
  "baseline_ref": "20260423-ch01-current-pipeline",
  "variable_changed": "generation_approach",
  "approach_description": "[concrete description of the pipeline steps, including model choice, prompt template, any post-processing]",
  "sample_count": 3,
  "samples": [
    {"passage_id": "1", "input_words": 512, "pangram": {...raw response...}, "verdict": "PASS|WARN|FAIL"},
    ...
  ],
  "aggregate": {
    "mean_fraction_ai": 0.82,
    "prediction_distribution": {"Human": 0, "AI-Assisted": 0, "Mixed": 1, "AI": 2},
    "passes": 0,
    "warns": 0,
    "fails": 3
  },
  "decision": "reverted|retained_as_candidate|promoted_to_full_chapter_validation",
  "rationale": "...",
  "next_variant_to_test": "..."
}
```

Commit every experiment journal entry to `crossroads-manuscripts` repo under `research/pangram-experiments/`. Git history IS the research record.

## Promotion gate — variant → SOP change

A variant can only become a ship-ready SOP change after passing THREE gates:

### Gate 1 — 500-word passage gate
- 3 passages, all score Human OR AI-Assisted
- Mean `fraction_ai < 0.20`
- Zero high-confidence AI windows across all 3 samples

### Gate 2 — Full 3,000-word chapter gate
- Generate 3 full sandbox chapters (Book 2+ warm-ups, NOT ship-bound Book 1 content) via the variant
- All 3 score PASS (Human, fraction_ai < 0.10) OR WARN with explicit Eleanor review
- Voice-preservation sanity check: Margaret EIC confirms the chapter reads as Briar-POV, not off-voice

### Gate 3 — Ratification
- Aria writes a proposal: what to change in Daniel's AGENTS.md / drafting process / skills attached / humanization rules
- Margaret ratifies the proposal as an EIC-approved SOP update
- Board approves any change that affects: voice-anchor definition, model selection at Daniel's level, mandatory sentence-level post-processing

Only after all 3 gates: SOP merges. Daniel's next chapter uses the new pipeline. Thomas's per-chapter Pangram gate remains in force as confirmation.

## Initial experiment batch (first week)

See `references/initial-experiments.md`. Six experiments to run first, one per day:

1. **Baseline re-measurement** — current pipeline, 3 sandbox passages, establishes internal control
2. **Multi-model chain v1** — Opus → Sonnet, different prompts per pass
3. **Multi-model chain v2** — Opus → Sonnet → GPT-4 polish
4. **Human-seed (20%) + AI fill** — Board writes openings/beats (~100 words), Daniel fills (~400 words)
5. **Stylometric camouflage overlay** — baseline + mechanical post-processing (punctuation irregularity, rare-word substitution, fragment injection)
6. **Heavy AI-only rewrite chain** — baseline → Claude rewrites with explicit "break statistical patterns" prompt → re-rewrite → final

Six experiments × 3 passages each = 18 Pangram runs = ~18 credits for the initial batch.

## Schedule

**Aria's cadence:** daily research run. One experiment per wake, average. Paperclip wakes her on a scheduled heartbeat (ideally) OR Board kicks her manually via issue comment until the scheduler is wired.

**Thomas's involvement:** when Aria promotes a variant to the full-chapter gate, Thomas runs the 3 validation chapters through his Pangram gate (same tool, same thresholds). Thomas's verdict is the second opinion.

**Weekly report:** Aria posts a summary issue every Friday: experiments run, variants promoted, variants reverted, current best baseline, proposed next week's experiments.

## What NOT to do

- Do NOT run experiments on ship-bound Book 1 chapters. Sandbox only.
- Do NOT multi-variable tests. One variable per experiment.
- Do NOT propose SOP changes without all 3 gates passing.
- Do NOT chase Pangram scores by inserting cosmetic anti-LLM patterns (em-dashes, typos) that degrade prose quality. The target is durable craft improvement, not score-gaming.
- Do NOT skip the voice-preservation check. A variant that beats Pangram by producing prose that doesn't sound like Briar is not a win.
- Do NOT discard failed experiments silently. Every failure teaches us something; log it.

## What success looks like

**Week 1:** baseline + 5 variants measured. Best-performing variant identified. Experiment journal committed.

**Week 2-3:** stacking tests. Combine top two variants. Test on 9 more 500-word passages. If a combined approach consistently scores Human or AI-Assisted, promote to Gate 2.

**Week 4:** full-chapter validation of top candidate. 3 sandbox chapters. Eleanor + Margaret voice-QA review. If passes, Aria writes SOP proposal.

**Week 5:** SOP update merges. Daniel re-drafts Ch 3 via new pipeline. Thomas runs Pangram. Ship-ready gate re-activates.

**Failure mode:** after 4 weeks, no variant consistently beats Pangram. Aria escalates to Board: options are (a) rebrand as AI-authored, (b) hire human editor for sentence-level rewrites, (c) pause the project. Don't keep running experiments indefinitely if no signal is emerging.
