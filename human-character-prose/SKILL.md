---
name: human-character-prose
version: 9.2
description: Complete reference manual for writing prose and building characters that read as human-authored fiction. Reflects everything learned through Prologue v9.2 (commit a3c5f9d, Pangram 0.000 Human verified). Three references — (1) write-human prose guide, (2) character-psychology manual, (3) failure-modes catalog with concrete before/after from JAS-58/63/72/74 iteration. Used by Daniel for drafting, Eleanor for dev-edit, Thomas for line-copy QA, Margaret for EIC ratification, Jason for routing decisions.
---

# Human-Character-Prose v9.2

Everything needed to draft, edit, ratify, and route human-feeling prose for *The Crossroads Inn*. **This skill version (v9.2) corresponds to the Prologue ship baseline** (commit `a3c5f9d` / merge `6c4acf3`, Pangram 0.000 Human, 9/9 windows Human Written). Future skill versions (v9.3, v10, etc.) will add rules as new failure patterns are diagnosed and ratified through the JAS-74 diagnostic-to-rule pipeline.

## When to use

- **Daniel (Series Writer)** — read all three references before drafting any chapter. Apply the condensed protocol in your `AGENTS.md`; look up specific patterns and failure modes when a situation needs judgment. Run the pre-commit pattern detector before claiming a draft done.
- **Eleanor (Dev Editor)** — use the character-psychology manual as your framework for dev-edit letters. Cross-check suggestions against the failure-modes catalog (Reference 3) — if you're proposing a revision that walks Daniel into a known failure mode, propose a different revision.
- **Thomas (Line/Copy Editor)** — use the write-human prose guide's Part One (surface tells) + Part Seven (rhythm) as your line-edit checklist. Cross-check edits against Reference 3 — your line-level "improvements" must NOT introduce parallel template, catalog enumeration, or literary withholding.
- **Margaret (EIC)** — use all three as your ratification framework. Ship-ready requires: detector passes (per `pangram-detector`), character logic holds (per character-psychology manual), prose reads human (per write-human prose guide), and Reference 3 failure modes are absent.
- **Jason (CEO)** — use Reference 3 (failure-modes catalog) as routing context. After ANY revision to a Pangram-cleared chapter, **re-Gate before allowing line/copy or ship-ready phases**. Today's v10 proved that "small" panel-feedback edits can introduce semantic-register catalog regressions that fully Pangram-fail an otherwise-clean manuscript.

## What this replaces + what it doesn't

**Replaces / supersedes:**
- Heartland-specific craft rules in `heartland-craft-library` and `heartland-fantasy-rubric` (residual after the 2026-04-24 Heartland Fantasy repositioning). Their voice rules defer to this skill.
- Prior `human-character-prose` v8 (rules 1-19 from JAS-60). v9.2 ADDS rules 20-23 + the failure-modes catalog. v8 rules are unchanged.

**Does NOT replace:**
- `pangram-detector` — statistical-register detector, different axis. AI-Assisted target is the detector gate; this skill is the craft gate.
- `pangram-beating-research` — Aria's research loop. Different owner.
- `scene-composition` — outline-to-scene-brief. Upstream of drafting.

## Three references

### 1. [references/write-human.md](references/write-human.md)
The prose manual. Thirteen parts covering surface tells (fix on sight), deep tells (require a different understanding), dialogue, POV, character, scene construction, rhythm, time, physical world, humor, what-prose-knows-that-characters-don't, the Daniel Standard, and a 20-step Quick Reference Scan. Read before every draft.

### 2. [references/character-psychology.md](references/character-psychology.md)
The character manual. Eight parts covering architecture of a real person, how people relate, specific psychology (trauma / grief / shame / love / loneliness / anger), and Crossroads Inn specifics. Read before writing any character's third appearance. Complete the APPENDIX profile template per character before the third scene.

### 3. [references/failure-modes.md](references/failure-modes.md)
**NEW in v9.2.** Concrete catalog of every Pangram failure pattern surfaced through the JAS-58 / JAS-63 / JAS-72 / JAS-74 iteration cycles, with before/after prose examples from the actual commits, the diagnostic that surfaced each pattern, and the fix that worked. Read this BEFORE proposing any revision to ship-bound prose. Designed to prevent the editorial team from re-creating today's mistakes on Ch 1-40.

---

## Condensed protocol (top 23 for Daniel's AGENTS.md)

Daniel's `AGENTS.md` carries these 23 rules as the pre-loaded working protocol. The full references are for lookup when a situation needs more than a rule.

### Rules 1-15 — Original prose protocol (pre-2026-04-24)

