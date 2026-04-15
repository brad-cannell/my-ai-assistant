---
title: Making the Prompts for Creating Labs and Quizzes
author: "Brad Cannell"
created: 2026-04-12
last_updated: 2026-04-14
---

# Overview (optional)

- Multi-step pipeline conversation for generating new lab assignments.

# SYSTEM PROMPT

- None.
- Did this in Claude.ai at: https://claude.ai/chat/307f49d7-6e04-444e-b632-9b5378a0ff7c

------------------------------------------------------------------------

# Inintial User Message

I need help creating a multi-step prompt to help me create lab assignments for EWB. My plan is to pass the prompt(s), lesson content, and a set of lesson competencies to Claude via the API. I read an article yesterday that made me think that I might get even better results if I break this process up into multiple prompts/steps.

Specifically, I was thinking about breaking it up into:

1.  Create a general outline of the tasks to include in the lab.
2.  Create a scenario and data that the tasks can be fitted to.
3.  Create coding tasks that match the scenario and data.
4.  Create at least one follow-up question in the COL question format to ensure the coding task was completed correctly. 
5.  Generate a complete lab assignment as a Quarto document that adheres to the format of the lab template Quarto file. 

What do you think of this strategy?

# Revisions

I'm attaching the lab that resulted from our multi-step process (lab_introduction_to_writing_functions_in_r.qmd). I'm also attaching a version of the lab I revised (lab_introduction_to_writing_functions_in_r_revised.qmd). Compare them, then suggest ways we could revise our templates and/or prompts so they produce a finished product more like the one I want.

Here are some things I noticed:

1.  I want to always use this paragraph exactly in the `# Load Packages` section: 'Remember, it's considered a best practice to load all the packages that our file will use at the top of the file. If we have not yet installed a package, we will need to do so by running `install.packages("package name")` in the R console. For example, to install the `dplyr` package, we would run `install.packages("dplyr")`. However, we typically **do not** want to type the code to install the package here in our Quarto file because we only need to install the package once on a given computer. Not every time we run our R code.'

2.  Load the individual packages needed to complete the lab (e.g., `library(dplyr, warn.conflicts = FALSE)`) instead of loading the `tidyverse` package. We often don't need the entire `tidyverse, and loading it` makes the packages we actually need less obvious/transparent.

3.  Chunk labels should be written as `#| label: load-packages`, not `{r, load-packages}`.

4.  Notes to students are good, but they aren't needed after every code chunk. They are only needed to describe non-obvious (to someone who completed the lessons) and/or novel coding choices.

5.  Quiz-style questions should never be used as tasks (`# Task x`). For example, Task 3 in the lab_introduction_to_writing_functions_in_r.qmd. Quiz style questions should always be labeled as questions (`## Question x`).

6.  Quiz-style questions should *almost* exclusively be used to check to make sure that the code was written correctly. For example, a lab I write for the data management course might ask learners to subset the rows of a data frame to include females only. The follow-up question might ask them to run `dplyr::glimpse()` and answer a fill-in-the-blank question about the number of rows and columns in the data frame. In that scenario, I don't actually care how many rows and columns the data frame has, per se. That isn't the competency we are testing. The only reason I ask that question is that they will get the wrong answer if they didn't write the subsetting code correctly. And it is much easier to check the correctness of their code this way in our LMS than it is to check the literal code.

7.  The current lab seems to emphasize quiz questions. The goal is for labs and module quizzes to emphasize coding tasks - where learners have to write code. I'm not saying there can't be any conceptual quiz questions. There should be some, but the ratio should be heavily skewed toward coding tasks.

8.  In the original Task 1, we ask learners to create a simulated data frame. I'm totally fine with that, but the task description, "Use `tibble()` to construct an inline dataset called **screening_data** containing 24 patient screening records from three EWBRC research sites (**Site_A**, **Site_B**, **Site_C**), with 8 records per site. The dataset should include the variables **site_id**, **patient_id**, **age**, **sbp_mmhg**, and **fasting_glucose**. Place one `NA` in **sbp_mmhg** at row 6 (patient **A-006**) and one `NA` in **fasting_glucose** at row 14 (patient **B-006**)", makes it sound like we want them to come up with the values for this data frame on their own. With data this complex, that isn't feasible. Instead, we need to just give them the complete code, a little bit of context about the data frame, and ask them to just run the code.

