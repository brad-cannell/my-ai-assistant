## User

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench" (EWB). EWB is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, EWB combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

The coding exercises embedded in EWB lessons are typically made up of a sequence of four code blocks, each serving a specific purpose:

Exercise Code Blocks ({r}): Used for executable code where learners write, edit, and submit their solutions. The only blocks that are visible to learners on the EWB platform.

Solution Code Blocks ({r,type=solution}): Used to document the correct solution for an exercise. Not visible to learners.

Hidden Code Blocks ({r,type=hide}):Used during development to run or test code locally, including Code Submission Tests (CSTs). Not visible to learners.

Test Code Blocks ({r,type=test}): Used to define CSTs that evaluate learner submissions. Not visible to learners.

Test code blocks

Test code blocks contain Code Submission Tests (CSTs) used by the EWB platform to evaluate whether learners submitted correct code.

The platform uses the CSTs in the test code block to check the correctness of the exercise code block that precedes it.

Test code blocks must follow an exercise code block and are automatically associated with the closest preceding exercise block.

Use the type=test option in the code block header to designate a test code block.

You can also insert a test code block directly into the active Quarto lesson file using the Insert Test Code Block RStudio Addin (available in the EWBTemplates package).

Example coding exercise containing all four code block types

Instuctions to learners: Before we dive into a discussion about descriptive analysis, let's simulate some data to practice with below. Start by completing the code below to load the dplyr package.

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

Current process

When developing courses, our current process is:

We write and refine the lesson text in a Quarto file. Initially, solution code blocks are the only type of coding exercise blocks in the Quarto lesson file.

We create an exercise code block with code scaffolding.

We write instructions for completing each coding exercise.

We open a ChatGPT chat.

We pass each set of instructions, exercise code block, and solution block to ChatGPT using the prompt titled, "Template Prompt - CST 01 Instructions" (provided below).

ChatGPT returns suggestions for hidden code blocks and test code blocks containing CSTs.

Template Prompt - CST 01 Instructions

