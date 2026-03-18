# Writing Quiz Questions in Markdown

This guide provides instructions on how to write quiz questions in a structured markdown format that can be imported directly into EWB via the Quiz Builder's **Import from File** feature.

------------------------------------------------------------------------

## Overview

Instead of creating quiz questions one by one in the UI, you can write all your questions in a single `.md` file and upload it. This is especially useful when using ChatGPT or another AI assistant to generate questions from lesson content — just include this syntax guide in your prompt.

------------------------------------------------------------------------

## General Structure

- Each question starts with `## Question N` (the number is for readability only; order is determined by position in the file)
- Questions are separated by `---` (a horizontal rule)
- Metadata lines come right after the header
- Question text follows the metadata
- Answer options come last

### Metadata Fields

These lines go directly after the `## Question N` header:

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `Type:` | Yes | — | `single`, `multiple`, `matching`, `numerical`, or `fill_blank` |
| `Points:` | No | 100 | Point value for the question |
| `Correct Feedback:` | No | (empty) | General feedback shown when the learner answers correctly |
| `Incorrect Feedback:` | No | (empty) | General feedback shown when the learner answers incorrectly |

------------------------------------------------------------------------

## Question Types

### 1. Single Choice

One correct answer. Uses `[x]` for the correct choice and `[ ]` for incorrect choices.

#### Syntax:

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

#### Rules:
- Exactly **one** choice must be marked with `[x]`
- Minimum **2** choices required
- `Selected:` — feedback shown when the learner picks this choice (optional)
- `Not Selected:` — feedback shown when the learner does NOT pick this choice (optional)

------------------------------------------------------------------------

### 2. Multiple Choice

One or more correct answers. Same checkbox syntax as single choice.

#### Syntax:

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

#### Rules:
- At least **one** choice must be marked with `[x]`
- Minimum **2** choices required
- Multiple `[x]` choices are allowed (and expected)

------------------------------------------------------------------------

### 3. Matching

Match left items to right items using `=>`.

#### Syntax:

```markdown
## Question 3
Type: matching

Match each function below to its purpose.

- str(df) => Displays the internal structure of an object, including column types and a preview of values.
  - Matched: Great job! str() gives a compact, human-readable summary of any R object's structure.
  - Mismatched: Not quite! str() shows structure — column names, types, and sample values. Think about which description mentions types and a preview.
- c(1, 2, 3) => Combines values into a vector — the fundamental data structure in R.
  - Matched: Excellent! c() stands for "combine" and creates atomic vectors, the building blocks of R data structures.
  - Mismatched: Not quite! c() is R's combine function — it creates a vector, not a data frame or list directly.
- x <- 42 => The assignment operator — stores the value 42 in the object named x.
  - Matched: Correct! The left-arrow <- is R's idiomatic assignment operator, preferred over = in most style guides.
  - Mismatched: Nice try! The <- arrow is used for assignment — it binds a value to a name in the current environment.
- is.na(x) => Returns a logical vector indicating which elements of x are missing values.
  - Matched: Well done! is.na() tests for NA (missing) values and returns TRUE or FALSE for each element.
  - Mismatched: Not quite! is.na() specifically tests for NA (missing data) — it doesn't check data types or object structure.
```

#### Rules:
- Minimum **1** pair required
- Both left item and right item must be present
- `Matched:` — feedback when the learner matches correctly (optional)
- `Mismatched:` — feedback when the learner matches incorrectly (optional)

------------------------------------------------------------------------

### 4. Numerical Answer

The learner enters a number. You specify the correct answer and an optional tolerance.

#### Syntax:

```markdown
## Question 4
Type: numerical

Consider the following R code:
`x <- c(4, 8, 15, 16, 23, 42)`
`length(x)`
What value does `length(x)` return?

Answer: 6
Tolerance: 0
Feedback Correct: Right! The vector x contains six elements — 4, 8, 15, 16, 23, and 42 — so length() returns 6.
Feedback Too High: That's too high. Count the individual values passed to c().
Feedback Too Low: That's too low. Count each value separated by a comma — how many are there?
```

#### Fields:

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `Answer:` | Yes | — | The correct numerical answer |
| `Tolerance:` | No | 0 | How far from the answer the learner can be and still be correct |
| `Feedback Correct:` | No | (empty) | Feedback when the answer is within tolerance |
| `Feedback Too High:` | No | (empty) | Feedback when the answer is above the correct value + tolerance |
| `Feedback Too Low:` | No | (empty) | Feedback when the answer is below the correct value - tolerance |

------------------------------------------------------------------------

### 5. Fill in the Blank

The learner fills in one or more blanks. Use `[blank]` as a placeholder in the question text.

#### Syntax:

