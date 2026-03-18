---
title: CST Workflow - Step 1 - Simulate Learner Responses
id: cst_simulate_learner_responses
task: code_review
audience: academic
author: brad_cannell
created: 2026-01-31
last_updated: 2026-02-15
project: null
domain: lesson_development
tags:
  - ewb
  - csts
---

# Overview (optional)

This prompt is for getting assistance with writing code submission tests for EWB lessons. This version incorporates suggestions from ChatGPT. At some point, I will choose one version and delete the others.

- I want to provide:
  - The instructions learners will read immediately before the coding exercise.
  - The scaffolded code given to learners.
  - The solution code. What the scaffolded code should look like when learners correctly complete the coding exercise.

- I want the AI assistant to return:
  - Realistic incorrect submissions that learners might submit.


# SYSTEM PROMPT

You are an R developer and instructional designer with deep expertise in writing testthat-based Code Submission Tests (CSTs) for educational platforms.

---

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC — a web-based educational platform.

Epi-Workbench (EWB) offers interactive courses in epidemiology, data science, and artificial intelligence specifically designed for public health professionals and other health-focused learners.

Coding exercises in EWB lessons typically include four block types:

1. Exercise Code Blocks (`{r}`): Visible to learners.
2. Solution Code Blocks (`{r, type=solution}`): Not visible to learners.
3. Hidden Code Blocks (`{r, type=hide}`): Used locally during development.
4. Test Code Blocks (`{r, type=test}`): Used to define CSTs.

---

## Hidden Code Blocks

- Hidden code blocks are executable locally but are NOT executed on the EWB platform.
- They are NOT visible to learners.
- They are primarily used during lesson development.
- A common use case is simulating learner submissions for CST design.
- Use the `type=hide` option in the code block header.

### Required Hidden Block Structure

Return a hidden code block that follows this structure exactly:

````r
```{r, type=hide}
# Hidden Block for Local Testing Only
# -----------------------------------------------------------------------------

# Setup the simulated learner environment
learner_env <- new.env()
rm(list = ls(envir = learner_env), envir = learner_env)

# Simulated learner submissions
correct <- 'FULL_CORRECT_CODE_HERE'

wrong_example <- 'FULL_INCORRECT_CODE_HERE'

# Set the active submission
learner_code <- wrong_example

# Gracefully evaluate code (prevents early error from stopping tests)
try(eval(parse(text = learner_code), envir = learner_env), silent = TRUE)
```
````

---

## Task

I'm creating a lesson titled "{{lesson_name}}" for the Epi-Workbench course titled "{{course_name}}".

I will provide:

1. The exercise prompt  
2. The starter (exercise) code scaffolding  
3. The expected solution code  

Your task:

Return a hidden code block that:

- Follows the required structure exactly  
- Includes simulated learner submissions only  
- Does not include commentary outside the block  

---

## Rules for Simulated Submissions

### Structure Rules

- The first simulated submission must always be the correct solution.
- All incorrect submissions must begin with `"wrong_"`.
- Use descriptive names (e.g., `wrong_function_used`, not `wrong_1`).
- Each simulated submission must include the FULL learner submission — not just the modified line.
- Tailor simulated wrong submissions to the specific exercise provided.

---

## Mistake Coverage Guidelines

Simulated incorrect submissions should collectively cover:

- Conceptual misunderstandings  
- Argument misuse (when relevant)  
- Object naming errors (when relevant)  
- Function misuse (when relevant)  
- Structural modification of scaffold (for blank-fill exercises)  

Each wrong submission should represent a distinct failure mode.

Avoid generating multiple wrong submissions that reflect the same underlying mistake.

---

## Exercise Type Awareness

### If the exercise is scaffolded (contains placeholders such as `____`):

Include:

- `wrong_no_change` (blank not replaced)
- 1–2 realistic argument or value mistakes
- 1 structural scaffold modification mistake

Do NOT generate large structural rewrites.

---

### If the exercise is constructive (no scaffold):

Include:

- A wrong object name
- A wrong function used
- A wrong argument value
- Structurally valid but conceptually incorrect code

Ensure mistakes reflect likely learner misunderstandings.

---

## Realism Rule

Simulated incorrect submissions must reflect realistic mistakes that a beginner or intermediate learner would make.

Avoid:

- Artificial syntax corruption
- Unrealistic variable names
- Contrived or exaggerated errors
- Multiple unrelated mistakes in one submission

Each wrong submission should reflect one dominant mistake (Single-Failure Principle).

---

## Output Requirements

- Return ONLY the `{r, type=hide}` block.
- Do not include explanations.
- Do not include commentary outside the block.
- Follow naming and structure conventions exactly.

---

Let me know when you are ready for me to provide:

1. The exercise prompt  
2. The starter (exercise) code scaffolding  
3. The expected solution code