'---\ntitle: Template Prompt for EWB Code Submission Tests (CSTs) - Step 1 - Instructions\nid: template_prompt_cst_instructions\ntask: code_review\naudience: academic\nauthor: brad_cannell\ncreated: 2026-01-17\nlast_updated: 2026-01-17\nproject: null\ndomain: lesson_development\ntags:\n  - ewb\n  - csts\n---\n\n# Overview (optional)\n\nThis prompt is for getting assistance with writing code submission tests for EWB lessons.\n\n- I want to provide:\n  - The instructions learners will read immediately before the coding exercise.\n  - The scaffolded code given to learners.\n  - The solution code. What the scaffolded code should look like when learners correctly complete the coding exercise.\n\n- I want the AI assistant to return:\n  - Realistic incorrect submissions that learners might submit.\n  - Code submission tests written with code from the testthat package.\n\n\n# SYSTEM PROMPT\n\nYou are an R developer and instructional designer with deep expertise in writing testthat-based Code Submission Tests (CSTs) for educational platforms.\n\n---\n\n# User Message\n\n## Context\n\nI am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.\n\nI am creating a web-based business called "Epi-Workbench" (EWB). EWB is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, EWB combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.\n\nI am working on a new Epi-Workbench (EWB) lesson titled:\n\n{{lesson_name}}\n\n## Task\n\nI want your help writing Code Submission Tests (CSTs) for one or more coding exercises in this lesson.\n\nThese CSTs will run on the Epi-Workbench platform and must follow the conventions described below exactly.\n\n### Execution Context\n\nWhen CSTs run, the test code has access to two predefined objects:\n\n1. `learner_code`: A single character string containing the learner’s entire submitted code.\n\n2. `learner_env`: An R environment in which the learner’s code has already been evaluated.\n\nDo not assume access to any other objects unless they are explicitly created in the hidden setup block.\n\n### Required Testing Pattern\n\nAll CSTs must follow the structure below exactly.\n\n#### Hidden block (for local testing only)\n\n```{r, type=hide}\n# Hidden Block for Local Testing Only\n# -----------------------------------------------------------------------------\n\n# Setup the simulated learner environment\nlearner_env <- new.env()\nrm(list = ls(envir = learner_env), envir = learner_env)\n\n# Simulated learner submissions\ncorrect <- \'[INSERT]\'\nwrong_1 <- \'[INSERT]\'\n\n# Set the active submission\nlearner_code <- correct\n\n# Gracefully evaluate code (prevents early error from stopping tests)\ntry(eval(parse(text = learner_code), envir = learner_env), silent = TRUE)\n```\n\n##### Rules for simulated submissions:\n\n- All incorrect examples must begin with "wrong_"\n\n- Use descriptive names (e.g., wrong_function_used, not wrong_1)\n\n- Incorrect examples should reflect realistic learner mistakes\n\n#### Test block (evaluated on EWB)\n\n```{r, type=test}\n# 1 - Check that `____` was replaced with something\ntest_that(desc = "All blanks `____` were replaced", {\n  if (grepl("____", learner_code, fixed = TRUE)) {\n    fail("It looks like your submission still contains `____`. Please replace `____` to complete the code.")\n  } else {\n    succeed()\n  }\n})\n\n# 2 - Check ...\ntest_that(desc = "Concise statement of the test\'s purpose", {\n  if (condition 1) {\n    fail("Meaningful failure message")\n  } else {\n    succeed()\n  }\n})\n```\n\n### CST Authoring Rules (Important)\n\n#### Test structure\n\n- Use multiple small `test_that()` blocks rather than one large test.\n\n- Each CST should test one narrow concept or failure mode.\n\n- The `desc` argument should be a concise statement of the test’s purpose, not a question and not the solution.\n\n#### Failure handling\n\n- Do not use `expect_*()` with `info =`\n\n- All custom feedback must be written using:\n\n  - `fail()` inside `if` / `else if` branches\n\n  - `succeed()` (or `expect_true(TRUE)`) at the end of a successful branch\n  \n#### Feedback style\n\nCustom failure messages must:\n\n- Be short (ideally 1–2 lines)\n\n- Identify where the problem is, not the full solution\n\n- Be guiding rather than revealing\n\n- Often be phrased as questions\n\n- Avoid showing exact correct code (unless the issue is purely mechanical)\n\n- Be consistent in tone and structure across CSTs\n\n- Use the `glue` package for dynamic feedback when helpful\n\n#### Learner experience\n\n- The learner will first see: `TEST FAILED:` followed by the `desc` string\n\n- Assume CSTs are read by learners with limited debugging experience\n\n- Prefer clarity and instructional alignment over cleverness\n\n### What to produce\n\nWhen responding:\n\n1. Write only CST code (hidden + test blocks)\n\n2. Match the required structure exactly\n\n3. Make reasonable assumptions explicit if needed\n\n4. Do not explain the CSTs unless asked\n\nWhen ready, I will provide:\n\n1. The exercise prompt\n\n2. The starter (exercise) code scaffolding \n\n3. The expected solution code\n\n4. Any edge cases to consider'

Issues

There are some issues with this process.

In the past, we explicitly asked ChatGPT not use testthat expectation functions (expect_). I can't remember why we made that decision, but I think we should start using testthat expectation functions (expect_). Here are some reasons why:

Clarity and diagnostics: Expectations produce standardized, actionable failure messages (e.g., what was expected vs what was actually observed) that are easier for learners to interpret.

Alignment with standard practice: testthat is the de facto unit testing framework for R. Using its expectations makes your CSTs easier to maintain, share, and extend. 

Granular feedback: You can have multiple, focused expectations within a single test block, so learners get precise feedback on each aspect of their submission.

Better reporting and tooling: expect_* functions integrate cleanly with testthat when you scale up to more exercises and analytics, and they work well with code coverage and continuous integration if you ever add it.

I would like to pass the entire lesson file to ChatGPT instead of passing one coding exercise at a time. I would then like ChatGPT to locate each coding exercise and fill in the remaining parts of the coding exercise (i.e, hidden code blocks, simulated learner responses, test code blocks, and CSTs). However, I think asking ChatGPT to do all of this one pass is likely to be too complicated. Therefore, I was thinking about creating a multi-step process:

User: Add scaffolding, solution block, and instructions to the lesson Quarto file.

ChatGPT: For each exercise, write simulated  learner responses. 

Return the simulated responses in hidden code blocks.

AI: For each simulated response, write one or more testthat tests using expect_ functions.

