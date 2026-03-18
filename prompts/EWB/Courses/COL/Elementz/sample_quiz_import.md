## Question 1
Type: single
Points: 100
Correct Feedback: Great job!
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

---

## Question 2
Type: multiple
Points: 100

Which of the following are valid R assignment operators?

- [x] <-
  - Selected: Correct! The left arrow is R's idiomatic assignment operator.
- [x] =
  - Selected: Yes! The equals sign works for assignment in most contexts.
- [ ] ->
  - Selected: Not quite! While -> exists, it's a right-assignment and rarely used.
- [ ] ==
  - Selected: That's the equality comparison operator, not assignment.

---

## Question 3
Type: matching

Match each function below to its purpose.

- str(df) => Displays the internal structure of an object, including column types and a preview of values.
  - Matched: Great job! str() gives a compact, human-readable summary of any R object's structure.
  - Mismatched: Not quite! str() shows structure — column names, types, and sample values.
- c(1, 2, 3) => Combines values into a vector — the fundamental data structure in R.
  - Matched: Excellent! c() stands for "combine" and creates atomic vectors.
  - Mismatched: Not quite! c() is R's combine function — it creates a vector.
- x <- 42 => The assignment operator — stores the value 42 in the object named x.
  - Matched: Correct! The left-arrow <- is R's idiomatic assignment operator.
  - Mismatched: Nice try! The <- arrow is used for assignment.
- is.na(x) => Returns a logical vector indicating which elements of x are missing values.
  - Matched: Well done! is.na() tests for NA (missing) values and returns TRUE or FALSE for each element.
  - Mismatched: Not quite! is.na() specifically tests for NA (missing data).

---

## Question 4
Type: numerical
Points: 100

Consider the following R code:
`x <- c(4, 8, 15, 16, 23, 42)`
`length(x)`
What value does `length(x)` return?

Answer: 6
Tolerance: 0
Feedback Correct: Right! The vector x contains six elements — 4, 8, 15, 16, 23, and 42 — so length() returns 6.
Feedback Too High: That's too high. Count the individual values passed to c(). The length() function counts elements, not their sum.
Feedback Too Low: That's too low. Count each value separated by a comma — how many are there?

---

## Question 5
Type: fill_blank
Points: 100

Complete the following R code to read a CSV file named "study_data.csv" into a data frame called df and then display the first six rows:

df <- [blank]("study_data.csv")

[blank](df)

- Blank 1: read.csv
  - Case Sensitive: false
  - Correct: Excellent! read.csv() is R's built-in function for importing comma-separated value files into a data frame.
  - Incorrect: Not quite! The function you need is part of base R, begins with "read," and specifies the file type in its name.
  - Close Match: Almost! Check the exact function name — the file extension and the function name share the same three letters.
  - Alternatives: read_csv
- Blank 2: head
  - Case Sensitive: false
  - Correct: Correct! head() returns the first six rows of a data frame by default.
  - Incorrect: Not quite! The function you need is a common, single-word base R function that is the conceptual opposite of tail().
