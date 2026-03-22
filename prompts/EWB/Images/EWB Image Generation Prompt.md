---
title: Generate EWB Brand-Aligned Image
id: generate_ewb_image
task: image_generation
audience: internal
interface: browser
author: "Brad Cannell"
created: 2026-03-22
last_updated: 2026-03-22
<!-- updated: added optional ideation section (Step 0) for starting from raw lesson text -->
project: null
domain: visual_design
tags:
  - image_generation
  - branding
  - ewb
  - dall_e
  - gemini
---

<!--
YAML HEADER NOTES

- task: image_generation (not text_revision or code_review — this template produces images, not text)
- interface: browser (DALL·E via ChatGPT or Google Gemini browser interface)
- This template is NOT passed to the AI. You fill it out, then manually compose the final
  image prompt using the assembled fields below.
- There is no system prompt section in this template. Image generation models (DALL·E, Gemini
  Imagen) receive a single natural language prompt — not a role + instruction structure like
  language models do. The "prompt" IS the full instruction.
- Color hex codes (#4E5F72) are not understood by image models. The EWB Brand Block below
  translates each hex value into descriptive color language the model can use.
-->

---

# Overview

Use this template when creating conceptual or explanatory illustrations for Epi-Workbench (EWB) course content, lesson headers, or supporting visuals. The goal is to produce images that are on-brand, visually consistent, and appropriate for a professional educational platform serving public health researchers and practitioners.

This template is designed for two tools:
- **DALL·E 3** — via ChatGPT (browser or API)
- **Google Gemini Imagen** — via Gemini browser interface

Both tools accept a single natural language prompt. After filling in the sections below, assemble them into the **Final Prompt** at the bottom.

---

# PROMPT TEMPLATE

## Step 0. Ideation (optional — use when you don't have a specific visual in mind)

> **When to use this step:** You have a paragraph of lesson text and want the AI to suggest visualization concepts before you commit to a specific image. Skip this step entirely if you already know what you want to depict and go straight to Section 1.
>
> **How to use:** Paste your lesson text into the field below, then submit *only this section* to a language model (ChatGPT, Claude, Gemini, etc.) using the prompt that follows. Review the suggestions, pick one, and use it to fill in Section 1 before proceeding with the rest of the template.
>
> Note: This step goes to a **language model**, not an image model. You're asking for ideas in plain text, not generating an image yet.

**Lesson text to visualize:**
{{lesson_text}}

---

**Ideation prompt** (copy this and submit it along with your lesson text above):

```
I'm creating an explanatory illustration for a lesson on an educational platform focused on epidemiology and public health (Epi-Workbench). The platform serves graduate students, researchers, and public health professionals.

Here is the lesson text:

[paste lesson text here]

Please suggest 2–3 distinct visual concepts that could help illustrate the core idea in this text. For each concept, describe:
1. What the image would depict (specific objects, people, settings, relationships)
2. What visual style would suit it best (e.g., flat design diagram, isometric illustration, semi-realistic illustration)
3. Why this concept would help a learner understand the material

Keep suggestions concrete and specific enough that I could hand them directly to an image generation tool like DALL·E or Gemini. Do not generate the image — just describe the concepts.
```

**AI's suggested concepts** (paste response here for your records):
{{ideation_response}}

**Selected concept** (carry this forward into Section 1 below):
{{selected_concept}}

---

## 1. Subject

> What is depicted in the image? Be specific. Name the objects, people, setting, and any actions or relationships between elements.
>
> Good: "A researcher seated at a desk reviewing a data dashboard on a laptop, with a chart visible on the screen"
>
> Avoid: "A person doing data science" (too vague for the model to render usefully)

**Subject:**
{{subject}}

---

## 2. Concept Being Illustrated (optional)

> What epidemiological, statistical, or public health concept does this image support? This helps you stay intentional about what the visual should communicate, even if the concept itself doesn't appear literally in the image.
>
> Example: "Selection bias," "Dose-response relationship," "Surveillance data pipeline"

**Concept:**
{{concept}}

---

## 3. Visual Style

> Choose the style that best fits the use case. Pick one and add any modifiers.

- [ ] **Flat design illustration** — clean, minimal, 2D. Good for diagrams and concepts.
- [ ] **Isometric illustration** — 3D-looking, geometric. Good for systems/workflows.
- [ ] **Semi-realistic digital illustration** — detailed but not photographic. Good for people/settings.
- [ ] **Minimalist icon / graphic** — simple, single-concept visuals.
- [ ] Other: {{style_other}}

**Style modifiers** (optional — e.g., "soft shadows," "outlined shapes," "geometric"):
{{style_modifiers}}

---

## 4. Mood & Atmosphere

> What feeling should the image convey?

- [ ] Professional and trustworthy
- [ ] Approachable and encouraging
- [ ] Clean and academic
- [ ] Energetic and modern
- [ ] Other: {{mood_other}}

---

## 5. Composition & Aspect Ratio

> How should the image be framed and sized?

**Intended use:**
- [ ] Inline lesson illustration (square or landscape, ~1:1 or 4:3)
- [ ] Lesson or chapter header banner (wide landscape, 16:9 or 3:1)
- [ ] Course card thumbnail (landscape, ~16:9)
- [ ] Other: {{use_other}}

**Aspect ratio:**
{{aspect_ratio}}

**Composition notes** (e.g., "subject centered," "leave left side open for text overlay"):
{{composition_notes}}

---

## 6. EWB Brand Block

> Copy this block verbatim into every EWB image prompt. It encodes the brand palette and visual identity in language image models can interpret. Do not change this block unless the brand evolves.

```
Color palette: deep steel blue (primary backgrounds and UI elements), bright golden yellow (accents and highlights), medium green (positive states and secondary elements), medium gray (text and borders), and warm orange (warnings and accent details). Use these colors intentionally; avoid introducing colors not in this palette. The overall aesthetic should feel modern, clean, and professional — consistent with a research-focused educational platform in public health and epidemiology. Avoid stock-photo clichés, generic "corporate" imagery, and overly cartoonish styles.
```

---

## 7. Exclusions (Negative Constraints)

> List anything the image should NOT contain. Both DALL·E and Gemini respond well to explicit exclusions. Add to or remove from the defaults as needed.

Default exclusions (keep unless you have a reason to remove):
- No embedded text, labels, or captions
- No watermarks or signatures
- No people of indeterminate or unrealistic anatomy
- No stock photo aesthetic
- No clashing colors outside the EWB palette

Additional exclusions for this image:
{{additional_exclusions}}

---

## 8. Iteration Notes

> Use this section to track what you tried and what worked. Useful for refining the prompt across multiple generations.

| Version | Key change from prior | Result / Notes |
|---------|----------------------|----------------|
| v1      | Initial prompt       |                |
| v2      |                      |                |
| v3      |                      |                |

---

# FINAL PROMPT

> Assemble the sections above into a single paragraph of natural language. The structure below is a reliable ordering for both DALL·E and Gemini. Replace all {{placeholders}} with your filled-in content before submitting.
>
> **Tip:** Write the final prompt as a description of the finished image, not as an instruction ("A flat design illustration of..." not "Create a flat design illustration of..."). Both tools respond similarly to either framing, but descriptive language tends to produce more compositionally grounded results.

---

**Template:**

A {{style}} illustration of {{subject}}. The mood is {{mood}}. Aspect ratio {{aspect_ratio}}; {{composition_notes}}. Color palette: deep steel blue (primary backgrounds and UI elements), bright golden yellow (accents and highlights), medium green (positive states and secondary elements), medium gray (text and borders), and warm orange (warnings and accent details). Use these colors intentionally; avoid introducing colors not in this palette. The overall aesthetic should feel modern, clean, and professional — consistent with a research-focused educational platform in public health and epidemiology. Avoid stock-photo clichés, generic "corporate" imagery, and overly cartoonish styles. No embedded text, labels, or captions. No watermarks. {{additional_exclusions}}.

---

**Your assembled prompt:**

{{paste_final_prompt_here}}
