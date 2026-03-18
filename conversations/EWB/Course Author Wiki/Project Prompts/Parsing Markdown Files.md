---
title: Parsing Markdown Files
id: parsing_markdown_files
task: explanation
audience: academic
status: draft
author: "Brad Cannell"
created: 2025-12-23
last_updated: 2025-12-23
project: project_course_author_wiki
domain: documentation
tags:
  - api
  - markdown
---

<!--
YAML HEADER INSTRUCTIONS

Complete the YAML header above for every prompt. These fields support organization,
reuse, and future search, but should remain lightweight and human-readable.

ID GUIDELINES
- id: Use a short, stable, human-readable identifier in lowercase snake_case.
- Base the id on the prompt’s core purpose using a verb–object pattern
  (e.g., rewrite_academic_tone, review_r_code_style).
- Avoid dates, version numbers, model names, project names, or author names.
- Treat the id as permanent; change it only if the prompt’s fundamental purpose changes.

FIELD DESCRIPTIONS
- title: A brief, human-readable description of what the prompt does.
- task: The primary type of work the prompt performs (e.g., text_revision, code_review).
- audience: The intended audience for the output (e.g., academic, student, developer).
- status: Current maturity of the prompt (draft, stable, experimental, deprecated).
- author: Name of the prompt author.
- created: Date the prompt was first created (YYYY-MM-DD).
- last_updated: Date of the most recent substantive revision (YYYY-MM-DD).
- project: Associated project, course, or initiative, or null if broadly reusable.
- domain: Subject area or disciplinary context (e.g., epidemiology, data_science, general).
- tags: Optional keywords to support browsing and future search.

Avoid including model names or API parameters in the YAML header.
-->

# Overview (optional)

- I want help revising the "categories and tags" wiki page.
- I wrote a draft of the page and saved it as "Initial Draft.md".
- I want to pass that draft to the AI assistant through the API.
- Before doing so, I also want to pass the AI assistant some background information. Specifically, two markdown files:
  - About EWB.md
  - About Me.md
- Both of those files (About EWB.md, About Me.md) have yaml headers that are intended to help organize them. However, I don't want to pass the yaml header to the AI assistant.
- I don't believe there is a way to upload the entire file to the AI assistant through the API like we could if we were interacting with the AI assistant through the browser.
- Therefore, I want to assemble the contents of "About EWB.md" and "About Me.md" - without the yaml header - into a formatted text string that I can pass to to the AI assistant through the API.

# SYSTEM PROMPT

You are a technology consultant with deep expertise in AI/LLMs and developer-facing AI tooling. You specialize in minimal, practical, reproducible setups for academic workflows in R (Quarto, Git, structured prompt libraries), and you explain concepts for someone new to APIs.

---

# USER MESSAGE

## Context

### My background & use case
I’m an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University, and I run a small web-based educational platform (Epi-Workbench / EWB). I use LLMs for writing, course materials, and code (mostly R).

### What I’m trying to do
I want to revise a wiki page called **“Categories and Tags”** for the **EWB Course Author Wiki**, but I want to do the workflow through the **OpenAI API from R** (not the browser UI).

### Current setup (R + Quarto)
- R project: `Project - Course Author Wiki`
- Folder: `conversations/Wiki Page - Tags/`
- Quarto file: `Wiki Page - Categories and Tags.qmd`
  - contains the R code I’m using for API calls (prefer **ellmer**)
  - contains notes
  - will eventually store the assistant responses for reproducibility

### Files involved
- `Initial Draft.md` — the draft wiki page to be revised
- `About EWB.md` — background context (has a YAML header)
- `About Me.md` — background context (has a YAML header)

Important: **Do not send the YAML headers** from `About EWB.md` or `About Me.md` to the model.

## Core question (planning the information flow)
I suspect I should:
1) read the three files in R,
2) strip YAML headers from the two context files,
3) combine them into one well-labeled prompt string,
4) send that prompt to the model via the API (ellmer).

But I’m not sure this is the best approach, especially regarding:
- file passing / “attachments” equivalence via API
- context length and prompt organization
- reproducibility and logging in a Quarto workflow
- whether to use one request vs multiple turns/messages
- how to structure roles (system vs user) when using ellmer

## What I want in your FIRST response
Only answer: **Is my proposed “concatenate text into a structured prompt string” approach the best approach here?**
- If yes, briefly explain why and what the high-level structure should be (no code).
- If no, propose a better approach and explain tradeoffs (no code).
- Keep it to a small set of actionable bullets.

We will implement the chosen approach in subsequent messages.

## Constraints
- Work through the **API** (not the browser)
- Prefer **R** and the **ellmer** package
- Assume I’m new to APIs: explain terms briefly and concretely when they matter

---

# Follow-up: How to Implement

Thank you for the guidance. I’d like to implement the structure you recommended, but I need to proceed very slowly and explicitly, one step at a time.

## Proposed next step
Before doing anything with the API or ellmer, let’s start with **local file handling only**.

Specifically, I’d like to:
- Read `About EWB.md` and `About Me.md` from disk in R
- Strip out their YAML headers
- Confirm that the remaining markdown body text is exactly what we expect

Please confirm whether this is the correct *first* step.  
If it is, implement **only this step**.

## What to include in this response
- R code only for:
  - Reading the two files
  - Removing the YAML headers
- Clear, line-by-line comments explaining what each part of the code does
- A simple checkpoint that prints or inspects the cleaned text so we can verify correctness before proceeding

## What NOT to include yet
- No API calls
- No ellmer usage yet
- No prompt construction
- No discussion of later steps beyond a brief sentence saying what would come next

## Constraints
- Language: **R**
- Assume I am new to API-oriented workflows
- Optimize for clarity and debuggability over cleverness


---

# Follow-up: How to Implement 2

I’m ready to move to the next step and want to proceed carefully.

### Proposed next step
I believe the next step is to **combine the cleaned context texts** (`About EWB.md`, `About Me.md`) **with the draft wiki page** (`Initial Draft.md`) into a **single, structured prompt string** that is *ready* to be sent to an LLM later.

Please confirm whether this is the correct *next* step.  
If it is, implement **only this step**.

### What to include in this response
- R code that:
  - Reads the cleaned versions of the two context files and the draft wiki page
  - Combines them into one prompt string with clear section labels (e.g., “Context: About EWB”, “Context: About Me”, “Draft Wiki Page”)
- Clear, line-by-line comments explaining what each part of the code does
- A simple checkpoint that prints or inspects the final prompt string so we can verify:
  - Section ordering
  - Labeling
  - That no YAML headers are included

### What NOT to include yet
- No API calls
- No ellmer usage
- No system/user role structuring
- No discussion of later steps beyond a brief note on what comes next

### Constraints
- Language: **R**
- Assume I am new to API-oriented workflows
- Optimize for clarity and debuggability over cleverness

