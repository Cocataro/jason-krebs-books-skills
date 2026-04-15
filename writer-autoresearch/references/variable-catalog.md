# Variable Catalog

What to tune, in order of expected impact. Change ONE variable per experiment.

## Variable 1 — Voice-anchor depth
**What:** Number of canonical Book 1 words Daniel re-reads before each drafting session.
**Current baseline:** 2,000 words (the weekly Monday voice-anchor document).
**Variants to test:** 500 / 5,000 / 10,000 / 0 (control — no re-read)
**Expected impact:** HIGH on voice-distance; MODERATE on rubric (more anchor = more tic deployment = better human feel)
**Cost delta:** +tokens for anchor re-read; +10–20 min per session for 5,000 word anchor
**Run first:** YES — high-leverage early test

## Variable 2 — Humanization-pass technique
**What:** How the humanization pass is structured.
**Current baseline:** post-self-edit, ~20% of drafting time, tic deployment + paragraph chaos + AI-fingerprint scan.
**Variants to test:**
- Pre-self-edit (humanize first, then self-edit)
- Two-pass (humanize, then light second humanization)
- Chapter-level humanization (write whole chapter clean, humanize the whole at end) vs scene-level (humanize each scene as drafted)
- Deliberate error injection (fragments + comma splice + quirky repetition) vs. natural-feel (no deliberate errors)
**Expected impact:** HIGH on rubric; MEDIUM on voice
**Cost delta:** varies; some variants save time

## Variable 3 — Prompt template (scene brief format)
**What:** How the scene brief is framed to Daniel.
**Current baseline:** `scene-composition` skill's 15-field structured brief.
**Variants to test:**
- Narrative brief (flowing paragraph of what should happen vs. field-list)
- Minimal brief (just scene goal + outcome; let Daniel improvise)
- Extended brief (fields + 2–3 reference passages from prior books)
- Voice-first brief (anchor passage + scene goal, skip structural fields)
**Expected impact:** MEDIUM on rubric; HIGH on voice (anchor-first may help)
**Cost delta:** marginal

## Variable 4 — Scene-composition depth
**What:** How detailed the scene brief is before drafting.
**Current baseline:** Full `scene-composition` skill output with all 15 fields.
**Variants to test:**
- Minimal brief (3 key fields: goal, outcome, sense-anchor)
- Maximum brief (all fields + reference passages + sample dialogue snippets)
- Iterative brief (brief expands during drafting as Daniel realizes what he needs)
**Expected impact:** MEDIUM on rubric; MEDIUM on voice; HIGH on speed
**Cost delta:** varies

## Variable 5 — Model + effort level
**What:** Claude model and reasoning effort.
**Current baseline:** claude-opus-4-6 / effort=high.
**Variants to test:**
- claude-opus-4-6 / effort=medium (cost savings, quality risk)
- claude-sonnet-4-6 / effort=high (different family; faster)
- claude-sonnet-4-6 / effort=medium (cheapest)
- claude-opus-4-6 / effort=high + temperature variance (0.7 vs 1.0 vs 1.3)
**Expected impact:** LOW-MEDIUM on rubric at top-tier models; HIGH on speed/cost
**Cost delta:** significant cost savings possible
**Board approval required** for model-family changes (Opus → Sonnet).

## Variable 6 — Tic deployment strategy
**What:** How POV character tics are distributed across the chapter.
**Current baseline:** ≥3 tics per chapter, spread across scenes.
**Variants to test:**
- Cluster tics in emotional beats (all 4+ tics in one dramatic scene)
- Even distribution (1 per scene)
- Heavy early-chapter tic deployment (establish voice up-front)
- Tic-swap experiments (use only interior tics, or only verbal-filler tics)
**Expected impact:** MEDIUM on voice; LOW on rubric
**Cost delta:** zero

## Variable 7 — Read-aloud pass
**What:** Daniel does a rhythm read-aloud check after drafting.
**Current baseline:** no mandatory read-aloud pass.
**Variants to test:**
- Read-aloud after humanization pass (catch smooth passages)
- Read-aloud after self-edit (catch awkward passages)
- Read-aloud at multiple points
**Expected impact:** LOW on rubric; MEDIUM on voice
**Cost delta:** +5–10 min per chapter

