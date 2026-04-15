---
name: ai-fingerprint-audit
description: 10-dimension rubric + tooling + thresholds for detecting and eliminating AI-default prose fingerprints in cozy fantasy drafts before ship. Based on Pangram/GPTZero/Binoculars research, 2024–2026 community ban-lists, and academic stylometry. Every chapter Daniel drafts passes through this audit via Thomas in the line/copy pass; Margaret spot-audits 1-in-5 chapters; final ship/no-ship gate. The core compliance target is the BookTok audience running their own detectors, not Amazon policy.
---

# AI Fingerprint Audit

The real risk is not KDP enforcement — it's a reader pasting a paragraph into Pangram or GPTZero, screenshotting the result, and posting to r/fantasy or BookTok. Every observable AI-prose case that blew up in 2025 followed this pattern. Every chapter of every Crossroads Inn book must pass this audit before ship.

See references:
- `banned-vocabulary.md` — Tier 1/2/3 word and phrase ban-list, cozy-fantasy-specific additions
- `detector-tooling.md` — Pangram + GPTZero setup, thresholds, usage workflow
- `lint-script.md` — in-house regex pass for D2–D9
- `recovery-playbook.md` — 48-hour response plan if a book gets flagged publicly
- `calibration-sprint.md` — how to set human-cozy-fantasy-baseline thresholds before Book 1 ships

## The 10-dimension rubric (replaces the old 7)

Ranked by load-bearing weight. Each chapter must PASS all **automated** dimensions (D1–D10). Human-judgment dimensions are audited by Thomas in the line pass and Margaret in ship/no-ship — not blocked by the automated gate.

### D1 — Pangram classifier score (HIGHEST WEIGHT)
- **Measure:** document AI-probability + worst-paragraph AI-probability
- **Tool:** Pangram API (~$0.002 per 1k words ≈ $0.20 per 90k book)
- **PASS:** doc <5%, every paragraph <20%
- **WATCH:** doc 5–20% OR any paragraph 20–50%
- **FAIL:** doc >20% OR any paragraph >50%
- **Why:** Pangram is the current SOTA commercial detector (neural classifier, 1-in-10,000 FP rate per their transparency report). Independent benchmarks (DetectRL, March 2025) confirm it's robust against humanizer tools that defeat GPTZero. It's also what BookTok readers use.

### D2 — Banned-vocabulary density
- **Measure:** counts of Tier 1 / Tier 2 / Tier 3 words + phrases per chapter (see `banned-vocabulary.md`)
- **Tool:** regex lint script (in-house)
- **PASS:** 0 Tier-1, ≤2 Tier-2, ≤3 Tier-3 per 5k words
- **FAIL:** ≥3 Tier-1 OR ≥6 Tier-2
- **Why:** the "AI accent." The single most reader-visible fingerprint. Specific words ("delve," "tapestry," "testament," "landscape of") are instant public giveaways.

### D3 — Sentence-opener diversity
- **Measure:** unique sentence-initial tokens per 100 sentences; count of banned paragraph openers (*Moreover, Furthermore, Additionally, Certainly, Indeed, Importantly, Ultimately, In essence, That said*)
- **Tool:** tokenizer + blacklist regex
- **PASS:** ≥60 unique openers per 100 sentences AND 0 banned paragraph openers
- **FAIL:** <45 unique openers OR ≥2 banned paragraph openers in the chapter
- **Why:** burstiness proxy at the syntactic level. Humans vary how they open sentences; AI subjects-first repeats.

### D4 — Em-dash & typography audit
- **Measure:** em-dash count per 1k words; stray unicode decoration (arrows →, non-ellipsis characters, inconsistent quote styles, unicode checkmarks)
- **Tool:** regex + unicode class check
- **PASS:** ≤2 em-dashes per 1k words; quote style consistent with style sheet; zero stray unicode decorations
- **FAIL:** >4 em-dashes per 1k words
- **Why:** em-dash density is the single most-cited AI tell. Community consensus: AI produces ~20+/3k words; human fiction averages 2–5/3k.

