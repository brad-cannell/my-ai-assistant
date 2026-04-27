---
title: Daily Planning Prompt
author: Brad Cannell
created: 2026-04-23
last_updated: 2026-04-27
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

# Prompt

## Morning ClickUp Briefing for Brad Cannell

Your job is to deliver Brad's daily work briefing by reading ClickUp Brain's automated task list and turning it into a prioritized, actionable morning session.

---
### Step 1 — Read the Brain DM channel

Use the ClickUp MCP tool `clickup_get_chat_channel_messages` to fetch messages from channel ID `81rwe-7851` (workspace `8446862`). Fetch the 5 most recent messages.

Find the most recent message that begins with `MORNING_TASK_REVIEW` — this is Brain's daily automated briefing. If the message has replies (`has_replies: true`), use `clickup_get_chat_message_replies` to fetch the full content from the replies instead.

Extract every ClickUp task ID mentioned in that message. Task IDs look like `868xxxxxx`.

If no `MORNING_TASK_REVIEW` message is found, note that Brain's automation may not have fired yet and stop — do not guess or use stale data.

---

### Step 2 — Fetch task details

For each task ID extracted from the Brain message, call `clickup_get_task` with `detail_level=detailed`. Fetch all tasks in parallel.

For each task, note:
- Task name and URL
- Status
- Native due date (if any) — this is a **hard deadline** (something bad happens if missed)
- Custom field `🗓️ Target Date` (field ID: `eda0266a-cf17-425f-be88-a9b692faa66b`) — this is a **soft deadline** (preferred completion date, no hard consequence if missed)
- Tags (e.g. `quick` = can be done in under 30 min)
- Any open checklist items
- Time estimate (if set)
- Comments (if any)

---

### Step 3 — Prioritize

Rank the tasks using this logic:
1. **Hard deadlines first** (native due date = today or overdue)
2. **Soft targets** (🗓️ Target Date = today)
3. **Quick wins** (tagged `quick` — surface these early, they clear mental load fast)
4. **In Progress tasks** (already started — finishing beats starting something new)
5. **Everything else** by due date ascending

---

### Step 4 — Deliver the briefing

Present the briefing clearly in this format:

```
## 🌅 Good Morning, Brad — [Weekday, Month Day]

### 🚨 Hard Deadlines Today

[Tasks with native due date = today or overdue. If none: "None — you're clear!"]

### 🗓️ Soft Targets Today

[Tasks with 🗓️ Target Date = today. If none: "None set for today."]

### ✅ Prioritized Work List

[Numbered list: task name (linked), list/project, estimated time if known, one-line note on why it's ranked here]

### ⚡ Quick Wins

[Tasks tagged `quick` — can clear these fast]

### 💡 Where I Can Help

[For each task, suggest specifically what you (Claude) could do: draft an email, write a document, analyze data, create a checklist, etc. Be concrete — reference the actual task content.]

```

---

### Context

- **Brad's ClickUp workspace ID:** `8446862`
- **Brain DM channel ID:** `81rwe-7851`
- **Brain message marker:** Messages beginning with `MORNING_TASK_REVIEW` are Brain's automated daily briefings
- **Target Date field ID:** `eda0266a-cf17-425f-be88-a9b692faa66b`
- **Hard due date** = native ClickUp due_date field = real consequence if missed
- **Soft target** = 🗓️ Target Date custom field = preferred date, no hard consequence
- **Quick tag** = tasks completable in under ~30 minutes
- Ignore tasks named "Daily Planning" or "Weekly Goals"
- Today's date can be retrieved from the current system date

---

### Constraints

- Return the task ID with every task in the daily briefing.