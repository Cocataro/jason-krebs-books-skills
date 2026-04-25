# Midjourney → Flux Conversion

Flux.dev handles natural-language prompts almost as well as Midjourney. Migration is mostly about stripping MJ-specific flags and expanding abbreviated tag-style phrasing.

## Direct conversion rules

| Midjourney | Flux |
|---|---|
| `--ar 2:3` | Add "2:3 aspect ratio" to prompt, or set in generation params |
| `--ar 16:9` | "16:9 landscape aspect ratio" |
| `--stylize 300` | Omit — Flux has its own default stylization |
| `--style raw` | Add "minimal stylization, natural lighting" |
| `--no [thing]` | Move to Flux's negative prompt (if supported by UI) or describe the absence in prompt |
| `--chaos 50` | Generate multiple variants; Flux doesn't use this flag |
| `--weird 250` | "surreal, unconventional composition" |
| `--ar 3:2 --stylize 500` | "3:2 portrait, highly stylized painterly aesthetic" |
| MJ's comma-separated tag lists | Convert to flowing sentences for best Flux results |

## Example

### MJ
```
A Heartland Fantasy inn, golden hour, warm amber lighting, a black cat with golden eyes on a threshold, snowy path, painterly illustration, studio ghibli style, character + place composition, --ar 2:3 --stylize 300 --no text
```

### Flux (natural language)
```
A Heartland Fantasy illustration of a warm inn at golden hour, with amber lamplight spilling through the windows. A black cat with luminous golden eyes sits on the threshold, watching a snow-dusted path. Painterly brush texture, Studio Ghibli storybook aesthetic for adults. Character and place composition, 2:3 portrait aspect ratio. No text, no signature. Highly detailed foreground, soft background.
```

### Flux (more concise)
```
Heartland Fantasy inn at golden hour. Warm amber lamplight through small-paned windows. Black cat with golden eyes on threshold, snow-dusted path. Painterly illustration, Studio Ghibli aesthetic, 2:3 portrait.
```

Both work. Flux is forgiving; use whichever reads more naturally to you.

## What Flux does differently from MJ

- **No default stylization curve.** MJ auto-romanticizes; Flux is more literal. Add "romantic lighting" or "dreamy atmosphere" explicitly if you want it.
- **Text rendering is better in Flux Pro** than MJ — but still not as good as Ideogram for typography.
- **More photoreal by default.** Explicitly state "illustration, painterly, not photorealistic" if MJ's instinct was to de-photo it.
- **Longer prompts OK.** Flux handles 100+ word prompts well. MJ caps at ~60 effective tokens.

## Seed + reproducibility

Flux supports `seed` parameter. Log the seed + full prompt for any image that goes into ideation archive — you can regenerate variants from the same seed.

## Common MJ → Flux pitfalls

- Forgetting to remove `--ar` flag → Flux reads it as literal text
- Over-reliance on MJ's auto-warmth → Flux output looks cold without explicit palette tokens
- Copying MJ's tag-heavy style → works but misses Flux's natural-language advantage
- Missing negative prompt → Flux may still produce AI fingerprints without suppression

## Batch generation for ideation

Generate 4–8 variants per prompt. Pick the best 1–3. Feed the best back into the prompt as inspiration. Iterate.
