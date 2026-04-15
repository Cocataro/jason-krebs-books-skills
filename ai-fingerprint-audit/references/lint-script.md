# In-House Lint Script (D2–D9)

Python script Thomas runs on every chapter before sending to Pangram/GPTZero. Free. Fast. Catches the deterministic fingerprints.

## Setup

Create `scripts/ai_lint.py` in the vault or studio tools repo:

```python
#!/usr/bin/env python3
"""
AI Fingerprint Lint — D2 through D9
Runs on a single chapter markdown/gdoc-export file.
Outputs pass/fail per dimension + specific flagged lines.
"""
import re
import sys
import json
import statistics
from pathlib import Path

# --- Tier 1 banned vocabulary ---
TIER_1_WORDS = [
    r'\bdelve\b', r'\btapestry\b', r'\btestament\b', r'\blandscape\b',
    r'\brealm\b', r'\becosystem\b', r'\bframework\b', r'\bparadigm\b',
    r'\bsynergy\b', r'\binterplay\b', r'\blabyrinth\b', r'\bmosaic\b',
    r'\bsymphony\b', r'\bkaleidoscope\b', r'\bmyriad\b', r'\bplethora\b',
    r'\bnavigate\b', r'\bleverage\b', r'\bharness\b', r'\butilize\b',
    r'\bstreamline\b', r'\bfoster\b', r'\bbolster\b', r'\bgarner\b',
    r'\bunderscore\b', r'\bshowcase\b', r'\bembody\b', r'\bresonate\b',
    r'\bpivotal\b', r'\bcrucial\b', r'\bvibrant\b', r'\brobust\b',
    r'\bprofound\b', r'\bintricate\b', r'\bmeticulous(ly)?\b',
    r'\benduring\b', r'\bunwavering\b', r'\bmultifaceted\b',
    r'\bcomprehensive\b', r'\bgroundbreaking\b', r'\brenowned\b',
    r'\bnestled\b',
]
TIER_1_PHRASES = [
    r'it is worth noting', r'it bears mentioning', r'importantly',
    r'notably', r'interestingly', r'in essence', r'at its core',
    r'in the realm of', r'in the heart of', r'navigating the complexities',
    r'a testament to', r'stands as a testament', r'paints a picture of',
    r'weaves a tapestry', r'rich tapestry of', r'more than just',
    r"in today's [a-z]+ landscape", r'at the end of the day',
]

TIER_2_WORDS = [
    r'\bjourney\b', r'\bquest\b', r'\bdepth\b', r'\bessence\b',
    r'\bexplore\b', r'\bembrace\b', r'\buncover\b', r'\bunveil\b',
    r'\btranscend\b', r'\btransform\b', r'\billuminate\b',
    r'\btimeless\b', r'\bseamless\b', r'\bdynamic\b', r'\binnovative\b',
    r'\btransformative\b', r'\binvaluable\b', r'\bunparalleled\b',
    r'\bintegral\b', r'\bnuanced\b', r'\bthoughtful\b', r'\bintentional\b',
    r'\bcurated\b', r'\bquietly\b', r'\bdeeply\b', r'\bfundamentally\b',
    r'\bremarkably\b', r'\barguably\b', r'\bcertainly\b',
    r'\bundoubtedly\b', r'\bindeed\b', r'\bundeniably\b',
]

TIER_3_COZY_WORDS = [
    r'\bethereal\b', r'\bluminous\b', r'\bshimmering\b', r'\bgossamer\b',
    r'\bverdant\b', r'\bwhimsical\b', r'\benchanting\b', r'\bmystical\b',
    r'\botherworldly\b', r'\bhoneyed\b', r'\bancient\b', r'\btimeless\b',
]

TIER_3_ARCHETYPAL_FILLERS = [
    r'\bancient forest\b', r'\btimeless village\b', r'\bforgotten recipe\b',
    r'\bforgotten lore\b', r'\bhidden glade\b',
]

# --- Banned paragraph openers ---
BANNED_OPENERS = [
    'Moreover', 'Furthermore', 'Additionally', 'Certainly', 'Indeed',
    'Importantly', 'Ultimately', 'In essence', 'That said',
    'In conclusion', 'To sum up', 'All in all', 'On the whole',
    'As such', 'Therefore',
]

# --- Copula-avoidance ---
COPULA_SUBSTITUTES = [
    r'\bserves as\b', r'\bstands as\b', r'\bmarks\b',
    r'\brepresents\b', r'\bembodies\b', r'\bfeatures\b',
    r'\bboasts\b', r'\bconstitutes\b',
]
PLAIN_COPULAS = [r'\b(is|are|was|were)\b']

# --- Patterns ---
NOT_X_Y_PATTERNS = [
    r"not [a-z ]{1,40}[—\-–][a-z ]{1,40}",
    r"not only [^,]{1,60}, but (?:also )?",
    r"not because [^,]{1,60}, but because",
]
PARTICIPLE_TAIL = r',\s+\w+ing [^.]{10,60}\.'
EM_DASH = r'—'
TRICOLON = r'(\w+,\s+\w+,\s+and\s+\w+)'
ADJ_STACK = r'\b\w+ and \w+\b'  # crude; tune per run

def count_matches(text, patterns):
    return sum(len(re.findall(p, text, re.IGNORECASE)) for p in patterns)

def check_chapter(path):
    text = Path(path).read_text()
    wc = len(text.split())
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    sentences = re.split(r'(?<=[.!?])\s+', text)

    results = {
        'word_count': wc,
        'paragraph_count': len(paragraphs),
        'sentence_count': len(sentences),
    }

    # D2 — banned vocab
    t1 = count_matches(text, TIER_1_WORDS + TIER_1_PHRASES)
    t2 = count_matches(text, TIER_2_WORDS)
    t3 = count_matches(text, TIER_3_COZY_WORDS + TIER_3_ARCHETYPAL_FILLERS)
    results['D2_tier1'] = t1
    results['D2_tier2'] = t2
    results['D2_tier3'] = t3
    results['D2_verdict'] = 'FAIL' if t1 >= 3 or t2 >= 6 else ('WATCH' if t1 > 0 or t2 > 2 or t3 > 3 else 'PASS')

    # D3 — sentence opener diversity
    openers = [s.strip().split()[0] if s.strip().split() else '' for s in sentences]
    unique_per_100 = (len(set(openers)) / max(1, len(openers))) * 100
    banned_paragraph_openers = sum(1 for p in paragraphs if p.strip().split() and p.strip().split()[0] in BANNED_OPENERS)
    results['D3_unique_openers_per_100'] = round(unique_per_100, 1)
    results['D3_banned_paragraph_openers'] = banned_paragraph_openers
    results['D3_verdict'] = 'FAIL' if unique_per_100 < 45 or banned_paragraph_openers >= 2 else ('WATCH' if unique_per_100 < 60 or banned_paragraph_openers > 0 else 'PASS')

    # D4 — em-dash & typography
    em_dash_count = len(re.findall(EM_DASH, text))
    em_dash_per_1k = (em_dash_count / wc) * 1000
    stray_unicode = bool(re.search(r'[→⇒✓✗★☆]', text))
    results['D4_em_dash_per_1k'] = round(em_dash_per_1k, 1)
    results['D4_stray_unicode'] = stray_unicode
    results['D4_verdict'] = 'FAIL' if em_dash_per_1k > 4 else ('WATCH' if em_dash_per_1k > 2 or stray_unicode else 'PASS')

    # D5 — "not X — Y" patterns
    not_x_y = count_matches(text, NOT_X_Y_PATTERNS)
    results['D5_not_x_y_count'] = not_x_y
    results['D5_verdict'] = 'FAIL' if not_x_y >= 3 else ('WATCH' if not_x_y == 2 else 'PASS')

    # D6 — tricolons
    tricolons = count_matches(text, [TRICOLON])
    tricolons_per_1500 = (tricolons / wc) * 1500
    results['D6_tricolons_per_1.5k'] = round(tricolons_per_1500, 1)
    results['D6_verdict'] = 'FAIL' if tricolons_per_1500 >= 3 else ('WATCH' if tricolons_per_1500 >= 2 else 'PASS')

    # D7 — paragraph-length chaos
    para_lengths = [len(p.split()) for p in paragraphs]
    if len(para_lengths) > 1:
        mean_pl = statistics.mean(para_lengths)
        stdev_pl = statistics.stdev(para_lengths)
        chaos = stdev_pl / mean_pl if mean_pl > 0 else 0
    else:
        chaos = 0
    results['D7_paragraph_chaos'] = round(chaos, 2)
    results['D7_verdict'] = 'FAIL' if chaos < 0.4 else ('WATCH' if chaos < 0.6 else 'PASS')

    # D8 — copula-avoidance ratio
    sub_count = count_matches(text, COPULA_SUBSTITUTES)
    plain_count = count_matches(text, PLAIN_COPULAS)
    ratio = sub_count / plain_count if plain_count > 0 else 0
    results['D8_copula_ratio'] = round(ratio, 3)
    results['D8_verdict'] = 'FAIL' if ratio > 0.15 else ('WATCH' if ratio > 0.05 else 'PASS')

    # D9 — participle tails
    tails = len(re.findall(PARTICIPLE_TAIL, text))
    tails_per_1k = (tails / wc) * 1000
    results['D9_participle_tails_per_1k'] = round(tails_per_1k, 1)
    results['D9_verdict'] = 'FAIL' if tails_per_1k > 5 else ('WATCH' if tails_per_1k > 2 else 'PASS')

    # Overall lint verdict
    fail_dimensions = [k for k, v in results.items() if k.endswith('_verdict') and v == 'FAIL']
    results['LINT_OVERALL'] = 'FAIL' if fail_dimensions else 'PASS'
    results['failed_dimensions'] = fail_dimensions

    return results

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ai_lint.py <chapter_file.md>")
        sys.exit(1)
    results = check_chapter(sys.argv[1])
    print(json.dumps(results, indent=2))
```

