# Launching CSS v2 on Argon (Gemini): checklist

A copy of `css-fable`, made Oct 24 so Argon and Claude can run the same brief independently and be compared. The brief is identical; the file name `FABLE_BRIEF_v2.md` doesn't matter to the agent.

## 1. Put this folder on GitHub (5 min)
1. github.com → **New repository** → name `css-argon-v2` → **Private** → Create.
2. Click **"uploading an existing file"**, then drag in everything inside `GregOS/projects/css-argon/`: `FABLE_BRIEF_v2.md`, `SETUP.md`, `OUTSIDE_REVIEW_PROMPTS.md`, and the `context`, `poc` and `reference` folders → **Commit changes**. (Skip `FABLE_BRIEF.md`, the old version, and `.DS_Store`.)
3. Check that `context/` shows 7 files, including `outside-reviews-full.md` and the `.xlsx`.

## 2. Start Argon
Connect it to the `css-argon-v2` repo and send:

> Read `FABLE_BRIEF_v2.md` in this repo and carry out everything from "THE PROMPT" down, including the merged outside-review notes at the end. Work on a branch named `argon-v2`, and commit after each part (Audit, Canon, Build, Review). Don't modify `poc/`.

If Argon can't run code or push to GitHub, ask for Parts 1–2 only (Audit + Canon) and have it return them as files.

## 3. Comparing with the Claude run
Read the two `CSS_V2_REVIEW.md` files side by side, then the two decision lists. Pick one v2 to carry forward rather than merging code.
