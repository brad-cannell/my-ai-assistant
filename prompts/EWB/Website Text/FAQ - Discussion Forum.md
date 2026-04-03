---
title: "FAQ: Discussion Forum"
id: faq_discussion_forum
status: draft
author: "Brad Cannell"
created: 2025-12-29
last_updated: 2025-12-29
tags:
  - faq
  - discussion forum
---

<!--
YAML HEADER INSTRUCTIONS

Complete the YAML header below for every prompt. These fields support organization,
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
- At our 2025-12-17 meeting, we discussed the need to add some general directions for using the discussion forum. For example, using the feature request tag and maybe a code of conduct.
- Brad needs to write the text for this.
- We will also pin a thread to the top of the discussion forum with some usage notes.

# SYSTEM PROMPT

You are a helpful assistant with expertise in technical writing and website user experience design.

---

# User Message

## Context

- Epi-Workbench has a discussion forum (https://forum.epi-workbench.com/).
- Our goal is to make the discussion forum a "value add" feature of our website. A place where learners and course authors can ask questions about epidemiology and statistical programming, exchange ideas, network, and request EWB features/courses.
- Currently, there aren't any written instruction for using the discussion forum. 
- We would like to create some guidelines and instruction for using the discussion forum. 

### User experience

- The discussion forum page doesn't support standalone documentation. 
- Therefore, our current plan is to write write the documentation in an FAQ format and add it to the EWB FAQ page (https://dev.epi-workbench.com/EPIWorkBench/FAQs/).
- Then, we will create a "pinned" post to the top of the discussion forum that will contain some brief instructions that link to the relevant section(s) of the FAQ page.

### FAQ page

- We will create a new "Discussion Forum" category on the FAQ page (https://dev.epi-workbench.com/EPIWorkBench/FAQs/).
- Here are some draft questions and answers to start with:
  - Question: "What is the discussion forum code of conduct?"
  - Answer: We should create something similar to the Stack Overflow code of conduct: https://stackoverflow.com/conduct
  - Question: "What is the expected behavior on the discussion forum?"
  - Answer: We should create something similar to this Stack Overflow post: https://stackoverflow.com/help/behavior
  - Question: "How do I write a good question?"
  - Answer: We should create a summary of this R for Epidemiology chapter: https://www.r4epi.com/chapters/asking_questions/asking_questions
  - Question: "How do I write a good answer?"
  - Answer: We should create something similar to this Stack Overflow post: https://stackoverflow.com/help/how-to-answer
  - Question: "How do I use tags to find topics I'm interested in?"
  - Answer: We should create something similar to this Stack Overflow post: https://stackoverflow.com/help/interesting-topics. Let's specifically call out the "Feature Requests" tag as a way to request new features and content.
  
### Pinned Thread

- The pinned thread on the discussion forum (https://forum.epi-workbench.com/) will contain a brief welcome message, a paragraph that summarizes some of the key points from the FAQs, and link to the FAQs for details.

## Task

- Please help me develop documentation for the EWB discussion forum.
- As a first step, please provide feedback on the general approach described above (mix FAQ and pinned thread). If you see problems with this approach, please suggest alternative approaches.
- In a subsequent chat, after we decide on the approach, we will finalize the language for the documentation. Not now.

## Constraints & Formatting

- None at this time.