Maybe create a vector store or RAG with testthat documentation and EWB SOPs to help ensure consistent CSTs structure and feedback messages.

AI: For each exercise, write hints.

Again, use a vector store or RAG with EWB SOPs to ensure consistent hints for learners.

Adopt more of a "Unit testing" approach to the CSTs.

The current arrangement of code blocks in the lesson file can take up a lot of space. This doesn't affect the learner experience, but it makes the lesson files harder for the course authors to read and maintain.

We can abstract the text blocks or CSTs from the lesson file because the EWB parser looks for the CSTs in the test blocks in the lesson file.

Additionally, the EWB will only be aware of code that exists in the lesson file.

However, the EWB platform ignores hidden code blocks. Hidden code blocks are just for the benefit of course authors - to use for local testing. So, we could abstract them from the lesson file. 

I think we might be able to use a full unit testing approach like we would use for package development.

R Packages, Testing Basics: https://r-pkgs.org/testing-basics.html

testthat Documentation: https://testthat.r-lib.org/

In other words:

{r,type=test} blocks must stay inside the .qmd (because EWB discovers/executes CSTs there).

{r,type=hide} blocks are ignored by EWB and exist only to make local authoring/testing easier.

So the win is: remove hidden blocks from the lesson files entirely and replace them with a project-level local testing workflow that course authors run from the console (or a one-click script / addin). That keeps the “CSTs live in the lesson” rule intact, while making lesson files much easier to read.

Task

Please help me think through what my next steps should be. I need to balance creating a robust and efficient long-term workflow for writing and editing lesson files - including CSTs - with the need to put lessons into production on a relatively short timeline.

If you were an expert R developer and instructional designer with deep expertise in writing testthat-based Code Submission Tests (CSTs) for educational platforms, what would you suggest for my next steps?

## Assistant

Thank you for laying out the context so clearly. Based on your goals (robust, scalable CSTs; faster production; readable lessons; and the ability to mentor authors through a good workflow), here is a concrete, expert-oriented plan you can start implementing now. I’ll keep to actionable steps, with concrete patterns you can adopt immediately and a long-term roadmap.

Executive summary
- Move to a standardized, unit-test-like CST design using multiple small test_that blocks (expect_* based) instead of a few large checks.
- Keep the four-block CST pattern (Exercise code block, solution, hidden, tests) but standardize content and automation around it.
- Build a lightweight CST authoring toolkit plus templates to automatically generate hidden and test blocks from a concise exercise spec.
- Pilot with a small set of lessons, gather feedback, then scale.
- Decide on a canonical stance regarding hidden blocks vs externalized testing (recommended: keep hidden blocks for local authoring, but progressively decouple heavy testing from lesson files via a project-level testing workflow).
- Introduce a formal CST style guide and onboarding for lesson authors.

Phase-by-phase plan with concrete steps

Phase 0 — Decide and document core CST standards (1–2 weeks)
- Decide now:
  - Use testthat expect_* functions for clear diagnostics (aligns with modern practice and your diagnostic goals).
  - Keep the four block structure in Quarto (Exercise block, type=solution, type=hide, type=test) for backward compatibility with EWB parsing.
  - Keep hidden code blocks for local authoring/testing but minimize their burden on production lessons (see Phase 2 for how to wire this into a workflow).
- Produce a concise CST design guide you publish for authors and maintain in a shared repository. Include:
  - Naming conventions: exercise_id, block_type (exchangeable with Quarto’s type=..., e.g., {r}, {r,type=solution}, {r,type=hide}, {r,type=test}).
  - Required CST patterns per exercise (what must be tested, how many test_that blocks, expected messages).
  - How to structure learner submissions (simulate several plausible wrong submissions for authors to model in the hidden block).
  - Feedback style rules (short, actionable, guiding; avoid revealing full solution).
- Create a starter checklist for authors (before publishing a lesson):
  - All blanks replaced
  - Key learning objective tested
  - Edge cases considered
  - Clear, machine-checkable hints available (if you plan hints)

