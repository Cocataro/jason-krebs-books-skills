---
name: scene-composition
description: Outline-to-scene-brief framework. Converts a chapter-level outline beat into a ready-to-draft scene brief with POV, goal, stakes, sensory anchor, emotional beat, voice tics to deploy, and target word count. Used by Series Writer during Monday planning wake and before each drafting session.
---

# Scene Composition

Daniel Hart (Series Writer) runs this skill at the start of each drafting week to convert the chapter-level outline into scene-by-scene drafting briefs. One brief per scene. One draft session = one or two briefs.

Target: ~15 minutes per chapter to generate briefs. Not a rewrite of the outline — a tactical expansion into drafting-ready prompts.

## When to run

- **Monday planning wake:** generate briefs for the week's 4–6 planned scenes.
- **Before any drafting session** if the brief isn't already prepared.
- **After a dev-edit letter lands:** rebuild briefs for affected scenes per the revision plan.

## Inputs

1. The chapter-level outline beat (from Crossroads Inn Book N outline on JAS-4).
2. Series bible state (character voice tics, relationship status, open canon questions) — query the SQLite DB or read vault notes.
3. Prior scene's ending (what momentum/mood is carrying in?).
4. The voice-anchor (2,000 canonical words of Book 1 prose — re-read Monday).

## The Brief (fields)

For every scene, produce:

### 1. Scene header
- Chapter number + scene index (e.g., `Ch 7 — Scene 2 of 3`)
- POV character
- Location (be specific — "the hearth corner of the common room" not "the inn")
- Time of day + season + weather

### 2. Scene goal (1 sentence)
What does the POV character want going into this scene? Concrete. External-object goal OR internal-emotional goal. If you can't name it in one sentence, the scene needs more thinking.

### 3. Scene outcome (1 sentence)
What state does the scene end on? Usually the goal is blocked, complicated, or partially achieved — not cleanly won. Flag if unresolved (carries to next scene).

### 4. Stakes calibration
- Personal / relational / local / communal — which level? (Cozy ceiling: never above communal.)
- What the POV character stands to lose emotionally if the scene goes badly.
- Flag any stakes-creep toward regional/epic. Escalate to EIC before drafting.

### 5. Genre beat served
Which of the 7 cozy fantasy rubric beats does this scene serve? Or mark `transitional`, `character`, `worldbuilding`, `warmth`. If none → cut candidate.

### 6. Warmth anchor
At least one explicit warmth moment per 2–3 chapters. Is this the warmth scene? If yes, note the form (shared food, kindness, shelter, comfort).

### 7. Sensory anchor (first 3 sentences)
Lock the opening sense-anchor BEFORE drafting. One or two senses: smell, texture, warmth, weight, sound. Specific — not "it smelled good," but "the hearth smoke carried a thread of applewood."

### 8. Voice tics to deploy (≥3)
Pull from the POV character's tic inventory in the character bible. For Briar in a given scene, e.g.:
- Briar's "honest" filler (x1–2)
- Restart-sentence pattern (x1)
- Regional "proper cold" or similar idiom (x1)
- Interior contradiction (she says she doesn't care; body language says she does)

### 9. AI-fingerprint watch
Flag any scene where you're tempted to:
- Open with a tricolon ("She was tired, hungry, uncertain.")
- Close with a summarizing thematic sentence
- Use an em-dash parenthetical twice in a paragraph
- Describe every noun with two adjectives
These are AI-default reflexes. Catch them at the brief stage, not the draft stage.

### 10. Food / drink / object
If this is a food/drink-present scene (one per 3 chapters minimum), specify what and how. Use nomenclature from the style sheet — invented dishes/drinks spelled canonically.

### 11. Dialogue-to-description target
Estimate split (e.g., 60/40 dialogue-heavy, or 30/70 description-heavy). Cozy fantasy runs ~50/50 on average; this scene may lean.

### 12. Target word count
2,500–4,500 range. If aimed >4,500: can this split into two scenes? If aimed <2,000: should this merge with adjacent?

### 13. Momentum handoff
What mood/image/unresolved tension carries into the NEXT scene? Name it. Prevents the "wait, where are we now?" drift between scenes.

### 14. Canon introductions
Any new named thing in this scene (character, place, invented term)? Flag for EIC ratification + style-sheet entry BEFORE drafting, not after.

### 15. Flags for editor
Uncertainties, outline deviations, areas where you know the draft will be rough. Better to flag at brief than at handoff.

## Brief template (paste + fill)

```
CH [N] — Scene [i/N] | POV: [character] | Loc: [specific] | Time: [tod/season/weather]

GOAL:       [one sentence]
OUTCOME:    [one sentence]
STAKES:     [personal/relational/local/communal] — [specific emotional stake]
GENRE BEAT: [arrival / found-family / disruption / warmth / personal-threat / community-response / re-settling / transitional / character / worldbuilding]
WARMTH?     [yes/no — if yes, describe form]
SENSE:      [smell/sound/texture/warmth/weight/taste — specific, 1-2 senses]
TICS (≥3):  [list from POV's inventory]
AI WATCH:   [specific reflex to resist in this scene]
FOOD/OBJ:   [if applicable — named from style sheet]
DIALOGUE:   [target ratio]
WORDS:      [target, 2500-4500]
HANDOFF:    [what carries to next scene]
NEW CANON:  [any — flag for EIC]
FLAGS:      [uncertainties, outline deviations, rough-area flags]
```

## Usage pattern

- Produce briefs in batch for the week on Monday.
- Re-read each brief immediately before drafting that scene.
- If a brief feels hollow (can't name the goal, can't name the stake), don't draft — return to the outline and reconcile with EIC.
- After drafting, update the brief with actual word count + voice tics actually deployed. Feed back into chapter-header metadata.

## Not a replacement for

- The series bible (canon source).
- The Style Guide (voice/craft source).
- The outline (structure source).
- The voice-anchor (rhythm/tone source).

This is an **intermediate layer** that converts strategic material into tactical drafting prompts. Daniel owns it. No handoff. No second voice.

## If briefs are taking more than 15 min per chapter

Signal of a deeper issue — likely the outline is thin or the book's stakes drifted. Escalate to EIC. Don't grind through thin briefs to meet schedule.
