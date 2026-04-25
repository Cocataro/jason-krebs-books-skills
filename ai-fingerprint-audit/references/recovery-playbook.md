# Recovery Playbook — If a Book Gets Publicly Flagged

If a BookTok / r/fantasy / r/romancebooks reader runs Pangram or GPTZero on a paragraph of a shipped book and posts the result publicly, you have ~48 hours before the pile-on becomes permanent reputation damage.

This is the second-order risk, not a hypothetical. Real 2025 cases:
- **Coral Hart** (~200 romance novels): BookTok exposure drove her off the platform within weeks.
- **Prompts-left-in-manuscript incidents** (mid-2025): published books found with "Certainly! Here is the rewritten..." literal strings. Either pulled or apology-cycle.
- **Reddit editor exposés** (mid-2025): "r/selfpublish editor" posts itemizing AI tells in specific published novels, with author-career consequences.
- **Hachette's *Shy Girl*** (2025): Pangram flagged it (likely false positive). Book was cancelled anyway. A warning even when wrong.

## Hour 0–4: detect and triage

### Detect fast
- Set Google Alerts on pen name + "AI," "AI-generated," "Pangram," "GPTZero," "AI tells"
- Monitor: r/fantasy, r/romancebooks, r/selfpublish, BookTok via TikTok-monitoring tool, Goodreads reviews
- Nina (or Marketing Lead when hired) checks social mentions daily during launch; every 2–3 days steady-state

### Triage the callout
**Is the callout:**
1. **A single reader's speculation** ("This feels AI-y")? — Monitor. Don't respond. Most die out.
2. **A Pangram/GPTZero screenshot with high AI probability**? — This is the escalation case. Proceed to Hour 4–24.
3. **A reader quoting specific AI-fingerprint patterns** (em-dash density, "delve/tapestry" clusters, "not X — Y")? — Also escalation case.
4. **An influencer post** (>10k followers) amplifying? — High-priority escalation.

### What NOT to do in the first 4 hours
- Do not publicly deny.
- Do not engage with the specific reader defensively.
- Do not issue a statement yet.
- Do not delete reviews or attempt to report the post.

## Hour 4–24: internal audit + decision

### Run the audit on the flagged book
1. Pangram full-document scan on every chapter.
2. GPTZero full-document.
3. In-house lint script per chapter.
4. Identify the chapter(s) or paragraph(s) the callout originated from.
5. Compare against calibration-sprint baseline — is this book actually drifting, or is it a false-positive spike?

### Decision matrix

| Audit result | Callout credible? | Action |
|---|---|---|
| Book is genuinely drifting (multiple chapters WATCH/FAIL) | Yes | **Full rewrite cycle.** Pull from pre-order; keep live book up during rewrite; release updated version with version note. Disclosure stance: "AI-assisted with human editor of record" per Amazon's policy distinction. |
| Book is clean; specific paragraph is ambiguous | No — likely false positive | **Hold the line quietly.** Do not publicly respond. Respond only to individual reader questions with "The book was written with AI assistance per Amazon's assisted-writing policy; all prose is human-edited." |
| Book is clean; Pangram flagged a specific chapter | Unclear | **Targeted rewrite of that chapter.** Re-release the updated chapter; quiet version bump. |
| Prompts-literally-in-book incident (AI artifact left in) | Yes, immediate | **Immediate unpublish.** Full manuscript re-scan. Re-release within 7 days with an author's note acknowledging the mistake. This is terminal for reputation without transparent handling. |

### Get counsel
If the book was marketed under Amazon's "AI-assisted" policy (your pre-declared stance), document that in writing now. Board decision needed: do we confirm that policy publicly, or stay silent?

**Recommendation:** pre-declare the Jason Krebs Books stance in the author bio before launch. "Jason Krebs writes Heartland Fantasy with the help of AI drafting tools and a human editor of record." Plain language, once, in the bio. Not defensive, not apologetic. Readers who are okay with it will buy; readers who aren't will self-select. If you get called out later, you point to the bio.

If you did not pre-declare, and the callout is catching steam, pre-declaring now (post-hoc) reads defensive. Handle case-by-case.

## Hour 24–48: response (if required)

