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