---
title: Generate Code Submission COL Questions From Lesson
id: generate_code_submission_col_from_lesson
date: brad_cannell
created: 2026-01-28
date-modified: 2026-01-28
interface: both
tags:
  - col
  - quizzes
---

# Overview (optional)
This prompt enables an AI to scan a Quarto Markdown lesson file for coding exercises and automatically generate 1-3 code submission COL (Code Submission) questions per exercise. Each generated COL question should reinforce the original concept without duplicating the exact solution from the lesson. The output should be formatted as Epi-Workbench (EWB) exercise blocks plus accompanying solution blocks suitable for the platform, using R with the tidyverse and testthat for CSTs.

We will request CSTs in a separate prompt.

# SYSTEM PROMPT

You are a helpful assistant that creates Code Submission COL questions for Epi-Workbench lessons.

# USER MESSAGE

## Context

You will be provided with the contents of a lesson file (Quarto Markdown, .qmd). The lesson contains one or more coding exercises, each typically presented as an explanatory text block followed by an R code block (e.g., an exercise block with {r}). For example, a lesson might include:

````markdown
Assign the value 2 to an object named `x`.
```{r}
x <- 2
```
````

## Task

Generate 2-5 code submission COL questions. Each COL question should reinforce the same concepts as the exercises but should not duplicate the exact solution. For example, if the exercise assigns x <- 2, a corresponding COL question might ask the learner to assign a different value to a similarly named object, or perform a related operation using a different value.

### Optional Lesson-Specific Guidance

If additional guidance is provided below, incorporate it when designing the COL questions. 
If no guidance is provided, proceed using only the general instructions.

{{lesson_specific_guidance}}

## Constraints & Formatting

Each COL question must be delivered as a pair of blocks:
  1) A Code Submission exercise block for learners to complete (R code). Use the EWB scaffolding conventions:
     - Use {r} for the code block.
     - Provide scaffolding as needed:
       - Complete scaffolding (fully filled) for introducing a concept, or
       - Partial scaffolding using blanks (____) to indicate missing code. Each blank should be represented by underscores, and different blocks should vary the number of underscores to ensure uniqueness.
       - No scaffolding (just blanks) is allowed in isolation; if used, ensure at least one non-blank line is present in the block to avoid an empty block.
     - Ensure each exercise block is unique (e.g., different variable names, different values, or different functions) so that CSTs can reliably distinguish them.
     - Do not reveal the exact solution to the learner in these blocks.
  2) A solution code block used to document the correct solution for the code submission question.
    - Use a separate code block with the header {r, type=solution}.

- Data and context alignment:
  - Each new COL question should reference the same dataset and variable names used in the corresponding exercise, when possible.
  - If the original exercise uses a specific dataset and variable (e.g., census$region_f), refer to the same concept but you may a different variable to ensure uniqueness across questions. The tests should still validate the intended outcome (e.g., a count per category, a summary statistic, etc.).
  - You may write code to generate new data if a suitable option doesn't already exist in the lesson.

- Uniqueness:
  - Every exercise block generated must be unique. Do not reuse identical code blocks across COL questions.

- Formatting:
  - Deliver blocks in Markdown as separate consecutive blocks.
  - Use the same Markdown rendering conventions as EWB (three backticks with {r} for code blocks and {r,type=solution} for solution blocks).
  - Do not include extraneous explanation outside the blocks; present only the generated COL blocks for each exercise, in order.

- Output language and framework:
  - Primary language: R
  - Libraries: tidyverse
  - Output style: Markdown blocks with the appropriate header in each block, no external links or verbose narration.

- Practical guidance:
  - If an exercise block is already fully scaffolded, you may still create 1-3 additional COL questions by varying the data or the requested operation slightly (e.g., change the target variable, use a different aggregation, or change the required output format) while keeping the concept intact.
  - If the lesson contains multiple exercises, ensure you generate 1-3 COL questions per exercise and present them sequentially.

- End-of-output rule:
  - Do not include any preface or meta-commentary. Present only the generated COL blocks, grouped per original exercise.

## Lesson File Content

{{lesson_content}}