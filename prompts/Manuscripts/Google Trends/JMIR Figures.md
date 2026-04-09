---
title: JMIR Formative Research Figure Revisions
author: "Brad Cannell"
created: 2026-04-09
last_updated: 2026-04-09
tags:
  - em
  - publishing
  - r_and_r
  - manuscripts
---

# Overview (optional)

- Working on revisions for JMIR Formative Research.
- Here is the link to the [copyediting webiste](https://jmir.kriyadocs.com/proof_review/?key=18617a50874e76eed7e5d3122e4b7e82:e69e24028eef431d745728b13e090e748bf971c4d9377f2007f83f46c78c1096a4bb0dc0b9d976bf252f38a9ccb5576f9cbb5a75510522b904d03a8c4ca190e73152262e75c2e87b34ccbf6c07f6e5913ed8f266eb70c1c3922b699af4e66f8a84e5cde5abe607a3a0c8fceabbcbd2847c29e6a3ba5eec2a2580e2e05f1669e0de)
- I'm giving the prompt to Claude Code and setting the project scope to: *'/Users/bradcannell/Library/CloudStorage/Box-Box/Manuscripts/Cannell - Google Trends'*

# SYSTEM PROMPT

None

------------------------------------------------------------------------

# USER MESSAGE

## Context

I'm working on some final revisions for a manuscript we are publishing in JMIR Formative Research titled, "Changes in Internet Search Term Popularity in Elder Mistreatment, (2018-2023): Infodemiology Study of Google Trends Data". The manuscript includes two figures, "Figure 1.png" and "Figure 2.png". All files related to the JMIR submission are in the 'JMIR Formative Research' folder.

The copyeditor the following comments for me about the figures:

<figure_1_comments> Please make the following changes to the figure, if applicable, and reupload the figure by clicking the "Replace" button. Use sentence case throughout (eg, revise "Child Abuse" to "Child abuse") </figure_1_comments>

<figure_2_comments> Please make the following changes to the figure, if applicable, and reupload the figure by clicking the "Replace" button. Use sentence case throughout (eg, revise "Elder Abuse" to "Elder abuse") Revise "Aug" to "August," "Dec" to "December," etc Please review the figure for any spelling errors and verify that there are no red underlines in the text before uploading. </figure_2_comments>

Unfortunately, I can't find the R code I used to create these figures. However, I do know that I created them in R, using the ggplot2 package.

Additionally, I'm not 100% which dataset(s) I used to create these figures. However, it looks like there are several potential datasets in the 'archive' folder.

## Task

1.  Please review the data in the 'archive' folder and report which dataset, or datasets, were most likely used to create Figure 1 and Figure 2. If it seems unlikely that Figure 1 and/or Figure 2 weren't built from any of the datasets in the 'archive' folder, please say so.

2.  Please generate the R code needed to recreate the figures, including the revisions requested by the copy editor.

# Revisions: Figure 1

I see some differences between 'Figure 1.png' and 'Figure 1 New.png' that I would like to correct.

1.  The image dimensions are different. Can we make them the same?
2.  In Figure 1, elder abuse is listed first in the legend. In Figure 1 New, child abuse is listed first in the legend.
3.  In Figure 1, child abuse is colored light gray. In Figure 1 New, child abuse is colored black.

Additionally, the month labels on the x-axis of Figure 1 New overlap. We need to fix that.

# Update to Data

I noticed that the data in 'Figure 1.png' and 'Figure 2.png' appeared more granular than that in 'Figure 1 New.png' and 'Figure 2 New.png'. I discovered that 'Figure 1.png' and 'Figure 2.png' were based on weekly data, while 'Figure 1 New.png' and 'Figure 2 New.png' are currently based on monthly data.

I figured out how to download the weekly data again - I had to switch to Google Trends "classic mode". Then, I replaced `fig1_elder_child_2018-2023.csv` and `fig2_elder_domestic_2018-2023.csv` with the new weekly data. However, the formatting of this data is slightly different. Please review it and update `figures.R` accordingly.

# More X-Axis Revisions

This is getting really close. The X-axis labels still overlap and look a little sloppy. What options do we have for further adjusting them?