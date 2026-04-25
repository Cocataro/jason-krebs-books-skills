# Midjourney → SDXL Conversion

SDXL needs more explicit prompt construction than Flux or MJ. Weight-based syntax, aggressive negatives, tuned checkpoints + LoRAs.

## Syntax rules

| Concept | MJ | SDXL |
|---|---|---|
| Emphasis | MJ handles via context | `(token:1.2)` for moderate, `(token:1.5)` for strong |
| De-emphasis | `--no token` | Add to negative prompt; use `[token]` for slight reduction |
| Aspect ratio | `--ar 2:3` | Set in generation width/height (e.g., 832×1216) |
| Style | Implicit via style transfer | Explicit via LoRA + keyword like "in the style of X" |
| Negative | `--no X` | `negative_prompt` field (separate from main prompt) |

## Recommended SDXL checkpoints for Heartland Fantasy

- **Juggernaut XL** — versatile, handles painterly well with negatives
- **Realvis XL** — tends photoreal; needs "illustration, painterly" weights
- **AnimagineXL** — anime-leaning; mostly avoid for cozy unless specific look
- **Dreamshaper XL** — good painterly baseline
- **Proteus XL** — high detail, artistic
- **Recommended first-try:** Juggernaut XL + Heartland Fantasy LoRA

## Recommended LoRAs

- **Storybook illustration LoRA** (various on CivitAI tagged "storybook," "children's book illustration," "cozy")
- **Studio Ghibli LoRA** (many versions; respect copyright — for internal/moodboard use only)
- **Watercolor / gouache LoRAs** — for painterly feel
- **Custom illustrator LoRA** — trained on retained illustrator's work; see `lora-strategy.md`

## Conversion example

### MJ
```
The Crossroads Inn at dusk, warm amber lamplight through small-paned windows, cat on the doorstep with golden eyes, snowy path, Heartland Fantasy illustration, warm palette, painterly, studio ghibli, --ar 2:3 --stylize 400 --no text, deformed, extra fingers
```

### SDXL (main prompt)
```
Heartland Fantasy illustration, (the crossroads inn at dusk:1.2), (warm amber lamplight:1.2), small-paned windows, (black cat with golden eyes on doorstep:1.1), snow-dusted path, painterly, (studio ghibli aesthetic:1.3), warm palette of amber and forest green, (single warm light source:1.1), hand-painted texture, visible brush strokes, detailed illustration, masterpiece, 8k
```

### SDXL (negative prompt)
```
photo, photograph, photorealistic, (cgi:1.2), (3d render:1.2), anime, manga, plastic skin, glossy, oversaturated, chromatic aberration, (extra fingers:1.5), (bad hands:1.5), (deformed:1.3), (uncanny:1.2), watermark, signature, text, (cropped:1.2), blurry, low quality, jpeg artifacts, noise, grain, underexposed, overexposed, romantasy, sultry, heroic pose, sword, battle, neon, cyberpunk
```

### Generation params
- Width: 832, Height: 1216 (close to 2:3)
- Sampler: DPM++ 2M Karras
- Steps: 30–40
- CFG: 6.5–8.0
- LoRA: Heartland Fantasy illustration LoRA at 0.7–0.9 weight

## SDXL pitfalls

- **Without aggressive negatives:** SDXL produces photoreal output that fails the Heartland Fantasy aesthetic.
- **Without an illustration LoRA:** output drifts toward 3D-render look.
- **Over-weighting emphasis (e.g., `(x:2.0)`):** produces burned / distorted output. Cap at 1.5 unless you know what you're doing.
- **Skipping negatives on hands/fingers:** SDXL struggles with hands. Always include `(bad hands:1.5)`, `(extra fingers:1.5)` in negatives.

## When SDXL beats Flux

- Faster batch generation on available GPU
- Huge LoRA ecosystem for style variety
- Better community-tuned checkpoints for specific looks
- Cheaper at scale for 100+ images

## When SDXL loses to Flux

- Natural-language prompt understanding
- Coherent text in images (but still worse than Ideogram)
- Painterly aesthetic without LoRA tuning
- Hand/face anatomy without careful negatives

## Model flexibility

If SDXL isn't giving you the cozy result you want, switch to Flux. If Flux is too slow for batch work, switch to SDXL. No loyalty to a single model — loyalty to output quality.