9.  In the original Task 2, we ask learners to view the data frame with `dplyr::glimpse()`, but it isn't clear why. We don't ask them any questions about what they see when they do. Because we are giving them the complete code to create the data, I don't see much value in asking them how many rows and columns the data frame contains at this point.

10. The original Task 3, "Read the four analyst scenarios below and determine which repetition-reduction approach is most appropriate for each. After reviewing all four, run the code chunk to store your answers.", tests concepts that haven't been covered yet: dplyr column-wise operations, the purrr package, and for loops. Where are those concepts being pulled from? They aren't in the lessons we passed to the AI assistant.

11. The example used in the original Task 4 is simple and easy to understand, but it doesn't do a good job of illustrating a scenario when we would need to create a custom function. We ultimately go on to build the `convert_mmhg_to_kpa()` based on this example. However, we could easily get the same result using this code without a custom function: `screening_data |> mutate(sbp_kpa = round(sbp_mmhg * 0.133322, 2))`.

12. The original Task 7 requires knowledge of the `purrr` package, which we haven't covered yet.

13. The example used in the original Task 10 doesn't do a good job of illustrating a scenario when we would need to create a custom function. We ultimately go on to build the `flag_elevated()` based on this example. However, we could easily get the same result using this code without a custom function: `screening_data |> mutate(glucose_elevated = fasting_glucose > 126)`. The custom function essentially does nothing for us.

I'm wondering if we should also create an eighth step in our workflow where I insert notes to Claude into the Quarto document (e.g., `<!-- 🔴 Note to Claude: This would be a good place to insert a question about X. -->`). Or perhaps I should have already done this in one of our existing steps.

------------------------------------------------------------------------

# Claude Cowork Prompt for Finding Repetitive Code

> I have an idea. What if I ask Claude Cowork to review all of my previous lesson files for repetitive code, and code that would otherwise benefit from a custom function? Then, it could record them in a markdown file that we can pass to our workflow. This could provide the AI assistant with concrete examples of the kinds of problems our learners might want to learn to address by writing custom functions.

<context>

I am developing a lab assignment for an R programming course called Epi-Workbench (EWB). The lab teaches learners how to write custom R functions. I need your help reviewing my existing course materials to find real examples of repetitive code patterns that a custom function could improve.

</context>

<task>

Please review all of the lesson files, lab assignments, and quizzes in the following locations:

- '/Users/bradcannell/Desktop/Git/Academia/Teaching/intro.r.public/modules'
- '/Users/bradcannell/Desktop/Git/Academia/Teaching/intro.r.private/modules'
- '/Users/bradcannell/Library/CloudStorage/GoogleDrive-brad.cannell@epi-workbench.com/My Drive/Courses/Introduction to Bivariate Descriptive Analysis in R'
- '/Users/bradcannell/Library/CloudStorage/GoogleDrive-brad.cannell@epi-workbench.com/My Drive/Courses/Introduction to Coding Tools and Best Practices in R'
- '/Users/bradcannell/Library/CloudStorage/GoogleDrive-brad.cannell@epi-workbench.com/My Drive/Courses/Introduction to Data Management in R'
- '/Users/bradcannell/Library/CloudStorage/GoogleDrive-brad.cannell@epi-workbench.com/My Drive/Courses/Introduction to Data Transfer in R'
- '/Users/bradcannell/Library/CloudStorage/GoogleDrive-brad.cannell@epi-workbench.com/My Drive/Courses/Introduction to Descriptive Analysis in R'
- '/Users/bradcannell/Library/CloudStorage/GoogleDrive-brad.cannell@epi-workbench.com/My Drive/Courses/Introduction to Univariate Descriptive Analysis in R'
- '/Users/bradcannell/Library/CloudStorage/GoogleDrive-brad.cannell@epi-workbench.com/My Drive/Courses/R Fundamentals'

For each repetitive code pattern you find, record it in a markdown file called `repetitive_code_patterns.md` using the format described below.

