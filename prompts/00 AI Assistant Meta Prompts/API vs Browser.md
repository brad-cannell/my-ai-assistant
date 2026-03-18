---
title: Using the API vs the Browser
id: using_api_vs_browser
author: brad_cannell
interface: browser
date: 2026-03-17
date-modified: 2026-03-17
tags:
  - api
  - ai
  - sop
---

# Overview (optional)

-   Conversation about using the API vs the Browser to interact with the AI assistant.
-   I want to reduce the cognitve overhead of deciding when and how to use the API vs the browser.
-   Link to conversation: https://claude.ai/chat/f8e40f6e-0b44-4066-a0d7-d948c6a7054f

# SYSTEM PROMPT

You are a technology consultant with deep expertise in artificial intelligence, large language models (LLMs), and developer-facing AI tooling, including API-based workflows.

------------------------------------------------------------------------

# USER MESSAGE

## My Background & Use Case

I am an epidemiologist, gerontologist, data scientist, and professor at Texas Christian University, and I also operate a small business developing a web-based educational platform.

I regularly use AI assistants to support:

-   Drafting emails, letters, and professional communications

-   Refining grant proposals and academic manuscripts

-   Developing course materials and instructional content

-   Writing and debugging code for data management and analysis (primarily R, Excel, and Google Sheets; occasionally Python, SAS, or Stata)

-   Occasionally generating images or visual assets

I used to interact with AI models almost exclusively through browser-based interfaces. For the past three months, I've been learning to use API calls as well. Now, I use a mix of browser-based interactions and API calls.

Here is my process for API interactions - I have a git repo titled my_ai_assistant. - In the repo I have a "prompts" folder that contains reusable prompts saved in markdown files. - I have a "conversations" folder that contains Quarto documents. The Quarto documents contain a mix of prose and code used to interact with the AI API. - I primarily use Python and the Chatlas package to make API calls. - In many cases, prompts are imported into the Quarto conversations and used in API calls.

## Question Under Consideration

I am actively considering the balance of browser-based interactions and API interactions in my workflow. My motivations for adopting API calls into my workflow included:

### 1. Security & Privacy Concerns

I have read about risks related to browser-based usage, including data exposure via browser extensions and potential collection or resale of chat data by third parties. I wanted to understand whether API-based usage meaningfully changes the security or privacy posture.

### 2. Prompt & Knowledge Management

I frequently reuse prompts (in whole or in part). The browser-based tools I was using did not provide robust systems for storing, organizing, searching, or versioning prompts, nor for linking prompts to responses or downstream artifacts. I was interested in whether API-based workflows would better support:

-   Structured prompt libraries

-   Searchable prompt and response archives

-   Linking prompts, responses, and notes in reproducible documents (e.g., Quarto)

### 3. Professional & Pedagogical Development

As someone who teaches programming and data science, I anticipate a growing need to teach applied AI usage, including APIs, automation, and agent-based systems. Developing fluency with APIs now may be important for future course development.

## Task

Please provide a structured, practical comparison of:

"Interacting with AI assistants via web-based chat interfaces versus direct API calls"

Specifically:

-   "Clearly outline the pros and cons of each approach"

-   "Address security and privacy considerations realistically (not marketing claims)"

-   "Discuss implications for prompt management, reproducibility, and knowledge organization"

-   "Comment on learning curve, tooling overhead, and long-term flexibility"

-   "Conclude with use-case–driven guidance (e.g., when browser-based use is sufficient vs. when API-based workflows are worth the investment)"

## Constraints & Formatting

-   Assume a technically sophisticated but time-constrained academic user, not a software engineer building a commercial SaaS product.

------------------------------------------------------------------------

# Follow-up: Pros and Cons of API vs Browswer

I have liked using the API to interact with Claude. - It has been rewarding to learn a new skill, and I feel like I understand LLM's better now. - I have been able to better automate large chunks of my EWB lesson creation workflow. I have a Quarto document I step through. It includes a mix of file cleaning and formatting code, and ApI calls to LLMs for convent review/creation. - It has been useful to store my conversations in an "ai" folder alongside my EWB lesson files. That folder also includes Markdown transcripts of the conversation with the AI assistant.

