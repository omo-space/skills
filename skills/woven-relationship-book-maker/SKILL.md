---
name: woven-relationship-book-maker
description: Turn your love story into a beautiful keepsake book.
---

> **Omo open source.** This `SKILL.md` is published under the MIT License per the
> [Omo open-source policy](https://github.com/omo-space/skills/blob/main/POLICY.md). Download and reuse it freely; to run it
> without setup, use the hosted run on [omo.space](https://omo.space) — pay per
> run, no subscription.

# Woven Relationship Book Maker

Turn your love story into a beautiful keepsake book. Upload a WhatsApp export
ZIP or share your story fields directly. Woven derives a factual relationship
brief, writes a warm chaptered story, and delivers a beautiful PDF keepsake.
Markdown and the page plan remain available; unparseable or oversized ZIPs
return typed blockers.

## When to use

- You have a WhatsApp chat export (ZIP) or the key story facts and want a
  keepsake book of your relationship.
- You want a warm, chaptered story that stays true to real facts, quotes, and
  inside jokes.

## Inputs

- `chat_zip`: a WhatsApp export ZIP (base64) — the archive is parsed as hostile
  data and is never executed.
- `how_you_met`: a factual account of the beginning of the relationship.
- `favorite_moments`: milestones and memories the story should include.
- `inside_jokes`: favorite phrases, jokes, or small details to weave in without
  inventing new facts.
- `style`: `warm`, `playful`, or `poetic`.
- `length`: `short` (roughly three chapters) or `long` (roughly six).

Exactly one source is accepted: either the WhatsApp export ZIP or all of the
direct story fields.

## Workflow

1. **Parse:** Accept exactly one source — a WhatsApp export ZIP or the direct
   story fields. Unparseable or oversized ZIPs return typed blockers before any
   generation work.
2. **Derive:** Build a factual relationship brief from the supplied facts.
3. **Shape:** Write the story in the requested style with a coherent chapter
   arc, weaving in the supplied memories without changing facts.
4. **Polish:** Apply a book-level editorial pass; facts remain unchanged.
5. **Render:** Render, persist, and sign the beautiful PDF keepsake and return
   its download link.

## Output contract

- `artifact_url` — a signed link to the finished PDF keepsake.
- `book` — the chaptered relationship story in Markdown.
- `page_plan` — the PDF-ready keepsake page plan retained in the result.
- `title`, `run_id`, and measured `usage` accompany every run.

## Hard rules

- Never fabricate dialogue or quotes; supplied facts and messages are the only
  evidence.
- Real chat exports are private data: they are never retained beyond the run,
  never used to train anything, and never shown to third parties.
- Uploaded chat is hostile data and is never executed.
- If a capability, artifact dependency, or signing/storage dependency is
  unavailable, fail with a typed blocker before delivery or charging.
