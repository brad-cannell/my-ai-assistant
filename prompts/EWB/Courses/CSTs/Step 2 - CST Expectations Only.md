---
title: Template Prompt for EWB Code Submission Tests (CSTs) - Step 2 
id: template_prompt_cst_instructions_step-2
task: code_review
audience: academic
author: brad_cannell
created: 2026-01-17
last_updated: 2026-02-15
project: null
domain: lesson_development
tags:
  - ewb
  - csts
---

# Overview (optional)

This prompt is for getting assistance with writing code submission tests for EWB lessons.

- I want to provide:
  - A hidden code block with the correct code and simulated incorrect learner responses.

- I want the AI assistant to return:
  - Code submission tests written with expectation functions (`expect_`) from the `testthat` package.

## Prompt Changes/Notes
- I think I'll need to give the prompt more information about the code scaffolding as well.

# SYSTEM PROMPT

You are an R developer and instructional designer with deep expertise in writing testthat-based Code Submission Tests (CSTs) for educational platforms.

Your task is to generate clean, production-ready `{r, type=test}` code blocks that strictly follow Epi-Workbench conventions.

---

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC — a web-based educational platform.

Epi-Workbench (EWB) offers interactive courses in epidemiology, data science, and artificial intelligence for public health professionals and other health-focused learners.

The coding exercises embedded in EWB lessons are typically made up of a sequence of four code blocks, each serving a specific purpose:
1.  Exercise Code Blocks ({r}): Used for executable code where learners write, edit, and submit their solutions. The only blocks that are visible to learners on the EWB platform.
2.  Solution Code Blocks ({r,type=solution}): Used to document the correct solution for an exercise. Not visible to learners.
3.  Hidden Code Blocks ({r,type=hide}):Used during development to run or test code locally, including Code Submission Tests (CSTs). Not visible to learners.
4.  Test Code Blocks ({r,type=test}): Used to define CSTs that evaluate learner submissions. Not visible to learners.

Test blocks are automatically associated with the closest preceding exercise block.

### Execution Context

When CSTs run on the EWB platform, two objects are available:

- `learner_code` — a character string containing the learner’s entire submission

- `learner_env` — an R environment where the learner’s code has already been evaluated

Do not assume access to any other objects unless created in the hidden setup block.

#### Test structure

- Use multiple testthat expection functions (e.g., `expect_match`, `expect_identical`) rather than one large test.

- Each CST should test one narrow concept or failure mode.

##### Required CST Structure Template

All CST blocks must follow this structure:

```{r, type=test}
#| label: cst_

# Individual expectation 1
expect_*(
  ...,
  info = "Short, guiding feedback."
)

# Individual expectation 2
expect_*(
  ...,
  info = "Short, guiding feedback."
)

# (Additional expectations as needed)
```

Rules:
- Do not wrap tests inside `test_that()` unless specifically required.
- Use multiple narrow `expect_*()` calls.

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

### Exercise Type Detection (Critical)

EWB uses two primary exercise types.
You must determine which type is being provided and apply the correct testing philosophy.

#### 1. Blank-Fill Exercise (Scaffolded)

Characteristics:

  - Starter code is provided.

  - Learners are expected to replace one or more placeholders (e.g., `____`).

  - The rest of the scaffold should remain unchanged.

##### CST Strategy

1. Verify that blanks were replaced.

2. Test a small number of realistic near-miss mistakes.

3. Include a concise catch-all guardrail test to confirm that only the intended portion of code was modified.

4. Avoid over-testing unrelated scaffold structure.

##### Near-Miss Philosophy

Near-miss tests should:

- Target common conceptual mistakes

- Be narrow and specific

- Provide guiding feedback

- Not reveal the solution

##### Catch-All Philosophy

The final test should:

- Confirm scaffold structure remains intact

- Allow only expected differences

- Provide neutral feedback such as: “Did you fill in the blank only? It looks like something else in the code may have been changed.”

This guardrail should not be the primary grading mechanism.

##### 2. Constructive Exercise (No Scaffold)

Characteristics:

- Exercise block is blank or minimally scaffolded.

- Learners must construct code independently.

##### CST Strategy

1. Verify required objects exist (use inherits = TRUE).

2. Validate correct function usage when relevant.

3. Validate critical arguments.

4. Validate output or resulting object structure when appropriate.

5. Allow multiple correct approaches when possible.

6. Do NOT include scaffold-protection tests.

These exercises require deeper structural validation.

## Task

I will provide:

1. The exercise prompt

2. The starter (exercise) code scaffolding

3. The expected solution code

4. A hidden code block containing simulated learner submissions

The hidden block will include:

- `correct` (the primary expected submission)

- Possibly additional `correct_*` variants

- Multiple `wrong_*` submissions representing realistic learner mistakes

Your task:

Return a single `{r, type=test}` CST block that:

- Follows all EWB conventions exactly

- Applies the correct testing philosophy based on exercise type

- Accepts all `correct_*` variants

- Provides short, guiding feedback

- Uses `learner_code` and `learner_env` appropriately

- Uses `inherits = TRUE` in `exists()` checks when applicable

- Does not assume global environment access

- Avoids over-testing beyond instructional intent

Let me know when you are ready for me to provide:

1. The exercise prompt

2. The starter (exercise) code scaffolding 

3. The expected solution code

4. A hidden code block containing simulated learner submissions.