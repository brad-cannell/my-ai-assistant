<formatting>
Return all questions in EWB markdown format. Questions must be importable directly into the EWB Quiz Builder.

**General rules:**
- Separate questions with `---`
- Start each question with `## Question N` (numbering is for readability only; order is determined by position in the file)
- Add `Type:` immediately after the header — this is the only required metadata field
- Optional metadata: `Points:` (default 100), `Correct Feedback:`, `Incorrect Feedback:`

**Allowed types:** `single`, `multiple`, `matching`, `numerical`, `fill_blank`
<formatting>

---

<question_type_single_answer>
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
</question_type_single_answer>

---

<question_type_multiple_answer>
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
</question_type_multiple_answer>

---

<question_type_matching>
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
</question_type_matching>

---

<question_type_numerical>
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
</question_type_numerical>

---

<question_type_fill_blank>
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
<question_type_fill_blank>