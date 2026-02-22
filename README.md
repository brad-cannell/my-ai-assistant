---
author: "Brad Cannell"
date: "2025-12-22"
updated: "2026-01-28"
---

# AI Assistant

This project is for interacting with AI assistants via their respective APIs. 

- Don't feel like you need to use the API for everything. You don't! 
- Use the browser when it makes sense to do so.
- A don't be afraid to use chat.app() for quick iteration.

## Help

- For help with using Python and Chatlas, see: `vignettes/Python and Chatlas.qmd`

-----

## Python Environment Setup (using uv)

This project uses **uv** for dependency management and virtual environments.

Do **not** commit or sync the `.venv/` directory. The environment is created locally on each machine.

### First-time setup on a new computer

```bash
brew install uv          # install uv (macOS)
uv venv                  # create the local virtual environment
uv sync                  # install dependencies from uv.lock
```

VS Code users should select the interpreter at `.venv/bin/python`.

All dependencies and versions are defined in `pyproject.toml` and `uv.lock`.

For details see `vignettes/UV Virtual Environments.qmd`.

-----

# Get and Set API Keys
API Keys (Using the keyring package)
- ChatGPT: keyring::key_get("bradGPT")
- Gemini: keyring::key_get("test-gemini-brad")
- Claude: keyring::key_get("test-claude-brad")

## Price

| Company   |   Model  | Input Price (per M) | Output Price (per M) |
|-----------|:--------:|:-------------------:|:--------------------:|
| OpenAI    |    5.2   |        $1.75        |        $14.00        |
| OpenAI    | 5.2-mini |        $0.18        |         $2.00        |
| Google    |  Gemini  |  Free (no privacy)  |   Free (no privacy)  |
| Anthropic | Opus 4.6 |        $5.00        |        $25.00        |
| Anthropic | Opus 4.5 |        $5.00        |        $25.00        |

-----

# Structure
AI Assistant/
  conversations/
  Project - .../
  prompts/
  scripts/
  snippets/
  vignettes/
  .gitignore
  AI Assistant.Rpoj
  README.md
  README.Rmd
  
## Conversations
This folder contains saved conversations with AI assistants.

## Projects
Conversations, prompts, scripts, and snippets about a single topic or project can be grouped into project folders. All project folder names should begin with `Project -`

## Prompts
This folder contains saved prompts. Including:
- One-off prompts used in the AI browser interface.
- Prompts templates and prompts that will be reused.
- One-off prompts passed in an API call should not be saved in this folder. They are already recorded in the conversation file.

## Scripts
Scripts are for helper functions and utility scripts.

## Snippets
Snippets aren't prompts - there is no request made of the AI assistant - they are reusable chunks of text, typically used for context in a prompt. For example, "About EWB".

## Vignettes
This folder contains user documentation written in the style of R Package vignettes in case we ever want to turn this into a package.
  
-----

# Prompt Template

## YAML Header Instructions

Complete the YAML header for every saved prompt. These fields support organization, reuse, and future search, but should remain lightweight and human-readable.

FIELD DESCRIPTIONS
- title: A brief, human-readable description of what the prompt does. Written in Title Case.
- id: Use a short, stable, human-readable identifier in lowercase snake_case.
- task: The primary type of work the prompt performs (e.g., text_revision, code_review). Written in snake_case.
- audience: The intended audience for the output (e.g., academic, student, developer). Written in snake_case.
- interface: Interface used to interact with AI assistant (api, browser, both). Written in snake_case.
- author: Name of the prompt author. Written in snake_case.
- created: Date the prompt was first created (YYYY-MM-DD).
- last_updated: Date of the most recent substantive revision (YYYY-MM-DD).
- project: Associated project, course, or initiative, or null if broadly reusable. Written in snake_case.
- domain: Subject area or disciplinary context (e.g., epidemiology, data_science, general). Written in snake_case.
- tags: Optional keywords to support browsing and future search. Written in snake_case.

ID GUIDELINES
- id: Use a short, stable, human-readable identifier in lowercase snake_case.
- Base the id on the prompt’s core purpose using a verb–object pattern
  (e.g., rewrite_academic_tone, review_r_code_style).
- Avoid dates, version numbers, model names, project names, or author names.
- Treat the id as permanent; change it only if the prompt’s fundamental purpose changes.

Avoid including model names or API parameters in the YAML header.

-----

# Conversation Template

## YAML Header Instructions

Complete the YAML header for every saved prompt. These fields support organization, reuse, and future search, but should remain lightweight and human-readable.

FIELD DESCRIPTIONS
- title: A brief, human-readable description of what the prompt does. Written in Title Case.
- id: Use a short, stable, human-readable identifier in lowercase snake_case.
- task: The primary type of work the prompt performs (e.g., text_revision, code_review). Written in snake_case.
- audience: The intended audience for the output (e.g., academic, student, developer). Written in snake_case.
- author: Name of the prompt author. Written in snake_case.
- created: Date the prompt was first created (YYYY-MM-DD).
- last_updated: Date of the most recent substantive revision (YYYY-MM-DD).
- project: Associated project, course, or initiative, or null if broadly reusable. Written in snake_case.
- domain: Subject area or disciplinary context (e.g., epidemiology, data_science, general). Written in snake_case.
- tags: Optional keywords to support browsing and future search. Written in snake_case.

ID GUIDELINES
- id: Use a short, stable, human-readable identifier in lowercase snake_case.
- Base the id on the prompt’s core purpose using a verb–object pattern
  (e.g., rewrite_academic_tone, review_r_code_style).
- Avoid dates, version numbers, model names, project names, or author names.
- Treat the id as permanent; change it only if the prompt’s fundamental purpose changes.

Avoid including model names or API parameters in the YAML header.
  
-----

