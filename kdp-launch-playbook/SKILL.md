---
name: kdp-launch-playbook
description: KDP Select launch operations — Upload Packet template, full field-by-field upload checklist (ebook + paperback), pre-order strategy, pricing playbook for Heartland Fantasy in KU, launch runbook with T-minus schedule, royalty monitoring, support ticket templates, and account-safety rules. Critical: no KDP API exists. Agents prepare inputs; Board (human) clicks Publish. Used by KDP Ops (primary), approved by CEO Jason on price/launch-date decisions.
---

# KDP Launch Playbook

**Non-negotiable:** No public KDP API exists. KDP dashboard requires browser login + 2FA + manual file uploads. Headless-browser automation against KDP = ToS violation = account ban = 6 books' sales evaporate. **Agents never log into KDP.** The Board (Nicole) logs in and executes the 20-minute manual session per book. The agent's job is to make that session mechanical and error-proof.

See references/:
- `upload-packet-structure.md` — per-book file bundle Nicole receives
- `kdp-upload-checklist.md` — every field, in dashboard order, with recommended answers
- `launch-t-minus-runbook.md` — T-60 through T+30 per-book schedule
- `pricing-playbook-ku.md` — Heartland Fantasy pricing strategy for KDP Select
- `support-ticket-templates.md` — pre-drafted KDP support requests

## Board Decisions (Locked)

- **Distribution:** KDP Select only. 90-day exclusivity, auto-renews. No wide before Book 3 minimum.
- **DRM:** OFF on ebook. Once set, cannot change. Heartland Fantasy standard.
- **ISBN:** Own Bowker 10-pack (~$295, ~$29.50/book) — enables imprint "Jason Krebs Books" and wide-print optionality.
- **Pre-order:** Book 1 NO pre-order (hard launch, 100% demand on Day 1). Books 2–6 pre-order 30–60 days out only, gated on EIC final sign-off.
- **Pricing default:** Book 1 $0.99 launch week then settle at $4.99; Books 2–6 launch at $4.99 directly.
- **Paperback:** cream paper, matte finish, 5.25×8 trim.

## Critical Safety Rules

- **Pre-order delivery is sacred.** Miss one = **1-year pre-order ban on the account.** Existential risk. Gate open-date on EIC sign-off that manuscript is final.
- **Wrong-file upload** kills also-boughts and can trigger refunds. Checksum files at packet assembly.
- **Regional pricing errors** (e.g., £0.99 when meant $0.99) are real and common. Stage manually per currency.
- **Trademarked keywords** in metadata = book delisted, account warning. Verify against forbidden-keywords list every upload.
- **Tax interview** must be completed before first royalty payout or payment is held.

## KPIs

- Upload accuracy: zero field errors on go-live
- Time from final-files-received to live: <48h ebook, <7 days paperback (proof-gated)
- Royalty reconciliation accuracy: <0.5% variance vs. Analytics model
- Category ranking: #1 in at least one narrow sub-category launch week (Book 1)
- Zero KDP support escalations caused by ops error
- Pre-order delivery: 100% on time, no exceptions

## Escalation Triggers

Immediately (same wake):
- Pre-order delivery at risk — CEO + EIC
- Account warning or suspension notice — CEO + Board
- Tax interview block — CEO
- Payment hold — CEO
- Rank drop >50% in 24h without known cause — CEO + Marketing within 4h
- Refund rate >5% — EIC + Marketing within 24h
- Wrong-file upload detected — CEO same wake; plan unpublish/republish (loses reviews; last resort)

## What the Agent DOES

- Formats in Vellum ($250 Mac, industry standard) or Atticus ($147 cross-platform)
- Validates files: Kindle Previewer pass, EPUBCheck pass, PDF preflight with embedded fonts, spine-width math verified
- Assembles Upload Packet (markdown checklist + files) for Board
- Monitors royalties from CSV exports Nicole pulls
- Drafts KDP support tickets for Nicole to send
- Maintains the metadata calendar (T-minus per book + 90-day refresh)

## What the Agent DOES NOT

- Log into KDP. Ever.
- Log into Author Central. Ever.
- Log into ACX. Ever.
- Complete the tax interview. Ever.
- Order proofs. Ever.
- Click Publish. Ever.

These are all Board (human) actions.