## Variable 8 — Pre-drafting research
**What:** Any domain research Daniel does before drafting.
**Current baseline:** series bible + outline only.
**Variants to test:**
- +competitor-chapter read (read a comp author's chapter in same mood before drafting)
- +sensory research (look up specific sensory details Daniel will use)
- +dialogue study (read a conversation from a comp author before drafting a dialogue-heavy scene)
**Expected impact:** LOW-MEDIUM on voice; LOW on rubric
**Cost delta:** +15–30 min per chapter; risk of comp-voice contamination

## Variable 9 — Drafting order (chapter construction)
**What:** Order of drafting within a chapter.
**Current baseline:** linear (scene 1 → scene 2 → scene 3).
**Variants to test:**
- Set-piece first (write the warmth midpoint scene first, build around it)
- Dialogue-first (draft the core dialogue, then surround with description)
- Ending-first (draft the chapter's ending, then write toward it)
**Expected impact:** LOW on rubric/voice; MEDIUM on chapter cohesion
**Cost delta:** minor

## Variable 10 — Session length
**What:** How many words drafted per session.
**Current baseline:** 2,500–3,500 words per daily session.
**Variants to test:**
- 1,500 words/session (more sessions per chapter; greater freshness)
- 4,500 words/session (fewer sessions; maintained flow)
- Variable based on scene natural breakpoints
**Expected impact:** LOW on rubric; LOW on voice; HIGH on fatigue/quality variance
**Cost delta:** zero

## Variable 11 — Self-edit rigor
**What:** How aggressive the self-edit pass is.
**Current baseline:** light self-edit (catch obvious issues; ≤5% rewrite).
**Variants to test:**
- No self-edit (raw draft → humanization only)
- Heavy self-edit (aggressive restructure before humanization)
- Self-edit with specific focus (dialogue only; or description only)
**Expected impact:** MEDIUM on rubric; MEDIUM on voice
**Cost delta:** varies

## Variable 12 — Chapter-level vs scene-level workflow
**What:** Whether Daniel drafts-humanizes-self-edits per scene or per chapter.
**Current baseline:** per-chapter (draft whole chapter, then humanize, then self-edit).
**Variants to test:**
- Per-scene workflow (draft scene, humanize scene, self-edit scene, move on)
- Hybrid (draft chapter fast, then per-scene humanize)
**Expected impact:** MEDIUM on rubric consistency; LOW on voice
**Cost delta:** minor

## Priority queue (first 6 experiments)

For Board approval to populate the initial experiment schedule:

1. **Voice-anchor depth: 500 vs 2,000 vs 5,000 words** (highest expected impact)
2. **Humanization pass: post-self-edit vs pre-self-edit**
3. **Prompt template: narrative vs structured brief**
4. **Model: Opus high vs Opus medium (cost/quality)**
5. **Tic deployment: spread vs clustered**
6. **Read-aloud pass: yes vs no**

Each experiment = 3 sandbox chapters × 2 variants = 6 chapters per experiment. At 1 experiment/week during low-draft periods, 6 weeks to run the priority queue.

## Variables NOT to tune (yet)

- **Canonical voice anchor content** — Board approval required; changing the target destabilizes the metric
- **Character bible content** — canon; Margaret's territory
- **Series Style Guide** — canon; not a tuning variable
- **Outline structure** — Eleanor's territory (dev edit); not Daniel's tuning variable

## Variable combinations (after priority queue)

Once individual variables are characterized, can test promising combinations:
- Deep voice anchor + pre-humanization + narrative brief (if all three individually improved)
- Run as one experiment per combination — still one-change-at-a-time rule, but each "change" is an approved-combination-of-proven-changes

## Log completion

When a variable has been tested at its variants (not just one):
- Add a summary note to the journal
- Mark as "characterized" in the variable catalog
- Move to next priority variable

## Retirement

When a variable is well-understood (tested + adopted or tested + deemed no-impact + documented):
- Stop re-testing it
- Note in catalog: "CHARACTERIZED — result: [adopted / no impact / rejected], confidence [high/medium/low]"
- Return to if the model or rubric materially changes
