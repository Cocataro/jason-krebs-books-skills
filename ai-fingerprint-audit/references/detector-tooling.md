# Detector Tooling — Pangram + GPTZero workflow

**Compliance target:** not KDP policy (which we can disclose our way through if needed). The real target is a BookTok reader running Pangram or GPTZero on a screenshot of a paragraph. **Every chapter must pass both detectors before ship.**

## Primary detector — Pangram

- **Why:** current SOTA commercial detector. Neural classifier trained on ~1M human (pre-2021) + AI (post-2022) docs, with hard-negative mining against synthetic humanizer outputs. Independent benchmarks confirm it defeats StealthGPT-class evasion where GPTZero collapses.
- **False-positive rate:** claimed 1-in-10,000 on general text, 1-in-100,000 on arXiv papers. Real-world exception: literary voice-y prose (Hachette's *Shy Girl*, NYT Modern Love column have false-positived). Cozy fantasy is closer to this exception territory — calibrate don't assume.
- **Cost:** ~$0.002 per 1k words. ~$0.20 per full 90k-word book. ~$1.20 total for Book 1 across all chapters at 5k each.
- **API:** [pangram.com](https://www.pangram.com) — request API access. Document + paragraph-level scores returned per request.
- **Pricing tier:** API metered, no monthly commit required.

### Pangram workflow per chapter

```bash
# Pseudocode — adapt to actual Pangram API when account is provisioned
curl -X POST "https://api.pangram.com/v1/classify" \
  -H "Authorization: Bearer $PANGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"$CHAPTER_TEXT\", \"mode\": \"paragraph\"}"
```

Response: document AI-probability + per-paragraph AI-probability + metadata.

### Pangram thresholds (ship/no-ship)

| Score | Verdict | Action |
|---|---|---|
| Doc <5% AI, every paragraph <20% | **PASS** | Ship-eligible |
| Doc 5–20% OR any paragraph 20–50% | **WATCH** | Targeted rewrite on flagged paragraphs; re-run |
| Doc >20% OR any paragraph >50% | **FAIL** | Kick back to Daniel with flagged paragraphs + rewrite brief |

## Secondary detector — GPTZero

- **Why:** independent model family (perplexity + burstiness + 7-component ensemble). Cross-validates Pangram. Known to collapse against StealthGPT humanizer but that's not our evasion vector — we're writing natural cozy prose, not piping through humanizer tools.
- **False-positive rate:** 0.24% claimed.
- **Cost:** ~$15/month flat for reasonable API volume.
- **API:** [gptzero.me](https://gptzero.me) — API access via account.

### GPTZero thresholds

| Verdict | Burstiness | Action |
|---|---|---|
| **Human** classification, burstiness not flat | PASS |
| **Mixed** classification OR flat burstiness | WATCH — rewrite flagged sections |
| **AI** classification | FAIL — kick back |

### Combined decision matrix

| Pangram | GPTZero | Decision |
|---|---|---|
| PASS | Human | **Ship** |
| PASS | Mixed | Margaret review — likely ship |
| PASS | AI | Margaret review — investigate discrepancy |
| WATCH | Human | Targeted rewrite; re-run |
| WATCH | Mixed | Significant rewrite required |
| WATCH | AI | FAIL — kick back to Daniel |
| FAIL | any | FAIL — kick back to Daniel |

## Detectors explicitly skipped (with rationale)

- **Originality.ai:** 4.79% false-positive rate is too high for literary voice. Adds noise not signal.
- **Copyleaks:** 90.7% claimed accuracy, but drops to 60% on paraphrased text. Too brittle.
- **Winston AI / Sapling / ZeroGPT:** self-reported 98%+ accuracy not independently verified. Untrusted for ship/no-ship decisions.

## Workflow integration

### Per chapter (Thomas / Line/Copy Editor)
1. Receive chapter from Daniel (Drive: `Crossroads Inn / Book N / Draft 1 / Ch NN`).
2. Run in-house lint script (D2–D9). If any FAIL, kick back to Daniel with flagged lines.
3. If lint passes, run Pangram on the full chapter.
4. If Pangram FAILs, identify flagged paragraphs and kick back with specific rewrite targets.
5. If Pangram PASSes or WATCHes-with-targeted-fixes, run GPTZero.
6. If GPTZero disagrees with Pangram, escalate to Margaret.
7. If both agree on human, mark chapter PASS in SQLite `revisions` table.
8. Proceed to line + copy pass.

### Per book (Margaret / EIC, ship/no-ship gate)
1. Full manuscript goes through Pangram document-level + random 10% paragraph sample.
2. GPTZero full-document.
3. If either flags >5% above chapter-level baseline, investigate which chapters drifted.
4. Calibration-sprint numbers are the reference floor.

### Monthly / quarterly
1. Re-check Pangram + GPTZero for model updates or threshold changes (they publish transparency notes).
2. Re-run calibration sprint against 2–3 new cozy fantasy human comps.
3. Update `banned-vocabulary.md` with any new community-flagged tells.

## SQLite logging

Extend the `revisions` table (or create `ai_audit_log` table):

```sql
CREATE TABLE IF NOT EXISTS ai_audit_log (
  id INTEGER PRIMARY KEY,
  chapter_id INTEGER REFERENCES chapters(id),
  run_date TEXT DEFAULT (datetime('now')),
  pangram_doc_score REAL,
  pangram_max_para_score REAL,
  pangram_verdict TEXT,          -- pass / watch / fail
  gptzero_verdict TEXT,          -- human / mixed / ai
  gptzero_burstiness REAL,
  gptzero_perplexity REAL,
  lint_d2_tier1_count INTEGER,
  lint_d2_tier2_count INTEGER,
  lint_d2_tier3_count INTEGER,
  lint_d3_unique_openers INTEGER,
  lint_d3_banned_openers INTEGER,
  lint_d4_em_dash_per_1k REAL,
  lint_d5_not_x_y_count INTEGER,
  lint_d6_tricolon_per_1.5k REAL,
  lint_d7_paragraph_chaos REAL,
  lint_d8_copula_ratio REAL,
  lint_d9_participle_tail_per_1k REAL,
  final_verdict TEXT,            -- pass / fail
  notes TEXT
);
```

Trend analysis: run `SELECT AVG(pangram_doc_score), AVG(gptzero_burstiness) FROM ai_audit_log WHERE chapter_id IN (SELECT id FROM chapters WHERE book_id=?)` per book. Improving scores across chapters = Daniel learning; flat or rising = signal he's drifting and needs a voice-anchor re-read + style-sheet audit.

## Cost projection

For a 6-book series, ~90k words each, 540k words total:
- Pangram: ~$1.08 total (most chapters pass on first run; budget ~2x for re-runs = ~$2.16)
- GPTZero: $15/mo flat × ~14 months series production = $210
- In-house lint: $0 (Python/Node script, free)
- **Total for entire series: ~$215** over ~14 months.

Well under the $500/mo vendor ceiling. This is not a cost pressure; quality is the constraint.

## Failure-mode playbook

**Pangram FAILs on a chapter Thomas believes is legitimately human-voiced:**
- Verify on 2 other paragraphs of the same chapter via GPTZero.
- Compare against calibration-sprint numbers for the same chapter position in a human cozy comp.
- If still flagged with no obvious AI fingerprint, escalate to Margaret. This is the false-positive risk. Decision: rewrite the flagged paragraphs with more dysfluency, fragments, and register variation — DON'T ship and hope.

**Pangram PASSes but Thomas or Margaret reads the chapter as AI-slick:**
- Trust the human read. Detectors miss what readers catch.
- Run the human-judgment dimensions (tic deployment, scene-end variety, character-voice differentiation) explicitly.
- Rewrite the flagged sections.

**Both detectors PASS, ships, then a BookTok reader flags the book post-launch:**
- Run `recovery-playbook.md` within 48 hours.
- Audit which dimensions the reader's screenshot highlights; update the rubric; calibrate thresholds stricter.
