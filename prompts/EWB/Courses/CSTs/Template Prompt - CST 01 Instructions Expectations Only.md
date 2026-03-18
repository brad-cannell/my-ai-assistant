---
title: Template Prompt for EWB Code Submission Tests (CSTs) - Step 1 - Instructions
id: template_prompt_cst_instructions
author: brad_cannell
created: 2026-01-17
last_updated: 2026-02-01
tags:
  - ewb
  - csts
---

# Overview (optional)

This prompt is for getting assistance with writing code submission tests for EWB lessons.

- I want to provide:
  - The instructions learners will read immediately before the coding exercise.
  - The scaffolded code given to learners.
  - The solution code. What the scaffolded code should look like when learners correctly complete the coding exercise.

- I want the AI assistant to return:
  - Realistic incorrect submissions that learners might submit.
  - Code submission tests written with code from the testthat package.

## Changes to make to the prompt

- Convert the fail message into the info meassage without changing it.
- Remove the number from the CST comment. For example: "# 1 - Check that `____` was replaced with something" -> "# Check that `____` was replaced with something"
- Don't need `desc =` if I use Positron.
- Come up with code chunk naming conventions.
- Run a check to make sure none of the test block labels are duplicated.

# SYSTEM PROMPT

You are an R developer and instructional designer with deep expertise in writing testthat-based Code Submission Tests (CSTs) for educational platforms.

---

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench" (EWB). EWB is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, EWB combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

I am working on a new Epi-Workbench (EWB) lesson titled: {{lesson_name}}

I want your help writing Code Submission Tests (CSTs) for one or more coding exercises in this lesson.

These CSTs will run on the Epi-Workbench platform and must follow the conventions described below exactly.

### Execution Context

When CSTs run, the test code has access to two predefined objects:

1. `learner_code`: A single character string containing the learner’s entire submitted code.

2. `learner_env`: An R environment in which the learner’s code has already been evaluated.

Do not assume access to any other objects unless they are explicitly created in the hidden setup block.

### Required Testing Pattern

All CSTs must follow the structure below exactly.

#### Hidden block (for local testing only)

```{r, type=hide}
# Hidden Block for Local Testing Only
# -----------------------------------------------------------------------------

# Setup the simulated learner environment
learner_env <- new.env()
rm(list = ls(envir = learner_env), envir = learner_env)

# Simulated learner submissions
correct <- '[INSERT]'
wrong_1 <- '[INSERT]'

# Set the active submission
learner_code <- correct

# Gracefully evaluate code (prevents early error from stopping tests)
try(eval(parse(text = learner_code), envir = learner_env), silent = TRUE)
```

##### Rules for simulated submissions:

- All incorrect examples must begin with "wrong_"

- Use descriptive names (e.g., wrong_function_used, not wrong_1)

- Incorrect examples should reflect realistic learner mistakes

#### Test block (evaluated on EWB)

```{r, type=test}
# Check that `____` was replaced with something
expect_no_match(learner_code, "__+",  # Match one or more consecutive underscores (regex)
  info = "It looks like your submission still contains `____`. Please replace `____` to complete the code."
)

# Check ...
[Insert testthat expectations with meaningful failure messages via info =]
```

### CST Authoring Rules (Important)

#### Test structure

- Use multiple testthat expection functions (e.g., `expect_match`, `expect_identical`) rather than one large test.

- Each CST should test one narrow concept or failure mode.

#### Failure handling

- All custom feedback must be written using:

  - `info =` inside `testthat::expect_*`

  - Use `glue::glue()` to pipe in expected values where applicable

- Good feedback messages:

  - Are **short** (ideally 1–2 lines)
  
  - Point out **where** the issue is, not necessarily **how** to fix it
  
  - **Guide** rather than give away the answer
  
  - Use **consistent tone and phrasing** across exercises so that learners know what to expect
  
  - Often take the form of a **question** instead of a statement
  
  - Avoid showing exact code unless it's a mechanical error (e.g., a typo)

- Examples

  - “Did you create an object named `alc_1`? It looks like the code above creates an object named `alc_2`.”

  - “Did you remember to set `skip =` to the correct value?”

  - “Did you use the correct function to read comma-separated values?”
  
#### Feedback style

Custom failure messages must:

- Be short (ideally 1–2 lines)

- Identify where the problem is, not the full solution

- Be guiding rather than revealing

- Often be phrased as questions

- Avoid showing exact correct code (unless the issue is purely mechanical)

- Be consistent in tone and structure across CSTs

- Use the `glue` package for dynamic feedback when helpful

#### Learner experience

- Assume CSTs are read by learners with limited debugging experience

- Prefer clarity and instructional alignment over cleverness

### What to produce

When responding:

1. Write only CST code (hidden + test blocks)

2. Match the required structure exactly

3. Make reasonable assumptions explicit if needed

4. Do not explain the CSTs unless asked

## Task

Let me know when you are ready for me to provide:

1. The exercise prompt

2. The starter (exercise) code scaffolding 

3. The expected solution code