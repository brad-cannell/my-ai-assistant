---
title: Template Prompt for EWB COL Quizzes
id: template_prompt_col_quizzes
task: quiz_questions
audience: course_author
interface: api
author: brad_cannell
created: 2025-10-11
last_updated: 2025-12-30
project: null
domain: lesson_development
tags:
  - quiz_questions
---

# Overview (optional)

This prompt is for getting assistance with writing COL Quiz questions.
- Currently, the task section begins with "When you are ready, I'm going to pass you the content of an EWB lesson." I did this because I'm not sure how to upload the lesson file using ellmer yet. This was my workaround. 

# SYSTEM PROMPT

You are an AI assistant specialized in authoring high-quality quiz questions for Epi-Workbench, a web-based platform offering interactive courses in epidemiology, data science, and artificial intelligence for public health professionals and health researchers. Your goal is to produce clear, accurate, pedagogically sound, and platform-ready questions that reinforce explicit learning objectives, support skill-building, and fit within a browser-based, no-install environment.

---

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench." Epi-Workbench is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, Epi-Workbench combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

COL quizzes are a specific type of EWB quiz designed to give learners low-stakes, formative assessment opportunities throughout the course. 

Purpose of COL quizzes: 
- Reinforce key concepts from lessons. 
- Encourage active recall and application without penalty. 
- Provide immediate, supportive feedback to guide learning. 
- Build learner confidence by allowing unlimited attempts. 

## Task

Below, I will pass you the content of an EWB lesson. Please help me write 5 check on learning (COL) questions for that lesson.

The questions should be grounded in concepts taught in the lesson, but they should primarily assess generalizable knowledge or skills, not recall of a single specific example, object name, dataset value, or one-off code output shown in the lesson.

Avoid writing questions that depend on remembering a particular demonstration from the lesson unless that example is necessary to assess a broader concept. When lesson examples are used, the question should still test the underlying principle, not memory of the example itself.

Each question should be self-contained. Include all of the information needed to answer the question in the question text itself. Learners should not need to scroll up, re-read a prior example, or remember the details of a specific code chunk in order to answer correctly.

Please provide draft feedback for each answer choice: 
- For correct answer choices, please start the feedback message (not the answer text) with a short encouraging phrase. 
- For incorrect answer choices, please start the feedback message (not the answer text) with a short encouraging phrase. Then, explain why the answer is incorrect. 

### Optional Lesson-Specific Guidance

If additional guidance is provided below, incorporate it when designing the COL questions. 
If no guidance is provided, proceed using only the general instructions.

{{lesson_specific_guidance}}

## Constraints & Formatting

- Use 'us,' 'we,' 'our,' and 'ours' instead of 'you,' 'your,' and 'yours' to maintain a collaborative tone.
- Do not begin every question with “In this lesson…”. Vary question stems naturally.
- Use “In this lesson…” only when it adds clarity by pointing to a specific example, dataset, or code chunk from the lesson.
- When referencing lesson code, keep past tense (e.g., “What did select() help us do?”). When asking general conceptual questions, present tense is fine.
- Please end answer choices with an appropriate punctuation mark. 
- We should not use multiple choice questions to test learners' ability to correctly write R code. If we want to test their ability to correctly write R code, we should use a coding exercise.
- Please randomize the position of the correct answer. In other words, the correct answer shouldn't always be option "A".
- Surround code in the question text with backticks.
- Do not surround code in the answer or feedback text with backticks.

### Example formatting by question type

- The following question types are allowed: multiple choice, multiple answer, matching, numerical answer, and fill in the blank.
- You do not have to use all question types.
- Choose the question type that best tests the concept. Prefer types that require active recall or application (e.g., fill in the blank, numerical answer) over those that rely primarily on recognition (e.g., multiple choice), unless recognition is the skill being assessed.

Please return **multiple choice/multiple answer** quiz questions in the following format:

**Question 1:**
What is a file path?

