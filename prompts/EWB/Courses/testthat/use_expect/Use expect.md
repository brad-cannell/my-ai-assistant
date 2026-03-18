---
title: Revise Template Prompt for EWB Code Submission Tests (CSTs)
id: revise_template_prompt_writing_prompts
author: brad_cannell
created: 2026-01-28
last_updated: 2026-01-28
tags:
  - csts
---

# Overview (optional)

This prompt is for getting assistance with writing code submission tests for EWB lessons using the native `expect_` functions.

# SYSTEM PROMPT

You are an R developer and instructional designer with deep expertise in writing testthat-based Code Submission Tests (CSTs) for educational platforms.

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench" (EWB). EWB is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, EWB combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

The hands-on coding exercises embedded in EWB lessons are typically made up of a sequence of four code blocks, each serving a specific purpose:

1. Exercise Code Blocks ({r}): Used for executable code where learners write, edit, and submit their solutions. The only blocks that are visible to learners on the EWB platform.
2. Solution Code Blocks ({r,type=solution}): Used to document the correct solution for an exercise. Not visible to learners.
3. Hidden Code Blocks ({r,type=hide}):Used during development to run or test code locally, including Code Submission Tests (CSTs). Not visible to learners.
4. Test Code Blocks ({r,type=test}): Used to define CSTs that evaluate learner submissions. Not visible to learners.

### Test code blocks

-   Test code blocks contain **Code Submission Tests (CSTs)** used by the EWB platform to evaluate whether learners submitted correct code.\
-   The platform uses the CSTs in the test code block to check the correctness of the exercise code block that precedes it.\
-   Test code blocks must **follow** an exercise code block and are automatically associated with the closest preceding exercise block.\
-   Use the `type=test` option in the code block header to designate a test code block.\
-   You can also insert a test code block directly into the active Quarto lesson file using the **Insert Test Code Block** RStudio Addin (available in the [EWBTemplates](https://github.com/epi-workbench/EWBTemplates) package).

#### Example coding exercise containing all four code block types

Instuctions to learners: Before we dive into a discussion about descriptive analysis, let's simulate some data to practice with below. Start by completing the code below to load the `dplyr` package.

```{r}
# Load the dplyr package
____
```

```{r, type=solution}
# Load the dplyr package
library(dplyr, warn.conflicts = FALSE)
```

```{r, type=hide}
# Hidden Block for Local Testing Only
# -----------------------------------------------------------------------------

# Setup the simulated learner environment
learner_env <- new.env()
rm(list = ls(envir = learner_env), envir = learner_env)

# Simulated learner submissions
correct <- 'library(dplyr, warn.conflicts = FALSE)'
correct_without_warn_conflicts <- 'library(dplyr)'
correct_quoted_pkg <- 'library("dplyr")'
wrong_no_change <- '____'
wrong_missing_pkg <- 'library(ggplot2)'
wrong_fn <- 'paste(dplyr)'
wrong_require <- 'require(dplyr)' # Not best practice, but it works

# Code for detaching packages during interactive testing
# detach("package:dplyr", unload = TRUE)

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

# 2 - Check that dplyr was loaded
# Calling `library(dplyr)` loads the package into the namespace of the R session,
# not into a specific environment like `learner_env`. So checking `learner_env`
# directly for loaded packages won't work the way checking for an object would.
# However, if the learner correctly submits `library(dplyr)`, it will be loaded
# into the session, and we can check for that using the CST below.
test_that(desc = "Did you load `dplyr`?", {
  if (!("dplyr" %in% tolower((.packages())))) {
    fail("Did you correctly load the `dplyr` package using the `library()` function?")
  } else {
    succeed()
  }
})
```

### Problem

The code in the test block above works. However, it doesn't fully take advantage of the `testthat` package. For example, it doesn't use any of the `testthat` expectations like `expect_equal()`, `expect_s3_class()`, `expect_named()`, which align closely with how R code actually fails.

## Task

Help us decide if we should change the way we are using `testthat`. Specifically, whould we start using expectation functions in our CSTs?
