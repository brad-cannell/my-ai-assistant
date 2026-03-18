---
title: Template Prompt for EWB Lesson Revisions - Super Simple Version
id: template_prompt_lesson_revisions_simple
interface: api
author: brad_cannell
created: 2025-06-19
last_updated: 2026-01-20
tags:
  - ewb
---

# Overview (optional)

This prompt is for getting assistance with revising EWB lesson text, not code.

I noticed that the first version of this prompt was giving me feedback that was nearly as creative as the feedback I was getting when interacting with ChatGPT via the browser. Sometimes that's a good thing and sometimes it isn't. I'm not sure if the difference between browser and API, or if it's because the prompt I had been using in the browser was way simpler.

# USER MESSAGE

## Context

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University. I am also the co-founder and owner of Epi-Workbench, LLC - a small business developing a web-based educational platform.

I am creating a web-based business called "Epi-Workbench." Epi-Workbench is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, Epi-Workbench combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.

## Task

I'm creating a lesson titled "{{lesson_name}}" for the Epi-Workbench course titled "{{course_name}}".

I'm going to pass you some excerpts from the lesson and I'd like your recommendations for improving them.

## Constraints & Formatting

- Use 'us,' 'we,' 'our,' and 'ours' instead of 'you,' 'your,' and 'yours' to maintain a collaborative tone.
- Change any references about this "book" to this "course" and any references about this "chapter" to this "lesson".
- Convert the formatting of any Quarto-style callout blocks to use the formatting recognized by the EWB platform. For example:
  - Change `::: callout-note` to `> [!note] Note`
  - Change `::: callout-warning` to `> [!danger] Danger`
