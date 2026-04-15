# Model Comparison (April 2026)

Current state-of-play for cozy fantasy imagery generation.

| Model | Cost | Quality (cozy) | Prompt style | Strengths | Weaknesses |
|---|---|---|---|---|---|
| **Flux.dev** | Free local; $0.05/img fal.ai | ★★★★★ | Natural language | Best overall for cozy painterly output; handles MJ-style prompts; excellent LoRA base | Requires 16GB+ VRAM local; generation slower than SDXL |
| **Flux Pro / Flux Ultra** | $0.05–$0.10/img | ★★★★★ | Natural language | Best in class for detail + coherence | Paid per image; no local option |
| **Midjourney v6.1 / v7** | $30/mo Standard | ★★★★★ | MJ-specific (`--ar`, `--stylize`) | Curated aesthetic; consistent warm painterly quality | Closed model; licensing concerns; no local |
| **Ideogram 2.0** | $20/mo Plus | ★★★★ | Natural language | Best text-in-image rendering; decent cozy painterly | Smaller community; fewer fine-tunes |
| **SDXL (+ cozy LoRA)** | Free local | ★★★★ | Tag-weight + negatives | Fast; huge checkpoint ecosystem; customizable | Needs explicit prompt tuning; more AI fingerprints without LoRA |
| **SD 1.5 (+ tuned checkpoint)** | Free local | ★★★ | Tag-weight + heavy negatives | Runs on older GPUs; massive LoRA library | Older; more hand/face issues; needs strong negatives |
| **Stable Cascade** | Free local | ★★★ | Natural language | Decent quality | Less community adoption |

## By task

- **Moodboard / quick ideation:** Flux.dev (local) or Midjourney
- **Illustrator brief reference sheet:** Flux.dev + LoRA on illustrator style
- **Marketing atmospheric shot:** Flux.dev
- **Character study / face reference:** Flux.dev + ControlNet for pose consistency
- **Typography mockups:** Ideogram
- **Batch generation (100+):** SDXL local
- **Low-hardware situations:** SD 1.5 + SDXL-Lightning

## Hardware guidance

- **16GB+ VRAM (e.g., RTX 4080/4090, A100):** run Flux.dev locally
- **12GB VRAM (RTX 3060/4070):** SDXL locally, Flux via API or quantized
- **8GB VRAM (RTX 2080, 3060 8GB):** SD 1.5 locally, SDXL with tiling, Flux via API only
- **No GPU / CPU only:** API-only (Midjourney, Flux Pro via fal.ai, Ideogram)

## Cost math for a 6-book series launch

Rough estimates for generating enough imagery across the series:

| Asset type | Count across 6 books | Cost (Flux via API) | Cost (local) |
|---|---|---|---|
| Moodboards (50/cover × 6) | 300 | $15 | $0 |
| Marketing atmospherics (20/book × 6) | 120 | $6 | $0 |
| Character references | 50 | $2.50 | $0 |
| A+ Content atmospherics | 40 | $2 | $0 |
| **Total** | **510** | **~$25** | **$0** |

Plus ~$30/mo Midjourney if team prefers that aesthetic for some work.

**Conclusion:** AI imagery for ideation + marketing is cheap. The budget lever is ILLUSTRATOR fees ($400–$1,200/cover × 6 = $2,400–$7,200) — not image gen costs.