However, I have also noticed some downsides to my API call workflow: - It takes longer to use the API than the browser-based interface. Even with template files, changing the metadata, updating file paths, and modifying API calling code takes more time and effort than tying into the browser window. - I miss the projects feature of the browser-based experience. Especially being able to add files for context. When using API calls, the best solution I've been able to come up with so far is to convert relevant files to text (by writing code), and send the text version of those files through the API call with my prompt. - Although I should be able to do a much more robust search of these files in theory. In reality, I haven't yet developed a workflow or tools for doing so. - Separating prompts (markdown files) and conversions (Quarto files) has its advantages. However, it feels like this workflow creates a lot of extra files. And updating the prompt and conversion in separate files can feel tedious. Additionally, it obscures the transaction history. The conversation Quarto document is an excellent record of the file path of the prompt that was loaded and sent to the LLM, but it says nothing about the content of prompt. If the prompt file is overridden, it will have same path but different contents.

I believe that the hybrid approach is probably best, but it also has challenges to consider. 1. I need to develop clear, accessible guidelines for choosing the browser vs the API. I shouldn't be making it up as I go. 2. To minimize time, effort, and friction, I still need to fine-tune my API workflow and tools. 3. If want to look up a chat later, I will need to search at least two place-the browser and my API repo. I would like to figure out a workflow to do so efficiently.

------------------------------------------------------------------------

# Follow-up: File Storage and Context

What about the lack of projects and storing files for context?

For example, in the browser I could create a project for creating EWB lessons. And I could attach formatting guidelines and example CSTs to the project that Claude could use for reference. I haven't figured out a good way to replicate that with my API workflow.

Additionally, let's say that I'm editing lesson 01 in that same browser-based Claude project. During those edits I ask Claude to remember a formatting rule. Then, when I upload lesson 02 and begin to revise it, Claude will usually remember the rule from lesson 01. Again, I haven't figured out a good way to replicate that with my API workflow.

------------------------------------------------------------------------

# Follow-up: Draft an SOP

Please draft an SOP or set of guidelines I can use to help me determine when and how to use the API vs the browser.

------------------------------------------------------------------------

# Follow-up: Refine the SOP

Please remove the following sections:

-   4\. API Workflow: Standard Operating Procedure

-   5\. Search and Retrieval

-   6\. When to Use Two Templates vs. One

I would like to limit this scope of this SOP to deciding to use the API vs the browser. I will write separate SOPs on the workflow to use after that decision has been made.

Additionally, please rewrite section 7, Maintenance, to decision scope only.

------------------------------------------------------------------------

# Follow-up: Tagging Specific Files

How do I attach a version number to the SOP in git? Not a version number for the entire repo, just for the SOP Rmd file.

------------------------------------------------------------------------

I'll use the approach you suggested, combining options 1 and 2. Here is the path and file name for the vignetter we've been working on: '/Users/bradcannell/Desktop/Git/AI/my-ai-assistant/vignettes/API vs Browser.Rmd'. I'm calling version 2.0 because it's a major revision to the previous version.

------------------------------------------------------------------------

# Follow-up: Codex, Claude Code, and chat.app()

I'm steering this conversation back toward `api-vs-browser.qmd` now. This file implicitly assumes that the choice is binary - browser *or* API, and that there is only one type of interaction within those two categories is homogeneous. I don't think either assumptions is correct.

I sometimes use OpenAi's Codex and Anthropic's Claude Code from my IDE (Positron).

Additionally, when interacting with ChatGPT or Claude through the API, I sometimes submit prewritten text through `chat.chat(user_message)` calls, but I sometimes use `chat.app()` to mimic the experience of interacting through the browser in my IDE.

Should we acknowledge this in the SOP? And if so, how deep should we go into it?