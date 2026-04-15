# Multi-Objective Gate

The hardest part of writer-autoresearch: you're optimizing two (sometimes three) objectives simultaneously — **rubric pass-rate** AND **voice-preservation** AND **dev-edit acceptance**. They can conflict. The gate defines how to decide.

## The three objectives

### Objective A — Rubric pass-rate
Measured by `ai-fingerprint-audit` rubric D1–D10 + Pangram + GPTZero.
Minimize AI-fingerprint score. Lower = better.

### Objective B — Voice-preservation
Measured by `voice-preservation-metric.md` stylometric distance from Book 1 anchor.
Minimize distance. Lower = better (closer to anchor).

### Objective C — Dev-edit acceptance (spot-check, every 5th cycle)
Measured by Margaret's voice-QA rating (1–5) + simulated dev-edit structural check.
Maximize rating. Higher = better.

## The tradeoff

Some variants improve A at cost of B (prose gets mechanically clean, voice drifts).
Some variants improve B at cost of A (prose holds voice, detector scores rise).
Some variants improve both (holy grail — voice-anchor-depth is likely one).
Some variants improve neither.

## The gate rule

**A variant is adopted only when all objectives are non-regressive AND at least one is improved.**

Not "average improves." Not "majority improves." **All non-regressive.**

| A | B | C | Decision |
|---|---|---|---|
| ↑ | ↑ | ↑ | Adopt (ideal) |
| ↑ | ↑ | = | Adopt |
| ↑ | = | = | Adopt |
| ↑ | ↓ | — | Revert (rubric-gaming) |
| = | ↑ | — | Adopt (voice-preservation pure win) |
| ↓ | ↑ | — | Revert (voice-only; AI risk rises) |
| ↓ | ↓ | — | Revert (nothing improves) |
| ↑ | = | ↓ | Revert (voice-QA regression despite rubric gain) |

## Noise bands

Within 5% of baseline on a given metric = considered "equal" (noise). Prevents over-reacting to small variance.

Beyond 5%: clear direction. Apply the gate.

## Three-chapter minimum

The gate applies to **mean across 3 sandbox chapters**. Not any one chapter.

If 2 of 3 variant chapters improve rubric but 1 regresses by 10%: inconclusive. Run 3 more.

If all 3 chapters move in the same direction: clear signal.

## Human-judgment override (Margaret)

Margaret can veto adoption even if A/B pass:
- She reads the chapters
- If her human-QA rating for variant chapters is lower than for baseline chapters
- Even if stylometric distance is unchanged

Her veto is final. Daniel proposes a different variant.

**Why:** voice has dimensions the metrics don't capture (emotional beat, character interiority, scene pacing rhythm). Margaret's trained eye catches what Python scripts miss.

## Board approval required for

- Variants that change the voice anchor
- Variants that change the production model family (Opus → Sonnet)
- Variants that change the rubric's ship/no-ship threshold
- Variants that change the labeled benchmark corpus

These are meta-changes. They reshape the optimization surface, not just the current point.

## Weighted gate (alternative — NOT recommended currently)

If you need a single number combining A/B/C (not recommended at this stage):

```
composite_score = (0.5 * rubric_score) + (0.3 * voice_preservation) + (0.2 * margaret_rating)
```

The composite lets tradeoffs balance numerically. But:
- Weights are arbitrary (why 0.5 not 0.4?)
- Composite can hide regressions (variant improves A, regresses B, net positive)
- Margaret's intuition can't be reduced to a number

Stick with the non-regressive gate unless data shows a clear case for composite.

## Pareto frontier

Over many experiments, each variant plots a point in (A, B) space. The Pareto frontier connects variants where improving one objective would necessarily worsen another.

Ideal production config = on the Pareto frontier.

Log each experiment's coordinates:
```
2026-Q2 baseline:        (rubric=0.82, voice=0.45)
2026-Q2 variant-anchor5k: (rubric=0.89, voice=0.32)  ← dominates baseline (both improve); adopt
2026-Q2 variant-sonnet:   (rubric=0.70, voice=0.42)  ← regression on rubric; reject
2026-Q2 variant-clusterTics: (rubric=0.82, voice=0.38)  ← voice improves; rubric stable; adopt
```

Periodically visualize the frontier. Identify regions to target next.

## Minimum improvement threshold for adoption

A variant that improves rubric by 1% while improving voice by 0.5% is technically non-regressive + improves. Should adopt?

**Decision: only adopt if at least one metric improves by >5%.** Tiny improvements aren't worth the config-complexity cost. Save the experiments for big moves.

Small improvements can accumulate (if 10 separate experiments each improve by 2–3%, adopt them). But flagging each variant's improvement as >5% keeps the signal clean.

## Statistical significance

Three chapters per variant isn't statistically rigorous. Don't pretend it is.

If variance is high across variant chapters (Pangram scores vary by >15% across 3 chapters on same variant): don't adopt. Run 3 more to build confidence.

Variance is itself a signal: stable variants are more predictable in production.

## When objectives can't be improved together

Sometimes you hit a wall. Variants either improve A at cost of B, or vice versa. Neither dominates.

This is Pareto-stuck. Options:
- Accept current production as optimal on the frontier
- Introduce a new objective (additional metric) to differentiate
- Research new variants that might dominate (e.g., new prompt techniques, new models)
- Accept the tradeoff via Board-level decision about priority

## Regression from production observation

After adoption, watch the next 3 ship-bound chapters carefully. If production scores regress vs. expected (based on sandbox):
- Revert to previous config
- Document the sandbox-production gap
- Investigate (sandbox outline bias? production outline complexity mismatch?)

## Documentation per gate decision

Every gate decision logged to the experiment directory + SQLite:

```
Decision: ADOPT / REVERT / INCONCLUSIVE
Variable: [what changed]
Baseline A mean: X | Variant A mean: Y | Δ: Z% | Verdict: [improved/regressed/stable]
Baseline B mean: X | Variant B mean: Y | Δ: Z% | Verdict: [improved/regressed/stable]
Baseline C mean: X | Variant C mean: Y | Δ: Z% | Verdict: [improved/regressed/stable]
Rationale: [1-2 sentences]
Approvers: Daniel / Margaret / Board [if required]
Adopted at: [timestamp]
```

## Retirement and re-test

A variable that was characterized and rejected doesn't get re-tested automatically. But:
- If the model updates materially: re-test (model behavior changed)
- If the rubric updates materially: re-test (optimization target changed)
- If the voice anchor changes: re-test (B metric's target changed)

These are meta-level triggers for re-opening closed variable questions.
