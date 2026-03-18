## User

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

## Assistant

Short answer: Yes. Start using testthat expectation functions (expect_*) in your CSTs.

Why switch to expect_* instead of custom fail/succeed messages
- Clarity and diagnostics: Expectations produce standardized, actionable failure messages (e.g., what was expected vs what was actually observed) that are easier for learners to interpret.
- Alignment with standard practice: testthat is the de facto unit testing framework for R. Using its expectations makes your CSTs easier to maintain, share, and extend.
- Granular feedback: You can have multiple, focused expectations within a single test block, so learners get precise feedback on each aspect of their submission.
- Better reporting and tooling: Expect_* functions integrate cleanly with testthat when you scale up to more exercises and analytics, and they work well with code coverage and continuous integration if you ever add it.

What to change (practical guidelines)
- Replace custom checks with expect_* calls. Each assertion should use an appropriate expect_ function (e.g., expect_false, expect_true, expect_equal, expect_match, etc.).
- Keep tests small and focused. Prefer several small tests (one per objective) over one large test with many conditions.
- Use the info/message argument to guide learners when an expectation fails. This helps keep feedback constructive and actionable.
- Don’t rely on global side effects. Use a consistent environment (e.g., learner_env) and guard against unintended leakage of state between submissions.
- When checking for a specific action (like loading a package), check robustly both for the namespace and for the attached package (e.g., isNamespaceLoaded("dplyr") and "package:dplyr" in search()).
- If you want to assert that the learner’s code executed without error, wrap in try and use expect_false(inherits(res, "try-error"), ...).

Concrete rewrite for your example CST
Below is a drop-in replacement for your two test blocks, using only testthat expectations. It preserves your existing logic (checking for the placeholder and ensuring the package is loaded) but provides clearer, standard feedback.

```{r, type=test}
# 1) Ensure all placeholders are replaced
test_that("All blanks `____` were replaced", {
  expect_false(grepl("____", learner_code, fixed = TRUE),
               info = "Please replace all placeholder blanks ('____') with actual code.")
})

# 2) Validate dplyr is loaded
test_that("dplyr is loaded via library(dplyr)", {
  attached <- "package:dplyr" %in% search()
  ns_loaded <- isNamespaceLoaded("dplyr")
  expect_true(attached || ns_loaded,
              info = "Did you load the dplyr package using library(dplyr) or require(dplyr)?")
})
```

(Optionally, if you want to explicitly ensure the learner’s code ran without errors, you can add another test block.)

```{r, type=test}
# 3) Ensure the learner code executes without error (in the isolated env)
test_that("Learner's submission executes without error", {
  res <- try(eval(parse(text = learner_code), envir = learner_env), silent = TRUE)
  expect_false(inherits(res, "try-error"), info = "Your submission produced an error when running.")
})
```

Notes on test design
- Use descriptive test names that reflect the learning objective.
- For loading checks, consider both attached packages and namespaces to accommodate variations in how learners write their submission (e.g., library(dplyr) vs. library("dplyr")).
- If you want to test functionality beyond loading (e.g., that a following exercise uses dplyr functions correctly), add a separate test that exercises a small code path with known input and expected output; e.g., create a tiny data frame and verify a dplyr operation yields the expected result, using expect_equal.
- Be mindful of false negatives. If you require exact string matching in learner_code (like “____”), ensure you’re not being overly strict about spacing or quotes unless that’s part of the exercise design.

Migration plan (quick start)
- Phase 1: Convert one or two CSTs to expect_* style as a pilot. Keep the same exercise logic.
- Phase 2: Expand to 3–4 small expect_* tests per exercise, with clear info messages.
- Phase 3: Review and standardize messages across CSTs so learners get uniform feedback.
- Phase 4: Optional enhancement: add tests that verify downstream behavior if the exercise requires a specific result (e.g., a dplyr operation producing a known outcome).

Bottom line
Adopting testthat expectation functions will make your CSTs more maintainable, informative, and aligned with standard R testing practices. Start with the two basic checks (no placeholders left and the package is loaded) and progressively add more targeted expectations as your exercises evolve. If you’d like, I can draft a complete migration plan or rewrite multiple CSTs in batch to adopt this pattern.

## User