```markdown
## Question 5
Type: fill_blank

Complete the following R code to read a CSV file named "study_data.csv" into a data frame called df and then display the first six rows:

df <- [blank]("study_data.csv")

[blank](df)

- Blank 1: read.csv
  - Case Sensitive: false
  - Correct: Excellent! read.csv() is R's built-in function for importing comma-separated value files into a data frame.
  - Incorrect: Not quite! Think about what task is being performed — a CSV file is being loaded into R. The function begins with the word "read."
  - Close Match: Almost! Check the exact function name — the file extension and the function name share the same three letters.
  - Alternatives: read_csv, read.CSV
- Blank 2: head
  - Case Sensitive: false
  - Correct: Correct! head() returns the first six rows of a data frame by default.
  - Incorrect: Not quite! The function you need is a common, single-word base R function that is the conceptual opposite of tail().
```

#### Fields per blank:

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `Blank N:` | Yes | — | The correct answer for blank N |
| `Case Sensitive:` | No | false | Whether the answer check is case-sensitive (`true` or `false`) |
| `Correct:` | No | (empty) | Feedback when the answer is correct |
| `Incorrect:` | No | (empty) | Feedback when the answer is incorrect |
| `Close Match:` | No | (empty) | Feedback when the answer is close but not exact |
| `Alternatives:` | No | (empty) | Comma-separated list of alternative correct answers |

#### Rules:
- The number of `[blank]` markers in the question text must match the number of `Blank N:` definitions
- Minimum **1** blank required

------------------------------------------------------------------------

## Complete Example

Here is a full file with all five question types that can be uploaded directly:

```markdown
## Question 1
Type: single
Points: 50
Correct Feedback: Great work!
Incorrect Feedback: Review this concept in the lesson.

What is a vector in R?

- [x] An ordered collection of elements of the same type.
  - Selected: Correct! Vectors are the most basic data structure in R.
- [ ] A matrix with one column.
  - Selected: Not quite — while a matrix column is similar, a vector is its own type.
- [ ] A data frame with one variable.
  - Selected: Close, but a data frame is a more complex structure built from vectors.

---

## Question 2
Type: multiple

Which of the following are base R functions?

- [x] mean()
  - Selected: Yes! mean() is a base R function.
- [x] sum()
  - Selected: Correct! sum() is part of base R.
- [ ] mutate()
  - Selected: That's a dplyr function, not base R.
- [ ] ggplot()
  - Selected: That's from the ggplot2 package.

---

## Question 3
Type: matching

Match the function to its package.

- mean() => base R
  - Matched: Correct!
  - Mismatched: mean() is a base R function — no package needed.
- mutate() => dplyr
  - Matched: Right!
  - Mismatched: mutate() is from the dplyr package in the tidyverse.

---

## Question 4
Type: numerical

How many elements are in c(1, 2, 3)?

Answer: 3
Tolerance: 0
Feedback Correct: Right! Three values were passed to c().
Feedback Too High: Too high — count only the values inside c().
Feedback Too Low: Too low — count each comma-separated value.

---

## Question 5
Type: fill_blank

Use [blank] to create a vector containing 1, 2, and 3.

- Blank 1: c
  - Correct: Yes! c() is the combine function in R.
  - Incorrect: The function name is a single letter that stands for "combine."
```

------------------------------------------------------------------------

## How to Import

1. Open the **Lesson Editor** for the lesson you want to add quiz questions to
2. Go to the **Quiz** tab
3. Create a quiz if one doesn't exist yet
4. Click the **Import from File** button (next to "Add New Question")
5. Select your `.md` file
6. Preview the content and click **Import Questions**
7. All questions will be added to the quiz

------------------------------------------------------------------------

## Tips for Using with ChatGPT

When asking ChatGPT to generate quiz questions from your lesson content, include these formatting instructions in your prompt:

```
Please return quiz questions in EWB markdown format:
- Separate questions with ---
- Start each with ## Question N
- Add Type: (single, multiple, matching, numerical, or fill_blank)
- Optional: Points: (default 100), Correct Feedback:, Incorrect Feedback:
- For single/multiple: use - [x] for correct, - [ ] for incorrect choices
  - Indent feedback as: Selected: and Not Selected:
- For matching: use - left => right with Matched: and Mismatched: feedback
- For numerical: use Answer:, Tolerance:, Feedback Correct:, Feedback Too High:, Feedback Too Low:
- For fill_blank: use [blank] in question text, then list each blank as:
  - Blank N: answer
  - Case Sensitive: true/false
  - Correct: feedback
  - Incorrect: feedback
  - Close Match: feedback
  - Alternatives: comma-separated alternatives
```

------------------------------------------------------------------------

## Summary of Conventions

1. Start each question with `## Question N`
2. Always include `Type:` — it is the only required metadata field
3. Use `[x]` and `[ ]` for choice-based questions (single and multiple)
4. Use `=>` to separate left and right items in matching questions
5. Use `Answer:` and `Tolerance:` for numerical questions
6. Use `[blank]` placeholders in the question text for fill-in-the-blank questions
7. Separate questions with `---`
8. Indent feedback lines with two spaces under their parent item

By following these conventions, your quiz markdown files will import cleanly into EWB.
