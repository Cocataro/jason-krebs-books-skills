# Banned Vocabulary — Tier 1 / 2 / 3

Consolidated from: Wikipedia "Signs of AI writing" catalog (2024–2026), `blader/humanizer` skill, `jalaalrd/anti-ai-slop-writing`, Walter Writes 2026 ban list, Jodie Cook's ban list, Kindlepreneur AI-pattern analysis, r/selfpublish + r/ChatGPT community lists. Cross-referenced against Colin Gorrie's rhetorical analysis of AI prose and recent arXiv stylometry research (April 2026).

## Tier 1 — cut on sight

Zero tolerance. If any appear in a chapter, kick back to Daniel. These are the BookTok-flagging instant-callout words.

### Nouns
`delve` (as verb, but listed here for recall), `tapestry`, `testament`, `landscape` (metaphorical), `realm` (metaphorical), `ecosystem` (metaphorical), `framework`, `paradigm`, `synergy`, `interplay`, `labyrinth`, `mosaic`, `symphony` (metaphorical), `kaleidoscope`, `myriad`, `plethora`, `heart of` (as in "in the heart of"), `tapestry of`

### Verbs
`delve`, `navigate` (metaphorical — "navigate complexities"), `leverage`, `harness`, `utilize`, `streamline`, `foster`, `bolster`, `garner`, `underscore`, `showcase`, `embody`, `resonate`, `align`, `craft` (metaphorical — "craft a story"), `weave` (metaphorical — "weave a tale"), `paint` (metaphorical — "paint a picture")

### Adjectives
`pivotal`, `crucial`, `vibrant`, `robust`, `profound`, `intricate`, `meticulous`, `enduring`, `unwavering`, `multifaceted`, `comprehensive`, `groundbreaking`, `renowned`, `nestled`

### Phrases
`it is worth noting`, `it bears mentioning`, `importantly`, `notably`, `interestingly`, `in essence`, `at its core`, `in the realm of`, `in the heart of`, `navigating the complexities of`, `a testament to`, `stands as a testament`, `paints a picture of`, `weaves a tapestry`, `rich tapestry of`, `more than just`, `in today's [X] landscape`, `at the end of the day`

### Rhetorical patterns
- `it's not X — it's Y` / `not X, but Y` / `not just X but Y`
- `not only X, but also Y`
- Fake rhetorical self-question: `The result? A disaster.`
- `despite its challenges` (acknowledge-then-dismiss)
- `from X to Y` where X and Y aren't on the same axis

## Tier 2 — cap at ≤2 per chapter

Use in fiction is possible but AI over-indexes on them. Watch for clustering.

### Nouns
`journey` (metaphorical), `quest` (metaphorical), `chapter of life`, `depth`, `essence`, `tapestry of`, `threads of`, `symphony of`, `dance of`, `realm of possibility`, `commitment`, `testament`

### Verbs
`explore`, `embrace`, `uncover`, `unveil`, `transcend`, `transform`, `illuminate`, `shape`, `mold`, `forge` (metaphorical), `paint` (metaphorical), `chart` (metaphorical), `elevate`, `empower`, `redefine`, `reshape`

### Adjectives
`profound`, `timeless`, `seamless`, `dynamic`, `innovative`, `transformative`, `invaluable`, `unparalleled`, `integral`, `nuanced`, `thoughtful`, `intentional`, `curated`

### Adverbs
`quietly`, `deeply`, `fundamentally`, `remarkably`, `arguably`, `certainly`, `undoubtedly`, `indeed`, `meticulously`, `undeniably`, `truly`, `genuinely`

### Phrases
`serves as a reminder`, `stands as a symbol`, `speaks to`, `captures the essence`, `fosters a sense of`, `offers a glimpse`, `invites us to`, `reminds us that`, `teaches us that`, `reflects on`, `prompts reflection`, `grapples with`, `wrestles with`

## Tier 3 — Heartland Fantasy-specific caps at ≤3 per chapter

Heartland Fantasy legitimately uses warm imagery, but AI over-indexes on these exact adjectives and stacks them. Watch for clustering, especially tricolons of these.