Thank you for the guidance. As part of my migration plan, I would like ChatGPT to pass existing CSTs to ChatGPT. Then, I would like ChatGPT to help me convert them to expect_* style. Will you please generate a reuseable prompt for that purpose?

## Assistant

Here is a self-contained, reusable prompt you can copy-paste into ChatGPT (or into your CST automation workflow) to convert an existing CST from a traditional test block to testthat expect_* style tests.

You can use one prompt version with a simple toggle inside (concise vs. verbose). The prompt is designed to:
- Accept the four CST blocks (exercise, solution, hidden, and test).
- Extract and rewrite the type=test block to use testthat expect_* functions.
- Preserve the original learning objectives and logic (e.g., placeholder checks, package loading, environment isolation).
- Provide both a concise version and a verbose, more diagnostic version. You can choose one by adjusting the “OUTPUT_STYLE” flag.

Reusable CST-to-expect-prompt (copy-paste)

System prompt (high level)
You are an R CST modernization assistant. Your job is to take an existing CST that uses custom fail/succeed messages in a test code block and convert it into a clean, idiomatic testthat v3 set of expectations (expect_*) that preserve the same learning objectives and behavior. Output only the rewritten test code block(s) (type=test) in proper Quarto/R code block syntax. Include concise, well-scoped tests with informative messages. Do not add extraneous commentary.

Input specification (what you will be given)
- Four code blocks from a CST:
  - Exercise code block: the learner’s code (not always needed for the conversion, but context helps).
  - Solution code block: the canonical solution (for reference).
  - Hidden code block: environment setup and the learner_code variable, and any helper logic (e.g., learner_env, correct answers, etc.).
  - Test code block: the CST you want to rewrite (this is what you must convert to expect_*).

- You will receive these blocks as text. You should extract the test code block and replace it with the new test_that blocks using expect_*.

Output specification (what you should return)
- Return a single code block with type=test that contains the rewritten tests using testthat expect_* functions.
- Preserve the same test structure and sequencing as the original (e.g., a first test checking for placeholders, a second test checking package loading, etc.), but implement each assertion with an appropriate expect_* call.
- If the original CST contains multiple objectives, split them into multiple small, focused tests (one expect_ per objective where reasonable).
- Do not include any extraneous explanation or commentary—just the rewritten test code block. If you want to provide optional notes, you can include a short inline info message within expect_* calls.

Style and design choices (guidance)
- Use testthat v3 conventions:
  - test_that("description", { expect_*(...) ; ... })
  - Use informative info messages via the info argument to guide learners when tests fail.
- Keep tests isolated and deterministic:
  - Use a consistent environment (learner_env) and avoid leaking state.
  - If you need to ensure the learner’s code runs, wrap in try() and use expect_false(inherits(res, "try-error"), ...).
- Common objective patterns you may encounter (examples you should implement as appropriate):
  - Placeholder replacement: ensure there are no "____" placeholders left (use expect_false with a suitable message).
  - Package loading: verify that the learner loaded a package via library() or require(), checking both the session namespace and the attached package as robust checks.
  - Execution without error: verify learner_code executes in learner_env without error.
  - Optional: verify a minimal functional outcome if the exercise requires a specific result (e.g., a small data manipulation yields expected values) using expect_equal or related expectations.

Concise toggle (how to request)
- OUTPUT_STYLE: concise | verbose
  - concise: produce a compact set of focused expectations (3–5 tests, no extra bells and whistles).
  - verbose: produce more robust tests (more edge-case checks, multiple paths, and clear diagnostics).

Example: (for reference only)
Original test block (type=test)
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

Converted test block (type=test) – concise version
```{r, type=test}
# 1) Ensure all placeholders are replaced
test_that("All blanks `____` were replaced", {
  expect_false(grepl("____", learner_code, fixed = TRUE),
               info = "Please replace all placeholder blanks ('____') with actual code.")
})

# 2) Validate dplyr is loaded
test_that("dplyr is loaded via library(dplyr)", {
  attached <- "package:dplyr" %in% search()
  ns_loaded <- isNamespaceLoaded("dplyr")
  expect_true(attached || ns_loaded,
              info = "Did you load the dplyr package using library(dplyr) or require(dplyr)?")
})
```

