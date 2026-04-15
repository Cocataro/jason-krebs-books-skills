# KDP Upload Checklist

Every field in dashboard order. Agent pre-fills; Nicole verifies + pastes.

## Kindle eBook Details tab

- [ ] **Language:** English
- [ ] **Book Title:** [exact, case as designed]
- [ ] **Subtitle:** [one genre phrase + series identifier, e.g., "A Cozy Fantasy Novel (The Crossroads Inn Book 1)"]
- [ ] **Series name:** [e.g., "The Crossroads Inn"]
- [ ] **Series number:** 1–6
- [ ] **Edition number:** leave blank for first edition
- [ ] **Author:** Jason Krebs (primary)
- [ ] **Contributors:** editor, cover artist, narrator (later) — add with correct role tags
- [ ] **Description:** paste validated HTML from `07-description.html` (Kindlepreneur-generator output)
- [ ] **Publishing rights:** "I own the copyright"
- [ ] **Keywords:** paste all 7 from `08-keywords.txt`
- [ ] **Categories:** 3 paths from `09-categories.txt` via KDP's category picker
- [ ] **Age range / Grade range:** leave blank for adult cozy fantasy
- [ ] **Pre-order:** yes/no per `13-pre-order.md`

## Kindle eBook Content tab

- [ ] **Manuscript:** upload `01-manuscript.epub`
- [ ] **Cover:** upload `02-cover-ebook.jpg`
- [ ] **ISBN:** leave blank (Amazon assigns ASIN for ebook)
- [ ] **DRM:** **OFF** (once set, cannot change — cozy fantasy Board default)
- [ ] **Preview:** run Kindle Previewer in the online viewer — spot-check chapter 1 drop cap, scene breaks, TOC

## Kindle eBook Pricing tab

- [ ] **KDP Select:** enroll (required for KU) — 90-day auto-renewing commitment
- [ ] **Primary marketplace:** Amazon.com
- [ ] **Royalty plan:** 70% (requires $2.99–$9.99)
- [ ] **List price USD:** per `12-pricing.md`
- [ ] **Regional overrides:** UK, EU, CA, AU manually set per pricing doc — do NOT trust auto-convert
- [ ] **Book Lending:** enabled (required for 70%)
- [ ] **Matchbook:** defunct since 2017; leave default
- [ ] **Territory rights:** Worldwide (Jason owns all)

## Paperback Details tab (separate upload flow)

- [ ] **ISBN:** own Bowker (from 10-pack) — imprint set to "Jason Krebs Books"
- [ ] **Trim size:** 5.25×8
- [ ] **Interior:** B&W, **cream paper**
- [ ] **Bleed:** No bleed (text-only interior)
- [ ] **Cover finish:** **Matte**
- [ ] **Interior PDF:** upload `04-paperback-interior.pdf`
- [ ] **Cover PDF:** upload `03-paperback-cover.pdf`
- [ ] **Spine width verification:** Amazon auto-calculates; confirm it matches agent's calc (pages × 0.0025")
- [ ] **Pricing:** list $14.99 (per pricing-playbook); KDP enforces minimum based on print cost

## Paperback proof gate (non-negotiable)

- [ ] Order author proof + printed proof (~10-day arrival)
- [ ] Physically approve proof before clicking Publish
- [ ] Mark approval in dashboard; paperback goes live

## Author Central (separate system)

- [ ] Log in at author.amazon.com (Nicole only)
- [ ] Claim author name (Jason Krebs)
- [ ] Bio: per `10-author-bio.md` — Author Central long version
- [ ] Author photo: 300×400+ high-res
- [ ] RSS feed: point to Jason Krebs newsletter landing page (ConvertKit / MailerLite)
- [ ] Twitter/X: if used
- [ ] Claim all published ASINs (ebook AND paperback separately)
- [ ] Set up Author Central per marketplace (.com, .co.uk, .de, .fr — separate for each)

## Post-upload audit (agent runs within 1h)

- [ ] Product page renders correctly on desktop
- [ ] Product page renders correctly on mobile (via mobile UA test)
- [ ] Title, subtitle, series, price, categories all correct
- [ ] Cover renders at 150px thumbnail, 300px product, 2560×1600 zoom
- [ ] Description HTML renders correctly (bold, italic, line breaks)
- [ ] KDP Ops updates SQLite with ASIN + listing URL

## If anything goes wrong

- Wrong title → contact KDP support (see `support-ticket-templates.md` → "Metadata correction")
- Wrong file → unpublish/republish (last resort — loses reviews)
- Wrong category → contact KDP support → "Category move request"
- Missing pre-order delivery → ALREADY CATASTROPHIC. Call CEO Jason immediately. 1-year ban in play.
