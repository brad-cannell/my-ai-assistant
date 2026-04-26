---
title: Daily Planning Prompt
author: "Brad Cannell"
created: 2026-04-23
last_updated: 2026-04-25
---

# Overview (optional)

- At a high level, I want Claude to read my task list for the day, help me plan and prioritize, and to suggest ways it can take work off my plate.
- ClickUp task: https://app.clickup.com/t/868jcdpn1
- Initial Claude.ai brainstorming session: https://claude.ai/chat/b3157c5a-e01a-4553-a8c8-bd11b873fd44

I haven't started writing the actual prompt yet...

# Conversation with Codex

2026-04-25

I use two different data fields in my tasks. I use the native "due date" field to designate hard due deadlines-something bad happens if the task isn't completed by the due date. I also have a custom field, "🗓️ Target Date", for soft deadlines-the date I would like to have the task finished by. If I miss the "🗓️ Target Date", however, there isn't necessarily a consequence. 

Each morning, I check all of the tasks that have a due date of today OR have a "🗓️ Target Date" of today. I would like my AI assistant to start checking those dates, helping me prioritize my work for the day and providing suggestions on how it can help.

## Token usage

ClickUp includes an AI feature called ClickUp Brain. I gave ClickUp Brain this prompt: "List every task and subtask (as separate items) that are due this week or have a custom field ‘🗓️ Target Date’ of this week. Please ignore "Daily Planning" tasks. The list you return should include the task name and task id." Here is the list it returned:

<clickup_brain_response>
Here are the tasks and subtasks (listed as separate items) that are due next week (Apr 27, 2026 to May 3, 2026) or have 🗓️ Target Date in that same range, excluding “Daily Planning” and items in Meetings:

Email Alejandro about PCORNet Data (868jd1vap)
Update the DETECT-RPC Dashboards (868h1xkd1)
Submit Monthly Research and Creative Activity Report (868hztavk)
2026-04-27 Weekly Goals (868jd48g4)
Update Personnel Budgets (868j3v80j)
Reconcile QuickBooks (868cucj7m)
Create a Lab and Module Quiz for the Functionals Module (868guwen3)
Schedule Travel to World Parkinson Congress (868jab56z)
Send Elaine Announcements (868jb0ag9)
Create a Lab and Module Quiz for the For Loops Module (868guwdta)
Review Zach's 2026-04-23 Feedback About the REDCap Surveys (868jcfgu8)
After Beta Test (868fvya8b)
</clickup_brain_response>

Could I use this prompt in conjunction with Claude/Codex? Specifically, could I 
1. Set the Click Brain prompt to run everyday automatically.
2. Pass this list of tasks to Claude/Codex.
3. Claude/Codex could search this focused list instead of every task.
4. Help me prioritize and suggest other ways to help with my tasks.


The tag thing could also work.