Converted test block (type=test) – verbose version
```{r, type=test}
# 1) Ensure all placeholders are replaced
test_that("All blanks `____` were replaced", {
  expect_false(grepl("____", learner_code, fixed = TRUE),
               info = "Replace all placeholder blanks of the exercise with valid code.")
})

# 2) Validate dplyr is loaded (robust check)
test_that("dplyr is available (attached or namespace loaded)", {
  attached <- "package:dplyr" %in% search()
  ns_loaded <- isNamespaceLoaded("dplyr")
  expect_true(attached || ns_loaded,
              info = "Load dplyr with library(dplyr) or ensure its namespace is loaded.")
})

# 3) Optional: ensure the learner's submission executes without error
test_that("Learner's submission runs without error", {
  res <- try(eval(parse(text = learner_code), envir = learner_env), silent = TRUE)
  expect_false(inherits(res, "try-error"), info = "Your submission produced an error when running.")
})
```

How to use
- Prepare the input CST blocks as your usual. The prompt will extract the existing test block and replace it with the two to three expect_* tests as shown.
- If you want a different focus (e.g., strict string checks, or additional package checks), specify that in the prompt via the OUTPUT_STYLE and by listing additional objectives in a brief “learning objectives” line so the converter can map them to appropriate expect_* calls.

Optional: JSON-friendly variant (if you’re automating this)
If you’re feeding CSTs via JSON, you can wrap the four blocks as:
{
  "exercise": "...",
  "solution": "...",
  "hidden": "...",
  "test_original": "..."
}
And require the assistant to return:
{
  "test_converted": "```{r, type=test} ... ```",
  "notes": "informational rationale or optional guidance"
}

If you’d like, I can tailor this prompt to your exact CST formatting (Quarto code fences, specific package checks, or other common objectives) and provide two ready-to-run prompt strings (concise and verbose) you can swap in your workflow.

Would you like me to produce a ready-to-copy pair of prompts (concise version and verbose version) that you can drop into your CST pipeline as-is?

## User

It would be even better if I could just pass the entire contents of the lesson to ChatGPT in markdown format. Then, ChatGPT could locate the test blocks in it's own, and return updated CSTs for all test blocks in the lesson.

## Assistant

Great idea. Here’s a reusable, copy-pasteable master prompt you can feed ChatGPT with an entire lesson in Markdown. It will locate all test blocks (type=test) and return a fully updated lesson where those test blocks are rewritten to testthat expect_* style tests. I’ve provided two variants: concise (lighter feedback) and verbose (more diagnostics and edge-case checks). You can pick one by setting OUTPUT_STYLE to concise or verbose.

How to use (quick guidance)
- Pass the full lesson Markdown as the "user content" to ChatGPT, and include a line specifying OUTPUT_STYLE: concise or verbose.
- If the lesson is very long, consider chunking it into sections (by headings) and processing sequential chunks, then reassembling in order.
- The prompt instructs ChatGPT to:

  - Find every code block with {r, type=test} (or the equivalent in your Quarto Markdown).
  - Convert each test block into one or more test_that("description", { expect_*(...) ... }) tests that preserve intent.
  - Leave all non-test blocks intact and preserve the original order.
  - Return only the updated Markdown document (no extra commentary).

Concise master prompt (copy-paste)
System prompt (concise)
You are an R CST modernization assistant. Your job is to take an input Markdown document (a lesson) that contains multiple CST blocks, locate every test block (code blocks with r, type=test), and convert each test block to idiomatic testthat v3 tests using expect_* functions. Preserve the same learning objectives and the surrounding code blocks; only replace the content of test blocks with test_that blocks that use expect_* style assertions. Output a single Markdown document with the updated test blocks in place, keeping all other blocks (exercise, solution, hidden) unchanged. Do not add extraneous commentary. If there are multiple test blocks, update them in the same order they appear. If a test block cannot be safely transformed, preserve it and add a clarifying note inside the test (using info within expect_* messages) but do not remove the test.

Input specification (concise)
- You will receive:
  - The complete lesson Markdown (as a single string).
  - A line (or a metadata header) specifying OUTPUT_STYLE = concise.
- You will return: The same Markdown document with every test block replaced by idiomatic testthat expect_* tests. Non-test blocks must be preserved exactly.

Output specification (concise)
- Return exactly one Markdown document (code fences and blocks preserved) with all test blocks rewritten to testthat expectations. No extra prose.

