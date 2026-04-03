---
title: Search My AI Assistant
author: brad_cannell
created: 2026-03-17
last_updated: 2026-03-17
---

# Overview (optional)

- I'm using this prompt with Claude Code.
- I want to use Claude Code so that it can update files for me.

# USER MESSAGE

This project is called "My AI Assistant". You can read more about it at `snippets/About My AI Assistant.md`. Since starting this project, one of my primary goals has been better prompt and knowledge management. I frequently reuse prompts (in whole or in part). The browser-based tools I was using did not provide robust systems for storing, organizing, searching, or versioning prompts, nor for linking prompts to responses or downstream artifacts. I am interested in learning how to make this project better support:

-   Structured prompt libraries

-   Searchable prompt and response archives

-   Linking prompts, responses, and notes in reproducible documents (e.g., Quarto)

---

# Follow-up: YAML Revisions

Before tackling the steps above, I've noticed that some of the yaml fields I've been using don't seem useful. Specifically:

In conversations:
- id
- audience
- domain

In prompts:
- task
- audience
- project
- domain

Should I drop these fields?

Additionally, am I currently using the best structure for the tags field or should I use something like a bracketed list?

---

# Follow-up: Debugging

I ran `quarto preview` and got this output:

<output>
Preparing to preview
[ 1/64] prompts/00 AI Assistant Meta Prompts/API vs Browser.md
ERROR: YAMLException: duplicated mapping key (prompts/00 AI Assistant Meta Prompts/API vs Browser.md, 6:1)
5: interface: browser
6: author: Brad Cannell
  ~~
7: date: 2026-03-17
</output>

And the prompts and conversations tables are still empty.

---

# Follow-up: The Prompt and Conversation Tables

That looks fine visually, but I have two questions:
1. Can search the contents of the files for keywords? Would it be best to just use my operating system to search the local files for keywords?
2. How would I maintain/update these tables?

<!-- 🔴 Left off here -->

---

# Follow-up: SOP

Please create a new vignette about searching this repo.