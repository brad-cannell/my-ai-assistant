---
title: Parkinson's Disease Regular Briefing
interface: Claude Cowork
author: Brad Cannell
created: 2026-04-05
last_updated: 2026-04-06
tags:
  - Parkinson's Disease
  - Scheduled
---

# Overview (optional)

- I am creating two scheduled Parkinson's Disease briefings to help me stay current on Parkinson's Disease.
  - A daily briefing that contains basic PD facts.
  - A weekly briefing that contains a more extensive review of recent advances in the field.
- I am using doing so with a [scheduled Claude Cowork task](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork).
- I worked on this prompt with [Claude.ai](https://claude.ai/chat/d2e73862-2c4c-4e7a-9d90-60f90cbefb17).
- I am recording a backup version of the prompt here.
  - Currently, this scheduled task is specific to the device it was set up on. If you want to view it on a different device, you have to create a new, independent task.
- The results are appended to markdown files stored in the same directory as the prompt.
  - pd_basics_log.md: Contains a record of the PD basic facts covered.
  - pd_researchers_log.md: Contains a record of the names of researchers mentioned in the weekly briefing.
  - pd_stories_log copy.md: Contains a record of the news stories mentioned in the weekly briefing.

# SYSTEM PROMPT

I don't think this arrangement uses a system prompt.

------------------------------------------------------------------------

# USER MESSAGE

# Parkinson's Disease Briefing Prompt

You are preparing a Parkinson's Disease basic facts briefing for Brad Cannell, PhD, MPH — an epidemiologist focused on healthy aging, elder mistreatment, and late-life quality of life.

## Log Files

There is a running log file maintained alongside this prompt in the same folder:

- **`pd_basics_log.md`** — a running log of all Parkinson's Disease basic facts covered in previous briefings.

At the start of each run, read the log file before searching the web or compiling the briefing. At the end of each run, append new items to `pd_basics_log.md` as described below. Do not write the briefing to new, separate files.

## Instructions

1.  Read **`pd_basics_log.md`** before proceeding.

2.  Search the web for Parkinson's Disease basic facts, prioritizing the most recent items first. Focus on:

    - The epidemiology of Parkinson's Disease.
    - The pathology of Parkinson's Disease.
    - Symptoms
    - Treatments and therapies
    - Comorbidities
    - Costs
    - Effects on quality of life
    - Effects on caregivers

3.  Avoid items already present in `pd_basics_log.md` unless there is a significant update or new finding. If an item is an update to a previously logged story, note that briefly (e.g., "Update: ...").

4.  Compile a briefing with the following structure:

------------------------------------------------------------------------

## Parkinson's Disease Review — \[Today's Date\]

### 🧠 Today's Basic Fact

\[One foundational fact about Parkinson's Disease — covering biology, epidemiology, diagnosis, pathophysiology, or history. Aim to build cumulative knowledge over time by varying the topic each day. Include an inline source link to a reputable reference (e.g., Parkinson's Foundation, Michael J. Fox Foundation, peer-reviewed review article).\]

------------------------------------------------------------------------

5.  Deliver the briefing to my "PD Briefing" ClickUp channel at: https://app.clickup.com/8446862/chat/r/81rwe-7731.

6. After delivering the briefing, append it to `pd_basics_log.md`. Do not re-log facts already present in the file unless today's item is a meaningful update, in which case add an "Update:" prefix.

7. Commit `pd_basics_log.md` using the message "[YYYY-MM-DD] PD Briefing". Then, push the commit to GitHub.

## Rules

- Append briefings to `pd_basics_log.md`. Do not write the briefing to new, separate files.
- Every item must include a working inline source link. Do not include items without a verifiable source.
- Prioritize peer-reviewed publications, preprints (bioRxiv/medRxiv), major medical news outlets (NEJM, Lancet, JAMA, Nature, Science), and reputable organizations (Michael J. Fox Foundation, Parkinson's Foundation).
- Write at a level appropriate for a PhD epidemiologist — technical but concise.