# Quarterly Research Loop

Fires every 90 days. Produces a proposed rubric diff for Thomas to benchmark.

## Dispatch prompt (for the research subagent)

The Paperclip scheduled trigger dispatches a research subagent with this prompt:

```
You are researching the state of AI-generated text detection in fiction for the quarterly update of the ai-fingerprint-audit skill at Jason Krebs Books.

The skill lives at /Users/nicoleopcl/Documents/Projects/Jason Krebs Books/skills/ai-fingerprint-audit/. Read SKILL.md and references/banned-vocabulary.md first.

Research goals for this quarter:

1. **Detector updates.** Pangram, GPTZero, Binoculars — transparency reports, changelogs, new versions, new competitors. Any accuracy or false-positive-rate changes since last quarter. Any new detectors worth testing (check Hugging Face, arXiv 2023–present).

2. **Community ban-lists.** Check these sources for new banned-word additions or pattern discoveries:
   - GitHub: blader/humanizer, jalaalrd/anti-ai-slop-writing
   - Walter Writes, Jodie Cook blog ban lists
   - r/selfpublish "AI tells" threads in the last 90 days (search: "AI tells," "sounds AI," "Pangram flag")
   - r/ChatGPT, r/writing creative writing critique posts
   - Kindlepreneur / Jane Friedman / ALLi / 20Booksto50K posts on AI in fiction

3. **BookTok / genre-specific incidents.** Has any cozy fantasy (or romantasy / cottagecore-adjacent) book been publicly flagged on BookTok/Reddit in the last quarter? What specific patterns did the reader identify? What was the author's response and outcome?

4. **Academic papers (arXiv, last 90 days):**
   - Search "AI-generated text detection," "stylometry," "burstiness," "perplexity classifier"
   - Read abstracts; flag papers claiming new SOTA or novel detection features
   - Any new stylometric dimensions we should test (beyond our D1–D10)

5. **Cozy fantasy-specific tells.** Any new patterns that specifically surface in cozy/cottagecore/found-family fiction? (e.g., food-list tricolons were a 2024–2025 discovery.)

6. **Current Pangram + GPTZero scoring drift.** Pull 3–5 randomly-sampled chapters from our benchmark corpus (class A human, class B AI) and re-score them. Compare to scores from last quarter. Are detectors getting stricter, looser, or stable?

Deliverable — produce a markdown document with the following structure:

## Proposed updates for Q[N] [YYYY]

### Detector landscape
[Summary of what changed since last quarter + any threshold adjustments recommended]

### Banned vocabulary additions
[New words/phrases to add to Tier 1/2/3 — with source citation per addition]

### Banned vocabulary removals
[Any entries that community sources have retired or that our benchmark shows are false-positive heavy]

### New rubric dimensions
[Any new D-level dimension to test — with measurement spec, tool, proposed threshold]

### Threshold adjustments
[Changes to PASS/WATCH/FAIL bands on existing dimensions — with rationale]

### Tooling changes
[New detector to add/replace, new API pricing, new lint-script capability]

### Incidents observed
[BookTok/Reddit flagging events with specific patterns the reader noted]

### Overall recommendation
[Confidence: high/medium/low. Merge-readiness: yes/benchmark-first/needs-discussion.]

Be specific. Cite sources. Mark confidence. Favor precision over coverage — prefer 3 well-sourced changes over 15 speculative ones.

Do not merge the changes yourself. Output the proposed diff for Thomas to benchmark.
```

## Workflow after research dispatch

1. **Research subagent completes** → posts proposed-diff document as comment on a Paperclip research issue (auto-created via scheduled trigger).
2. **Thomas (Line/Copy Editor) picks up the research issue** → runs the proposed diff through the labeled corpus benchmark (see `benchmark-corpus.md`).
3. **Benchmark passes:** Thomas posts results + recommends merge. Margaret approves. Git commit + skill reimport.
4. **Benchmark fails:** Thomas posts results + analysis of why. Margaret decides: re-research, archive, or escalate. Diff archived.
5. **Board review for threshold changes:** Any change that moves a FAIL threshold requires Board sign-off before merge (even if benchmark passes).

## Cycle timing

- Day 0 (fire date): Paperclip cron fires; research subagent dispatched
- Day 1–3: Research subagent produces proposed diff
- Day 3–5: Thomas benchmarks
- Day 5–7: Margaret reviews; Board reviews threshold changes if any
- Day 7–10: Merge + reimport + changelog entry
- Day 10–14: Re-run calibration sprint IF the merge materially changed thresholds
- Day 14+: Watch for false-reject / false-pass rate on live chapters — rollback if real-world signal contradicts benchmark

Total cycle ~14 days per quarter. Three weeks buffer before next quarter's dispatch.

## Changelog format

Every merge adds an entry to `skills/ai-fingerprint-audit/CHANGELOG.md`:

```
## 2026-Q3 update (merged 2026-07-22)

### Added
- Tier 1 phrase: "in the twilight of" (source: r/selfpublish 2026-06-14 thread; confirmed in 3 BookTok callouts)
- Tier 2 word: "luminous" — deprecation from Tier 3 to Tier 2 based on Pangram update v3.4 elevating its weight

### Removed
- "Meticulously" from Tier 1 → Tier 2 (false-positive rate on human cozy fantasy was 12%; demoted)

### Threshold changes
- D7 paragraph-chaos FAIL threshold: 0.4 → 0.45 (benchmark showed human cozy comps trend higher than initial calibration)

### Rubric dimensions
- Added D11 (experimental): sentence-embedding cluster test. Benchmark results: precision_A +2%, recall_B +4%, no regression. Merged as experimental; re-evaluate in Q4.

### Tooling
- Pangram v3.4 rolled out; adjusted PASS band from <5% doc to <4% doc (Pangram reduced sensitivity per their 2026-Q3 notes).

### Incidents referenced
- 2026-07-03: [Book title redacted] BookTok callout — specific pattern: stacked "ancient X / timeless Y / forgotten Z" triads in single paragraph. Added detection.

### Source citations
[List every source URL referenced in the cycle]
```

## Anti-drift rules

- **No change lands without a source citation.** "Feels right" isn't valid.
- **No change lands without a benchmark pass.** No exceptions.
- **Archive every rejected diff** with rationale. Future quarters shouldn't re-propose rejected changes unless new evidence supports.
- **Don't flip-flop.** If Q3 removed "meticulous" from Tier 1, Q4 doesn't re-add without fresh evidence.
- **Calibration sprint re-runs only on material changes.** Minor word additions don't trigger re-calibration; threshold changes do.

## Fallback if research subagent isn't available

The loop can run manually if automation breaks:

1. Board or Margaret runs the research prompt manually in a Claude conversation
2. Posts the proposed-diff doc to the quarterly research issue
3. Thomas picks up and benchmarks as usual
4. Merge process identical

Budget ~2 hours of human research time as the backup.

## Monitoring

Every quarterly cycle's output is logged to:
- Paperclip issue thread (per-quarter parent issue)
- Vault: `00-Meta/Fingerprint-Research-Log/YYYY-QN/`
- Changelog on the skill repo

Board reviews the quarterly log in the Monday slate review closest to the cycle end.