### Principles of the response (if you choose to respond)
- **Plain language.** Not corporate. Not legal-ese. First-person Jason Krebs voice.
- **Short.** 150–250 words.
- **Specific.** Acknowledge the specific callout, don't wave it off generally.
- **No attacking the reader.** They have every right to flag concerns.
- **Concrete next step.** Either "the chapter is being revised" or "here's how the book was made."
- **Do not re-state as "AI-assisted"** if you pre-declared. Reference the bio.
- **Do not go viral with the response.** Post once, in one place (author newsletter, author Instagram, a pinned thread reply). Don't tour it through every platform.

### Template A — "legitimate concern, revising"
```
Hi. I saw the concern raised about [chapter/passage] in [book]. I want to address it directly.

[Book] was drafted with help from AI tools — I've noted this in my bio, and it's something I've been transparent about. The prose is edited by a human editor before publication.

The paragraph flagged in [the callout] is one I've re-read and agree reads too smoothly. I'm revising it this week and will push an update to Amazon that will replace the current version. I appreciate the reader community's care for Heartland Fantasy's craft — it's why I work in this genre.

If you've bought the book and want the updated version, Amazon will push it automatically to Kindle within 24 hours of my republication. If you'd prefer a refund, that's also fair, and you can get one through Amazon's standard process.

Thank you for reading.
— Jason Krebs
```

### Template B — "audit clean, standing behind the book"
Only use if you pre-declared the AI-assisted stance AND your audit confirms clean:
```
Hi. I saw the post running [book] through [Pangram / GPTZero].

As my bio notes, I write Heartland Fantasy with AI drafting assistance and a human editor. The specific paragraph flagged reads, to me, the way I wrote it — I know it because I remember the line. Detectors can flag genuine human-edited prose, especially in the warm voice Heartland Fantasy uses. That's a known issue with these tools.

That said, the concern is legitimate and I take it seriously. I'll continue to be transparent about process, and my editor and I will keep holding the voice to a high bar.

Thanks for reading.
— Jason Krebs
```

### Template C — "prompts-left-in incident"
Immediate unpublish. Then:
```
I need to apologize. An earlier version of [book] included [a literal AI prompt / a stray artifact from the drafting process] that shouldn't have made it past editing. It's been unpublished today. A corrected version will be live within seven days.

If you bought the book, the update will push automatically to Kindle. Refunds are available through Amazon if you prefer.

This is on me. I'm sorry for the error. I'll be taking [specific process change] to prevent it.

— Jason Krebs
```

## Hour 48+: monitoring + trend

- Continue Google Alerts + social monitoring for 14 days.
- If the story dies in 48 hours without public traction: move on. Do not re-open.
- If the story has traction at Day 3: consider whether to issue the response.
- If a second book gets flagged: treat as pattern. Re-baseline the whole pipeline, not just this book.
- Log the full incident in the studio's compliance note for future calibration.

## Prevention (the actual goal)

The playbook above is damage control. Prevention is the real play:

1. **Pre-declare AI-assisted status in the author bio.** Remove the surprise factor.
2. **Calibrate thresholds against human comps** before shipping. Don't guess.
3. **Humanization pass is mandatory every chapter.** No schedule exceptions.
4. **Two-detector sign-off before ship.** Pangram + GPTZero.
5. **Human read-aloud every 5 chapters** (Margaret). Catches what detectors miss.
6. **Monthly competitor scan.** What Heartland Fantasy books are getting flagged this month? What patterns are readers learning to notice? Update the ban-list.

## Don't do

- Don't silent-delete negative reviews (violates Amazon ToS; bad-faith signal).
- Don't report flagging posts (streisand effect).
- Don't sue. Don't threaten. Don't DM the reader.
- Don't issue a blanket "AI has a place in fiction" ideology post. Nobody wants the Heartland Fantasy industry's position paper. Stay in the lane: you make books, readers read them.
- Don't go on podcasts to "explain your process" — gives the story oxygen.
- Don't re-pitch the book as "AI-assisted" after the fact to claim protection — reads as post-hoc defense.

## Board-level decisions that should be made BEFORE launch

1. **AI-disclosure wording** in the author bio. Pre-declare or stay silent?
2. **Pre-order delivery protocol** if a pre-order-visible book gets flagged before release.
3. **KU refund exposure** — Amazon will refund reader complaints. Budget implication.
4. **Pen-persona silence policy** — if questioned directly, does Jason Krebs respond, or stay silent?
5. **Pipeline improvement commitment** — on what flag frequency do we halt production and re-baseline? (Recommendation: any flag during the first 3 books triggers a re-baseline.)

These go to the CEO/Board for discussion before Book 1 launches. Not after.