### Adjectives (Heartland Fantasy tells)
`ethereal`, `luminous`, `shimmering`, `gossamer`, `verdant`, `ancient` (as filler modifier), `timeless`, `whimsical`, `enchanting`, `magical` (as filler), `mystical`, `otherworldly`, `rustic`, `weathered`, `worn`, `cozy` (as authorial claim — readers hate this), `warm` (stacked), `golden` (as metaphor), `honeyed`, `flickering`, `crackling`, `dancing` (of flames/shadows)

### Nouns (cozy-overused)
`cottage`, `hearth` (fine sparingly, overused if >3x/chapter), `lantern`, `kettle` (same), `firefly`, `woodsmoke`, `parchment`, `herb`, `sprig`, `glade`, `clearing`, `meadow` (fine sparingly), `tome`, `bookshop`, `tavern`, `inn`

### Phrase patterns (cozy-specific)
- `warm glow of [something]`
- `soft light of [something]`
- `flickering light of the [hearth/lantern/candle]`
- `dancing flames`
- `the smell of [cinnamon / baking bread / old books / rain / tea]` — classic tricolon abuse
- `as if [thing] had a mind of its own` (living-object cliché)
- `the [building] seemed to [verb]` (building-as-character cliché)

### Archetypal filler triad (limit to 1 per chapter)
- `ancient forest`
- `timeless village`
- `forgotten recipe`
- `forgotten lore`
- `hidden glade`
- `secret garden` (outside Burnett context)

>2 of these in one chapter = instant cozy-AI tell.

## Paragraph openers — banned as paragraph starters

Zero tolerance in fiction. Humans almost never open a narrative paragraph with these.

`Moreover`, `Furthermore`, `Additionally`, `Certainly`, `Indeed`, `Importantly`, `Ultimately`, `In essence`, `That said`, `In conclusion`, `To sum up`, `All in all`, `On the whole`, `As such`, `Therefore` (as paragraph opener, not mid-sentence)

## Copula-avoidance substitutes (flag count, not outright ban)

These are legitimate verbs. The problem is AI uses them to *avoid saying "is"*. Track ratio.

Flagged: `serves as`, `stands as`, `marks`, `represents`, `embodies`, `features`, `boasts`, `constitutes`

Ratio: count-of-flagged ÷ count-of-plain-copulas (`is/are/was/were`)
- PASS: ratio <0.05
- FAIL: ratio >0.15

## Adjective-stacking pattern

"the old wooden door, weathered and creaking" — AI's signature two-adjectives-per-noun pattern. Scan for pattern `[adj],? and [adj]` applied to nouns in narration. If >3 per 1k words, flag.

## Participle-tail pattern (D9)

Sentences ending with `, V-ing ...` trailing clause. Extremely common in Claude Heartland Fantasy output.

Examples:
- "She closed the door, the latch clicking softly against the old wood, sealing the room in warm silence." (triple tail — brutal)
- "He smiled, his eyes crinkling, reflecting the firelight." (double tail)

Cap: ≤2 per 1k words. Above that = AI fingerprint.

## Curated good alternatives (for Daniel/Thomas reference)

When replacing banned vocabulary, reach for plain words first, then specific sensory words. Never substitute one banned-list word for another from the same list.

| Instead of | Try |
|---|---|
| delve into | look at, dig into, poke around, get into |
| tapestry | patchwork, weave, layering, mess |
| testament | proof, evidence, record |
| navigate | get through, work past, push past, feel my way |
| pivotal | key, important, big |
| nestled | tucked, sitting, crammed |
| unwavering | stubborn, steady, solid |
| whimsical | odd, funny, out-of-place |
| shimmering | flickering (fine sparingly), glinting, glowing |
| ancient (filler) | old, older than she knew, weathered |

When in doubt: the plainer word is the right word in Heartland Fantasy prose. Readers forgive plain prose; they punish inflated prose.

## Update cadence

This list is updated quarterly based on:
- New Pangram/GPTZero transparency reports
- New r/selfpublish and BookTok callouts
- New arXiv stylometry papers
- New community ban-lists published
