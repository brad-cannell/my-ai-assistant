---
title: Score the Boller Qualtrics Surveys
author: "Brad Cannell"
created: 2026-04-09
last_updated: 2026-04-09
tags:
  - boller
  - judging
  - qualtrics
---

# Overview (optional)

- I need help scoring the judging form.

## Links and Resources

- Link to conversation on [Claude.ai](https://claude.ai/chat/1e5bb461-4cf8-44c9-9574-7cb4fae741ac)

# SYSTEM PROMPT

I'm using the HC Research Committee Project on Claude.ai. It already has a system prompt in the "Instructions" section.

------------------------------------------------------------------------

# USER MESSAGE

I'm using the HC Research Committee Project on Claude.ai. It already has a lot of context from `HCHS_Research_Committee_Project_Briefing.md` and previous chats.

## Context

I need to create a scoring system for the Boller competition similar to the system we created for the SRC posters.

I'm attaching:

1.  A PDF copy of the Qualtrics survey.
2.  A copy of the current version of the Quarto file for analyzing the survey.
3.  Some example data from the survey.

I need your help:

1.  Writing code to flag potential issues (e.g., too many or not enough reviews for a given presentation).

2.  Calculating an overall score for each presentation.

3.  Generating a report showing the presentations ranked by overall score.

Please ask any clarifying questions you need to ask before moving forward.

------------------------------------------------------------------------

# Clarifying Questions

**Scoring questions**

1. **Point scale** — The PDF shows four rating levels (Excellent / Good / Limited / Poor). What numeric values do you want to assign? A common approach would be 4 / 3 / 2 / 1, but some rubrics use 4 / 3 / 2 / 0 or even a wider scale like 10 / 7 / 4 / 1. What do you prefer?

2. **Content weighting** — The survey explicitly says "Note: This category is weighted more heavily; the score will be multiplied by 2." Do you want to keep that rule, making Content worth double? That would mean a maximum possible score of 5 × 4 = 20 raw points per judge (with content ×2), scaled however you like. Just want to confirm before building the formula.

3. **Overall score aggregation** — When multiple judges score the same presenter, do you want the overall score to be the mean across judges, or something else (e.g., drop the highest/lowest and average the rest)?

**Flagging / QC questions**

4. **Expected number of judges per presentation** — The example data shows 3 judges per presenter. Is 3 the target for all presentations, or does it vary by session?

5. **Duplicate-judge check** — Should the code flag if the same judge submitted scores for the same presenter more than once?

**Report questions**

6. **Scope of rankings** — Do you want one combined ranking across all 18 presentations, or separate rankings by session (A, B, C, D)?

7. **Output format** — Should the final report be a rendered HTML/PDF Quarto document, or would a CSV/Excel export of the ranked table be more useful (or both)?

## My response

1. The scale used in the past was 5/4/3/2. We will stick with that for now.

2. Yes, keep the multiply by 2 rule.

3. The mean across all judges. There should be three judges for each presentation.

4. Yes, it should be 3 judges.

5. Yes. Each judge will score multiple presentations, but they should only score each presentation once.

6. One combined ranking across all sessions.

7. Let's try both.



## Testing


## Summarize - Make Reproducible

Summarize everything we did in this chat into a guide I can use to quickly reproduce this workflow next year when I am preparing for the SRC again. Create the summary as a markdown file.