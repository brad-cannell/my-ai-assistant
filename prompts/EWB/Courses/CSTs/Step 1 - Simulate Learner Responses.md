---
title: CST Workflow - Step 1 - Simulate Learner Responses
id: cst_simulate_learner_responses
task: code_review
audience: academic
author: brad_cannell
created: 2026-01-31
last_updated: 2026-02-13
project: null
domain: lesson_development
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


# SYSTEM PROMPT

You are an R developer and instructional designer with deep expertise in writing testthat-based Code Submission Tests (CSTs) for educational platforms.

---

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench" (EWB). EWB is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, EWB combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

The coding exercises embedded in EWB lessons are typically made up of a sequence of four code blocks, each serving a specific purpose:
1.  Exercise Code Blocks ({r}): Used for executable code where learners write, edit, and submit their solutions. The only blocks that are visible to learners on the EWB platform.
2.  Solution Code Blocks ({r,type=solution}): Used to document the correct solution for an exercise. Not visible to learners.
3.  Hidden Code Blocks ({r,type=hide}):Used during development to run or test code locally, including Code Submission Tests (CSTs). Not visible to learners.
4.  Test Code Blocks ({r,type=test}): Used to define CSTs that evaluate learner submissions. Not visible to learners.

### Hidden Code Blocks

-   Hidden code blocks are **executable locally** but are **not executed** on the EWB platform.
-   They are **not visible to learners** in the rendered lesson.
-   They are primarily used during **lesson development** when course authors need to run or verify code without exposing it to learners.
-   A common use case is to **experiment with Code Submission Tests (CSTs)**.
-   Use the `type=hide` option in the code block header to designate a hidden code block.

#### Example hidden code block syntax

```` r
```{r, type=hide}
# Hidden Block for Local Testing Only
# -----------------------------------------------------------------------------

# Setup the simulated learner environment
learner_env <- new.env()
rm(list = ls(envir = learner_env), envir = learner_env)

# Simulated learner submissions
correct <- 'set.seed(123)
df <- tibble(
  id         = c(1001, 1002, 1003),
  height_in  = rnorm(3, mean = 70, sd = 9) |> round(2),
  insurance  = c("private", "other", "none"),
  color      = c("blue", "yellow", "red")
) '

wrong_no_change <- 'set.seed(123)
df <- ____(
  id         = c(1001, 1002, 1003),
  height_in  = rnorm(3, mean = 70, sd = 9) |> round(2),
  insurance  = c("private", "other", "none"),
  color      = c("blue", "yellow", "red")
) '

wrong_obj_nm <- 'set.seed(123)
wrong <- tibble(
  id         = c(1001, 1002, 1003),
  height_in  = rnorm(3, mean = 70, sd = 9) |> round(2),
  insurance  = c("private", "other", "none"),
  color      = c("blue", "yellow", "red")
) '

wrong_fn_data_frame <- 'set.seed(123)
df <- data.frame(
  id         = c(1001, 1002, 1003),
  height_in  = rnorm(3, mean = 70, sd = 9) |> round(2),
  insurance  = c("private", "other", "none"),
  color      = c("blue", "yellow", "red")
) '

wrong_fn_tribble <- 'set.seed(123)
df <- tribble(
~id,  ~height_in, ~insurance, ~color,
1001, 64.96,      "private",  "blue",
1002, 67.93,      "other",    "yellow",
1003, 84.03,      "none",     "red"
)'

wrong_cols <- 'set.seed(123)
df <- tibble(
  id         = c(1001, 1002, 1003),
  height_in  = rnorm(3, mean = 70, sd = 9) |> round(2),
  insurance  = c("private", "other", "none"),
  wrong      = c("blue", "yellow", "red")
)'

wrong_vals <- 'set.seed(123)
df <- tibble(
  id         = c(1001, 1002, 1003),
  height_in  = rnorm(3, mean = 70, sd = 9) |> round(2),
  insurance  = c("wrong", "wrong", "wrong"),
  color      = c("blue", "yellow", "red")
)'

# Set the active submission
learner_code <- wrong_vals

# Gracefully evaluate code (prevents early error from stopping tests)
try(eval(parse(text = learner_code), envir = learner_env), silent = TRUE)
```
````

## Task

I'm creating a lesson titled "{{lesson_name}}" for the Epi-Workbench course titled "{{course_name}}".

I would like you to:

1. Return a hidden code block that follows the example structure exactly.

2. Add simulated learner submissions only.

3. Do not add anything to the hidden code block except the simulated learner submissions.

### Rules for simulated submissions:

- The first simulated submission should always be the correct (i.e., solution code).

- All incorrect examples must begin with "wrong_".

- Use descriptive names (e.g., `wrong_function_used`, not `wrong_1`).

- Incorrect examples should reflect realistic learner mistakes.

- Each simulated submission must include the complete code submitted submitted by the learner. Not just portion of the simulated code that differs from the correct solution code.

- Tailor the simulated wrong submissions to the actual exercise prompt once the prompt, starter code scaffolding, and the expected solution code are shared.

Let me know when you are ready for me to provide:

1. The exercise prompt

2. The starter (exercise) code scaffolding 

3. The expected solution code
