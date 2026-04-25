# Voice-Preservation Metric

Stylometric distance between a generated chapter and the canonical Book 1 voice anchor. Lower = closer to anchor = voice preserved. Higher = voice drift.

## The anchor

The voice anchor is a curated 2,000-word passage of canonical Book 1 prose — the passage Daniel re-reads every Monday. Stored at:

```
/Users/nicoleopcl/Desktop/Vaults/Jason Krebs Books/00-Meta/voice-anchor.md
```

The anchor is canonical per Board + Margaret decision. Changing it requires approval.

## What we measure

Three dimensions of voice, combined into a distance score:

### 1. Sentence-length distribution match
Compute sentence-length histogram (binned: 1–5, 6–10, 11–15, 16–20, 21–30, 31+). Compare to anchor's histogram. Distance = sum of absolute-value differences per bin. Perfect match = 0; maximum mismatch = 2.0.

### 2. Type-token ratio (TTR) ratio match
TTR = unique words / total words. Moving-average TTR over 500-word windows. Compare the chapter's average MATTR to the anchor's. Difference = distance (0 = perfect, >0.1 = significant drift).

### 3. Function-word distribution match
Top 100 function words (the, of, and, to, a, in, that, etc.). Compute frequency per 1,000 words in chapter and in anchor. Cosine similarity between the two vectors. Distance = 1 - cosine (0 = identical, 1 = orthogonal).

### Combined distance score

```
voice_distance = (0.35 * sent_length_dist) + (0.25 * ttr_diff) + (0.40 * function_word_dist)
```

Weights: function words weighted highest (best-studied human-voice signature); sentence length next; TTR least (noisier signal).

Range: 0.0 (identical to anchor — impossible in practice) to ~1.0 (completely different voice).

## Target bands

| Score | Interpretation | Action |
|---|---|---|
| 0.0–0.3 | Very close to anchor | Voice preserved excellently |
| 0.3–0.5 | Within anchor family | Voice preserved; normal variation |
| 0.5–0.7 | Drifting | Watch; review tic deployment + opener variety |
| 0.7–1.0 | Significant drift | Fail voice gate; revert to anchor-heavy process |

**Production ship threshold:** voice_distance ≤0.5 per chapter.
**Experiment revert threshold:** any variant where voice_distance increases by >0.1 over baseline = revert even if rubric improves.

## Implementation

Python script at `scripts/voice_distance.py`:

```python
#!/usr/bin/env python3
import re
import json
import sys
from collections import Counter
from pathlib import Path
from math import sqrt

# Top 100 English function words (simplified list — expand as needed)
FUNCTION_WORDS = set("the of and to a in that is was he for it with as his on be at by i this had not are but from or have an they which one you were her all she there would their we him been has when who will more no if out so said what up its about into than them can only other new some could time these two may then do first any my now such like our over man me even most made after also did many before must through back years where much your way well down should because each just those people mr how too little state good very make world still own see men work long get here between both life being under never day same another know while last might us great old year off come since against go came right used take three states".split())

def read_text(path):
    return Path(path).read_text()

def sentence_length_histogram(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    lengths = [len(s.split()) for s in sentences if s.strip()]
    bins = {'1-5': 0, '6-10': 0, '11-15': 0, '16-20': 0, '21-30': 0, '31+': 0}
    for l in lengths:
        if l <= 5: bins['1-5'] += 1
        elif l <= 10: bins['6-10'] += 1
        elif l <= 15: bins['11-15'] += 1
        elif l <= 20: bins['16-20'] += 1
        elif l <= 30: bins['21-30'] += 1
        else: bins['31+'] += 1
    total = sum(bins.values()) or 1
    return {k: v/total for k, v in bins.items()}

def matttr(text, window=500):
    words = re.findall(r"\b\w+\b", text.lower())
    if len(words) < window:
        return len(set(words)) / max(1, len(words))
    scores = []
    for i in range(len(words) - window + 1):
        w = words[i:i+window]
        scores.append(len(set(w)) / window)
    return sum(scores) / len(scores) if scores else 0

def function_word_vector(text):
    words = re.findall(r"\b\w+\b", text.lower())
    total = len(words)
    counts = Counter(w for w in words if w in FUNCTION_WORDS)
    return {w: counts.get(w, 0) / total * 1000 for w in FUNCTION_WORDS}

def histogram_distance(h1, h2):
    return sum(abs(h1[k] - h2[k]) for k in h1)

def cosine_distance(v1, v2):
    keys = set(v1) | set(v2)
    dot = sum(v1.get(k, 0) * v2.get(k, 0) for k in keys)
    norm1 = sqrt(sum(v1.get(k, 0)**2 for k in keys))
    norm2 = sqrt(sum(v2.get(k, 0)**2 for k in keys))
    cos = dot / (norm1 * norm2) if (norm1 * norm2) > 0 else 0
    return 1 - cos

def voice_distance(chapter_path, anchor_path):
    ch = read_text(chapter_path)
    an = read_text(anchor_path)
    sent_dist = histogram_distance(sentence_length_histogram(ch), sentence_length_histogram(an))
    ttr_diff = abs(matttr(ch) - matttr(an))
    fw_dist = cosine_distance(function_word_vector(ch), function_word_vector(an))
    combined = 0.35 * sent_dist + 0.25 * ttr_diff + 0.40 * fw_dist
    return {
        'sentence_length_distance': round(sent_dist, 3),
        'ttr_difference': round(ttr_diff, 3),
        'function_word_distance': round(fw_dist, 3),
        'combined_voice_distance': round(combined, 3),
    }

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: voice_distance.py <chapter.md> <anchor.md>")
        sys.exit(1)
    result = voice_distance(sys.argv[1], sys.argv[2])
    print(json.dumps(result, indent=2))
```

