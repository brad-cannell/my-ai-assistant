---
title: Daily Planning Prompt
author: "Brad Cannell"
created: 2026-04-23
last_updated: 2026-04-23
---

# Overview (optional)

- At a high level, I want Claude to read my task list for the day, help me plan and prioritize, and to suggest ways it can take work off my plate.
- ClickUp task: https://app.clickup.com/t/868jcdpn1
- Initial Claude.ai brainstorming session: https://claude.ai/chat/b3157c5a-e01a-4553-a8c8-bd11b873fd44

I haven't started writing the actual prompt yet...

# SYSTEM PROMPT

Describe the role the model should assume.

> Examples:  
> You are a helpful assistant for drafting academic manuscripts in public health.
> You are a technology consultant with deep expertise in AI/LLMs and developer-facing AI tooling, with particular strength in minimal, practical setups for academic workflows.

---

# USER MESSAGE

## Context
Provide any background information the model needs to perform well.

> Example:  
> The text comes from the methods section of an epidemiologic study intended for submission to a peer-reviewed journal.

## Task
State clearly what the model should do.

> Example:  
> Rewrite the provided text to be more formal and concise while preserving the original meaning.

## Constraints & Formatting
List any important constraints or rules.
- Preserve the original meaning
- Avoid adding new information
- Maintain an academic tone
- Primary Language: R (Tidyverse)
- Citation Style: APA 7th Edition
- Format: {{output_format}}