## Running

```bash
python3 scripts/ai_lint.py Crossroads-Book-1-Ch01.md
```

Outputs JSON with every dimension's score + verdict + overall pass/fail.

## Flagged-line extraction (helpful for kick-backs to Daniel)

Extend the script to output specific flagged sentences per failed dimension — makes the rewrite brief actionable.

```python
def extract_flagged_lines(text, patterns, label):
    flags = []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    for i, s in enumerate(sentences):
        for p in patterns:
            if re.search(p, s, re.IGNORECASE):
                flags.append({'sentence_idx': i, 'label': label, 'text': s.strip()[:120]})
                break
    return flags
```

Call this with TIER_1_WORDS, NOT_X_Y_PATTERNS, PARTICIPLE_TAIL regex to surface the specific sentences. Output a "here are the lines that tripped D2/D5/D9" list that Daniel gets in the kick-back.

## Integration with Thomas's workflow

1. Thomas wakes on chapter delivery (event).
2. Run `ai_lint.py` on the chapter file.
3. Parse JSON output.
4. If OVERALL = FAIL, gather flagged lines + post to the book's issue comment: "Daniel: lint failed. D5 count 4 — here are the lines. D9 count 7 — here are the lines. Please revise before I line-edit."
5. If OVERALL = PASS, proceed to Pangram API call, then GPTZero, then line edit.

## Why in-house lint first

- Free + fast (sub-second on a chapter)
- Catches the deterministic fingerprints that detectors also catch — but cheaper
- Actionable flags (specific sentences, not just "this chapter is 35% AI")
- Daniel learns the patterns from repeated kick-backs, which makes later drafts cleaner

## Maintenance

- Banned-word lists in this script mirror `banned-vocabulary.md` — keep in sync on update.
- Regex patterns may need false-positive suppression for cozy fantasy (e.g., "ancient" used descriptively in dialogue is different from "ancient" as AI-filler).
- Quarterly review + tune.

## Possible enhancements

- POS-tagging (via spaCy) to detect participle tails more accurately
- Sentence-embedding similarity checks for elegant-variation pattern
- Character-voice TTR differentiation check (requires tagged speaker lines)
- Paragraph-embedding clustering to flag "outline-shaped prose" structural tell

These go in the backlog. Ship the regex-level version first; add only when specific failure modes slip through.