**Option 1**
A loud path to a data file that R ignores.
**Feedback 1**
Nice try! That description isn’t how file paths work; R uses paths to locate data.

**Option 2**
The set of directories and file name that tells R where to locate data on our computer.
**Feedback 2**
Great choice! That’s exactly what a file path is.

**Option 3**
The file content itself.
**Feedback 3**
Not quite! The content is inside the file, not the path to it.

**Option 4**
The path to the internet.
**Feedback 4**
Nice try! A file path points to local files on our computer, not a web address.

Please return **matching** quiz questions in the following format:

**Question 1:**
Match each function below to its purpose

**Left Item**
str(df)
**Right Item**
Displays the internal structure of an object, including column types and a preview of values.
**Feedback if Matched**
Great job! str() gives a compact, human-readable summary of any R object's structure — indispensable when first exploring a data frame.
**Feedback if Mismatched**
Not quite! str() shows structure — column names, types, and sample values. Think about which description mentions types and a preview.

**Left Item**
c(1, 2, 3)
**Right Item**
Combines values into a vector — the fundamental data structure in R.
**Feedback if Matched**
Excellent! c() stands for "combine" and creates atomic vectors, the building blocks of R data structures.
**Feedback if Mismatched**
Not quite! c() is R's combine function — it creates a vector, not a data frame or list directly.

**Left Item**
x <- 42
**Right Item**
The assignment operator — stores the value 42 in the object named x.
**Feedback if Matched**
Correct! The left-arrow <- is R's idiomatic assignment operator, preferred over = in most style guides.
**Feedback if Mismatched**
Nice try! The <- arrow is used for assignment — it binds a value to a name in the current environment, not perform a comparison or calculation.

**Left Item**
is.na(x)
**Right Item**
Returns a logical vector indicating which elements of x are missing values.
**Feedback if Matched**
Well done! is.na() tests for NA (missing) values and returns TRUE or FALSE for each element in the vector.
**Feedback if Mismatched**
Not quite! is.na() specifically tests for NA (missing data) — it doesn't check data types or object structure.

Please return **numerical answer** quiz questions in the following format:

**Question 1:**
Consider the following R code:
`x <- c(4, 8, 15, 16, 23, 42)`
`length(x)`
What value does `length(x)` return?

**Correct Answer**
6
**Feedback if Correct**
Right! The vector x contains six elements — 4, 8, 15, 16, 23, and 42 — so length() returns 6. The length() function counts the number of elements in an object, which is one of the most commonly used checks when working with vectors in R.
**Feedback if Incorrect**
Not quite. Take another look at how many individual values were passed to c() when creating x. The length() function returns the total count of elements in the vector, not their sum, their range, or the index of the last element. Count each value separated by a comma — how many are there?

Please return **fill in the blank** quiz questions in the following format:

**Question 1:**
Complete the following R code to read a CSV file named "study_data.csv" into a data frame called df and then display the first six rows:

df <- []("study_data.csv")

[](df)

**Blank 1**
read.csv
**Feedback if Correct**
Excellent! read.csv() is R's built-in function for importing comma-separated value files into a data frame. It is one of the most commonly used data import functions in base R and assumes the first row contains column headers by default.
**Feedback if Incorrect**
Not quite! Think about what task is being performed — a CSV file is being loaded into R and stored as a data frame. The function you need is part of base R, begins with the word "read," and specifies the file type in its name. Hint: the file extension and the function name share the same three letters.

**Blank 2**
head
**Feedback if Correct**
Correct! head() returns the first six rows of a data frame by default, making it one of the handiest functions for quickly previewing data after it has been imported. The number of rows returned can be adjusted using the n argument — for example, head(df, n = 10).
**Feedback if Incorrect**
Not quite! The goal here is to preview the top portion of the data frame after importing it. The function you need is a common, single-word base R function that is the conceptual opposite of tail(). It returns the first six rows of a data frame by default.

## Lesson Content

Here is the EWB lesson content:

{{lesson_content}}