### D5 — "Not X — Y" and negative-parallelism count
- **Measure:** matches for:
  - `not [A-Za-z ]{1,40}[—\-][A-Za-z ]{1,40}` ("not tired — exhausted")
  - `not only [^,]{1,60}, but (also )?` ("not only a kettle, but a promise")
  - `not because [^,]{1,60}, but because`
- **Tool:** regex
- **PASS:** 0–1 per chapter
- **FAIL:** ≥3 per chapter
- **Why:** the signature AI rhetorical move. Strongest single-pattern tell across every source.

### D6 — Tricolon and rule-of-three frequency
- **Measure:** count of 3-item comma-separated lists in prose (not dialogue), including food-list stacks which are especially AI-default in cozy fantasy
- **Tool:** regex + short LLM check to exclude legitimate recurring lists
- **PASS:** ≤1 per 1.5k words
- **FAIL:** ≥3 per 1.5k words
- **Why:** AI clusters tricolons; humans use one, move on. Cozy-fantasy sensory-list tricolons ("cinnamon, fresh bread, and old books") are the genre's single most abused pattern.

### D7 — Paragraph-length chaos
- **Measure:** standard deviation of paragraph word count ÷ mean paragraph word count
- **Tool:** script (word-count per paragraph, stdev, mean)
- **PASS:** stdev/mean >0.6
- **FAIL:** stdev/mean <0.4
- **Why:** uniformity fingerprint. AI produces consistent 3–5-sentence paragraphs; human fiction has 1-line paragraphs, fragments, and long breathers mixed in.

### D8 — Copula-avoidance ratio
- **Measure:** count(`\b(serves as|stands as|marks|represents|embodies|features|boasts)\b`) ÷ count(`\b(is|are|was|were)\b`) in narration (not dialogue)
- **Tool:** regex ratio
- **PASS:** <0.05
- **FAIL:** >0.15
- **Why:** subtle AI tell editors miss manually. AI substitutes inflated copulas for plain *is/are*; humans use plain copulas 4–10× more often in fiction.

### D9 — -ing participle-tail density
- **Measure:** sentences ending with a ", V-ing ..." trailing participial clause ("her heart pounding, echoing the rhythm of the ancient forest")
- **Tool:** regex + POS tag (optional)
- **PASS:** ≤2 per 1k words
- **FAIL:** >5 per 1k words
- **Why:** extremely common in Claude output. The "highlighting its importance" tell in the nonfiction register → in fiction it surfaces as dual-participle trailing clauses.

### D10 — Second-opinion detector (GPTZero)
- **Measure:** classification verdict + burstiness/perplexity numbers
- **Tool:** GPTZero API (~$15/mo flat)
- **PASS:** classified "Human"; burstiness score not flat
- **FAIL:** "AI" or "Mixed" verdict
- **Why:** independent model family; cross-validates Pangram. When Pangram and GPTZero agree on "human," ship. When they disagree, escalate.

## Human-judgment dimensions (audited, not auto-gated)

These don't automate reliably. Thomas includes them in the line pass; Margaret spot-checks on 1-in-5 chapters.

- **Tic deployment consistency** — POV character's documented verbal/cognitive tics deployed ≥3x per chapter, from the character bible
- **Scene-end variety** — no more than 60% of scenes in a chapter end on a reflection/summary/thematic sentence
- **Character-voice differentiation** — dialogue from different characters has distinct lexical-diversity signatures (TTR variance >0.05 across speakers in dialogue-heavy scenes)
- **Emotion showing vs. telling** — body/action evocation beats named-emotion telling (cozy fantasy reader expectation)
- **Controlled dysfluency** — at least one deliberate fragment, one comma splice, or one non-elegant repetition per 2k words

## Cozy fantasy-specific tells (extra-dangerous in this genre)

