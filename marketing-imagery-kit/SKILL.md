---
name: marketing-imagery-kit
description: Acceptable-use rules for AI-generated imagery across marketing surfaces. Distinguishes ship-surface imagery (covers, A+ Content, product page) from atmospheric imagery (social, newsletter, ads, ARC comms). AI-generated imagery is FORBIDDEN on ship surfaces and PERMITTED on marketing atmospherics under specific rules. Used by Cover Art Director, Blurb & Metadata Writer (A+ Content), and Marketing Lead when hired.
---

# Marketing Imagery Kit

Where AI-generated imagery is OK, where it is forbidden, and what the rules are per surface.

See `references/surface-rules.md`, `references/disclosure-policy.md`, `references/asset-naming.md`.

## The Core Distinction

| Surface | AI-generated imagery? | Why |
|---|---|---|
| **Book cover (ebook + paperback + hardcover)** | **FORBIDDEN** | Conversion killer; cozy fantasy audience flags AI covers; KDP Sept 2023 disclosure required; brand-damaging |
| **A+ Content title banner** (represents the cover) | **FORBIDDEN** | Effectively part of the cover on the product page |
| **A+ Content atmospheric modules** (quotes, setting shots) | **PERMITTED with rules** | Below-the-fold; not cover substitutes |
| **Product page main image** | **FORBIDDEN** | Same as cover |
| **Amazon Author Central banner / author photo** | **FORBIDDEN** (photo); atmospheric OK | Author photo is a person-claim; use real |
| **Social media (Instagram, TikTok, Twitter/X, Threads)** | **PERMITTED with rules** | Not a purchase-decision surface; mood-building |
| **Newsletter hero images** | **PERMITTED with rules** | Owned audience already bought in |
| **Newsletter/email atmospheric** | **PERMITTED with rules** | Same |
| **Amazon Ads creative (sponsored product, sponsored brands)** | **PERMITTED with rules** | Ads are not the cover; variety helps |
| **Facebook / Instagram paid ads** | **PERMITTED with rules** | Same |
| **BookBub ad creatives** | **PERMITTED with rules** | Same |
| **Launch reveal graphics (cover reveal, 3D mockup)** | Cover part is human; atmospheric surround can be AI | 3D mockups via Book Brush are fine; cover pixels are human |
| **Pinterest boards (private ideation)** | **PERMITTED — internal only** | Moodboard for illustrator, etc. |
| **Pinterest boards (public promotional)** | **PERMITTED with rules + disclosure where appropriate** | Public-facing brand impression |
| **ARC communication imagery** | **PERMITTED with rules** | Direct-to-reviewer comms |
| **Press kit imagery** | **PERMITTED (atmospheric); FORBIDDEN (cover mockups)** | Press gets the real cover |

## Rules for PERMITTED AI imagery

When using AI imagery on any permitted surface:

### 1. Style consistency with the cover
Must visually read as "same world" as the covers. Use the illustrator-style LoRA (see `stable-diffusion-prompts` skill). Without consistency, AI imagery jars against the cover and damages brand perception.

### 2. AI-fingerprint audit
Pass the same checklist used for cover concepts:
- No extra fingers / bad hands → crop out hands or use three-quarter back view
- No uncanny faces → use back view, silhouette, or object-focused composition
- No garbled text
- No architectural incoherence
- No "AI shimmer" overexposed highlights

Fail any → regenerate.

### 3. Composition discipline
Favor:
- **Object focus** (steaming mug, stack of books, key on a counter)
- **Setting shots** (inn at dusk, forest path, hearth corner)
- **Back views / silhouettes** of characters (avoids face/hand risks)

Avoid:
- Close-up faces
- Hands doing specific actions
- Elaborate dialogue / social scenes with multiple characters
- Text-heavy signage / book titles in image

### 4. Disclosure per platform (see `references/disclosure-policy.md`)
- Amazon KDP: AI content disclosure if uploaded to product-facing surfaces (N/A for social/newsletter external to Amazon)
- Instagram / TikTok: platform-specific AI-disclosure labels if applicable (both platforms have AI labels)
- BookTok / bookstagram culture: transparency builds trust; gratuitous AI use flagged

### 5. Don't misrepresent
- AI image cannot masquerade as the cover
- AI character image of Briar cannot appear as the canonical Briar the illustrator draws
- Marketing copy must not claim "illustrated by X" if the image is AI

### 6. Cover-reinforcement, not cover-replacement
Marketing atmospherics should point back to the cover. When a reader sees an AI atmospheric, their next impulse should be "oh I want to see the book" — not "this is the book."

## FORBIDDEN uses (repeat for emphasis)

- Final shipped book cover (any format, any size, any country)
- A+ Content title banner (the one that usually shows cover + tagline)
- Amazon product page main image
- Any "cover reveal" image where the AI image stands in for the cover itself
- Author photo on Author Central (must be real)
- Press kit cover mockups

Violating any of these is a terminating offense for the agent responsible. The brand cost is permanent.

## Brand consistency across marketing

### Palette lock
Every AI-generated marketing image follows the series palette:
- Core: amber, warm gold, forest green, cream
- Single warm light source
- Per-book accent color for that book's campaign (spring-sage, summer-gold, autumn-rust, winter-indigo, etc.)

### Typography (when text-in-image)
- Add typography in post (Affinity Designer) rather than generating in-image — AI text rendering is inconsistent
- Use the series typography lockup for consistency with covers

### Asset archive
All marketing imagery lives in vault: `04-Marketing/Imagery/Book-N/` (or `/Series-Level/` for cross-book)
- Include prompt + seed + model in filename metadata
- Log to SQLite if useful for campaign analytics

## Hard rules

1. AI imagery NEVER ships as a cover or cover-substitute. HARD GUARDRAIL.
2. AI-fingerprint audit every image before it goes public.
3. Platform disclosure where required.
4. Brand-palette consistency with the covers.
5. No fabricating as human-illustrated when it's AI.
6. The retained illustrator's consent covers their work; it doesn't cover "AI in the illustrator's style" — separate consent for LoRA training.