Identify code patterns that meet at least one of the following criteria:

1.  **Copy-paste repetition** — the same or nearly identical code block appears two or more times, differing only in variable names, column names, or literal values.
2.  **Built-in function limitation** — code that uses a workaround because a built-in R function doesn't produce the exact result needed (e.g., handling NA values in a comparison, coercing output format).
3.  **Multi-step boilerplate** — a sequence of 2 or more steps that always appear together and always serve the same purpose (e.g., compute a statistic, round it, assign it to an object).

For each pattern found, record the following:

- **Pattern name** — a short descriptive label (e.g., "Repeated grouped summary by variable").
- **Criterion met** — which of the three criteria above applies.
- **Source** — the file name(s) where the pattern appears.
- **Description** — 2–3 sentences describing what the code does, why it is repetitive or limited, and what a custom function would improve.
- **Representative example** — a short code excerpt (the smallest example that clearly illustrates the pattern). If the pattern appears in multiple files, show one representative example only.
- **Function opportunity** — one sentence describing what a custom function built around this pattern would accept as arguments and return as output.

</task>

<constraints> 

- Focus on patterns that are realistic and common in public health data analysis workflows — not obscure edge cases. 
- Only include patterns where writing a custom function would provide a clear, demonstrable benefit over the inline code. If a single tidyverse expression already handles the pattern cleanly, skip it. 
- Do not include patterns that require packages or techniques not already used in the course materials. 
- Order the patterns from most common/impactful to least. 
- If you find more than 15 patterns, include only the 15 strongest. 

</constraints>

------------------------------------------------------------------------

# Claude Cowork Conversation About Creating a Prompt that Creates a Google Doc Version of the Lab/Quiz

This was done on my work computer. It won't be visible online.

## Check for Google Docs access

Are you able to view the Google Doc: __https://docs.google.com/document/d/1R75ktQJ5e849WOMhlSORjCe6xWsWFRCsvDles1_tUUQ/edit?tab=t.0__?

## Compare Quarto and Google Docs

I'm attaching a Quarto document here as well. The Google Doc and the Quarto document are from the same lab assignment for my Introduction to R Programming course.

When I write new lab assignments, I start by writing them in Quarto documents. In the past, I would manually create the Google Doc by copying and pasting content from the Quarto Document, then spend a long time formatting it.

Why do I write the lab in two different formats? Google Docs usually feel more familiar to my students than Quarto documents do. So, they generally start by opening the Google Doc and using it as a set of instructions to follow while they complete the lab assignment. Then they can download and open the Quarto file to use as an answer key.

I would like your help with writing a prompt I can use to have Claude do this conversion for me. Take note of where the format, structure, and content of these documents are the same and where they differ. 

The goal is for me to pass Claude this prompt and a new Quarto lab file, and for Claude to return a formatted Google Doc.

## Word and the API

**I passed this to Claude Code, not Claude Cowork**

I'm passing the prompt to Claude through an API call, assisted by functions from the Chatlas package. 

The code doing the work looks like this: [highling the code]

<code>
# Create Chat Object
chat_step_08 = ChatAnthropic(
    model=model_complex,
    system_prompt=system_prompt,
    max_tokens=20000
)

# Pass the prompt to the AI assistant
chat_step_08.chat(user_message_step_08, echo='none')

# Save the assembled lab as a .qmd file
lab_docx_path = lab_folder_path / f"lab_{lab_quiz_name.lower().replace(' ', '_')}.docx"
lab_docx_path.write_text(str(chat_step_08.get_last_turn()), encoding="utf-8")

print(f"Lab saved to: {lab_docx_path}. Upload it to Google Docs next.")
</code>

This code doesn't work because `lab_docx_path.write_text(str(chat_step_08.get_last_turn()), encoding="utf-8")` doesn't actually create a Word document. What's the best way to generate a Word document from this API call?

### Follow-up Question about Google Docs

Ultimately, I really want to end up with a Google Doc. Is there any way to skip straight to creating a Google Doc or do I need to create Word document first?

### Word template

Okay. It sounds like I need to make a Word template from my Google Doc. How do I do that?

### Start with a plain markdown document

