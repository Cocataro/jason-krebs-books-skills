# Variable catalog — what to tune, ranked by expected impact

These are the variables in the prose-generation pipeline that are candidates for experimentation. Ranked by expected impact on Pangram score (highest first). Test ONE per experiment.

## Rank 1 — Generation approach

**Highest impact. Most likely to move the needle.**

- **Single-model baseline** (Claude Opus drafts whole chapter) — current, scores 100% AI
- **Two-model chain** (Opus drafts → Sonnet rewrites with different prompt) — breaks single-signature
- **Three-model chain** (Opus → Sonnet → GPT-4 polish) — stacks diverse signatures
- **Cross-vendor chain** (Claude + Gemini + GPT-4) — maximum signature diversification
- **Human-seed + AI-fill** (human writes 15-25% of sentences; AI fills the rest) — breaks statistical signature with real human content
- **Back-translation laundering** (EN → FR → EN via different models) — degrades quality, sometimes passes detectors
- **Iterative AI-only rewrite** (baseline → Claude rewrites → Claude rewrites again → …) — shifts surface patterns but may not fundamentally change fingerprint

## Rank 2 — Post-generation edit pass

**Second-highest impact. Applied after generation, before scoring.**

- **None** (baseline)
- **Aggressive human sentence-level rewrite** (~30-50% of sentences rewritten by real human) — known to work, expensive
- **Light human polish** (10-15% of sentences touched for natural variation) — cheaper, less effective
- **Mechanical stylometric camouflage** (post-processing script injects anti-LLM patterns: idiosyncratic punctuation, rare-word substitution, fragment insertion) — cheap if scripted, risks cosmetic score-gaming
- **Voice-tic injection pass** (targeted insertion of Briar's documented verbal/cognitive tics) — light touch, preserves voice

## Rank 3 — Prose seed style

**What the first-pass prose looks like before any humanization.**

- Generic LLM prose with Style-Guide humanization prompts (baseline)
- Fragment-heavy first pass (LLM explicitly told to produce rough, broken prose, then cleaned up)
- Stylometric anchor (prompt includes a 2,000-word sample of real human fantasy prose as the voice target)
- Author-specific mimicry (prompt asks to draft in the sentence-rhythm distribution of a named author, e.g., Robin Hobb, Patricia McKillip)

## Rank 4 — Chunking strategy

**How much prose gets generated per call.**

- Whole-chapter generation (baseline)
- Scene-by-scene with distinct prompts (more prompt diversity = more signature diversity)
- Paragraph-by-paragraph (maximum prompt diversity, risks coherence)
- Dialogue-first then prose-around (different generators for dialogue vs. narration)

## Rank 5 — Model choice

**Which model does the baseline generation.**

- Claude Opus (current)
- Claude Sonnet
- Claude Haiku
- GPT-4
- GPT-4o
- Gemini Ultra / Pro
- Open-source local models (Llama, Mistral)

## Rank 6 — Prompt structure

**How Daniel's drafting prompt is constructed.**

- Outline-driven (current) — detailed outline + voice directives
- Free-style (minimal outline, relies on model's judgment)
- Voice-anchor-heavy (2,000-word voice anchor dominates the prompt)
- Constraint-based (explicit anti-LLM pattern constraints baked into prompt)

## Rank 7 — Humanization rule set

**Which humanization directives are included in the drafting prompt.**

- Current Style-Guide rules (fragment ratio, tricolon limits, em-dash caps, etc.)
- Stripped-down minimal rules (only the most essential 3-4)
- Expanded catalog (everything in the current rules + community anti-AI-slop lists + academic stylometry findings)
- Author-specific rules (rules tuned to a target human author's documented patterns)

## Rank 8 — Sentence-level perturbation

**Post-processing transformations that break surface patterns.**

- Random fragment insertion (break 1-in-N paragraphs with an intentional fragment)
- Punctuation irregularity (occasional comma splice, intentional semicolon misuse, etc.)
- Rare-word substitution (swap common words for rarer synonyms at controlled rate)
- Paragraph-length jitter (vary paragraph length beyond LLM-default distribution)
- Sentence-opener variation (enforce N% of sentences not starting subject-first)

## Combinations to watch

Single variables first. But once 2-3 individual variants show promise, test combinations:

- **Multi-model chain + stylometric camouflage overlay** — maximum signature break
- **Human-seed + aggressive human rewrite** — maximum real-human content
- **Cross-vendor chain + voice-tic injection** — diverse generation + Briar-consistent surface
