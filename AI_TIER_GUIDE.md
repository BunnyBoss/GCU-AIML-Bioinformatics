# AI Tier Reference Guide
*For use by Claude when creating or editing any unit, lab, or assessment file in this repository.*

## Purpose
Every student-facing file (notebook or `.md`) carries an `ai_tier` field in its frontmatter. This tells students — and any AI tool they use — how much AI assistance is appropriate for *that specific file*, rather than applying one blanket rule to the whole course. When creating or editing a file, use this guide to decide (or suggest) the correct tier instead of leaving it blank or guessing.

## The tiers

| Tier | Label | Meaning | Typical file type |
|---|---|---|---|
| 1 | **No AI** | Student must complete this entirely unaided. No AI explanation, hinting, or code generation. | Midterm/final practical exams, timed in-class exercises |
| 2 | **AI Planning Only** | AI may help brainstorm, outline, or explain concepts/errors — but must not generate the actual analysis code or answer. | Graded homework notebooks, labs (early-to-mid semester) |
| 3 | **AI Collaboration (Disclosed)** | Student may use AI throughout the task, but must note where/how it was used. | Later-semester labs, once foundational skills are established |
| 4 | **Full AI + Reflection** | Any AI use is allowed, but the student must write a short reflection on what the AI contributed and where they corrected or overrode it. | Capstone project, open-ended applied work |
| — | **Full AI (Learning Aid)** | Not an assessment at all — pure learning material. AI can explain freely, generate extra examples, quiz the student. No submission, no grading. | Theory notebooks/`.md` guides, self-check quizzes, supplementary resources |

## How to decide the tier for a new file

Ask, in order:
1. **Is this graded or assessed?**
   - No → it's a **learning aid** (last row). Default to generous AI support — the goal is understanding, not testing.
   - Yes → continue.
2. **Is this testing whether the student can do the work independently (a skill check)?**
   - Yes, strictly → **Tier 1 (No AI)**.
   - Partially, with room to use AI as a tool → **Tier 2**.
3. **Is this later in the semester, after foundational skills are established, and closer to real-world practice?**
   - Yes → **Tier 3**.
4. **Is this an open-ended, applied, or capstone-style task where judgment matters more than recall?**
   - Yes → **Tier 4**.

If none of this is obvious from context, ask me rather than guessing — don't silently default to any tier.

## What to do with the tier once decided

- Fill the `ai_tier` field in the file's frontmatter using the label from the table above (e.g. `ai_tier: "Tier 2: AI Planning Only"`, or `ai_tier: "Full AI (Learning Aid)"`).
- Don't invent new tier names or wording beyond what's listed here — consistency across files matters more than precision of phrasing.
- If a file doesn't clearly fit one tier (e.g. a lab with both a guided warm-up section and a graded independent section), say so explicitly rather than picking one tier for the whole file — flag it back to me so we can decide whether to split the file or note mixed tiers.

## Default assumption by folder (unless told otherwise)

- `units/` → Learning Aid (unless a specific sub-file is marked as an assessed exercise)
- `labs/` → Tier 2, unless we've discussed a different tier for that specific lab
- `assessments/` → Learning Aid for self-checks; Tier 1 for anything explicitly called an "exam" or "practical test"
- `instructor_resources/` → not applicable (teacher-only, not student-facing)

This guide will be updated as the labs folder structure and per-lab tiering gets finalized — treat current lab defaults as provisional until then.
