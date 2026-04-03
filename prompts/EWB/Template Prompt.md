---
title: <short, human-readable title>
id: <unique_prompt_id>
interface: <api | browser | both >
author: brad_cannell
created: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
tags:
  - tag1
  - tag2
---

<!--
YAML HEADER INSTRUCTIONS

Complete the YAML header above for every prompt. These fields support organization, reuse, and future search, but should remain lightweight and human-readable.

FIELD DESCRIPTIONS
- title: A brief, human-readable description of what the prompt does. Written in Title Case.
- id: Use a short, stable, human-readable identifier in lowercase snake_case.
- task: The primary type of work the prompt performs (e.g., text_revision, code_review). Written in snake_case.
- audience: The intended audience for the output (e.g., academic, student, developer). Written in snake_case.
- interface: Interface used to interact with AI assistant (api, browser, both). Written in snake_case.
- author: Name of the prompt author. Written in snake_case.
- created: Date the prompt was first created (YYYY-MM-DD).
- last_updated: Date of the most recent substantive revision (YYYY-MM-DD).
- project: Associated project, course, or initiative, or null if broadly reusable. Written in snake_case.
- domain: Subject area or disciplinary context (e.g., epidemiology, data_science, general). Written in snake_case.
- tags: Optional keywords to support browsing and future search. Written in snake_case.

ID GUIDELINES
- id: Use a short, stable, human-readable identifier in lowercase snake_case.
- Base the id on the prompt’s core purpose using a verb–object pattern
  (e.g., rewrite_academic_tone, review_r_code_style).
- Avoid dates, version numbers, model names, project names, or author names.
- Treat the id as permanent; change it only if the prompt’s fundamental purpose changes.

Avoid including model names or API parameters in the YAML header.
-->

# Overview (optional)
Briefly describe *why* this prompt exists and *when* it should be used. This section is for the prompt author or future maintainers, not the AI assistant.

Use this space to capture motivation, background, assumptions, or reminders that should not be included in the system prompt or user instructions.

# SYSTEM PROMPT

Describe the role the model should assume.

> Example:  
> You are a helpful assistant for drafting academic manuscripts in public health.
> You are a technology consultant with deep expertise in AI/LLMs and developer-facing AI tooling, with particular strength in minimal, practical setups for academic workflows.

---

# USER MESSAGE

## Context
Provide any background information the model needs to perform well.

> Example:  
> *The text comes from the methods section of an epidemiologic study intended for submission to a peer-reviewed journal.*

## Task
State clearly what the model should do.

> Example:  
> *Rewrite the provided text to be more formal and concise while preserving the original meaning.*

## Constraints & Formatting
List any important constraints or rules.
- Preserve the original meaning
- Avoid adding new information
- Maintain an academic tone
- Primary Language: R (Tidyverse)
- Citation Style: APA 7th Edition
- Format: {{output_format}}