It looks like I can upload a markdown document to Google Docs, and then edit and share it exactly like I would a native Google Doc. Perhaps my next step should be to create a revised markdown document, upload it Google Docs, do some light manual editing, and then share it intead of a Google doc. In fact, perhaps I should skip Google Docs altogether and just use GitHub.

**Asking Claude Code to write some helper functions**

<context>
I write lab assignments in Quarto (`.qmd`) files. These files serve as the instructor's answer key — they contain full R code solutions, explanatory notes for students, and question-and-answer pairs. Your job is to convert the answer key Quarto files into student-facing lab instructions documents I can upload to GitHub and share with students.

The student-facing instructions differs from the lab answer key in several important ways:
- All R code is removed. Students write their own code in a separate Quarto file.
- All "Notes for students" sections (which contain answers and explanations) are removed.
- Question answers are stripped.
</context>

<task>
Help me write four Python helper functions for creating a new instructions document from the lab answer key with the following removed:
 
1. **YAML header** — everything between the opening and closing `---` delimiters at the top of the file.
2. **All R code** — remove every the R code inside all ` ```{{r}} ... ``` ` blocks. Do not replace it with anything. Leave the code blocks and comments.
3. **"Notes for students" subsections** — remove every `### Notes for students` heading and all content beneath it (until the next heading of equal or higher level).
4. **Question answers** — the `### Question N` subsections each contain a question followed by a bullet-point answer. Remove the heading, keep only the question text (reworded to be student-facing if needed), and strip the answer. The questions are reformatted elsewhere (see below).
</task>

<constraints>
- The new helper functions should be saved to the same location as my existing helper functions: '/Users/bradcannell/Desktop/Git/AI/my-ai-assistant/py_scripts/py_scripts'. I will load the helper functions in the "# Load Packages and Helper Functions" section of this document.
- The first function in the pipeline should accept the lab answer key as input and return the modifed file to the file path saved to `lab_instructions_path`.
- All subsequent functions in the pipeline should overwrite the the modifed file saved to `lab_instructions_path`.
</constraints>

#### Follow-up

Please make the following adjustments to the functions:

lab_remove_yaml_header()
- Change this function to be called `lab_update_yaml_header()`.
- Instead of removing the YAML header completely, make the following modifications:
  - Change the `author` field to `author: "[Your Name]"`
  - Change the date in the `date-modified` field to `[Enter Date]`

lab_remove_r_code():
- Don't remove R code that imports data.
  - These will typically include a `read_*` function.
- Don't remove R code that creates tibbles and data frames using the `tibble()`, `tribble()` or `data.frame()` functions.

lab_remove_question_answers():
- The `### Question N` subsections each contain a question followed by a bullet-point answer. KEEP the heading and the question text, but strip the answer.
- Some questions use {r, eval=false} code blocks as multiple-choice answer options rather than * bullet answers. After `lab_remove_r_code` runs, those blocks still contain the comment text (e.g., `# Correct. Block 3 is labeled Midwest...`). I want those stripped too. Please extend `lab_remove_question_answers` to also drop code blocks within question sections.
 - When the answer choices are removed, please add "See our course LMS for the answer choices and submit your response." verbatim to the end of the question text.

------------------------------------------------------------------------

# Creating a Module Quiz from the Lab

At this point, I have a complete lab assignment created. Now, I need to create a culminating exercise. 

Culminating exercises are final assessments that mirror the structure of labs but with minimal guidance. These exercises challenge learners to synthesize and apply everything they've learned, encouraging self-assessment and reflection. They serve as capstone experiences that reinforce mastery and readiness for real-world application.

I could start the process of creating a culminating exercise from scratch, but I don't think that's the most efficient path. The intent is for culminating exercises to cover the exact same content as the labs, and even for the tasks to be similar. The examples and data should be different, and therefore the follow-up questions and answers will be different, but a student who does well on the lab should have no problem doing well on the culminating exercise. Therefore, it seems like providing the lab to the AI assistant could be the most approprite starting point.

All that said, the culminating exercise should be more difficult than the lab. However, the additional difficulty should be the result of providing less guidance (e.g., no "Notes to students" sections or hints) rather more difficult material.

## Follow-up

