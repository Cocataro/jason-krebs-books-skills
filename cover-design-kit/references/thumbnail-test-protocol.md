# Thumbnail Test Protocol

Run at every milestone: concept sketch, pre-type composite, final.

## Export sizes

1. **150px wide** — Amazon browse thumbnail. Primary test size.
2. **80px wide** — mobile category scroll. Worst-case legibility.
3. **300px wide** — product page. Verifies design still holds up larger.

## Pass criteria

- [ ] Title legible in < 1 second at 150px
- [ ] Genre reads as Heartland Fantasy in < 2 seconds at 150px (test with 3+ non-team readers)
- [ ] Placed next to prior Book covers — reads as same series?
- [ ] Placed next to prior Book covers — reads as different book (not accidentally identical)?
- [ ] Placed next to 3 top-20 Heartland Fantasy comps — holds its own or disappears?
- [ ] Warm palette survives sRGB compression + Amazon JPEG pass
- [ ] 80px mobile scroll: title + figure + genre all still communicate

## Failure modes

- Title too thin at 150px — up-weight stroke or increase scale
- Figure too small at 80px — foreground figure, decrease background detail
- Palette washes out after JPEG compression — increase saturation on warm tones
- Series-sibling test fails: typography or palette drift — bring back to series system

## Fail → back to composite

Any single failure blocks sign-off. Do not move to final delivery with a thumbnail test fail.

## Reference shelf

Compare the candidate cover at 150px against a curated grid of:
- Current Amazon Heartland Fantasy Top 20 (refresh monthly)
- Anchor comps: *Legends & Lattes*, *Bookshops & Bonedust*, *Emily Wilde*, *Tomes & Tea*, *The Spellshop*, *The Very Secret Society of Irregular Witches*, *The House in the Cerulean Sea*
- Prior Books in the series (for consistency)
