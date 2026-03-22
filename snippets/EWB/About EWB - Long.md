---
title: "About Epi-Workbench (EWB) - Long Version"
author: "Brad Cannell"
date: 2025-04-11
date-modified: 2026-03-21
tags: [ewb, branding, about, epidemiology, context, lesson-types, colors, logos]
---

<introduction>
# About Epi-Workbench (EWB)

We are creating a web-based business called "Epi-Workbench" (EWB). Epi-Workbench is an online platform offering interactive courses in epidemiology, data science, and artificial intelligence specifically designed for people working in public health and other health professions and, to a lesser extent, members of the general public who are interested in learning more about health research. With beginner to advanced-level courses, Epi-Workbench combines real-person instruction with hands-on coding exercises and integrated AI tools for a comprehensive learning experience. Learners can develop skills in statistical programming, applied statistical analyses, and scientific communication—all from the convenience of their browser, with no installation required.
</introduction>

---

<context_purpose>
This document provides branding context for AI assistants generating content on behalf of Epi-Workbench.
</context_purpose>

---

<about_ewb>
# Epi-Workbench (EWB) Branding Guidelines

## About Epi-Workbench

**Tagline:** Learn Epidemiology. Code With Purpose.

**Elevator pitch:** From theory to coding to application, learn to generate evidence, improve decisions, and advance research in public health, healthcare, and biomedical science.

### Mission

Our mission is to make the best tools and methods from epidemiology, data science, and artificial intelligence accessible to everyone working to improve health and well-being, empowering them to analyze data, generate insights, and drive positive change in public health, healthcare, and the biomedical sciences.

### Our Name

Epidemiology is the study of the distribution and determinants of health and well-being across populations. Yet the desire to understand and improve human health extends far beyond those who formally identify as epidemiologists. Epi-Workbench is a community for anyone passionate about health and well-being — a place to explore, learn, and practice using tools that advance this vital mission.

### What We Offer

Epi-Workbench provides interactive, browser-based courses that combine expert instruction with hands-on coding, quizzes, labs, and culminating projects. Learners progress from beginner to advanced levels while practicing on real datasets, receiving immediate feedback, and building confidence through unlimited practice. Beyond individual learning, we foster a growing community where health professionals, researchers, and learners can exchange ideas, share solutions, and learn from one another. Our courses are designed to be engaging, flexible, and practical — helping learners develop skills in statistical programming, data management, analysis, and scientific communication without the need for software installation.

### Why Choose Us?

Unlike other data learning platforms, we focus specifically on the needs of professionals in public health, healthcare, and the biomedical sciences. At Epi-Workbench, you'll find:

- **Interactive Courses** that provide real-time, custom feedback while you practice coding.
- **R and Python Training** designed for health applications, not generic data science.
- **Expert Instruction** from practicing professionals who bring years of real-world experience into every lesson.
- **Practical Tools** to streamline common research workflows and address pain points, from managing health data to running power and sample size calculations.
- **A Growing Community** where learners and professionals connect, share ideas, and learn from each other.
</about_ewb>

---

<brand_colors>
## Brand Colors

### Primary Colors

| Name      | Hex       | Usage                                                   |
|-----------|-----------|---------------------------------------------------------|
| Dark Blue | `#4E5F72` | Primary brand color; headers, backgrounds, UI elements  |
| Yellow    | `#FFD662` | Primary accent; highlights, calls-to-action             |

### Secondary Colors

| Name  | Hex       | Usage                         |
|-------|-----------|-------------------------------|
| Green | `#28A745` | Success states, secondary UI  |
| Gray  | `#6C757D` | Body text, borders, muted UI  |

### Accent Colors

| Name   | Hex       | Usage                        |
|--------|-----------|------------------------------|
| Orange | `#FD7E14` | Accent highlights, warnings  |
</brand_colors>

---

<logos>
## Logos

Logo files are maintained in the `EWBTemplates` R package (`man/figures/ewb_logos/`). Available variants:

