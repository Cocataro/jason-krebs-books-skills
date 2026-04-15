# Calibration Sprint — Human Cozy Fantasy Baseline

The thresholds in the rubric (em-dash per 1k, copula ratio, paragraph chaos, etc.) are synthesized from indie community consensus + academic stylometry. They're reasonable starting points. They're not validated against real cozy fantasy prose — which has its own rhythm and warmth patterns.

**Before Book 1 ships, run this sprint.** The goal: empirically measure where legitimate human cozy fantasy sits on every D1–D9 dimension, and set the studio's PASS band at ±1 standard deviation of that human baseline.

**Why:** if you ship at the generic indie thresholds, you may be either (a) letting through prose that flags as AI to a reader running Pangram, or (b) rejecting chapters that would have been fine because the baseline is calibrated for nonfiction-register text, not cozy-voice fiction.

## The comp titles

Run all 5. Each is a published, widely-read cozy fantasy benchmark. You're not copying their voice — you're using their numbers.

1. **Legends & Lattes** — Travis Baldree (2022). The archetype of modern cozy fantasy.
2. **Bookshops & Bonedust** — Travis Baldree (2023). Prequel; Baldree voice proven across two books.
3. **Can't Spell Treason Without Tea** — Rebecca Thorne (2022). Found-family + romantic cozy.
4. **Emily Wilde's Encyclopedia of Faeries** — Heather Fawcett (2023). Academic-voice cozy; useful contrast.
5. **The Spellshop** — Sarah Beth Durst (2024). Single-protagonist cozy; also useful contrast.

Optional 6th: **The Very Secret Society of Irregular Witches** — Sangu Mandanna. Cozy with stronger stakes.

## Procedure

For each comp:
1. Get the ebook (purchase, then extract to text for internal calibration use — fair-use, not distributed).
2. Split into chapters.
3. Run the in-house lint script (D2–D9) on each chapter.
4. Run Pangram on 5 random chapters.
5. Run GPTZero on the same 5 chapters.
6. Record every dimension's value per chapter.

## What to record (per chapter per book)

```
comp_title: [book name]
chapter: N
word_count: [n]
D1_pangram_doc: [%]
D1_pangram_max_paragraph: [%]
D2_tier1_count: [n]
D2_tier2_count: [n]
D2_tier3_count: [n]
D3_unique_openers_per_100: [n]
D3_banned_paragraph_openers: [n]
D4_em_dash_per_1k: [n]
D5_not_x_y_count: [n]
D6_tricolons_per_1.5k: [n]
D7_paragraph_chaos: [ratio]
D8_copula_ratio: [ratio]
D9_participle_tails_per_1k: [n]
D10_gptzero_verdict: [human/mixed/ai]
```

Target: 10+ chapters per comp × 5 comps = 50+ data points per dimension.

## Analysis

For each dimension, compute:
- **Mean** across all comp chapters
- **Standard deviation**
- **Minimum** (outlier)
- **Maximum** (outlier)

## Set the studio's PASS band

### Option A — Conservative (recommended)
Studio PASS band = mean ± 1 stdev (covers ~68% of human cozy fantasy prose)

| Dimension | Comp mean | Comp stdev | Studio PASS band | Studio FAIL threshold |
|---|---|---|---|---|
| D2 Tier 1 | [measured] | [measured] | ≤ mean+1σ | > mean+2σ |
| D4 em-dash/1k | [measured] | [measured] | ≤ mean+1σ | > mean+2σ |
| D5 not-X-Y | [measured] | [measured] | ≤ mean+1σ | > mean+2σ |
| D7 para chaos | [measured] | [measured] | ≥ mean-1σ | < mean-2σ |
| D8 copula ratio | [measured] | [measured] | ≤ mean+1σ | > mean+2σ |
| D9 participle tails | [measured] | [measured] | ≤ mean+1σ | > mean+2σ |

### Option B — Aggressive
Studio PASS band = mean of comps (strict). Any chapter above mean fails.

**Don't use Option B** unless the studio is chasing zero-flag-risk at the cost of creative breathing room. Cozy fantasy readers forgive warm prose; they punish obvious fingerprints. Option A tunes to the realistic reader tolerance band.

### Option C — Per-dimension dynamic
Some dimensions may cluster tighter than others. Set band per-dimension based on observed distribution:
- If a dimension's stdev is tiny (e.g., comp em-dash per 1k is 2.0 ± 0.3), tight band (mean ± 0.5σ)
- If a dimension's stdev is large, wider band (mean ± 1σ)

## What if the comps fail the default rubric?

**Very likely outcome.** Cozy fantasy prose is warm and textured — it may legitimately exceed the generic indie thresholds on some dimensions.

If this happens:
1. **Do NOT lower your ship/no-ship gate to accommodate both comps and your own drafts.** That defeats the point.
2. Update your PASS band to what the human comps actually show.
3. Re-run the rubric on the comps with the updated band to confirm.
4. Document each threshold change with rationale: "Comp mean em-dash/1k = 3.4 ± 0.8, updated PASS to ≤4.2 (was ≤2)."
5. Commit the calibration data to the studio's compliance note.

## What if the comps PASS the default rubric?

Good news — your default rubric is already genre-valid. Use the default thresholds. Skip updating the PASS band.

## Cost of the sprint

- 5 ebooks × ~$9.99 each = ~$50
- Conversion + tokenization: 2 hours of script work
- Lint + Pangram + GPTZero runs: ~$2 in API calls
- Analysis: 4 hours of manual review

Total: ~$60 and a day of focused work. Pays for itself on Book 1 by catching mis-calibrated thresholds before they trigger a false-rejection cycle on Daniel's drafts.

## Re-run cadence

- Every 12 months (books and reader tolerance shift)
- After any material detector update (Pangram v2, GPTZero threshold change)
- After any time the studio considers expanding beyond cozy fantasy (recalibrate for new genre)

## Owner

- Thomas runs the lint.
- Thomas runs Pangram/GPTZero.
- Margaret audits the analysis + signs off on the new thresholds.
- CEO Jason approves ship-blocker threshold changes.

## Output artifact

Produce a one-pager: "Jason Krebs Books AI-Fingerprint Thresholds — April 2026 Calibration."
Stored at `/Users/nicoleopcl/Desktop/Vaults/Jason Krebs Books/00-Meta/ai-audit-calibration.md`

Contains:
- The 50+ data points
- Per-dimension mean, stdev, min, max
- The studio's chosen PASS band per dimension + rationale
- Re-baseline date
