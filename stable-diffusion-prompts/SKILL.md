---
name: stable-diffusion-prompts
description: Adapts Midjourney-style prompts to Stable Diffusion variants (Flux.dev, Flux Pro, SDXL, SD 1.5) for Heartland Fantasy imagery. Includes syntax conversion, model-specific tuning, Heartland Fantasy palette presets, LoRA recommendations, and a hard guardrail that AI-generated pixels NEVER ship as final book covers. Used by Cover Art Director (ideation, moodboards, illustrator references) and Marketing (atmospheric imagery, per marketing-imagery-kit rules).
---

# Stable Diffusion Prompts

Adapt the studio's Midjourney prompt library (on JAS-4 comments) for Flux / SDXL / SD 1.5. Pick the right model for the job.

See `references/model-comparison.md`, `references/mj-to-flux.md`, `references/mj-to-sdxl.md`, `references/heartland-fantasy-presets.md`, `references/lora-strategy.md`.

## HARD GUARDRAIL (non-negotiable)

**No AI-generated pixels ship as the final book cover on Amazon. Ever.** This applies to every model (Midjourney, Flux, SDXL, SD 1.5, any future model). AI imagery is for ideation, marketing atmospherics, and illustrator reference only — not the product-page cover or the A+ Content title banner.

See the `marketing-imagery-kit` skill for the detailed acceptable-use rules.

## Model selection by task

| Task | Best model | Why |
|---|---|---|
| Moodboard / composition test | **Flux.dev** (local) | Best quality-to-cost, free local, handles natural-language MJ-style prompts well |
| Fast iteration, 10–20 variants | **Flux Pro** (fal.ai ~$0.05/img) or **Midjourney** | Faster feedback loop |
| Typography-in-image mockup | **Ideogram** | Best-in-class text rendering |
| Character study for illustrator | **Flux.dev** + LoRA | Consistent style when LoRA is trained |
| Atmospheric marketing shot (social, newsletter) | **Flux.dev** | Warm cozy aesthetic matches brand |
| Large-batch generation (100+ images) | **SDXL** local | Fastest local if GPU available; more prompt tuning needed |
| Prototyping on low-end hardware | **SD 1.5** + SDXL-Lightning | Runs on older GPUs |

**If a model isn't working for a specific task**, switch. Don't force. Different checkpoints + fine-tunes will perform differently on Heartland Fantasy aesthetics.

## Syntax portability (MJ → SD family)

### MJ prompt example
```
The Crossroads Inn at golden hour, warm interior light spilling through small-paned windows onto a snow-dusted path, cat with golden eyes on the doorstep, Heartland Fantasy illustration, warm palette of amber and forest green, painterly brush texture, studio ghibli style, --ar 2:3 --stylize 300
```

### → Flux.dev (natural language, very close to MJ)
```
A Heartland Fantasy illustration of The Crossroads Inn at golden hour. Warm interior light spills through small-paned windows onto a snow-dusted path. A black cat with golden eyes sits on the doorstep. Warm painterly palette dominated by amber and forest green. Visible brush and pencil texture. Studio Ghibli storybook aesthetic for adults. Portrait composition, 2:3 aspect ratio. Soft focus background, detailed foreground.
```
(Flux handles flowing English better than tag lists.)

### → SDXL (more explicit weights + negatives)
```
Prompt: Heartland Fantasy illustration, (the crossroads inn:1.2), (golden hour:1.1), warm interior lamplight through small-paned windows, snow-dusted path, (black cat with golden eyes on doorstep:1.1), painterly brush texture, (studio ghibli aesthetic:1.2), (warm palette:1.1), amber and forest green, detailed illustration, 8k, masterpiece

Negative: photo, photograph, photorealistic, cgi, 3d render, anime, manga, chromatic aberration, oversaturated, plastic skin, (extra fingers:1.5), (bad hands:1.5), (deformed:1.2), watermark, signature, text, blurry, low quality
```

### → SD 1.5 (even more explicit, aggressive negatives)
Use with heartland-fantasy-tuned checkpoints (e.g., RevAnimated, CyberRealistic with illustration focus). SD 1.5 needs stronger LoRAs and more careful weighting. See `references/mj-to-sdxl.md` for exact adaptation.

## Heartland Fantasy baseline additions (every prompt)

Add these tokens to any Heartland Fantasy prompt, tuned per model:

- Style: `painterly illustration`, `storybook aesthetic`, `studio ghibli for adults`, `Heartland Fantasy cover art`
- Palette: `warm amber and sage green palette`, `single warm light source`, `golden hour`, `hearthfire glow`
- Texture: `visible brush texture`, `pencil underdrawing`, `hand-painted texture`, `no plastic sheen`
- Composition: `character + place composition`, `three-quarter or back view figure`, `inviting not confrontational`

## Heartland Fantasy AVOIDANCE list (add to negatives)

- `photorealistic, photograph, photo, cgi, 3d render, plastic, glossy, anime, manga`
- `romantasy, sultry, provocative pose, seductive` (wrong genre)
- `heroic pose, battle, sword raised, vast vista, apocalyptic` (wrong genre)
- `neon, cyberpunk, cityscape, leather jacket` (wrong genre)
- `watermark, signature, text on image, cropped, blurry, low quality`
- `deformed, extra fingers, bad hands, missing limbs, melted face, uncanny` (AI fingerprint suppression)

## LoRA strategy

- **Train a LoRA on your retained illustrator's style** once Sofia locks one.
- Use for: consistent in-series moodboards, illustrator reference sheets, character studies, marketing atmospherics.
- Base model: Flux.dev is current best for LoRA training quality.
- Training data: 30–50 curated images from the illustrator's Heartland Fantasy work, with consent.
- Never ship LoRA-generated final covers (still governed by the HARD GUARDRAIL).

See `references/lora-strategy.md` for training + use specifics.

## Quality audit before using any generated image

Same AI-fingerprint checklist as covers:
- [ ] Fingers / hands anatomically correct
- [ ] Faces symmetric (or face obscured / three-quarter back if uncertain)
- [ ] No garbled text within image
- [ ] Architecture lines coherent
- [ ] Scene-consistent shadow direction
- [ ] No "AI shimmer" overexposed highlights
- [ ] No plastic skin

Fail any → regenerate or reject.

## Workflow

1. Source a Midjourney prompt from JAS-4 or compose new.
2. Select model per task (table above).
3. Adapt syntax (see `references/mj-to-flux.md` or `references/mj-to-sdxl.md`).
4. Add Heartland Fantasy baseline tokens.
5. Add Heartland Fantasy negatives.
6. Generate batch of 4–8.
7. AI-fingerprint audit each image.
8. Select 1–3 winners for the task.
9. Log the final prompt + seed + model in the marketing/moodboard archive for reproducibility.

## Model version flexibility (Board policy)

If a specific SD variant produces better results for a given task, use it. No dogma about which checkpoint. Evaluate on output quality against the Heartland Fantasy visual grammar, not the model's popularity.
