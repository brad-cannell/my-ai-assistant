---
title: ADR SharePoint Welcome Screen
id: adr_welcome
task: text_revision
audience: academic
status: draft
author: "Brad Cannell"
created: 2025-12-27
last_updated: 2025-12-27
project: adr_sharepoint
domain: academia
tags:
  - tag1
  - tag2
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
Make a welcome page for the ADR SharePoint site.
- Introduce myself.
- Introduce the purpose of the SharePoint site.
- The primary purpose is to answer people's questions. However, I should probably provide links more than writing my own answers. I want the most up to date information possible and it will get stale if I write it.
- Should we use SharePoint or something else? People are more familiar with box. Maybe this should be the first prompt.
- Should I also create an ADR-oriented "About Me" snippet?

---

# SYSTEM PROMPT

You are a helpful assistant with expertise in technical writing, corporate communications, and SharePoint.

- 2025-12-28: Left off here so I could go to bed.

---

# User Message

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
