---
title: ADR Knowledge Base Technology
id: adr_knowledge_base_technology
task: text_revision
audience: academic
status: draft
author: "Brad Cannell"
created: 2025-12-27
last_updated: 2025-12-27
project: adr_sharepoint
domain: academia
tags:
  - knowledge_base
  - sharepoint
  - box
  - wiki
  - sop
---

<!--
YAML HEADER INSTRUCTIONS

Complete the YAML header above for every prompt. These fields support organization,
reuse, and future search, but should remain lightweight and human-readable.

ID GUIDELINES
- id: Use a short, stable, human-readable identifier in lowercase snake_case.
- Base the id on the prompt’s core purpose using a verb–object pattern
  (e.g., rewrite_academic_tone, review_r_code_style).
- Avoid dates, version numbers, model names, project names, or author names.
- Treat the id as permanent; change it only if the prompt’s fundamental purpose changes.

FIELD DESCRIPTIONS
- title: A brief, human-readable description of what the prompt does.
- task: The primary type of work the prompt performs (e.g., text_revision, code_review).
- audience: The intended audience for the output (e.g., academic, student, developer).
- status: Current maturity of the prompt (draft, stable, experimental, deprecated).
- author: Name of the prompt author.
- created: Date the prompt was first created (YYYY-MM-DD).
- last_updated: Date of the most recent substantive revision (YYYY-MM-DD).
- project: Associated project, course, or initiative, or null if broadly reusable.
- domain: Subject area or disciplinary context (e.g., epidemiology, data_science, general).
- tags: Optional keywords to support browsing and future search.

Avoid including model names or API parameters in the YAML header.
-->

# Overview (optional)

I want to make a web-based resource for the ADR office. The primary purposes of the resource are:

1. Serve as a knowledge base for Harris College faculty. A place where they can find information about all aspects of conducting research at TCU. For example, applying for grants, submitting IRB applications, executing contracts, etc.

However, when possible, I should probably provide links to resources (e.g., the IRB page) - supplementing as needed to fill in gaps - rather than write my own resources from scratch. Otherwise, it will be difficult to keep the resources up-to-date.

2. Disseminating information about research at Harris college. For example, funding opportunities, training opportunities, colleuges recent successes.

3. Introduce myself and how to communicate with me.

Target audience: Primarily Harris College faculty.

Should we use SharePoint or something else? People are more familiar with box.

---

# SYSTEM PROMPT

You are a helpful technology consultant with a wealth of experience with designing and implementing intranets and knowledge bases for medium and large organizations, including academic institutions.

---

# User Message

## Context

Brad Cannell, PhD, MPH is an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University (TCU). He is also the Associate Dean for Research (ADR) of Harris College of Nursing and Health Sciences at TCU.

## Associate Dean for Research (ADR) Role and Responsibilities

The Associate Dean for Research (ADR) is responsible for supporting faculty and student research endeavors in the college, facilitating a culture of research and scholarship that promotes interdisciplinary and interprofessional connections, and linking the college programs of research to the greater university research enterprise. The ADR provides support and guidance to academic unit administrators, faculty, and students for developing strong interdisciplinary collaborations and synergistic, coordinated research foci in the college. The ADR advises and supports the Dean, performing additional duties as needed.

### The specific duties of the position include:

- Monitor and assess the research productivity and funding metrics of academic units in the college.

- Assist all units in the College to achieve research and external funding goals.

- Serve as the college liaison to the Office of Research and Sponsored Projects.

- Serve as the college representative for the TCU Graduate Research Committee.

- Lead and work with the Harris College Research Committee to develop, oversee, and assess a strategic plan for research productivity and extramural funding across all academic units and college institutes/centers, ensuring alignment with the college's strategic plan.

- Foster collaborative, interdisciplinary research associations between departments/schools of Harris College and between Harris College and other units at TCU.

- Provide guidance and support for faculty mentorship/development plans (especially junior faculty) focused on growing and sustaining programs of research.

- Monitor and develop the appropriate college infrastructure necessary to support funded programs of research across all academic units.

- Oversee the Associate Dean for Research budget and those programs that the budget supports.

- Organize college-level student research activities, including but not limited to the annual student research symposium, Boller competition, and 3-Minute Thesis competition;
Organize faculty research symposiums.

- Oversee appointment of graduate faculty (research, associate, and clinical) within Health Sciences units of Harris College, in collaboration with the Associate Dean for Health Sciences and the Associate Dean for Nursing & Nurse Anesthesia.

- Teach classes and pursue scholarly endeavors as appropriate.

## Web-based resource

I want to make a web-based resource for the ADR office. The primary purposes of the resource are:

1. Serve as a knowledge base for Harris College faculty. A place where they can find information about all aspects of conducting research at TCU. For example, applying for grants, submitting IRB applications, executing contracts, etc. However, when possible, I should probably provide links to resources (e.g., the IRB page) - supplementing as needed to fill in gaps - rather than write my own resources from scratch. Otherwise, it will be difficult to keep the resources up-to-date.

2. Disseminating information about research at Harris college. For example, funding opportunities, training opportunities, colleuges recent successes.

3. Introduce myself to faculty and how provide information about  how to communicate with me.

## Target audience

The target audience for this resource will primarily be Harris College faculty. Although, there may be some staff and students who use it as well.

## Current technology stack

- We have a Harris College page on the TCU website. There is also a subpage dedicated to research. It currently has very limited information. Additionally, it is visible to the general public and I dont have the ability to directly modify the content of the TCU website. I have to request changes from the website team.

- We have a subscription to Box. It's a great tool for backing up and sharing files and there are existing knowledge bases for other tooics built using Word documents hosted on Box. This approach is simple to spin up and maintain, familiar to Harris Colleg faculty, doesn't require spending any additional money. However, its also clunky and lacks polish, lacks the features of some other potential solutions, and isn't easy to organize or navigate.

- We have a SharePoint site for the ADR office. However, we havent built it out yet. I have experience with using SharePoint to build intranet sites and web-based document libraries for large research projects. These SharePoint sites generally worked well and were fairly feature-rich. However, there is not a tradition of using SharePoint at TCU, and Im not sure how the introduction of another technology will be received, or if people will remember to use it.

## Task

Suggest 2-3 technologies I should use to make a web-based resource for the ADR office.

## Constraints & Formatting

List any important constraints or rules.
- None




# Follow-up: Word vs SharePoint Pages

Option 2 makes sense to me.

- SharePoint = front door + communication layer

- Box = system of record for documents

- TCU website = minimal public-facing presence linking inward

In this system, do you recommend writing the knowledge base/SOPs as Word documents stored in Box or as HTML SharePoint pages?
