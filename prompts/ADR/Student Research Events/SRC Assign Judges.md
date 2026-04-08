---
title: Assigning Judges for the SRC
author: "Brad Cannell"
created: 2026-04-06
last_updated: 2026-04-07
tags:
  - src
  - boller
---

# Overview (optional)

- I'm not sure what the best interface to use is, or the best place to write this down, but I'm trying not to get paralyzed by that. I'm trying to just write and figure the rest out later.
- Link to conversation on Claude.ai: https://claude.ai/chat/edf466ac-95f4-4416-8a92-7f8a07d32c58

# SYSTEM PROMPT

None at the moment.

------------------------------------------------------------------------

# USER MESSAGE

## Initial message

I'm making final preparations for the Student Research Conference (SRC) that is taking place in 4 days (2026-04-10).   I think these are the more important steps I need to complete this week: \* Import the judging volunteer survey from Qualtrics. \* Clean the judging volunteer survey from Qualtrics. \* The result should be a data frame with the names of faculty who volunteered to be an SRC judge, along with the session they volunteered for: morning, afternoon, or both. \* Review the poster presentation schedule spreadsheet. \* Remove the names of presenters who withdrew their posters. \* Assign a group of judges to review each poster. \* Ideally, we will have 3 judges per poster. They will complete judging as a team. \* Ideally, each judging team will be assigned 5-7 posters. \* Judges should not be assigned a poster being presented by one of their mentees to avoid conflicts of interest.   Please help me develop a step-by-step plan for assigning judges.   Please suggest tools I already use to make the process efficient and reproducible: Positron, Quarto, R, Python, Claude Code, Claude Cowork, Microsoft Office, and Qualtrics.

## Follow-up 01

I'm attaching the cleaned judge volunteer data (judged.csv), the cleaned list of posters that need to be assigned a judge (posters_for_judging.csv), and the COI table (coi.csv).  Please walk me through next steps.

## Follow-up 02

Here are the updated files with normalized names.

------------------------------------------------------------------------

# 2026-04-07: Issues Reported by Eva

Look at Eva's issues:

- Claudia Urbina withdrew

  - Remove from both spreadsheets and the Word document.

- PS1: The poster numbers are off for Hannah Bratcher, Rylea Brose, Harlee Fuentes, Karla Fuentes Maldonado, and Natalie Goodson. Additionally, Natalie Goodson should be in PS2.

- The judge assignments sheet has Ashley Kirby listed as poster 22.

- 

I found some issues with the judging assignments. They are notated directly on the attached assignment sheet. I will also list them here:

I want it to give me a reproducible process rather than a finished schedule.