Transformation guidelines (concise)
- For a placeholder check like “All blanks `____` were replaced”:
  - Replace with test_that("All blanks `____` were replaced", { expect_false(grepl("____", learner_code, fixed = TRUE), info = "Please replace all placeholder blanks ('____') with actual code.") })
- For package loading checks:
  - Replace with a robust load check, e.g.:
    - test_that("dplyr is loaded via library(dplyr)", {
        attached <- "package:dplyr" %in% search()
        ns_loaded <- isNamespaceLoaded("dplyr")
        expect_true(attached || ns_loaded, info = "Did you load the dplyr package using library(dplyr) or require(dplyr)?")
      })
- If the original test used succeed()/fail(), convert to equivalent expect_* semantics with informative messages.
- If you need to verify execution without error, wrap in try() and use expect_false(inherits(res, "try-error"), info = "...").

Verbose master prompt (copy-paste)
System prompt (verbose)
You are an R CST modernization assistant. Your job is to take an input Markdown document (a lesson) that contains multiple CST blocks, locate every test block (code blocks with r, type=test), and convert each test block to idiomatic testthat v3 tests using expect_* functions. Preserve the same learning objectives and the surrounding code blocks; only replace the content of test blocks with test_that blocks that use expect_* style assertions. Output a single Markdown document with the updated test blocks in place, keeping all other blocks (exercise, solution, hidden) unchanged. Do not add extraneous commentary. If there are multiple test blocks, update them in the same order they appear. If a test block cannot be safely transformed, preserve it and add an informative message inside the test using expect_* so that learners understand the issue. When applying transformations, aim for clear, focused tests (one expectation per objective where feasible), and use the info argument to provide actionable feedback. If a test block involves running learner_code, ensure you wrap the execution in a safe try() and verify with expect_false(inherits(..., "try-error"), info = "...").

Input specification (verbose)
- You will receive:
  - The complete lesson Markdown (as a single string).
  - A directive OUTPUT_STYLE = verbose.
  - Optional: a brief list of objectives for each test block to guide expected behavior (if provided, map each objective to a corresponding expect_* test).
- You will return: The same Markdown document with every test block replaced by idiomatic testthat expect_* tests. Non-test blocks must be preserved exactly.

Output specification (verbose)
- Return exactly one Markdown document with updated test blocks. Include concise but informative test_that descriptions. If you added extra tests (e.g., for execution without error), keep them small and clearly scoped. Do not add extraneous commentary outside of test_that blocks.

Transformation examples (verbose guidance)
- Placeholder check:
  - From: a test that uses if/else and fail/succeed about "____"
  - To: a test_that with expect_false(grepl("____", ...), info = "...")
- Package load check:
  - From: manual if/else around library(...)
  - To: a test_that that checks attached namespaces or loaded namespaces with isNamespaceLoaded and search()
- Run-without-error:
  - From: a test that directly eval(parse(text = learner_code), envir = learner_env)
  - To: a test_that that runs the code inside try(...) and uses expect_false(inherits(..., "try-error"), ...)
- Functional outcome (optional):
  - If a test has a concrete expected outcome, use expect_equal or similar to compare actual vs expected.

JSON-friendly variant (optional)
If you want to automate via JSON, you can wrap the inputs as:
{
  "lesson_markdown": "<full lesson markdown here>",
  "OUTPUT_STYLE": "concise" | "verbose"
}
And require the assistant to return:
{
  "updated_lesson_markdown": "<markdown with test blocks rewritten>",
  "notes": "<optional diagnostics>"
}

Sample minimal ready-to-run prompt pair (concise version)
[Copy-paste the concise master prompt above, starting from "System prompt (concise)".]

Sample minimal ready-to-run prompt pair (verbose version)
[Copy-paste the verbose master prompt above, starting from "System prompt (verbose)".]

Would you like me to generate two ready-to-run prompt strings (concise and verbose) that you can drop into your CST pipeline as-is? If yes, tell me which style you prefer by setting OUTPUT_STYLE to concise or verbose, and I’ll provide the exact text blocks ready for copy-paste.
<br><br>
<details><summary>System prompt</summary>


You are an R developer and instructional designer with deep expertise in writing testthat-based Code Submission Tests (CSTs) for educational platforms.

</details>