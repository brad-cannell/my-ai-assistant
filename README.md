---
author: "Brad Cannell"
date: "2025-12-22"
updated: "2026-03-17"
---

# My AI Assistant

`my-ai-assistant` is a personal knowledge and workflow repository built around API-based interactions with LLMs like Claude and ChatGPT. At its core, the repo organizes reusable **prompt templates** (stored as Markdown files in `prompts/`) and **conversation workflows** (Quarto documents in `conversations/`), with Python and the [Chatlas](https://posit-dev.github.io/chatlas/) package powering most API calls.

Beyond prompting, the repo includes a lightweight documentation site — using Quarto to render a set of **vignettes** that capture SOPs, guidelines, and worked examples for AI-assisted workflows.

**Published site:** <https://brad-cannell.github.io/my-ai-assistant/>

---

## Repository Structure

```
my-ai-assistant/
  conversations/    # Quarto (.qmd) conversation workflows
  prompts/          # Reusable prompt templates (Markdown with YAML headers)
  snippets/         # Reusable context chunks (descriptive text, not prompts)
  vignettes/        # Documentation site source (published to GitHub Pages)
  _quarto.yml       # Quarto site configuration
  pyproject.toml    # Python dependencies (managed with uv)
```

---

## API Keys

API keys are stored in the system keyring — never in git. See the [Keyring vignette](https://brad-cannell.github.io/my-ai-assistant/vignettes/keyring.html) for setup instructions.

---

## Documentation

All workflow documentation lives in the published vignettes:

- [Python and Chatlas](https://brad-cannell.github.io/my-ai-assistant/vignettes/python-and-chatlas.html) — getting started with API calls
- [Keyring](https://brad-cannell.github.io/my-ai-assistant/vignettes/keyring.html) — storing and retrieving API keys
- [System Prompts](https://brad-cannell.github.io/my-ai-assistant/vignettes/system-prompts.html) — when and how to use system prompts
- [Saving and Resuming Chats](https://brad-cannell.github.io/my-ai-assistant/vignettes/save-and-resume-chats.html) — pickle and markdown export strategy
- [Prompt Format](https://brad-cannell.github.io/my-ai-assistant/vignettes/prompt-format.html) — YAML header conventions for prompts
- [uv Virtual Environments](https://brad-cannell.github.io/my-ai-assistant/vignettes/uv-virtual-environments.html) — Python dependency management
