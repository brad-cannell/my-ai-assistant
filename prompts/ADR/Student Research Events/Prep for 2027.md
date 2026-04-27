---
title: Prepare for 2027
author: "Brad Cannell"
created: 2026-04-27
last_updated: 2026-04-27
---

# Overview (optional)

- We recently finished all three events for 2026. Now that I have my first year under my belt, I want to document some lessons learned and put processes in place to make preparations much easier and more efficient next year.  
- Specifically, I have a ClickUp tasks related to this overarching goal: https://app.clickup.com/t/868hy0wcy
- We also have some ClickUp Docs here: https://app.clickup.com/8446862/v/dc/81rwe-4031/81rwe-12311
- Here is a prompt we can paste directly into Claude Code. It is written to orient Claude Code to the full context, give it access to the right materials, and structure the work in stages — starting with a plan before touching anything.

- Add links to ClickUp

# Context

You are helping Brad Cannell, PhD, MPH — an epidemiologist and Associate Dean for Research (ADR) at TCU's Harris College of Nursing & Health Sciences — document lessons learned and build reusable processes for three annual student research events he organizes:

1. Student Research Conference (SRC) — poster presentations judged by faculty
2. Boller Competition (Boller) — oral presentations judged by faculty
3. 3-Minute Thesis (3MT) — short oral presentations, university-wide competition

The 2026 cycle just concluded. The goal of this project is to translate this year's experience into SOPs, ClickUp task structures, templates, and (where possible) automation so that next year's events run more efficiently with less friction and less reliance on memory.

There is 

---

# Your Access

You have access to Brad's Box folders containing all documents, emails, spreadsheets, forms, and materials created for the 2026 events (SRC, Boller, 3MT). Before doing anything else, explore the relevant Box folders and build an inventory of what exists. Look for:

- Qualtrics survey exports or form descriptions (intent-to-participate, judge volunteer, scoring forms)
- Spreadsheets used to manage registrations, scheduling, judging assignments, and scoring
- Email templates or sent communications
- Poster and presentation instructions sent to students
- Judging rubrics and scoring criteria
- Any SOPs or process notes (even informal ones)
- Website content or instructions
- Anything else that appears to be event-related

Do not modify, move, or delete any files. Read only at this stage.

Additonally, you have access to the "Update the HC Planner Board" ClickUp task at: https://app.clickup.com/t/868hy0wcy. Do not modify, move, or delete this task. Read only at this stage.

Finally, you have access to the the Student Reserach ClickUp Docs at: https://app.clickup.com/8446862/v/dc/81rwe-4031/81rwe-12311. Do not modify, move, or delete these Docs. Read only at this stage.

---

# Known Lessons Learned

In addition to whatever you find in Box, here is a curated list of lessons learned and improvement ideas already captured by Brad. Treat these as ground truth — they are confirmed priorities for next year.

## Intent-to-Participate Forms
- Add a question asking about student availability on Fridays
- Add digit-count validation to the student ID field
- Collect co-author names in a structured way (not a free-text box)
- Ask students to identify as undergraduate, master's, or doctoral (not just undergrad/grad — this distinction is needed for award calculations)

## Scheduling & Logistics
- Set timeslots first, then assign projects and judges to them
- Boller presentations: 20-minute slots; try to group by department
- Boller and SRC poster sessions should not overlap
- Assign Research Committee members as Boller judges; ask AM/PM availability
- Brad should not serve as a judge — he needs to be free to troubleshoot
- Schedule judge alternates
- Send calendar invites to both judges and students
- Schedule automated reminder emails

## Judges
- Replace the open-ended "student mentees" question with a structured field
- After student names are collected, ask faculty directly about conflicts of interest in the judge volunteer survey
- Ensure every judge volunteer is actually used
- Collect judge cell phone numbers at registration
- Send judges the scoring criteria in advance; consider posting it publicly

## Box / File Management
- Create a shared Box folder for Boller presentations
- Create a shared Box folder for SRC poster files
- Accept PowerPoint only — remove all PDF references from emails, website, and printing instructions
- Include the Box upload link (with expiration date) in all communications and on the website
- Do not ask students to email posters directly

## Poster Withdrawals
- When a presenter withdraws, leave the poster number vacant — do not renumber remaining posters

## SRC Scoring Criteria
- Bring back detailed criteria as presentation guidance/tips for students, even if it is no longer formally scored (e.g., "poster legible from 6 feet away")

## Student Preparation
- Send presentation tips before each event (SRC, Boller, 3MT)
- Share resources on statistical significance
- Host a group presentation coaching session for Boller participants 1–2 weeks before the event
- Encourage practice with and without an audience
- Remind students the audience is professionally diverse — advise them to explain everything
- Invite junior students (not just seniors) to attend

## Boller Event Day
- Have all participants in a session arrive at the start, not just before their slot
- Prepare a brief intro for each session: gratitude, developmental framing, ground rules for Q&A
- Have the PowerPoint available for the audience to view

## ClickUp / Project Management
- Use year-based tasks with due dates and target dates, filterable by year
- Consolidate small related tasks into parent tasks with subtasks
- Make tasks recurring (subtasks do copy when recurring)
- Build SOPs and link them to ClickUp tasks, templates, and R code

## Automation Targets
- Automated cleaning of the SRC registration spreadsheet (flag/remove duplicates, notify Brad)
- Auto-email to students/mentors when a duplicate entry is detected
- Check the Qualtrics faculty roster against the updated Harris College faculty roster

---

# Staged Approach — Start with a Plan

Do NOT begin creating documents, SOPs, or ClickUp tasks yet.

## Stage 1 (Your task right now): Produce a Project Plan

After reviewing the materials, produce a written project plan that includes:

1. **File inventory** — A structured summary of every relevant file you found in Box: file name, type, apparent purpose, and whether it appears reusable as a template next year.

2. **Gap analysis** — Based on the lessons learned above and what you found in Box, identify what is missing. For example: Is there already an email template that just needs to be updated? Is there no scheduling spreadsheet at all? Is there a rubric but no student-facing version?

3. **Proposed SOP structure** — Recommend a set of SOPs to create (e.g., one per event, or one per phase across events). For each proposed SOP, describe what it would cover and what existing materials would inform it.

4. **Proposed ClickUp task structure** — Recommend a set of parent tasks, subtasks, and a rough timeline (working backward from typical event dates in spring) for the 2027 cycle. Flag which tasks are good candidates for recurrence.

5. **Automation opportunities** — Identify which tasks are strong candidates for automation (R scripts, Qualtrics logic, scheduled emails, etc.) and what inputs/outputs each automation would need.

6. **Recommended sequencing** — In what order should the Stage 2 work be done? What should be built first, and why?

Present the plan as a structured markdown document. Brad will review it before any work begins.