1. **Ban named feelings.** No "sadness," "fear," "joy" as nouns. Render the body.
2. **Fear > desire as motivator.** For every significant decision, identify what the character is afraid of. That fear drives the behavior.
3. **One named emotion maximum per scene.** If you must name one, pick the most important.
4. **Character-specific verbs, not safe ones.** "Bolted," "clipped across" — not "walked quickly."
5. **One adjective per noun.** Two means the noun is wrong. Find a better noun.
6. **First detail of any space is the unexpected one.** Not the establishing shot.
7. **Enter scene 2 beats late. Exit 2 beats early.**
8. **Once per chapter: a character does something they cannot fully explain.** Don't caption it.
9. **Once per chapter: a character is wrong about their own emotional state.** Don't correct it.
10. **Once per chapter: a character is unkind to someone they love.** Not fully wrong, not fully right.
11. **Specific cowardice.** Every primary character has one thing they cannot make themselves do.
12. **The thing unresolved at scene end.** Don't close emotional loops cleanly.
13. **Subtext is the point.** What's not being said is the real scene.
14. **Body before mind.** In revelation or dread, the body responds one beat before conscious understanding.
15. **Primary emotion under anger.** When a character is angry, name the underlying fear/grief/shame/hurt.

### Rules 16-19 — Added 2026-04-25 from JAS-60 comparative benchmark research

16. **No literary withholding.** Meta-commentary on inability to name is itself an AI fingerprint. Banned phrases (non-exhaustive): "she couldn't have said," "the quiet went on for a long time," "blurred together," "for a long time," "she was not [X]. she was.", "without [verbing] [X]." **Either name the specific thing, or move on without commenting on the absence.** Benchmark example: Cerulean Sea names *193 Lakewood*. Our v4 said "towns that blurred together." That's the difference.

17. **No uninterrupted catalogs.** Physical-detail enumerations of 4+ sentences without an interrupt (action, dialogue, or sensory shift) flag as AI. Subtypes:
    - **Object-attribute catalogs** ("dry. stacked. settled. steady.")
    - **Sentence-fragment physical catalogs** ("Stone. Cold. Knees up. Wall.")
    - **Sequential-action parallel beats** (arm / scabbard / mouth — three "looked at" beats in a row)

18. **Emotional-aftermath substitution.** When the protagonist breaks down, processes grief, or has a long internal moment, **substitute the scene with prosaic action**, not more interiority. Show what they DO; the grief is in the action. Today's v8 substitution proved this: floor-breakdown grief beat → physical departure scene cleared the window the grief beat couldn't.

19. **Prosaic specificity, not literary-irony specificity.** Name the concrete thing as a character noticing it (the farrier with burn scars), not as a writer's polished observation. Test: does this read like the character noticing, or like the writer crafting? If the latter, simplify.

### Rules 20-23 — Added 2026-04-25 from Prologue v9.2 ship cycle (JAS-58/63/72/74)

20. **No parallel template across vignettes.** In any sequence of 3+ scenes/vignettes/transactions in the same section, **no two adjacent items may share grammatical opening template**. Pangram detects parallel structure across the whole window, not individual sentences.
    - **v9 failure:** `"In Thornwall... In Bracken... In Ashford... In Millhaven..."` × 4 → flagged High-confidence AI
    - **v10 regression:** `"In Bracken, a woman..."` `"In Ashford, a guard..."` × 2 adjacent → flagged High-confidence AI
    - **v10.1 partial fix:** Bracken restructured (item-led: `"The left gauntlet went in Bracken..."`); High-conf cleared but Medium remained
    - **Fix that works:** vary subject across all items (item-led / character-led / place-led / action-led) AND ensure no two ADJACENT items share grammar
    - **Rule of thumb:** if you can write the openers as a regex template `"In [Town], [character] [action]..."`, you've created the failure