Phase 1 — Standard CST design and example patterns (2–4 weeks, parallel with Phase 0)
- Establish a small set of canonical CST patterns to reuse across exercises. For example:
  - Pattern A: Placeholder check
    - test_that("No placeholders remain", { expect_false(grepl("____", learner_code, fixed = TRUE), info = "Replace all placeholders before submission.") })
  - Pattern B: Package loading check
    - test_that("Did you load the required package?", { expect_true("pkgname" %in% (.packages()), info = "Load the package with library(pkgname).") })
  - Pattern C: Basic functionality check
    - test_that("Your code yields the expected result (e.g., a vector length)", { expect_equal(length(result), expected_length, info = "Return a vector of the expected length.") })
  - Pattern D: Safe/isolated execution
    - test_that("Learner code does not produce unintended side effects in the environment", { expect_true(is.environment(learner_env)) })
- Provide a couple of realistic “wrong submission” presets for each exercise to demonstrate CSTs. For example:
  - wrong_without_library <- "library(dplyr)" (valid but sometimes learners forget the correct argument)
  - wrong_with_warning <- "library(dplyr, warn.conflicts = TRUE)" (not best practice)
  - wrong_wrong_package <- "library(ggplot2)" (loads a different package)
- Draft a minimal solution block for the exercise (type=solution) with the canonical correct submission.
- Draft a hidden block (type=hide) to simulate a few learner submissions and to set up the environment (as in your example), but keep it compact and representative.

Phase 2 — Build an authoring toolkit and scalable workflow (4–8 weeks, can run in parallel with Phase 1)
Goal: authors write one concise exercise spec, and the toolkit expands it into:
- The exercise code block (visible to learners)
- The solution block (type=solution)
- The hidden block with simulated learner submissions
- The test block(s) (type=test) with multiple small test_that blocks using expect_*

What to build
- A CST generator (R-based, optional integration into EWBTemplates) that takes an exercise spec and outputs the four blocks.
- A small domain-specific language (DSL) or templated spec per exercise, e.g. YAML or a light JSON-like snippet embedded in the Quarto file, that describes:
  - exercise_id
  - learning objective(s)
  - required code scaffolding
  - list of simulated wrong submissions
  - the canonical correct submission
  - a standard set of tests (with labels and messages)
- An insertable add-in (RStudio or web UI) to populate the four CST blocks from the spec, with a single-click "generate CST blocks" action.
- A “CST linter” that checks the lesson file for:
  - presence of all block types after an exercise
  - adherence to the canonical test patterns
  - consistent messaging style
- A lightweight, local testing runner that can run the hidden and test blocks to validate that the CST behaves as expected before publishing.

Phase 3 — Pilot with 2–3 lessons and iterate (6–10 weeks)
- Pick 2–3 representative lessons to convert to the new CST pattern.
- For each exercise, author:
  - An exercise spec (your DSL)
  - A set of simulated learner submissions for type=hide
  - A test block (type=test) built from the canonical patterns
- Run the local testing runner to validate:
  - All tests pass with the correct submission
  - All tests fail with the simulated incorrect submissions, providing actionable feedback
- Collect feedback from a small group of authors and early learners to refine:
  - The clarity of test messages
  - The balance between guidance and not giving away solutions
  - The time it takes to author CSTs
- Iterate the CST design, the generator, and the feedback language accordingly.

Phase 4 — Production rollout with scalable processes (ongoing)
- Roll out the CST pattern across all lessons in a staged manner (pilot → broader adoption).
- Institute a review process for CSTs (peer review of tests, messages, and edge cases).
- Integrate the CST linter into your content creation pipeline (CI or pre-publish hook).
- Build a library of reusable hints tied to CST failures (optionally powered by a simple rule-based system or a lightweight RAG-like system with a fixed dictionary of hints for common mistakes).
- Track metrics:
  - Time to author per exercise
  - Frequency and type of learner failures (from CST results)
  - Learner satisfaction with feedback quality
- Consider a future enhancement: an externalized or centralized test runner that runs across all lessons, so you don’t rely on authors to run tests locally.

What the immediate next 2–3 weeks could look like
- Week 1:
  - Finalize a CST design guide and one-page authoring checklist.
  - Draft the canonical CST templates for a small set of archetypes (at least 3 patterns).
  - Create a first-pass “CST generator” prototype (mock, minimal viable product) in R that can emit {r}, {r,type=solution}, {r,type=hide}, {r,type=test} blocks from a small spec.
- Week 2–3:
  - Pilot the generator on 2 lessons. Produce: 1–2 exercises per lesson using the new format.
  - Validate with a small author group and collect feedback.
  - Refine the generator and the CST messages, update the design guide.
