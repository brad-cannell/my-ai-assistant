---
title: Template Prompt for EWB COL Quiz Step 2 — Question Generation
id: template_prompt_col_quiz_step_2
task: quiz_questions
audience: course_author
interface: api
author: brad_cannell
created: 2026-03-21
last_updated: 2026-03-21
project: null
domain: lesson_development
tags:
  - quiz_questions
  - pipeline
  - question_generation
  - ewb_markdown
---

# Overview (optional)

- Step 2 of the 3-step COL quiz generation pipeline. 
- Generates one COL quiz question per competency from the approved competency list produced in Step 1. 
- Output is returned as a single, upload-ready EWB markdown file.

Placeholder variables:
- {{competency_list}} — the approved competency list from Step 1
- {{lesson_content}} — the full text of the EWB lesson
- {{lesson_specific_guidance}} — optional guidance; leave blank if not needed

# SYSTEM PROMPT

You are an AI assistant specialized in authoring high-quality quiz questions for Epi-Workbench, a web-based platform offering interactive courses in epidemiology, data science, and artificial intelligence for public health professionals and health researchers. Your goal is to produce clear, accurate, pedagogically sound, and platform-ready questions that reinforce explicit learning objectives, support skill-building, and fit within a browser-based, no-install environment.

# USER MESSAGE

<context>

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench." Epi-Workbench is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, Epi-Workbench combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

COL quizzes are a specific type of EWB quiz designed to give learners low-stakes, formative assessment opportunities throughout the course.

Purpose of COL quizzes:
- Reinforce key concepts from lessons.
- Encourage active recall and application without penalty.
- Provide immediate, supportive feedback to guide learning.
- Build learner confidence by allowing unlimited attempts.
</context>

<task>

## Task

Below I will pass you a list of competencies extracted from an EWB lesson, along with the original lesson content. Please write one COL quiz question for each competency.

Each question should:

- Directly assess the competency it is paired with.
- Be grounded in the concepts taught in the lesson, but assess generalizable knowledge or skills — not recall of a specific example, object name, dataset value, or one-off code output shown in the lesson.
- Be self-contained. Include all information needed to answer the question in the question text itself. Learners should not need to scroll up, re-read a prior example, or remember details of a specific code chunk in order to answer correctly.

For each question, choose the question type that best fits the competency being assessed. Prefer types that require active recall or application (e.g., fill_blank, numerical) over those that rely primarily on recognition (e.g., single), unless recognition is the skill being assessed.

Please provide draft feedback for each answer choice:
- For correct answer choices, start the feedback message with a short encouraging phrase.
- For incorrect answer choices, start the feedback message with a short encouraging phrase, then explain why the answer is incorrect.

Return all questions as a single, contiguous EWB markdown file, ready to upload to the Quiz Builder.

## Optional Lesson-Specific Guidance

{{lesson_specific_guidance}}
</task>

<constraints>

## Constraints

- Use 'us,' 'we,' 'our,' and 'ours' instead of 'you,' 'your,' and 'yours' to maintain a collaborative tone.
- Do not begin every question with "In this lesson…". Vary question stems naturally.
- Use "In this lesson…" only when it adds clarity by pointing to a specific example, dataset, or code chunk from the lesson.
- When referencing lesson code, keep past tense (e.g., "What did select() help us do?"). When asking general conceptual questions, present tense is fine.
- End answer choices with an appropriate punctuation mark.
- Do not use multiple choice questions to test learners' ability to correctly write R code. If we want to test their ability to correctly write R code, we should use a coding exercise.
- Randomize the position of the correct answer. The correct answer should not always be the first option.
- Surround code in the question text with backticks.
- Do not surround code in the answer or feedback text with backticks.
</constraints>

<formatting>

## Formatting

Return all questions in EWB markdown format. Questions must be importable directly into the EWB Quiz Builder.

**General rules:**
- Separate questions with `---`
- Start each question with `## Question N` (numbering is for readability only; order is determined by position in the file)
- Add `Type:` immediately after the header — this is the only required metadata field
- Optional metadata: `Points:` (default 100), `Correct Feedback:`, `Incorrect Feedback:`

**Allowed types:** `single`, `multiple`, `matching`, `numerical`, `fill_blank`

---

### single — one correct answer

