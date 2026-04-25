# Benchmark Corpus — Labeled Dataset for Rubric Testing

Every proposed rubric change is tested against this corpus before merging. Without this gate, the rubric drifts.

## Dataset composition

Target: ~120 labeled chapter-length samples across three classes.

### Class A — Human Heartland Fantasy ("human")
**Target: 50 chapters.** The calibration-sprint corpus from `ai-fingerprint-audit/references/calibration-sprint.md` becomes the seed. Add 10 more chapters per quarter from newly released human Heartland Fantasy (check NYT bestseller list, Goodreads Choice winners, r/fantasy top cozy recommendations).

### Class B — Unedited AI-default ("AI")
**Target: 50 chapters.** Generate from Claude Opus / GPT-5 / Gemini on the 6-book Crossroads outline and other Heartland Fantasy outlines. **Do not run any humanization pass.** This is the raw baseline AI output — what would ship if Daniel did nothing but outline → Claude → push.

Generation protocol:
- Use 3 different model families (Anthropic, OpenAI, Google)
- Different temperature settings (0.7, 1.0, 1.3)
- Different prompt styles (chapter-and-beat vs free expansion)
- Chapter length 2,500–4,500 words
- Do not cherry-pick — include both "good" and "mediocre" AI output
- Refresh 15 chapters per quarter (swap for newer model outputs)

### Class C — Humanized-drafted ("studio-shipping")
**Target: 20 chapters.** The critical class — this is what Daniel actually produces: AI-drafted-then-humanized prose. Built from:
- Daniel's shipped chapters once they exist
- Before Daniel has enough chapters: have a freelance ghostwriter do a humanization pass on 20 Class B samples
- Once Daniel has 20+ shipped chapters, rotate those in + freelance samples out

**Why this class matters:** Class A vs B is an easy separation. The real test is whether the rubric can correctly pass Class C (don't false-reject the studio's legitimate output) while correctly failing Class B (catch raw AI that slipped the humanization pass).

## Labeling

Each chapter is tagged with:
- **class:** A / B / C
- **source:** book title + chapter number (A), model + temperature + date (B), author + date (C)
- **word_count**
- **date_added**
- **replacement_candidate:** true/false (older samples rotate out)

## Storage

```
/Users/nicoleopcl/Desktop/Vaults/Jason Krebs Books/00-Meta/Fingerprint-Benchmark-Corpus/
├── class-A-human/
│   ├── legends-and-lattes-ch01.md
│   ├── legends-and-lattes-ch02.md
│   ├── emily-wilde-ch01.md
│   └── ...
├── class-B-ai-default/
│   ├── crossroads-book1-ch01-claude-opus-t1.0-2026q2.md
│   └── ...
├── class-C-studio-shipping/
│   ├── crossroads-book1-ch01-daniel-2026q2.md
│   └── ...
└── labels.json
```

`labels.json`:
```json
{
  "samples": [
    {
      "file": "class-A-human/legends-and-lattes-ch01.md",
      "class": "A",
      "source": "Travis Baldree - Legends & Lattes - Chapter 1",
      "word_count": 3214,
      "date_added": "2026-04-15",
      "replacement_candidate": false
    },
    ...
  ],
  "last_updated": "2026-04-15",
  "next_rotation_due": "2026-07-15"
}
```

## Legal + fair use

- Class A uses published books for **internal calibration use only.** Not distributed. Not shared outside the studio. Defensible as fair-use research.
- Class B is studio-generated content.
- Class C is studio-owned content (or freelance-work-for-hire).
- No corpus artifact leaves the studio vault. Ever. If the corpus is exported for analysis, the export must be run on local tools (no third-party SaaS analysis services).

## Rubric evaluation run

```python
# Pseudocode for benchmark run
import json
from pathlib import Path
from ai_lint import check_chapter  # from the lint script
from pangram_api import score       # Pangram API wrapper
from gptzero_api import classify    # GPTZero API wrapper

labels = json.load(open("labels.json"))

for sample in labels["samples"]:
    path = Path(sample["file"])
    text = path.read_text()
    lint = check_chapter(path)
    pangram = score(text)
    gptzero = classify(text)

    # Apply rubric verdict
    auto_fail = any(lint[k] == "FAIL" for k in ["D2_verdict", "D4_verdict", "D5_verdict", "D8_verdict", "D9_verdict"])
    pangram_fail = pangram["doc_score"] > 0.20 or pangram["max_para"] > 0.50
    gptzero_fail = gptzero["verdict"] == "AI"

    verdict = "FAIL" if auto_fail or pangram_fail or gptzero_fail else "PASS"

    # Compute per-class metrics
    sample["rubric_verdict"] = verdict
    sample["pangram_doc"] = pangram["doc_score"]
    sample["gptzero"] = gptzero["verdict"]
```

## Precision / recall computation

For Class A ("human"):
- Precision_A = TP_A / (TP_A + FP_A) where TP = correctly PASSed, FP = PASSed samples from class B/C
- Recall_A  = TP_A / (TP_A + FN_A) where FN = A samples incorrectly FAILed

For Class B ("AI-default"):
- Precision_B = TP_B / (TP_B + FP_B) where TP = correctly FAILed B samples
- Recall_B  = TP_B / (TP_B + FN_B) where FN = B samples incorrectly PASSed

For Class C ("studio-shipping"):
- Precision_C and Recall_C on whether rubric correctly passes legitimate output

## Pass/fail gate for proposed rubric changes

Required to merge a proposed change:

| Metric | Current baseline | Post-change | Required |
|---|---|---|---|
| Recall_A (don't reject humans) | (measure) | ≥ current | No regression |
| Recall_B (catch raw AI) | (measure) | ≥ current | No regression |
| Recall_C (pass legitimate studio output) | (measure) | ≥ current | No regression |
| Precision on ship class (C+A) | (measure) | ≥ current | No regression |
| At least one dimension improvement | — | strictly positive | Yes |

Current baselines are populated on first run after corpus is built. Updated each cycle.

## Edge cases

- **A sample that gets PASSed by old rubric + FAILed by new rubric:** regression. Reject the change.
- **A sample that gets FAILed by old rubric + PASSed by new rubric:** improvement if it's class A/C; regression if it's class B.
- **Ambiguous sample (a Class A human chapter that legitimately has high em-dash density):** flag for manual review. May indicate corpus-level drift, not rubric error.

## Corpus maintenance cadence

- **Weekly (automated):** verify all file paths still resolve; no corrupted samples.
- **Quarterly (manual + Thomas):** rotate 10% of samples — add newer Heartland Fantasy, newer AI models, newer Daniel shipping samples.
- **After any incident:** the flagged-then-shipped book's chapter added to the corpus as a permanent reference sample.
- **Annually:** full review. Retire any class-A samples from books that underperformed commercially (we're calibrating against successful Heartland Fantasy, not all Heartland Fantasy).

## When to expand corpus

- New genres (separate sub-corpus per genre)
- New writing adapters (if studio adds Codex/Gemini/other adapters for Daniel)
- New humanization techniques (Sudowrite, LoRA-style finetunes) — separate class