| File                                      | Description                                            |
|-------------------------------------------|--------------------------------------------------------|
| `epi_workbench_dark_blue_full_logo.png`   | Full logo, dark blue — use on white/light backgrounds  |
| `epi_workbench_full_logo_on_dark_bg.png`  | Full logo, light — use on dark backgrounds             |
| `epi_workbench_full_logo_white.png`       | Full logo, white — use on colored backgrounds          |
| `epi_workbench_dark_blue_epi_logo.png`    | "EPI" mark only, dark blue                             |
| `epi_workbench_epi_on_dark_bg.png`        | "EPI" mark only, light                                 |
| `epi_workbench_epi_white_logo.png`        | "EPI" mark only, white                                 |
| `epi_workbench_dark_blue_ewb_logo.png`    | "EWB" mark only, dark blue                             |
| `epi_workbench_ewb_on_dark_bg.png`        | "EWB" mark only, light                                 |
| `epi_workbench_ewb_white_logo.png`        | "EWB" mark only, white                                 |
| `epi_workbench_epi_favicon.png`           | Favicon / icon                                         |

**Logo usage rules:**
- Use the dark blue full logo on white or light-colored backgrounds.
- Use the light/white logo variants on dark or colored backgrounds.
- Do not recolor, stretch, or modify logos.
</logos>

---

<voice_and_tone>
## Voice & Tone

- **Tone:** Clear, professional, and approachable. Aimed at learners and practitioners in epidemiology and public health data science.
- **Audience:** Graduate students, researchers, and public health professionals learning R, Python, and data science methods for health applications.
- **Voice:** Educational and supportive — avoid jargon where possible; explain technical concepts accessibly. Emphasize real-world application and community.
- **Key themes:** Accessibility, empowerment, evidence generation, public health impact.
</voice_and_tone>

---

<r_package>
## R Package Resources

Brand assets are distributed via the [ewb](https://github.com/epi-workbench/ewb) R package:

```r
# Install
pak::pak("epi-workbench/ewb")

# Access color palette data frame
data(ewb_colors)

# Visualize palette
color_plots(ewb_colors, "ewb")
```

Color palette data frame structure:

```
group | subgroup  | hex      | description
ewb   | primary   | #4E5F72  | Dark Blue
ewb   | primary   | #FFD662  | Yellow
ewb   | secondary | #28A745  | Green
ewb   | secondary | #6C757D  | Gray
ewb   | accent    | #FD7E14  | Orange
```
</r_package>

---

<lesson_types>
# Lesson Types on Epi-Workbench

Epi-Workbench courses are built using a structured hierarchy: Courses are divided into Chapters, which are further broken down into individual Lessons. Lessons are the building blocks of all content and come in six types: written lessons, video lessons, coding exercises, check-on-learning (COL) quizzes, labs, and course culminating exercises.

Each lesson type serves a specific purpose in the learning process:

## Written lessons

Written lessons introduce key concepts, background information, and theoretical foundations. Content is presented in a clear, blog-style format—like a digital textbook—with optional images and figures. While foundational, written lessons will generally comprise a smaller proportion of content in mature courses to keep learners actively engaged.

## Video lessons

Video lessons deliver core content through short, engaging clips (typically 2–5 minutes long). These lessons are designed to be informative and fun, providing a low-pressure way for learners to absorb new material through visual and auditory formats.

## Coding exercises

Coding exercises are the primary mode of content delivery on Epi-Workbench. These lessons combine brief instructional text or video with interactive coding blocks and real datasets. Learners write and run code directly in their browser, receive immediate feedback, and can request hints when needed. These exercises are designed to be engaging, low-pressure, and iterative—perfect for building hands-on skills in statistical programming and data analysis. Learners can complete each coding exercise as many times as they like, promoting practice and confidence without penalty.

## Check-on-Learning (COL) Quizzes

COL quizzes are short, low-stakes assessments embedded throughout each course. They help learners quickly check their understanding of key concepts introduced in written lessons, videos, or coding exercises. Learners can take each quiz as many times as they like, promoting practice and confidence without penalty.

## Lab Exercises

Each course includes at least one lab exercise. Labs allow learners to apply multiple concepts from the course in a more comprehensive and realistic scenario. Labs provide structured guidance while offering more complexity than individual lessons, helping learners bridge the gap between theory and practice. Learners can complete each lab exercise as many times as they like, promoting practice and confidence without penalty.

## Course Culminating Exercises

Culminating exercises are final assessments that mirror the structure of labs but with minimal guidance. These exercises challenge learners to synthesize and apply everything they've learned, encouraging self-assessment and reflection. They serve as capstone experiences that reinforce mastery and readiness for real-world application.
</lesson_types>