```markdown
## Question 1
Type: single
Points: 100
Correct Feedback: Well done!
Incorrect Feedback: Review the lesson material.

What is a file path?

- [x] The set of directories and file name that tells R where to locate data on our computer.
  - Selected: Great choice! That's exactly what a file path is.
  - Not Selected: This was the correct answer — a file path describes the location of a file.
- [ ] A loud path to a data file that R ignores.
  - Selected: Nice try! That description isn't how file paths work; R uses paths to locate data.
- [ ] The file content itself.
  - Selected: Not quite! The content is inside the file, not the path to it.
- [ ] The path to the internet.
  - Selected: Nice try! A file path points to local files on our computer, not a web address.
```

Rules: exactly one `[x]`; minimum 2 choices; `Selected:` and `Not Selected:` feedback are optional.

---

### multiple — one or more correct answers

```markdown
## Question 2
Type: multiple

Which of the following are valid R assignment operators?

- [x] <-
  - Selected: Correct! The left arrow is R's idiomatic assignment operator.
- [x] =
  - Selected: Yes! The equals sign works for assignment in most contexts.
- [ ] ->
  - Selected: Not quite! While -> exists, it's a right-assignment and rarely used.
- [ ] ==
  - Selected: That's the equality comparison operator, not assignment.
```

Rules: at least one `[x]`; minimum 2 choices.

---

### matching — match left items to right items using `=>`

```markdown
## Question 3
Type: matching

Match each function below to its purpose.

- str(df) => Displays the internal structure of an object, including column types and a preview of values.
  - Matched: Great job! str() gives a compact summary of any R object's structure.
  - Mismatched: Not quite! str() shows structure — column names, types, and sample values.
- c(1, 2, 3) => Combines values into a vector — the fundamental data structure in R.
  - Matched: Excellent! c() stands for "combine" and creates atomic vectors.
  - Mismatched: Not quite! c() is R's combine function — it creates a vector.
- x <- 42 => The assignment operator — stores the value 42 in the object named x.
  - Matched: Correct! The left-arrow <- is R's idiomatic assignment operator.
  - Mismatched: Nice try! <- binds a value to a name in the current environment.
- is.na(x) => Returns a logical vector indicating which elements of x are missing values.
  - Matched: Well done! is.na() tests for NA values and returns TRUE or FALSE for each element.
  - Mismatched: Not quite! is.na() tests for missing data — it doesn't check data types or structure.
```

Rules: minimum 1 pair; `Matched:` and `Mismatched:` feedback are optional.

---

### numerical — learner enters a number

```markdown
## Question 4
Type: numerical

Consider the following R code:
`x <- c(4, 8, 15, 16, 23, 42)`
`length(x)`
What value does `length(x)` return?

Answer: 6
Tolerance: 0
Feedback Correct: Right! The vector x contains six elements, so length() returns 6.
Feedback Too High: That's too high. Count the individual values passed to c().
Feedback Too Low: That's too low. Count each value separated by a comma — how many are there?
```

Fields: `Answer:` (required); `Tolerance:` (default 0); `Feedback Correct:`, `Feedback Too High:`, `Feedback Too Low:` (all optional).

---

### fill_blank — learner fills in one or more blanks

```markdown
## Question 5
Type: fill_blank

Complete the following R code to read a CSV file named "study_data.csv" into a data frame called df and then display the first six rows:

df <- [blank]("study_data.csv")

[blank](df)

- Blank 1: read.csv
  - Case Sensitive: false
  - Correct: Excellent! read.csv() is R's built-in function for importing comma-separated value files.
  - Incorrect: Not quite! The function begins with the word "read" and the file extension and function name share the same three letters.
  - Close Match: Almost! Check the exact function name.
  - Alternatives: read_csv, read.CSV
- Blank 2: head
  - Case Sensitive: false
  - Correct: Correct! head() returns the first six rows of a data frame by default.
  - Incorrect: Not quite! The function you need is the conceptual opposite of tail().
```

Fields per blank: `Blank N:` (required); `Case Sensitive:` (default false); `Correct:`, `Incorrect:`, `Close Match:`, `Alternatives:` (all optional). The number of `[blank]` markers in the question text must match the number of `Blank N:` definitions.
</formatting>

## Input

<competency_list>

### Competency List

{{competency_list}}
</competency_list>

<lesson_content>

### Lesson Content

{{lesson_content}}
</lesson_content>
