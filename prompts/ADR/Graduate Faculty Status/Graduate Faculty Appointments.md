---
title: Graduate Faculty Appointments
author: "Brad Cannell"
created: 2026-04-22
last_updated: 2026-04-22
---

# Overview (optional)

- Prompt to help automate the graduate faculty appointments.
- Completed in two steps:
  1. Create a spreadsheet with necessary information (names, dates, etc.).
  2. Create appointment letters based on templates and the information in the spreadsheets.

# SYSTEM PROMPT

You are assisting **Dr. Brad Cannell**, Associate Dean for Research (ADR) at **Harris College of Nursing and Health Sciences, TexasChristian University (TCU)**.

Your job is to help organize **Harris College student research events**, including:

---

# USER MESSAGE

## Context

The Associate Dean for Research (Brad Cannell, PhD) needs to issue appointment letters to ~17 graduate faculty across Harris College. The materials — HC Grad Faculty Appointment Forms, CVs, and recommendation letters — live in department subfolders. Four letter templates exist for four appointment types: Research, Clinical, Associate Research, and Provisional.

The goal is two self-contained prompts the user can paste into Claude Code to run sequentially:
1. **Prompt 1** – Scrape every faculty folder and produce a comprehensive Excel spreadsheet.
2. **Prompt 2** – Read that spreadsheet and generate a filled-in appointment letter (DOCX) for each faculty member.

---

## Directory Map (for reference in prompts)

- **Root:** `/Users/bradcannell/Library/CloudStorage/Box-Box/HC Graduate Faculty - Main/2026 Grad Faculty Appointments to Review/01 Spring 26 submitted by Units for AD4R to Review`
- **Department folders:** `KINE/`, `NRAN/`, `NURS/`, `SOWO/`, `Materials submitted by Interim Dean Ward/` (OTD)
- **Possibly already complete:** `01 New Hires Eff Jan 2026_Complete/` (clarify with user)
- **Templates:** `2026 Letter Templates for AD4R/` (4 DOCX files)
- **Output:** `Completed Letters from AD4R/`

## Template → Appointment Type Mapping (3 types in this batch)

| Template File | Appointment Type |
|---|---|
| `ResearchGraduateFaculty appt ltr 2026.docx` | Research |
| `ClinicalGraduateFaculty Appt Ltr 2026.docx` | Clinical |
| `ProvResearch GraduateFaculty AD Ltr 2026.docx` | Provisional |

*Associate Research template not needed for this batch. January 2026 new hires (folder `01 New Hires Eff Jan 2026_Complete`) are already processed — skip.*

## Template Placeholder → Spreadsheet Column Mapping

| Template placeholder | Spreadsheet column |
|---|---|
| `Name, Credentials` | Full Name + Credentials (e.g., "Jane Smith, PhD, RN") |
| `TCU Dept. name` | Department Full Name |
| `Dr. Last name` | Last Name |
| `DATE` | Start Date |
| `DATE RANGE` | "Start Date – End Date" |
| `(unit head)` / `Unit Head` | Unit Head Name |
| `(term)` (Associate template) | "Start Date – End Date" |
| `Description of standard not met` (Associate template) | Notes / Standards Not Met |

---

## Confirmed Scope
- **Skip** `01 New Hires Eff Jan 2026_Complete` — those letters are already done.
- **Skip** Associate Research template — only Research, Clinical, and Provisional needed.

---

## Prompt 1: Extract Faculty Data into Spreadsheet

