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
  -  pd_stories_log copy.md: Contains a record of the news stories mentioned in the weekly briefing.

# SYSTEM PROMPT

I don't think this arrangement uses a system prompt.

------------------------------------------------------------------------

# USER MESSAGE

# Parkinson's Disease Briefing Prompt

You are preparing a Parkinson's Disease research briefing for Brad Cannell, PhD, MPH — an epidemiologist focused on healthy aging, elder mistreatment, and late-life quality of life.

## Log Files

Two running log files are maintained alongside this prompt in the same folder:

- **`pd_stories_log.md`** — a running log of all news and research items covered in previous briefings.
- **`pd_researchers_log.md`** — a running log of all researchers identified across previous briefings.

At the start of each run, read both log files before searching the web or compiling the briefing. At the end of each run, append new items to each log file as described below.

## Instructions

1.  Read `pd_stories_log.md` and `pd_researchers_log.md` before proceeding.

2.  Search the web for Parkinson's Disease news and research published or updated in the last week, prioritizing the most recent items first. Focus on:

    - New or updated clinical research and trial results
    - Basic science advances (e.g., neuroprotection, biomarkers, alpha-synuclein, neuroinflammation)
    - Epidemiology, risk factors, and population-level findings — especially those relevant to aging populations, elder mistreatment, social isolation, screening, or late-life outcomes
    - Treatment and medication updates
    - Caregiver and quality-of-life findings

3.  Avoid items already present in `pd_stories_log.md` unless there is a significant update or new finding. If an item is an update to a previously logged story, note that briefly (e.g., "Update: ...").

4.  Compile a briefing with the following structure:

------------------------------------------------------------------------

## Parkinson's Disease Briefing — \[Today's Date\]

### 🔬 Research & Science

\[2–4 items, each with a 2–3 sentence summary and an inline source link\]

### 🏥 Clinical & Treatment Updates

\[1–3 items, each with a 2–3 sentence summary and an inline source link\]

### 📰 News & Other Noteworthy Items

\[1–2 items if available, with inline source links\]

### 💡 Today's Deeper Dive

\[Pick the single most significant or interesting item — with preference for population-level, aging, or screening research when available — and provide a richer 4–6 sentence summary explaining why it matters and its implications for epidemiologic research or public health practice\]

### 👩‍🔬 Researchers to Know

\[List any researchers named in today's briefing. For each, provide: full name, institutional affiliation if available, and a one-sentence description of their area of focus based on the work cited. This section helps build a running knowledge of key figures in the PD research community.\]

------------------------------------------------------------------------

5.  If no significant new items are found in a category, note that briefly rather than leaving it empty.

6.  After delivering the briefing, update the log files as follows:

### Updating pd_stories_log.md

Append one entry per new story covered in today's briefing using this format:

```         
## [Today's Date]
- **[Story title or brief headline]** | [Source name] | [URL]
- **[Story title or brief headline]** | [Source name] | [URL]
```

Do not re-log stories already present in the file unless today's item is a meaningful update, in which case add an "Update:" prefix.

### Updating pd_researchers_log.md

Append any researchers from today's briefing who are not already in the file using this format:

```         
## [Researcher Full Name]
- **Affiliation:** [Institution, if known]
- **Focus:** [One-sentence description of their research area based on today's citation]
- **First noted:** [Today's Date]
- **Source:** [URL]
```

If a researcher is already logged, do not create a duplicate entry. If new information about an existing researcher is available (e.g., a new affiliation or focus area), update their entry in place rather than appending a new one.

## Rules

- Every item must include a working inline source link. Do not include items without a verifiable source.
- Prioritize peer-reviewed publications, preprints (bioRxiv/medRxiv), major medical news outlets (NEJM, Lancet, JAMA, Nature, Science), and reputable organizations (Michael J. Fox Foundation, Parkinson's Foundation).
- Write at a level appropriate for a PhD epidemiologist — technical but concise.
- Do not pad with evergreen content. If it's a slow news day, say so briefly and deliver only what's genuinely new.