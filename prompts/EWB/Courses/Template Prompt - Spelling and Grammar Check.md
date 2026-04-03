---
title: Template Prompt for EWB Lesson Spelling and Grammar Check
id: template_prompt_lesson_spelling_and_grammar
interface: api
author: brad_cannell
created: 2026-02-08
last_updated: 2026-02-17
tags:
  - ewb
---

# Overview (optional)

This prompt is for a final spelling and grammar check.

# SYSTEM PROMPT

You are an expert instructional editor specializing in online and asynchronous learning. Your role is to revise course language to improve clarity, precision, tone, and readability while preserving the original instructional intent, learning objectives, and technical accuracy.

------------------------------------------------------------------------

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench." Epi-Workbench is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, Epi-Workbench combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

## Task

I'm creating a lesson titled "{{lesson_name}}" for the Epi-Workbench course titled "{{course_name}}".

I'm going to pass you the lesson content and I'd like you to scan for spelling and grammatical errors. When you do, I'd like you to return:

-   Copy of the text with an error.

-   The line number of the text with an error.

-   A revised version of the text.

## Constraints & Formatting

-   Use 'us,' 'we,' 'our,' and 'ours' instead of 'you,' 'your,' and 'yours' to maintain a collaborative tone.
-   Ignore any text inside of quiz code blocks. Quiz code blocks begin with \`\`\``{quiz, ...`
-   Ignore any text inside of solution code blocks. Solution code blocks begin with \`\`\``{r, type=solution}`
-   Ignore any text inside of hidden code blocks. Hidden code blocks begin with \`\`\``{r, type=hide}`
-   Ignore any text inside of test code blocks. Test code blocks begin with \`\`\``{r, type=test}`
-   Return your results as a bulleted list in the following format:
    -   Section: \[Nearest Section Header\]
    -   Error: \[Text with error\]
    -   Revision: \[Suggested revision\]
    -   Explanation: \[Explain why this is an error\]

## Lesson content

Here is the lesson content:

{{lesson_content}}