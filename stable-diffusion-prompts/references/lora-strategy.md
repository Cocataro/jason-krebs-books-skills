# LoRA Strategy

LoRAs are low-rank adaptations that specialize a base model (Flux, SDXL) on a specific style, character, or concept. For Jason Krebs Books, the highest-leverage LoRA is a **custom illustrator-style LoRA** trained on the retained illustrator's work.

## Why it matters

Once Sofia Reyes (Cover Art Director) locks a human illustrator for the series, you want to generate moodboards, character references, and marketing imagery that LOOKS like the illustrator's style — so every touchpoint across the series reads as one visual system.

Without a LoRA: every AI-generated image drifts toward Midjourney-average or SDXL-default cozy, which won't match the illustrator.

With a LoRA: every AI image reads as "same world" as the covers — even when readers only see the AI image (marketing atmospherics), the vibe is consistent.

## Training

### Data collection (with consent)
- 30–50 curated images from the illustrator's Heartland Fantasy work
- Minimum: 20 images with diverse compositions (characters, interiors, exteriors, still lifes)
- High-resolution originals (1024×1024+ minimum)
- Consistent style: same illustrator's "voice"
- **License:** training requires illustrator's explicit written consent. Include in the illustrator retainer contract.

### Training base model choices
- **Flux.dev LoRA** — current best quality; 16GB+ VRAM recommended
- **SDXL LoRA** — faster training, smaller compute requirement; still good quality
- Avoid SD 1.5 LoRAs for new training — older base model

### Training tools
- **Kohya_ss** (open source, SDXL + Flux) — industry standard
- **AI-toolkit** (for Flux specifically)
- **fal.ai LoRA training** (paid service, simpler UX)
- **Replicate LoRA training** (paid service, easy UI)

### Training parameters (rough starting points, SDXL)
- Learning rate: 1e-4
- Epochs: 10–20
- Network dim: 32–64
- Batch size: 1–4 depending on VRAM
- Optimizer: AdamW8bit

Start conservative and validate; over-training destroys flexibility.

### Training cost
- Local with existing GPU: ~2–8 hours
- Cloud (fal.ai, Replicate): ~$5–$25 per training run

## Usage

Apply LoRA at **0.7–0.9 weight** for consistent illustrator-style output. Lower weights (0.4–0.6) for lighter influence. Above 0.9 tends to overfit.

Example SDXL prompt with illustrator LoRA:
```
<lora:crossroads-illustrator-style:0.8> Heartland Fantasy illustration, the crossroads inn at golden hour, warm amber lamplight, (black cat on doorstep:1.1), painterly texture, Studio Ghibli aesthetic, warm palette, 2:3 portrait
```

## Licensing + ethics

- **Consent is non-negotiable.** Never train on an illustrator's work without written permission.
- **Internal use only.** Never distribute the LoRA file publicly. It belongs to the studio + illustrator per contract.
- **Never ship LoRA-generated pixels as final cover.** HARD GUARDRAIL still applies. LoRA just makes the non-cover uses look consistent with the covers.
- **Compensation:** factor LoRA training rights into the illustrator retainer (either as part of the retainer fee or a separate licensing line).
- **Illustrator credit:** when AI imagery with LoRA is used publicly (social, marketing), consider crediting the illustrator for the underlying style (optional but respectful).

## Alternative: style reference without LoRA

If the illustrator doesn't consent to LoRA training (or you want to start before LoRA is trained):

- **Use IP-Adapter** (ControlNet addon) — pass a reference image at generation time, output mimics reference style without permanent model change
- **Use prompt-only consistency:** "in the style of watercolor illustration with visible brush strokes, warm amber palette, Studio Ghibli aesthetic" — never names the illustrator, mimics mood only

Both are less consistent than a trained LoRA but respect the illustrator's IP more fully.

## When LoRA is NOT worth it

- Before a retained illustrator is locked (don't LoRA-train on random illustrators)
- For one-off Book 1 ideation (IP-Adapter is faster)
- If marketing volume is low (<50 atmospheric images expected across the series)

## When LoRA IS worth it

- Retained illustrator across 6-book series (consistency compounds)
- High marketing volume expected (social-heavy launch strategy)
- Multiple pen names eventually under the Jason Krebs umbrella (per-pen-name LoRAs)
- Ongoing ad creative generation (ad rotation is constant; LoRA saves creative hours)
