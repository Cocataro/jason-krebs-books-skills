# Upload Packet Structure

Delivered to Nicole per book. Everything pre-answered and pre-validated. She works through in ~20 minutes in the KDP dashboard.

## Folder

```
/Upload-Packets/Book-N/
├── 00-CHECKLIST.md                # Every field, in dashboard order (see kdp-upload-checklist.md)
├── 01-manuscript.epub             # Validated via EPUBCheck, passed Kindle Previewer
├── 02-cover-ebook.jpg             # 2560×1600 min, 1.6:1, sRGB, <50MB
├── 03-paperback-cover.pdf         # Full wrap, spine calc verified
├── 04-paperback-interior.pdf      # Fonts embedded, preflight passed
├── 05-hardcover-cover.pdf         # If applicable
├── 06-hardcover-interior.pdf      # If applicable
├── 07-description.html            # KDP-allowed HTML, mobile-tested, Kindlepreneur-generator validated
├── 08-keywords.txt                # 7 phrases, 50 chars each, forbidden-list verified
├── 09-categories.txt              # 3 category paths
├── 10-author-bio.md               # Amazon product page version (80–150w) + Author Central version (200–300w)
├── 11-aplus-assets/
│   ├── title-banner.jpg           # 970×600
│   ├── series-banner.jpg
│   ├── comparison-table.jpg
│   └── author-bio-banner.jpg
├── 12-pricing.md                  # USD + regional overrides (EUR/GBP/CAD/AUD)
├── 13-pre-order.md                # Open date, release date, delivery date (strictly tied to EIC sign-off)
└── 14-support-tickets/            # Pre-drafted tickets if any are needed this launch
```

## Checksum manifest

At `00-CHECKLIST.md` top, log SHA-256 of every file. Verify before Nicole uploads. Mismatched checksum = wrong-file risk = stop and reconcile.

## Delivery signal

- Packet assembled and validated → post comment on the book's parent issue tagging Nicole: "Upload Packet ready for Book N. All files validated. Assembled at [path]. Ready for your session."
- Nicole executes the upload. Comments back with ASINs + Listing URLs.
- Agent updates SQLite:
  ```
  UPDATE books SET kdp_asin=?, kdp_listing_url=?, published_at=datetime('now') WHERE slug=?;
  ```
- Agent hands launch URLs to Marketing (when hired).

## Post-upload audit

Within 1 hour of Nicole going live, the agent:
- [ ] Scrapes the product page — verify title, subtitle, series, price, categories, keywords all render correctly
- [ ] Verifies cover image renders at 150px thumbnail, 300px product page, 2560×1600 zoom
- [ ] Tests the description renders correctly on mobile (via mobile useragent)
- [ ] Logs any anomaly to the issue thread

## Paperback proof gate

Paperback does NOT go live until Nicole has ordered and approved a physical proof copy.
- Packet includes proof-ordering instructions.
- Agent stages the paperback as "ready for proof order."
- Nicole orders proof, approves physically, then returns to dashboard and clicks Publish.
- Expected proof delivery: ~10 days. Do not schedule paperback launch inside 14 days of packet delivery.
