---
title: Graduate Faculty Appointments
author: "Brad Cannell"
created: 2026-04-22
last_updated: 2026-04-22
---

# Overview (optional)

- Prompt to help automate the graduate faculty appointments.
- Complements: https://app.clickup.com/8446862/v/dc/81rwe-4031/81rwe-24891
- Completed in two steps:
  1. Create a spreadsheet with necessary information (names, dates, etc.).
  2. Create appointment letters based on templates and the information in the spreadsheets.

# SYSTEM PROMPT

You are assisting **Dr. Brad Cannell**, Associate Dean for Research (ADR) at **Harris College of Nursing and Health Sciences, TexasChristian University (TCU)**.

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

## Task
Read every HC Grad Faculty Appointment Form PDF (supplemented by CVs and recommendation letters) from each department subfolder and extract faculty appointment data into a new Excel spreadsheet.

## Root Directory
[PASTE THE FULL PATH TO THE SEMESTER WORKING FOLDER HERE]
Example: /Users/bradcannell/Library/CloudStorage/Box-Box/HC Graduate Faculty - Main/2026 Grad Faculty Appointments to Review/01 Spring 26 submitted by Units for AD4R to Review

## Folders to Search
Search ALL subfolders of the root directory EXCEPT:
- `[Year] Letter Templates for AD4R`
- `Completed Letters from AD4R`
- Any subfolder named `New Hires` or containing `_Complete` in the name (those letters are already done)

Typical department folders: KINE, NRAN, NURS, SOWO, and a folder for materials submitted by the Interim Dean (which contains OTD faculty and any department chairs being nominated).

For each faculty member, read their HC Grad Faculty Appointment Form PDF first. If credentials (degrees, certifications) are missing or unclear on the form, read the CV.

## Columns to Extract (one row per faculty member)

| Column | Description | Source |
|---|---|---|
| Department Code | Abbreviation (KINE, NRAN, NURS, SOWO, OTD, etc.) | Folder name |
| Department Full Name | Full department name (e.g., "Kinesiology", "Nursing") | Appointment form |
| Last Name | Faculty last name | Appointment form / CV |
| First Name | Faculty first name (complete — not just initials) | Appointment form / CV |
| Credentials | All degrees and certifications in CV order (e.g., PhD, RN; DNP, CRNA, FAAN) | CV preferred, form as fallback |
| Full Name with Credentials | "First Last, Credential1, Credential2" | Combined |
| Appointment Type | Research / Clinical / Associate Research / Provisional — based on checked box | Appointment form |
| Start Date | Effective start date written out (e.g., "June 1, 2026") | Appointment form |
| End Date | Appointment end date written out (e.g., "May 31, 2031") | Appointment form |
| Appointment Term String | "June 1, 2026 – May 31, 2031" | Combined |
| Unit Head Name | Name + credentials of the department chair / unit head | Appointment form or recommendation letter |
| Notes | Special circumstances (e.g., Provisional end year, unit head is the nominee) | Appointment form |

## Important Rules
- If a faculty member IS the department chair, the nomination will have been signed by Interim Dean Ward. Use Ward as the Unit Head.
- Provisional appointment end dates vary — use the date on the form exactly; do not default to 5 years.
- Use the CV as the authoritative source for credentials and their order.
- Do NOT include faculty from any folder that contains "Complete" in its name.

## Output
Save the spreadsheet as:
`[root directory]/[Year] Grad Faculty Appointments - Data.xlsx`

Format:
- Worksheet named "Appointments"
- Bold, dark-background header row with white text
- Alternating row shading for readability
- Column widths fitted to content
- Arial font throughout

---

## Prompt 2: Generate Appointment Letters

## Task
Read the faculty data spreadsheet, then generate one filled-in DOCX appointment letter per faculty member using the correct template.

## Root Directory
[PASTE THE SAME PATH AS STAGE 1]

## Input Spreadsheet
`[root directory]/[Year] Grad Faculty Appointments - Data.xlsx`
Read every row from the "Appointments" worksheet.

## Template Files
Templates are in: `[root directory]/[Year] Letter Templates for AD4R/`

Select the template based on the "Appointment Type" column:
- Research → `ResearchGraduateFaculty appt ltr [Year].docx`
- Clinical → `ClinicalGraduateFaculty Appt Ltr [Year].docx`
- Provisional → `ProvResearch GraduateFaculty AD Ltr [Year].docx`
- Associate Research → `AssocResearchGraduateFaculty appt ltr [Year].docx` (rarely used)

## Placeholder Replacements
For each faculty member, replace all highlighted placeholder text in the template:

| Placeholder | Replace with |
|---|---|
| `Name, Credentials` | Full Name with Credentials (e.g., "Susan Fife, DNP, RN") |
| `TCU Dept. name` / `TCU Dept name` / `TCU Dept` | Department Full Name |
| `Last name` / `Last Name` | Faculty last name only |
| `DATE` (first occurrence, in "effective DATE") | Start Date |
| `DATE RANGE` | Appointment Term String |
| `(unit head)` / `unit head` / `Unit Head` / `Unit head` | Unit Head Name (with credentials) |

**Provisional template special case:** The body contains "June 1, DATE - May 31, DATE". Replace this entire phrase with the Appointment Term String from the spreadsheet (which handles cases where the start month is not June).

## Technical Approach
- Use python-docx to load each template
- For each paragraph, concatenate all run texts, apply replacements, write result back to the first run, and clear subsequent runs
- Remove yellow highlight formatting from replaced runs
- Apply replacements in order from most specific to most general (e.g., "DATE RANGE" before "DATE", "Last name," before "Last name")

## Output
Save each letter to: `[root directory]/Completed Letters from AD4R/`
Filename: `[LastName]_[FirstName]_GradFaculty_Appt_Ltr.docx`
(Replace spaces in multi-word first names with underscores)

## Verification
After generating all letters:
1. Report a summary table: Faculty name | Appointment type | Template used | Output filename | Any issues
2. Flag any paragraph where a known placeholder string was NOT replaced
3. Confirm the total count matches the number of rows in the spreadsheet

---

## Verification

After running both prompts:
1. Open 2–3 completed letters and confirm all placeholders are replaced (no leftover `DATE`, `Name, Credentials`, etc.)
2. Verify the cc line in each letter includes the correct unit head name
3. Check that Provisional letters have years (not the word "DATE") in the term line
4. Confirm all 17 faculty have a letter in `Completed Letters from AD4R/`