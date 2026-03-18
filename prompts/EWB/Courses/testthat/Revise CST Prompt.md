---
title: Revise Template Prompt for EWB Code Submission Tests (CSTs)
id: revise_template_prompt_writing_prompts
author: brad_cannell
created: 2026-01-17
last_updated: 2026-01-17
tags:
  - ai
  - prompts
  - csts
---

# Overview (optional)

The purpose of this prompt is to write a better template prompt for getting help with writing CSTS.

I probably won't use the API for this one. I'll probably just pass it to ChatGPT through the browser.

# SYSTEM PROMPT

You are a technology consultant with deep expertise in AI and LLMs.

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench" (EWB). EWB is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, EWB combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

The hands-on coding exercises embedded in EWB lessons are typically made up of a sequence of four code blocks, each serving a specific purpose:

1. Exercise Code Blocks ({r}): Used for executable code where learners write, edit, and submit their solutions. The only blocks that are visible to learners on the EWB platform.
2. Solution Code Blocks ({r,type=solution}): Used to document the correct solution for an exercise. Not visible to learners.
3. Hidden Code Blocks ({r,type=hide}):Used during development to run or test code locally, including Code Submission Tests (CSTs). Not visible to learners.
4. Test Code Blocks ({r,type=test}): Used to define CSTs that evaluate learner submissions. Not visible to learners.

## Task

Please help me write a prompt that I can pass to an AI assistant requesting help with writing CSTs. Here's the draft I have so far:

I'm working on a new EWB lesson called "Insert_Lesson_Name".

I want your help writing [testthat](https://testthat.r-lib.org/index.html) Code Submission Tests (CSTs) for one or more coding exercises in this lesson.

The tests we write will run on the EWB platform and will have access to these two variables:

1. `learner_code`: A character string containing the learner’s full submitted code.

2. `learner_env`: An environment where that code has already been evaluated.

Please follow these instructions when writing test code:

- Instead of using `expect_*()` with `info =`, write all custom failure messages using the `fail()` function inside an `if (...)` or `else if (...)` block. Only call `succeed()` or `expect_true(TRUE)` at the end of a successful branch to pass the test.

- Match the test code structure shown below exactly.

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

```{r, type=test}
# 1 - Check that `____` was replaced with something
test_that(desc = "All blanks `____` were replaced", {
  if (grepl("____", learner_code, fixed = TRUE)) {
    fail("It looks like your submission still contains `____`. Please replace `____` to complete the code.")
  } else {
    succeed()
  }
})

# 2 - Check ...
test_that(desc = "Concise statement of the test's purpose", {
  if (condition 1) {
    fail("Meaningful failure message")
  } else {
    succeed()
  }
})
```

- When simulating incorrect learner submissions in the hidden code block, please use descriptive names like wrong_function_used, not wrong_1. However, they should all begin with the word "wrong".

- The first thing the learner will see in the toast is TEST FAILED: followed by a description of the test that failed. The description is taken from the desc argument to the test_that() function used to write the CST. The description should be a concise statement of the CST's purpose.

- The custom failure messages:
  - Are short (ideally 1–2 lines).
  - Identify where the problem is, but not necessarily what the correct answer is.
  - Are guiding, not giving. Think nudge, don't solve.
  - Are consistent across exercises, so learners know what to expect.
  - Often prefer questions over statements
  - Avoid revealing the solution unless it's a simple mechanical error (e.g., typo or missing object), avoid showing exact code in feedback.
  - Use the `glue` package to inject dynamic feedback when helpful.

- In general, we prefer breaking up CSTs into multiple `testthat` blocks with a narrower focus to long `testhat` blocks that test lots of things. We will show some concrete examples in the docs.

When you are ready, I'll pass you information about coding exercises I need your help writing CSTs for.
