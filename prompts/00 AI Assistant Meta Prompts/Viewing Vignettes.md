---
title: Viewing Vignettes
id: viewing_vignettes
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

-   I'm trying to figure out the best way to view vignettes.
-   Link to conversation: https://claude.ai/chat/9d00e530-b6e0-4f24-8923-97270e6a3f97

# SYSTEM PROMPT

You are a technology consultant with deep expertise in artificial intelligence, large language models (LLMs), and developer-facing AI tooling, including API-based workflows.

------------------------------------------------------------------------

# USER MESSAGE

## Context

-   I have a code repository named `my-ai-assistant` that contains snippets, prompts, conversation templates, and R/Python helper functions for interacting with ChatGPT and Claude, including through the API.
-   That repository also has a folder named `vignettes` where I store vignettes containing example code and guidelines.
-   I borrowed the vignettes idea from R packages, which I've created in the past.
-   In an R Package setting, I can view the rendered vignette in my IDE (Positron or RStudio) using `vignette("vignette-name", package = "packagename")`.
-   I can also view a rendered version of vignettes on the web with the help of R's `pkgdown` package and GitHub Pages.
-   I would like to adopt a similar framework for my `my-ai-assistant repo`. However:
    -   This repo isn't an R package. I believe R's `pkgdown` package only works with R package repos.
    -   This repo contains both R and Python code. So, a R-specific solution my not be best.
-   Of course, I can just open the markdown files and read them, but ideally, I'd like an easy way to view the rendered vignettes in Positron's Viewer pane and/or my web browser.

## Task

Please suggest a workflow for writing, maintaining, a viewing my vignettes.

---

# Follow-up: Issues

This is a great start. However, I'm running into some issues.

1. Not all of my vignettes are currently Quarto documents. Some are R Markdown documents. I've attached an example. I'm assuming I will need to convert all R Markdown documents to Quarto documents. 

2. When I convert to Quarto, what are the key elements that need to be included in the YAML header?

3. The vast majority of the files in my repo are not files that I want rendered for the website. I pretty much only want to render the files in the vignettes folder. However, when I submit quarto preview , Quarto tries to render every Quarto document in the repo. How do I modify that behavior?

4. "Vignettes" is a term borrowed from R packages. Does it still make sense to use it in this context?

5. Should we go ahead and adopt a file naming sytle early in this process?

Here is the current contents of my vignettes folder:
```
└── 📁 vignettes
    ├── 📄 API vs Browser.Rmd
    ├── 📄 git-tags.Rmd
    ├── 📄 Prompt Format.Rmd
    ├── 📄 Python and Chatlas.qmd
    ├── 📄 Snippets.qmd
    ├── 📄 UV Virtual Environments.qmd
    └── 📄 Virtual Environments.qmd 
```

---

# Follow-up: Update vignette files

Please review this document, including its YAML header.
--- 

# Follow-up: Vignette Template

Great! I think all of the existing vignettes are "good enough" for now. As a next step, will you please create a vignette template I can use when creating vignettes in the future?

--- 

# Follow-up: Testing

Now that we have revised and normailzed the vignettes, please walk me through testing the process for viewing vignettes (where the conversation started) to make sure it works as expected.

---

When I run `quarto preview​`, this is what appears in the terminal:

```
Preparing to preview
[1/3] vignettes/uv-virtual-environments.qmd
[2/3] vignettes/venv-virtual-environments.qmd
[3/3] index.qmd

Watching files for changes
Browse at http://localhost:3667/vignettes/uv-virtual-environments.html
GET: /vignettes/uv-virtual-environments.html
```

And the browser opens up to a rendered version of `uv-virtual-environments.qmd`.

I was expecting all of the Quarto documents to be rendered, and for the browser to open up to the rendered version of `index.qmd`.

---

This is the contents of my `_quarto.yml` file:

```
project:
  type: website
  output-dir: _site
  render:
    - index.qmd
    - vignettes/*.qmd

website:
  title: "My AI Assistant"
  # navbar:
  #   left:
  #     - href: index.qmd
  #       text: Home
  #     - href: vignettes/index.qmd
  #       text: Vignettes

format:
  html:
    theme:
      - cosmo
      - brand
    css: styles.css
    toc: true
    code-fold: true       # great for prompt/snippet repos
    code-tools: true


execute:
  eval: false
  echo: true
```

When I run `ls vignettes/`, this is the result I get:

```
_vignette-template.qmd          git-tags.qmd                    python-and-chatlas.qmd          uv-virtual-environments.qmd
api-vs-browser.qmd              prompt-format.qmd               snippets.qmd                    venv-virtual-environments.qmd
```

---

`quarto preview index.qmd` returned the expected result. Thank you!

I would like to make a change to the structure of the website. Is it possible for `index.qmd` to provide a brief introduction to the repo, and can this be labled "Home" in the nav bar?

Additionaly, should we create a separate page with the links to the rendered vignettes or should we keep them in `index.qmd` below the introduction?

--- 

# Follow-up: Publishing

Thank you! I think we have a solid first version of the solution here. How do I make this "live" online? Additionally, I'm not currently working on the main branch.

--- 

# Follow-up: SOP

It appears to be working now! 

Please write a brief new vignette that summarizes:
1. The purpose of vignettes.
2. Our rationale for the workflow we chose.
3. Instructions for writing, maintaining, and viewing vignettes.

---

Do I need to run quarto preview or quarto render before committing and pushing the new vignettes?