## Running

```bash
python3 scripts/voice_distance.py sandbox/chapter-1.md /Users/nicoleopcl/Desktop/Vaults/Jason\ Krebs\ Books/00-Meta/voice-anchor.md
```

Outputs the three sub-distances + combined score.

## Per-book anchor drift

The anchor is Book 1 prose. As the series progresses, a Book 4 voice-distance reading against Book 1 anchor is expected to increase slightly (voice legitimately matures). Track anchor-distance per-book.

If anchor-distance rises monotonically across books: normal voice evolution.
If anchor-distance rises then falls: indicates editorial correction.
If anchor-distance rises sharply between books: investigate — is Daniel drifting, or is the outline pushing voice?

## Supplemental metrics (per `experiment-design.md`)

Beyond the combined distance, measure:

- **Tic deployment count** — count of POV character's documented tics deployed per chapter (target ≥3)
- **Character-voice TTR differentiation** — for dialogue-heavy scenes, measure TTR variance across speakers (target >0.05)

These are additional voice signals not captured by stylometric distance alone.

## When the metric disagrees with human judgment

If a chapter has low voice distance (0.3) but Margaret's read says "feels off":
- Trust Margaret. Voice has dimensions the stylometric metric doesn't capture (emotional beat, dialogue rhythm, character interiority).
- Add notes about what Margaret caught; feed into future dimension research (maybe add an emotional-beat metric in a future cycle).

If a chapter has high voice distance (0.6) but Margaret's read says "feels exactly right":
- Investigate. The anchor may be under-representative (only one mood of Briar).
- Consider expanding or splitting the anchor (different moods / POVs).
- Don't reject the chapter over the metric alone.

## Anchor expansion (future)

When Book 1 is fully drafted and Margaret-approved, consider expanding the anchor from one 2,000-word passage to:
- 3 anchor passages covering different Briar moods (contemplative, wry, urgent)
- Chapter scores measured against the closest-matching anchor

Requires Board approval.

## Calibration

Similar to the rubric, calibrate this metric against the 5 human Heartland Fantasy comps:
- Compute voice-distance between Book 1 anchor and each comp author's chapters
- Expect 0.4–0.6 range (different but genre-adjacent voices)
- Any variant that pushes Daniel's output to ~0.5 distance is drifting toward comp-author voice, not toward Jason Krebs's canonical voice

## Cost

- Running the voice-distance script: free (pure Python, no API)
- Anchor storage: ~5 KB
- Marginal cost per chapter: zero
