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

🔴 When the opportunity arises, here are some QR details to think through:

- How large should they be, and how should we attach them?

- Should they have the expected judges' names printed on them as well?

- How should we inform judges which posters they need to judge? We will send them an email, but should we also have a form available to review on the day of?

- What happens if they mess up or need to revise a score?

Ask Claude to create instructions that I can email out to judges.

Ask Claude to summarize all of this into a guide I can use when I have to repeat this process next year.