See full list in `banned-vocabulary.md` §cozy-fantasy. Key tells:

1. **Warmth-by-adjective-stacking:** "warm, golden, honeyed" trios read Hallmark-AI, not cozy-craft
2. **Sensory-list comfort beats:** tricolons of cozy objects ("cinnamon, fresh bread, old books") are the single most abused AI move in the genre
3. **Found-family dialogue regularity:** each side-character gets one personality trait expressed verbatim every scene they appear in
4. **Low-stakes symmetry:** every chapter resolves. Humans leave one emotional thread hanging
5. **Too-perfect magical exposition:** AI info-dumps; humans bury magic in side-chatter
6. **"Ancient forest / timeless village / forgotten recipe" triad:** >2 of these archetypal fillers in a chapter = tell

## Workflow for every chapter (Line/Copy Editor runs)

1. **Receive chapter from Daniel.**
2. **Run in-house lint** (D2–D9). Auto-reject if any D2, D4, D5, D8, or D9 FAILs — kick back to Daniel with specific flagged lines.
3. **If lint passes, run Pangram** (D1). If FAIL, do targeted rewrite of flagged paragraphs.
4. **Run GPTZero** (D10). Cross-check.
5. **If D1 + D10 agree on human,** ship to Margaret for ship/no-ship gate.
6. **If D1 + D10 disagree,** escalate to Margaret for human review before shipping.
7. **Every 5th chapter:** Margaret runs a full human read-aloud pass for tic/scene-end/voice dimensions that don't automate.

## Calibration sprint (one-time, before Book 1 draft starts)

See `calibration-sprint.md`. Summary: run the full D1–D10 pipeline on 3–5 human cozy fantasy comp titles (*Legends & Lattes*, *Bookshops & Bonedust*, *Can't Spell Treason Without Tea*, *Emily Wilde's Encyclopedia of Faeries*, *The Spellshop*). Record their numbers. Set the studio's PASS band at ±1 standard deviation of that human cozy-fantasy baseline.

**Why:** the numeric thresholds above are synthesized from indie consensus — they need to be validated against human cozy fantasy to avoid shipping prose that's been over-humanized into unreadable jaggedness. Cozy fantasy has its own rhythm and warmth that some "AI-default" patterns (warm adjectives, sensory anchoring) imitate; don't strip what the genre legitimately needs.

## What happens when Pangram flags a human cozy fantasy book

Real risk, real cases: Pangram has publicly flagged literary human fiction (Hachette's *Shy Girl*, a viral NYT Modern Love column). The tool has false positives at the literary-voice end of the distribution — exactly where cozy fantasy lives.

**Mitigation:**
1. Calibration sprint sets the target band empirically.
2. Two-detector consensus (Pangram + GPTZero) before shipping.
3. If a shipped book gets publicly flagged post-launch, run `recovery-playbook.md` within 48 hours.

## Hard rules

- D1 (Pangram) FAIL blocks ship. No exceptions.
- D10 (GPTZero) FAIL blocks ship unless Margaret overrides with documented reasoning.
- D2 (banned vocab) FAIL kicks back to Daniel — no silent normalization by Thomas.
- Calibration sprint must run before the first ship. Without it the thresholds are guesses.
- Every run of the rubric is logged to the SQLite DB (`revisions` table extended with D1–D10 scores).
- When detectors or research update, re-baseline quarterly.

## Not measured here (on purpose)

This audit catches specific failure modes (AI-default prose). It does NOT judge:
- Whether the prose is good
- Whether the character voice is distinctive
- Whether the scene earns its emotional moment
- Whether the book is commercially viable

Margaret, Eleanor, and the dev-edit + ship-no-ship gates handle those. This skill is one narrow instrument in a larger kit.

## Versioning

Update this skill quarterly. Detector accuracy improves; banned-word lists grow; reader tolerance shifts. Log each update with rationale + date in the repo changelog.