- Week 4+:
  - Expand to 1–2 more lessons; begin documenting the process as SOPs.
  - Start a small central repository for CST templates and examples to ensure consistency.

Concrete example: updated CST blocks (illustrative)
Below is a minimal but realistic example showing how you could structure the four blocks with expect_* tests. This aligns with your four-block pattern and uses the modern testthat expectations.

- Exercise code block (visible to learner)
```{r}
# Load the dplyr package
____
```

- Solution code block (type=solution)
```{r, type=solution}
library(dplyr, warn.conflicts = FALSE)
```

- Hidden code block (type=hide) for local testing and simulating learner submissions
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
wrong_require <- 'require(dplyr)'

# Set the active submission
learner_code <- correct

# Gracefully evaluate code (prevents early error from stopping tests)
try(eval(parse(text = learner_code), envir = learner_env), silent = TRUE)
```

- Test code block (type=test) with expect_ tests
```{r, type=test}
# 1 - Check that `____` was replaced with something
test_that(desc = "All blanks `____` were replaced", {
  expect_false(grepl("____", learner_code, fixed = TRUE),
               info = "It looks like your submission still contains `____`. Please replace `____` to complete the code.")
})

# 2 - Check that dplyr was loaded
test_that(desc = "Did you load `dplyr`?", {
  loaded <- "dplyr" %in% (.packages())
  expect_true(loaded, info = "Did you correctly load the `dplyr` package using `library(dplyr)`?")
})
```

Notes and rationale for this pattern
- Using multiple small test_that blocks with expect_* gives precise, actionable feedback. If a learner’s submission fails a single aspect, the failure message pinpoints that aspect without leaking the solution.
- The placeholder check (no "____") is kept as a discrete, early check to encourage proper completion.
- The package-load check uses (.packages()) to confirm the package is loaded in the current session as a direct observable side-effect of library(dplyr). This is robust for the CST context and aligns with your current intent.
- This approach preserves the explicit four-block structure and supports local testing while enabling a scalable, unit-test-like framework across many exercises.

Addressing your concerns about “hidden blocks” and production workflow
- You can keep hidden blocks for local authoring/testing, but we recommend:
  - Centralizing the heavy, realistic learner-submission simulations into a small, version-controlled repository (or a CST-spec file per exercise) that your generator consumes to produce the type=hide blocks. This keeps lesson files readable and reduces duplication.
  - Providing a separate, lightweight “lesson test runner” that executes all type=test blocks in a controlled environment (isolated per-lesson runner, not the learner session).
  - Optionally, migrating to a “semi-externalized” model where the heavy tests live in a separate file that is sourced by the lesson during testing, so the main lesson file remains concise.
- This aligns with your goal of releasing lessons quickly while having a robust long-term testing backbone.

Edge-case considerations to plan for
- Learner submissions that try to exploit the environment (e.g., loading packages in a non-standard way). Decide on a restrained evaluation strategy (e.g., using a fresh environment, avoiding global assignment, etc.).
- Ensuring tests remain stable across R versions and across a range of browser-based R runtimes that the EWB platform may use.
- Ensuring that hints and feedback do not reveal exact solutions; keep guidance high-level and targeted.

What you should do next (concrete actions)
- Pick a small, representative set of 3–5 exercises and implement them using the new CST approach (with type=hide and type=test blocks).
- Build a minimal CST generator prototype (R script) that, given a small exercise spec, outputs the four blocks (exercise code, solution, hidden, test).
- Create a CST design guide and authoring checklist you can share with your content team.
- Run a 1–2 week pilot with a few authors to validate:
  - Ease of authoring new CSTs
  - Quality and usefulness of the learner feedback
  - Time saved in the long run
- Decide on the long-term plan for externalizing or decoupling hidden code blocks, and implement the chosen workflow across the library.

If you’d like, I can draft:
- A compact CST design guide (one-pager) you can publish for authors.
- A ready-to-run R script for a prototype CST generator from a simple YAML/JSON-like exercise spec.
- A few more example CST blocks (for different exercise types) to seed your library.

Would you like me to prepare:
- A starter CST design guide and a small prototype generator (R) you can run now?
- Or a detailed blueprint for the pilot with example specs for 2–3 exercises?