# Asset Naming + Archive Convention

For every marketing image, AI-generated or otherwise.

## File naming

```
[BookN_or_Series]_[Surface]_[Type]_[Date]_[Model]_v[N].ext
```

Examples:
- `Book1_Instagram_Atmospheric_2026-04-20_Flux.dev_v1.png`
- `Series_Newsletter_Hero_2026-05-15_SDXL_v2.png`
- `Book2_AmazonAds_Background_2026-06-01_Flux.dev_v3.png`
- `Book1_Pinterest_Moodboard_2026-04-20_Midjourney_v1.png` (private moodboard, internal)

## Folder structure (vault)

```
04-Marketing/
├── Imagery/
│   ├── _Templates/            # Reusable templates (Canva, Affinity, etc.)
│   ├── _Prompts/              # Prompt archive (separate from images for text search)
│   ├── Book-1/
│   │   ├── Social/
│   │   │   ├── Instagram/
│   │   │   ├── TikTok/
│   │   │   ├── Twitter/
│   │   │   └── Pinterest/
│   │   ├── Email/
│   │   ├── Ads/
│   │   │   ├── Amazon/
│   │   │   ├── Meta/
│   │   │   └── BookBub/
│   │   └── ARC/
│   ├── Book-2/ ... Book-6/
│   └── Series-Level/          # Cross-book imagery
```

## Metadata sidecar

For every AI-generated image, save a `.meta.json` sidecar:

```json
{
  "filename": "Book1_Instagram_Atmospheric_2026-04-20_Flux.dev_v1.png",
  "generated": true,
  "model": "Flux.dev",
  "model_version": "1.0",
  "prompt": "A Heartland Fantasy illustration of a steaming mug of tea...",
  "negative_prompt": "photo, photograph, photorealistic, extra fingers...",
  "seed": 1234567890,
  "sampler": "DPM++ 2M",
  "cfg_scale": 7.5,
  "steps": 30,
  "lora": "crossroads-illustrator-style-v1 at 0.8 weight",
  "date": "2026-04-20",
  "surface": "Instagram",
  "book": "The Crossroads Inn - Book 1",
  "disclosure_applied": true,
  "notes": "Atmospheric post for launch week teaser"
}
```

Allows reproducibility and auditing.

## Prompt archive

Keep a separate archive at `04-Marketing/Imagery/_Prompts/`:

```
_Prompts/
├── inn-exteriors.md           # Reusable prompts for inn exterior shots
├── character-studies.md       # Character reference prompts
├── still-lifes.md             # Food / drink / object prompts
├── seasonal-variations.md     # Book N seasonal palette prompts
├── atmospheric-moods.md       # Generic cozy mood prompts
└── archive-by-book/
    ├── book-1-launch-week-prompts.md
    ├── book-2-launch-week-prompts.md
    └── ...
```

When an image is saved, if its prompt is reusable or notable, add to the prompt archive.

## SQLite (optional)

If marketing analytics require it, log to a `marketing_assets` table:

```sql
CREATE TABLE marketing_assets (
  id INTEGER PRIMARY KEY,
  book_id INTEGER REFERENCES books(id),
  series_id INTEGER REFERENCES series(id),
  surface TEXT,               -- 'instagram', 'newsletter', 'amazon_ads', etc.
  asset_type TEXT,            -- 'atmospheric', 'cover_reveal', 'quote_graphic'
  filename TEXT,
  is_ai_generated BOOLEAN,
  model TEXT,
  prompt TEXT,
  seed INTEGER,
  lora TEXT,
  disclosure_applied BOOLEAN,
  publish_date TEXT,
  notes TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);
```

## Retention

- Source prompts + seeds: keep forever
- Generated images: keep 2 years minimum; archive beyond that
- AI detector scores at audit: optional log

## Cleanup

Quarterly: remove experiment outputs that didn't ship. Keep shipped + reference-worthy only.