21. **Semantic-register catalog ceiling — UNFIXABLE BY SYNTAX.** A sequence of 3+ short commercial/transactional vignettes is itself an AI signature regardless of opener variation. Discovered v10.2: all four town openers varied (`she sold...`, `the gauntlet went...`, `Ashford. A guard...`, `the breastplate went...`) but Pangram still flagged 0.128 Mixed. **Cannot be fixed by syntax. Must be solved structurally:**
    - Collapse to flowing prose (single paragraph, mixed scene-shapes)
    - Restructure (interleave with present-tense interior, or with off-screen events)
    - Substitute the section type (replace with a different scene shape entirely — what v8 did with the floor-breakdown→departure substitution)
    - Cut the vignettes (compress to indirect summary that doesn't enumerate)

22. **Expansion regression.** When an EIC asks to "expand" or "rebalance" a previously-compressed section, the natural prose move IS parallel template (rule 20) or semantic catalog (rule 21). **Resist that move.** Before expanding any section into a series of similar items, check: am I creating a sequence of comparable scene-types? If yes, find a different way (substitute one scene, restructure, indirect summary, present-tense break, character-interior interruption between vignettes).
    - **Today's example:** v9.1 Bracken+Ashford were COMPRESSED to summary because the v9 catalog flagged. Margaret EIC then approved Bracken+Ashford rebalance per panel feedback. Daniel re-expanded both into vignettes, re-creating the v9 catalog under different syntax. Pangram flagged again. Two cycles wasted.

23. **Departure-scene rhythm parallelism.** Short paragraphs with clean parallel structure (3 short sentences each starting with the same subject + verb shape) will flag. Discovered v9.1 → v9.2: "She put the seal in the saddlebag. She tied the knot. She stood." Fix: interrupt mid-sequence with sensory intrusion, fragment, or non-action beat. Today's v9.2 fix added flint-kit fumble, cord-tying struggle, and "Stood there." fragment.

### Rule 24 — Added 2026-04-25 from Ch 1 cycle (JAS-81/85/89/90/91/92)

24. **No solo-protagonist observation scenes at chapter-establishing scale.** Pure solo-protagonist observation prose — protagonist alone, observing/cataloging environment, in clipped fragmentary sentences without dialogue or another character — IS itself an AI signature for chapter-establishing register. This is NOT caught by rules 16-23; it is the *aggregate density* of clipped observation that flags, not any specific phrase or structure.

   **Discovery (Ch 1 trajectory):** v9.2 fresh draft scored 1.000 AI. Three iterations of line-edits + register rewrites moved fraction_ai from 0.667 to 0.649 — essentially flat. The 5 failing windows in Ch 1 v3 register rewrite were ALL solo-protagonist observation scenes (morning wake, common room with Oldevar, inn reconnaissance, Pip intro, traveler confrontation setup). The 3 PASSING windows were: magistrate signing (heavy dialogue, transactional), post-confrontation (multi-character, action stakes), cellar ledger (dialogue with Pip). Same writer, same skill, same draft cycle, opposite scores.

   **The rule:** chapter openings and any chapter scene longer than ~200 words MUST contain at least one of:
   - **Dialogue exchange** between the protagonist and another character (preferred)
   - **Physical interaction** with another character (door-opening, item-passing, struggle)
   - **Active transaction or decision-with-stakes** that implicates another character or institution
   - **Sensory intrusion that breaks observational mode** (a sound that demands response, a body sensation that interrupts thought, a physical event that forces attention)

   **What does NOT count as breaking solo-observation mode:**
   - Self-talk / italicized interior thought (still solo)
   - Memory of another character (memory is solo)
   - Description of the environment, no matter how specific (still solo)
   - Body sensations the protagonist passively notes (still solo)

   **Applied to chapter design:** the FIRST 500 words of any chapter must contain dialogue with another character. If the chapter outline calls for a solo establishing beat, OPEN the chapter mid-action with another character present and BACKFILL the establishing through dialogue/action. (See Prologue v8 fix: "departure scene with the innkeeper" replaced "morning wake observation" — same purpose, different scene type.)

   **Detection status:** Pattern 8 in `pre-commit-pattern-check.py` is *defined but not active*. Initial heuristic (200+ words without dialogue or interaction verb) false-positives on the shipped Prologue's letter-writing scene (which scored 0.000 Human despite being solo). The Prologue's solo-letter scene works because it has dense named specificity (Wren age 17, Denna left-handed, 89 names) that grounds the prose; Ch 1's solo-morning-wake fails because its observations are generic. Phase 2 detector work needs per-paragraph register classification, not regex. **For now: this rule is a chapter-design constraint Daniel + Margaret enforce manually during outline review, not a pre-commit detector pattern.**

These 24 are compression. Read the full references for depth. Read Reference 3 (failure-modes.md) BEFORE proposing any revision to a Pangram-cleared chapter.

---

## Pre-commit checklist — MANDATORY (Daniel runs before claiming done; failure = no commit)

This is a HARD GATE. Effective 2026-04-25 after Ch 1 v9.2 fresh draft (commit `242ad98`) was committed with 15 forbidden-construction violations Daniel didn't catch. Pangram flagged 1.000 AI. The protocol rules ARE sufficient — what failed was enforcement. This checklist now enforces.

### Step 1 — Run the unified detector

Single command. Catches rules 1, 2, 3, 6, 16-23 in one pass.

```bash
python3 /paperclip/instances/default/skills/<company-id>/pangram-detector/scripts/pre-commit-pattern-check.py path/to/your/draft.md
```

Expected output: `PASS <filename> — no pattern hits`

If output is `FAIL ... N hit(s)`: **revise before commit.** Each hit lists pattern, rule, line, and snippet. Address each one. Re-run until PASS.

### Step 2 — Substitution check

Any emotional-aftermath beat over 100 words that's pure interiority? If yes, substitute per rule 18 (action over interiority).

### Step 3 — Commit with proof-of-audit

Commit message MUST include the detector output as proof. Format:

```
[Chapter draft message]

Pre-commit audit:
- pre-commit-pattern-check.py: PASS (0 hits)
- substitution check: clean / [if applies, list any 100+ word interiority blocks and the rationale]
```

A commit without the audit-output line in the body is NOT a valid commit. Board reverts unaudited commits.

### Step 4 — Frontmatter `patterns_applied` is a CLAIM, not proof

The frontmatter `patterns_applied: zero-inference-register, ...` field declares which protocol you intended. The DETECTOR OUTPUT is the proof. Discrepancies between intent and output are caught by Pangram and waste 4-7 hours per chapter to fix. Don't claim, verify.

### Why this matters

Today's Ch 1 v9.2 fresh draft had:
- 5 instances of "the way" (similes)
- 4 instances of "like" (similes)
- 3 instances of "because" (explanatory clauses)
- 1 instance of "since"
- 2 instances of "as if"

Daniel's commit frontmatter claimed `patterns_applied: zero-inference-register`. That was a lie — the patterns weren't applied. Pangram caught it. Hours wasted on diagnosis, revision, and discovery that the detector didn't yet cover rules 1-15.

The detector now covers all 23 rules. The protocol works. Don't skip the gate.

---

## EIC ratification gate (Margaret)

Ship-ready requires:
- ✓ Pangram detector passes (per `pangram-detector` v9.2 thresholds)
- ✓ All 23 rules verified absent of violation in submitted prose
- ✓ Character logic holds (per character-psychology manual)
- ✓ Prose reads human (per write-human prose guide)
- ✓ No regression of any failure mode in failure-modes.md
- ✓ Reader panel reception ≥6/7 (per Iris's CRO panel — applies to ship-bound chapters)
- ✓ Bible canonical entries ratified for any new named entities

If you're tempted to approve revisions that walk back to a previously-failed pattern, see Reference 3 first. Today's v10 cycle proved that EIC adjudication itself can introduce regressions.

---

## Diagnostic-to-rule pipeline (Aria's standing role addition, 2026-04-25)

When Aria diagnoses a new failure pattern in any future Pangram verdict, her output includes a **structured rule proposal**:

```
RULE PROPOSAL (Aria → Margaret)
Name: [pattern name]
Description: [one paragraph]
Detection method: [grep, pattern, semantic check]
Before example: [text excerpt that failed]
After example: [text excerpt that fixed it]
Confidence: [skill-rule | research-only candidate]
Target skill version: v9.X / v10
```

Margaret reviews. If approved, Ben (or future skill-engineer) bumps the skill version and adds the rule + example to references/failure-modes.md. Synced to all 5 agents (Daniel/Margaret/Eleanor/Thomas/Jason).

**Closed loop:** every Pangram failure → permanent rule preventing the same failure later.

---

## 8 inputs required (currently pending)

Both prose and character references defer to series-specific inputs. Board has delegated these to Margaret + Eleanor + Thomas. Until delivered, Daniel applies generic craft; series-specific work ratchets up once inputs land:

1. Series image vocabulary (Margaret)
2. "Jason" voice fingerprint (Margaret)
3. Character verbal tics (Eleanor + Margaret)
4. Character perceptual filters (Eleanor)
5. Character blind spots (Eleanor)
6. Off-page character lives (Eleanor + Margaret)
7. Chapter emotional-context notes (Margaret)
8. Object history list (Margaret + Thomas)

---

## Standard (the test, not the checklist)

**Chapter passes when:**
- Eleanor marks at least one line in pencil
- Margaret puts it down for a moment
- Readers stay up past when they should have stopped
- One detail pays off the reader didn't see coming
- The character continues to exist in the reader's mind after the last page
- Pangram returns Human or AI-Assisted with no High-conf or Medium-conf AI windows

**Chapter fails when:**
- Nothing was worth marking in pencil
- Every emotional loop closed
- No character did anything inexplicable
- The reader closed the book and the character stopped existing
- Any rule 16-23 pattern is detectable in the prose

The 23 condensed rules are the floor. The standard is the ceiling. The work is everything between.