```
Use the `anthropic-skills:xlsx` skill to create a comprehensive faculty data spreadsheet.

## Task
Read every HC Grad Faculty Appointment Form PDF (and supplement with CVs where needed) from each department folder listed below. Extract the specified fields for every faculty member and write them all into a new Excel spreadsheet.

## Root Directory
`/Users/bradcannell/Library/CloudStorage/Box-Box/HC Graduate Faculty - Main/2026 Grad Faculty Appointments to Review/01 Spring 26 submitted by Units for AD4R to Review`

## Folders to Search
Search ALL subfolders of the root directory EXCEPT `2026 Letter Templates for AD4R` and `Completed Letters from AD4R`. This includes:
- `KINE/`
- `NRAN/`
- `NURS/`
- `SOWO/`
- `Materials submitted by Interim Dean Ward/` (Occupational Therapy / OTD faculty)

For each subfolder, look for the HC Grad Faculty Appointment Form PDF. Also read the faculty CV (PDF or DOCX) to find credentials (degrees) when not on the form.

## Columns to Extract (one row per faculty member)

| Column | Description | Source |
|--------|-------------|--------|
| Department Code | Abbreviation (KINE, NRAN, NURS, SOWO, OTD) | Folder name |
| Department Full Name | e.g., "Department of Kinesiology" | Appointment form |
| Last Name | Faculty last name | Appointment form |
| First Name | Faculty first name | Appointment form |
| Credentials | Degrees and certifications (e.g., PhD, DNP, RN) | CV or form |
| Full Name with Credentials | "First Last, Credential1, Credential2" | Combine above |
| Appointment Type | One of: Research / Clinical / Associate Research / Provisional | Appointment form (checked box) |
| Start Date | Appointment effective start date (e.g., June 1, 2026) | Appointment form |
| End Date | Appointment end date (e.g., May 31, 2031) | Appointment form |
| Appointment Term String | "June 1, 2026 – May 31, 2031" | Combine start + end |
| Unit Head Name | Name of the department chair/unit head | Appointment form or recommendation letter |
| Notes | Any special circumstances (e.g., "Provisional – tenure year 2027") | Appointment form |

## Output
Save the spreadsheet as:
`[root directory]/2026 Grad Faculty Appointments - Data.xlsx`

Format the spreadsheet with:
- Bold header row
- Column widths auto-fitted to content
- Alternating row shading for readability
- One worksheet named "Appointments"
```

---

## Prompt 2: Generate Appointment Letters

```
Use the `anthropic-skills:docx` skill to generate one appointment letter per faculty member.

## Task
Read the data spreadsheet, then for each faculty member select the correct letter template, fill in all placeholder fields with the faculty's data, and save the completed letter as a DOCX file.

## Root Directory
`/Users/bradcannell/Library/CloudStorage/Box-Box/HC Graduate Faculty - Main/2026 Grad Faculty Appointments to Review/01 Spring 26 submitted by Units for AD4R to Review`

## Input Spreadsheet
`[root directory]/2026 Grad Faculty Appointments - Data.xlsx`
(Created in Stage 1 — read every row of the "Appointments" worksheet.)

## Template Files (in `[root directory]/2026 Letter Templates for AD4R/`)
Select the template based on the "Appointment Type" column:
- **Research** → `ResearchGraduateFaculty appt ltr 2026.docx`
- **Clinical** → `ClinicalGraduateFaculty Appt Ltr 2026.docx`
- **Provisional** → `ProvResearch GraduateFaculty AD Ltr 2026.docx`

## Placeholder Replacements
Replace every placeholder with the faculty's data:

| Placeholder in template | Replace with |
|-------------------------|-------------|
| `Name, Credentials` | Full Name with Credentials column |
| `TCU Dept. name` or `TCU Dept name` or `TCU Dept` | Department Full Name column |
| `Dr. Last name` or `Dr. Last Name` | `Dr. [Last Name]` |
| `DATE` (first occurrence, or standalone) | Start Date column |
| `DATE RANGE` | Appointment Term String column |
| `(unit head)` or `Unit Head` or `Unit head` | Unit Head Name column |

For the Provisional template, the date appears in the pattern "June 1, DATE – May 31, DATE" — replace each `DATE` with the correct year from the Start Date and End Date columns respectively.

## Output
Save each letter as a DOCX file in:
`[root directory]/Completed Letters from AD4R/`

Naming convention: `[LastName]_[FirstName]_GradFaculty_Appt_Ltr.docx`
Example: `Porter_Ryan_GradFaculty_Appt_Ltr.docx`

After generating all letters, print a summary table confirming:
- Faculty name
- Appointment type
- Template used
- Output filename
- Any errors or fields that could not be filled
```

---

## Verification

After running both prompts:
1. Open 2–3 completed letters and confirm all placeholders are replaced (no leftover `DATE`, `Name, Credentials`, etc.)
2. Verify the cc line in each letter includes the correct unit head name
3. Check that Provisional letters have years (not the word "DATE") in the term line
4. Confirm all 17 faculty have a letter in `Completed Letters from AD4R/`