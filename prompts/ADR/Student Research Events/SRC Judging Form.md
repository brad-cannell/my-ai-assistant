---
title: Assigning Judges for the SRC
author: "Brad Cannell"
created: 2026-04-08
last_updated: 2026-04-08
tags:
  - src
  - judging
  - qualtrics
---

# Overview (optional)

- I need help creating the judging form. Specifically, I need to do two at least two things:
  1.  I need to simplify the form and criteria. I was told that judging took too long in the past.
  2.  I need to understand how to build the judging form into Qualtrics.

## Links and Resources

- Link to [HCNHS SRC Judging Handbook 2024.docx](https://tcu.box.com/s/gdcg9ex42d3qnhbzrrooa9oszt7l1nqm)
- Link to [2026_SRC_Judge_Assignments.xlsx](https://tcu.box.com/s/hqii1odpjhfhciwp6vgr23naywcqaph9)
- Link to conversation on [Claude.ai](https://claude.ai/chat/b54978fa-9800-4704-a1c9-f915ae1ec914)

# SYSTEM PROMPT

I'm using the HC Research Committee Project on Claude.ai. It already has a system prompt in the "Instructions" section.

------------------------------------------------------------------------

# USER MESSAGE

I'm using the HC Research Committee Project on Claude.ai. It already has a lot of context from `HCHS_Research_Committee_Project_Briefing.md` and previous chats.

## Context

I need help creating the judging forms for the Student Research Conference. Specifically, I need help with two high-level tasks: 1. I need to simplify the form and criteria. I was told that judging took too long in the past. 2. I need help building the judging form in Qualtrics.

### Simply the judging form

In our last meeting, the Harris College Research Committee members told me that we needed to simplify the judging criteria that was used in the past. They said that many judges felt like it was overly complex and took too long to complete.

I'm attaching **HCNHS SRC Judging Handbook 2024.docx**. This document is two years old, but it contains the scoring criteria that was used in the past. It also contains some potentially relevant background information.

### Build the judging form in Qualtrics

After creating the content and simplified criteria for the judging forms, I need to disseminate the forms to the judges. I believe the best way to do so is to build the forms in Qualtrics. I am already familiar with Qualtrics, and many of our faculty judges are too. Additionally, using Qualtrics should make scoring the forms relatively easy.

Building a basic version of the judging form in Qualtrics isn't an issue for me. I can do that without assistance. However, I'm not sure what the best way to best way to link posters and judges is.

The current plan is for judges to scan a QR code that opens the qualtrics survey on their phone or tablet, but how does Qualtrics know which poster is being scored and which judge is doing the scoring?

I can add questions to the survey that ask judges to select the poster number and their name from a dropdown list, but leaves room for data entry errors (i.e., accidentally selecting the wrong value). Additionally, that is potentially a lot of values to scroll through.

Ideally, I would have a unique QR or link for each judge that automatically selects the form for the correct poster, but I don't know how to build that, and I'm not sure it's worth the development time to build.

## Task

To start with, I'd like you to read my prompt and the attached documents, ask any clarifying questions you need to ask, and then help me come up with a plan for moving forward.

------------------------------------------------------------------------

# Clarifying Questions

> Before I draft the simplified rubric, I want to confirm a few things:

> 1.  How many scoring categories do you want? The project briefing mentions a simplified rubric with 5 criteria totaling 100 points. Does the committee want to stick with roughly that structure, or are you open to even fewer (e.g., 3–4 categories)?

> 2.  Should there still be a pre-event review component? The 2024 process allowed judges to score Visual and Content sections in advance from the poster file, then only score Verbal on the day of. Do you want to keep that two-phase approach, or simplify to a single day-of scoring pass?

> 3.  Do you want written comments? The old form included a comments section. Should the new form include an optional comment box (e.g., for constructive feedback to students), or would you prefer to drop it to save time?

> 4.  On the Qualtrics linking question — this is where I have the most to say, so let me lay out the options now.

## My response

1.  I think that structure sounds like a reasonable start. I'm also open to exploring what even fewer categories might look like. I do think it's important to try to maintain some level of consistency with previous years.

2.  No. The committee was clear that they did not want a pre-event review component. In fact, that was part of the reason the committee asked me to simplify the scoring criteria. No pre-review, but a shorter, simpler in-person review.

3.  I'm sort of indifferent. I don't think we will use the comments in the judging process, but it might be a good idea to include an optional comment box for judges.

4.  Thanks for providing these ideas. I'm leaning toward option C. There aren't any links for judges to search for or anything. They just walk around the room and scan the QR code at the appropriate poster. Having said that, how do we prevent others from scanning the QR code and impersonating a judge?

## Response 2

Actually, there are monetary stakes. Students with the highest scores win money (1st, 2nd, and 3rd place). So, there would be some incentive to impersonate a judge and pad their scores. I think the simple PIN solution could be enough of a barrier to prevent this situation, though.

Yes, please draft the 5-category version with brief scoring anchors next.

## Response 3: Review of the scoring rubric

I want to make sure I'm understanding this scoring rubric correctly. As an example, if I am a judge, I'm reviewing a poster, and I believe that the "Poster is visually polished, easy to read from a reasonable distance, logically organized, and free of errors. Figures, tables, and graphics enhance understanding." I would select a score in Qualtrics between 17 and 20 for this criterion. Is that correct?

Initially, I was put off by the uneven point values associated with each scoring category. However, your explanation makes sense to me, and I'm willing to give it a try. Before moving on to the next step, please generate a markdown document version of the scoring rubric. Then, let's move on to the Qualtrics survey design.

## Response 4: Starting the Qualtrics build

Please generate a step-by-step build guide I can follow to create the Qualtrics survey. I will use the version that creates the conditional dropdown questions. Additionally, will you please include some very brief introductory text I can place at the top of the form?

## Response 5: Guide Refinement

Before moving on, please add an additional appendix section to the guide. The new appendix section should list the members of each judge team on separate lines. This allows for easy cut-and-paste into the Step 3 judge identification questions via Qualtric's "Edit multiple" question option. Please return only the additional appendix material. I will manually copy and paste it into the markdown guide.

Anonymous Link: <https://tcu.co1.qualtrics.com/jfe/form/SV_ba4iUmEmlCbLBhI>

## Testing

I'm attaching a PDF screenshot of the first complete version of the Qualtrics survey. If you are able, please review it for typos and errors.

1.  Great catch! I deleted `judges_02_03`
2.  I double-checked the recode values. They are all correct.
3.  I created a custom end-of-survey message that says, "Thank you! Your scores for Poster \#`${e://Field/PosterNum}`{style="color: rgb(0, 0, 0); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"} have been recorded. You may close this window and scan the next poster's QR code." I stored it in my Qualtrics end-of-survey message library. I added it to the survey by clicking "Survey Flow" -\> "Add a New Element Here" -\> "End of Survey" -\> "Customize" -\> "Custom end of survey message..." -\> selecting "SRC Judging For EOS Message" from the dropdown list. I'm not sure why it doesn't appear on the survey builder screen, but it does appear when I test the survey. Please write some instructions I can add to the guide about this, and suggest a place for me to add them.
4.  Yes, I prefer it in the same block as the scoring questions. That creates one less "Next" button for judges to click.

## QR Code

1.  I would like a simple printable sheet (one label per poster with poster number, student name, and QR code). Should we also add the names of the judges to the label?
2.  This is the base anonymous link: https://tcu.co1.qualtrics.com/jfe/form/SV_ba4iUmEmlCbLBhI

## Instructions

These work great! Thank you! Now, please help me create instructions for the faculty judges. Please generate the instructions as a markdown document.

1.  I plan to email these instructions to judges and also print copies for the day of the event.
2.  Yes, judges are to be told to contact "Brad Cannell (573-239-8876)." I'm afraid I won't receive it in time if they email me. I'll also be judging and doing other event management tasks during the SRC.
3.  Please add the actual PIN. Please also add instructions to keep the PIN private.
4.  Yes, it's probably a good idea to mention that there is no pre-review this year.

## Email

Now I need to write an email to send to the judges. The email needs to include their judging assignments (I haven't sent them out yet). I will also attach the instruction sheet we just created.

Additionally, I'm wondering whether I should send a separate email to each judging team rather than a single email to all judges for at least two reasons:

1.  Some teams are judging fewer posters than others. Teams with more posters may feel resentful if they see it in the email.
2.  It may be easier for judges to digest the email if it only has their assignments rather than a table of all assignments.

### Email Follow-up Question Responses

1.  One email per team.
2.  I think we should include the poster titles.
3.  I plan to send them tonight (Wednesday). The event is on Friday.
4.  I want to cc Eva Leon (E.LEON\@tcu.edu) on all of these emails.

### Add the Emails to Outlook

Additionally, what's the best way to preserve the formatting when I paste this content into an Outlook (web) email? And should I try to automate the process of writing and sending the emails?

## Testing the Survey

I'm testing the process for importing and analyzing judges' scores in Positron using R. I'm attaching the code I have so far. When I import the Qualtrics data through the API, I get the following error:

<error> ── Column specification ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── cols( .default = col_logical(), StartDate = col_datetime(format = ""), EndDate = col_datetime(format = ""), Status = col_character(), IPAddress = col_character(), Progress = col_double(), `Duration (in seconds)` = col_double(), RecordedDate = col_datetime(format = ""), ResponseId = col_character(), LocationLatitude = col_double(), LocationLongitude = col_double(), DistributionChannel = col_character(), UserLanguage = col_character(), judges_01_01 = col_character(), judges_01_13 = col_character(), judges_01_19 = col_character(), judges_02_23 = col_character(), judges_02_28 = col_character(), pin = col_double(), poster_design = col_character(), science = col_character() \# ... with 6 more columns ) ℹ Use `spec()` for the full column specifications.

Warning messages: 1: There was 1 warning in `dplyr::mutate()`. ℹ In argument: `poster_design = readr::parse_factor(...)`. Caused by warning: ! 2 parsing failures. row col expected actual 4 -- value in level set Good Generally readable and organized with minor issues — e.g., some clutter, small text, or a figure that could be clearer. 5 -- value in level set Good Generally readable and organized with minor issues — e.g., some clutter, small text, or a figure that could be clearer. 2: There was 1 warning in `dplyr::mutate()`. ℹ In argument: `science = readr::parse_factor(science, levels = ln, ordered = TRUE, include_na = FALSE)`. Caused by warning: ! 2 parsing failures. row col expected actual 3 -- value in level set Good Most key sections are present and adequate, but one area (e.g., background, methods, or results) is underdeveloped or somewhat unclear.\
5 -- value in level set Adequate Multiple sections are missing, unclear, or underdeveloped. It's hard to understand the full scope of the research from the poster alone. 3: There was 1 warning in `dplyr::mutate()`. ℹ In argument: `presentation = readr::parse_factor(...)`. Caused by warning: ! 1 parsing failure. row col expected actual 4 -- value in level set Good The student explains the work adequately. The explanation is generally clear but may lack depth, confidence, or engagement in some areas. 4: There was 1 warning in `dplyr::mutate()`. ℹ In argument: `critical_thinking = readr::parse_factor(...)`. Caused by warning: ! 1 parsing failure. row col expected actual 3 -- value in level set Good The student can discuss limitations and next steps at a basic level and answers most questions adequately. </error>

Will you please help me troubleshoot this error an come up with solutions?

### Importing Qualtrics data with labels

Unfortunately, when I try option B, the judges' names are also imported as numeric values.

### Scoring each poster

I'm attaching my updated code file with just a couple of updates. I'm also attaching a file showing what the data currently looks like (src_scores_clean.csv). I need your help:

1.  Writing code to flag potential issues (e.g., too many or not enough reviews for a given poster).
2.  Calculating an overall score for each poster.
3.  Generating a report showing the posters ranked by overall score.

## Summarize - Make Reproducible

Summarize everything we did in this chat into a guide I can use to quickly reproduce this workflow next year when I am preparing for the SRC again. Create the summary as a markdown file.

------------------------------------------------------------------------

# Updates to the Report

I want to split this file (Summarize_Scores.qmd) into three files. 1. Import and clean. An R script that imports the data from Qualtrics, cleans it, and saves the clean data as a CSV file. 2. Data quality checks. A Quarto file that imports the cleaned CSV file from step 1, performs data quality checks, and renders as an HTML report. 3. Scoring and Results. A Quarto file that scores and ranks, and renders as an HTML report.

Please help me make the following updates to `data_quality.qmd`: 1. I would like to add the date and time the report was last run to the top of the rendered report. 2. I want to be able to run `import_clean.R` at the top of this file, but I don’t want it to run by default (`#| eval: false`). 3. I don’t want the Load Packages or Import Data headings or code blocks to be visible in the rendered report. 4. I don’t want to collapse the code blocks for Check Review Counts, Check for Duplicate Submissions, Check for Missing Scores, and Check for Score Outliers by default. 5. I want the tabular results to be displayed in the rendered report with the `DT` package.

Please help me make the following updates to `scoring_results.qmd`: - In addition to the overall ranking, I need to rank the posters by grad status (undergraduate, graduate, doctoral). - The poster number and undergraduate/graduate status is available in: '/Users/bradcannell/Library/CloudStorage/Box-Box/ADR Admin/HC Research Committee Shared/Student Research Conference/2026 SRC/2026 Poster Session Assignments.xlsx'