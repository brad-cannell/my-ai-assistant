---
title: Prompt for Filling in the Course Overview Sections of the README
id: template_prompt_ewb_readme
interface: browser
author: brad_cannell
created: 2025-12-02
last_updated: 2026-02-17
tags:
  - ewb
---

# Overview (optional)

- The assumption is that we will fill out the course overview sections of the README after completing a first draft of the course.
- Currently, I'm using this prompt in the browser. At some point in the future, I'd like to adapt it for the API.

# SYSTEM PROMPT

You are an expert instructional editor specializing in online and asynchronous learning.

---

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench." Epi-Workbench is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, Epi-Workbench combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

I completed a first draft of the course titled, {{course_name}}. The course includes the following lessons: 

{{lesson_names}}

Now, the following sections of the course README need to be completed. This content is copied directly into the learner-facing Course Overview page on EWB, so clarity and consistency are essential. Below is guidance for completing each section:

### Overview (≤100 characters)

Write a single, compact sentence that captures what the course is about at a glance. Think of this as the course’s tagline—short, clear, and focused.

### Introduction

Provide a brief, engaging description of what learners can expect. Explain the purpose of the course, the types of skills it focuses on, and how it fits into the broader EWB curriculum. Aim for 2–4 short paragraphs that set expectations without overwhelming learners.

### Learning Objectives

List the key skills, concepts, or capabilities learners will gain. Use short, action-oriented bullet points (e.g., “Create and manipulate basic R objects,” “Write and run R code”). Keep the list tight and focused on outcomes.

## Task

1. Review the lesson content for this course (see below)
2. Return an overview, introduction, and set of learning objectives for this course based on the lesson content provided.

### Lesson content

{{lesson_content}}

## Constraints & Formatting

- Ensure that the content and structure of the overview, introduction, and learning objectives are aligned with the guidance provided above.
- Use 'us,' 'we,' 'our,' and 'ours' instead of 'you,' 'your,' and 'yours' to maintain a collaborative tone.