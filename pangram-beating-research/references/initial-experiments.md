# Initial experiment batch — first week

Six experiments to run in the first week, one per day. Each produces 3 × ~500-word sandbox passages, scored via Pangram.

Sandbox scene spec for all six: **Briar encountering a new traveler at the inn** — a 500-word scene that fits the existing *Crossroads Inn* voice context. Use the same scene spec across all six so variance is attributable to the generation approach, not the story.

Shared scene prompt stub:

> A 500-word scene from *The Crossroads Inn*, Book 1. POV: Briar Thornheart (ex-mercenary turned reluctant innkeeper). Setting: the common room of the inn at dusk. A new traveler arrives — not threatening, but unexpected. Briar assesses them, offers tea, they speak briefly. Voice: Heartland Fantasy, deep POV, restrained warmth, sensory anchors, fragment-tolerant. Include at least one Briar voice tic (e.g., "Good morning to you too" as internal address). End with the traveler taking a seat by the hearth. Do not resolve their purpose or identity.

## Experiment 1 — Baseline

- **Hypothesis:** Current pipeline (single-model Opus with Style-Guide humanization prompts) produces ~100% AI on Pangram. Re-measure to confirm.
- **Pipeline:** Claude Opus, single pass, full Style-Guide humanization prompt, no post-processing.
- **Sample count:** 3 × 500 words.
- **Expected result:** All 3 score `prediction=AI`, `fraction_ai > 0.80`.
- **What this tells us:** The internal control. Every variant is measured relative to this.

## Experiment 2 — Two-model chain (Opus → Sonnet)

- **Hypothesis:** A second-model rewrite with a different prompt shape breaks single-signature enough to tip Pangram below 0.50 fraction_ai.
- **Pipeline:** Claude Opus drafts the passage per baseline prompt. Then Claude Sonnet receives the Opus draft with a distinct prompt: "Rewrite this passage for stronger Briar-POV voice. Preserve all story beats. Break any prose that sounds LLM-smooth." No post-processing.
- **Sample count:** 3 × 500 words.
- **Expected result:** Better than baseline. Maybe `prediction=Mixed`, `fraction_ai 0.40-0.70`. Probably still fails Gate 1.

## Experiment 3 — Three-model chain (Opus → Sonnet → GPT-4)

- **Hypothesis:** Stacking a third cross-vendor model diversifies the statistical signature further.
- **Pipeline:** Experiment 2's output + GPT-4 polish pass with prompt: "Light polish. Fix only genuine errors. Preserve every voice tic, fragment, and intentional imperfection."
- **Sample count:** 3 × 500 words.
- **Expected result:** Better than Exp 2. Possibly `prediction=AI-Assisted`, `fraction_ai 0.20-0.50`.
- **Note:** Requires GPT-4 API access. If not available, skip or substitute Gemini.

## Experiment 4 — Human-seed + AI-fill

- **Hypothesis:** If 20-25% of sentences are written by a real human (Board or hired writer), Pangram's statistical signal is diluted enough to score AI-Assisted or Human.
- **Pipeline:**
  1. Board writes the first paragraph (~100 words) by hand: opening image, Briar's first observation, one line of internal voice.
  2. Board writes one line of dialogue for the traveler (~20 words).
  3. Board writes the final sentence (~25 words): Briar watches the traveler sit.
  4. Claude Opus fills the remaining ~355 words, given Board's anchors and the scene prompt.
  5. No further post-processing.
- **Sample count:** 3 × 500 words. (Board writes 3 distinct sets of anchors; AI fills each.)
- **Expected result:** The most promising of the AI-heavy variants. Possibly `prediction=AI-Assisted` or `Human`.
- **Cost:** ~30 minutes of Board's time per passage set. Significant time cost for ongoing pipeline.

## Experiment 5 — Stylometric camouflage overlay

- **Hypothesis:** Mechanical post-processing that injects anti-LLM surface patterns tips Pangram without touching prose content.
- **Pipeline:**
  1. Claude Opus drafts per baseline.
  2. Script-driven post-processing applies:
     - Randomly fragment 1-in-5 paragraphs (split at a chosen clause boundary)
     - Substitute 5% of common words with rarer synonyms (from a curated list of Heartland Fantasy register — not GRE-word obscure)
     - Replace some periods with comma splices in interior-voice passages (semantically OK, LLM-uncommon)
     - Insert 1-2 intentional em-dash interruptions per 500 words (not more)
- **Sample count:** 3 × 500 words.
- **Expected result:** Mixed. Cosmetic manipulation may fool Pangram briefly but degrades prose quality and gets re-trained against. Include for data.

## Experiment 6 — Heavy AI-only rewrite chain

- **Hypothesis:** Multiple rewrites by the same model (Claude Opus) with escalating "break LLM patterns" prompts eventually produce prose that scores Human.
- **Pipeline:**
  1. Claude Opus drafts baseline.
  2. Claude Opus rewrites with prompt: "Rewrite. Break every paragraph that sounds LLM-smooth. Add at least 2 fragments. Remove any 'not just X but Y' constructions."
  3. Claude Opus rewrites again with prompt: "Make this rougher. Reader must feel a specific human intelligence behind the prose. Avoid completeness; embrace interruption."
  4. Final Claude Opus pass: "Light polish. Preserve roughness. Only fix genuine errors."
- **Sample count:** 3 × 500 words.
- **Expected result:** Better than baseline, worse than Experiments 3-4. Tests whether pure-AI iteration can escape the signature without cross-vendor or human input.

## After the first six

Weekly Aria report compares all six against the baseline. Pick top 2 approaches for Week 2 stacking tests:

- Combine approach A's generation with approach B's post-processing
- Run 3 more 500-word passages per stacked variant
- If a stacked variant scores Human consistently, promote to Gate 2 (full-chapter validation)

## Credit budget

- Baseline + 5 variants × 3 passages × 1 credit each = 18 credits (Week 1)
- Stacking tests Week 2: ~15 more credits
- Full-chapter validation (Gate 2): 3 chapters × 3 credits = 9 credits per candidate
- Buffer: 30 credits for re-runs, edge-case tests, incident responses

Target spend: ~80 credits over first month. Remaining: ~509 credits. Plenty of headroom.

## What Aria reports each day

One comment on the ongoing Aria research issue:

```
## Experiment {N} — {name}
- Variant: {one-line description}
- Samples: 3 × 500w, scored {H: n, AA: n, M: n, AI: n}
- Mean fraction_ai: 0.XX (baseline was 0.XX)
- Decision: reverted / retained as candidate / promoted
- Journal entry: research/pangram-experiments/{date}-{slug}.json @ commit {SHA}
- Next: {what I test tomorrow}
```

Plus the full JSON journal committed to the manuscripts repo.
