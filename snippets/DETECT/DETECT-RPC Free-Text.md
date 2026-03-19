---
title: "About the DETECT-RPC Free-Text Project"
author: "Brad Cannell"
date: "2026-03-19"
date-modified: "2026-03-19"
tags: ["DETECT-RPC", "Research", "Analysis"]
---

<context_purpose>
This document provides structured background information about the DETECT-RPC free-text analysis for use by AI assistants. It is intended to support accurate summarization, grant writing, manuscript drafting, presentation development, and question answering about the analysis.
</context_purpose>

<relationship_to_parent_study>
This document is intended to complement, not replace, the main "About DETECT-RPC" document. It focuses specifically on the free-text analysis component of the broader DETECT-RPC project and does not repeat general study background already described elsewhere.
</relationship_to_parent_study>

<tl_dr>
This project analyzes free-text responses from the DETECT-RPC screening tool to develop a reliable categorization system. Human-labeled data will be used to train and refine a large language model to automatically classify future responses. The purpose of classifying the free-text responses is two-fold: (1) to identify patterns in the responses, and (2) to uncover opportunities to improve DETECT-RPC.
</tl_dr>

<key_definitions>
- EM: Elder mistreatment, including abuse, neglect, and exploitation
- HBPC: Home-based primary care
- DETECT-RPC: Adapted program for HBPC clinicians
- SBMI: The McWilliams School of Biomedical Informatics, one of the six schools of UTHealth Houston
</key_definitions>

<background>
- Clinicians have the option to enter free-text responses into seven open-ended fields when completing the DETECT-RPC tool.
- At present, these responses are not being systematically categorized or analyzed.
- A key early step is to assign meaningful category labels to the free-text responses so that patterns and trends can be examined.
- Our colleagues at the School of Biomedical Informatics (SBMI) have already used a large language model (LLM) to generate preliminary category labels.
</background>

<analysis_objective>
The objective of this project is to develop a reliable and scalable system for categorizing free-text responses from the DETECT-RPC tool, enabling quantitative analysis of clinician observations and improving decision support models.
</analysis_objective>

<analysis_goals>
- Develop a reliable and reproducible set of category labels for free-text responses.
- Enable quantitative analysis of previously unstructured data.
- Improve the performance of LLM-based classification models for ongoing data collection.
- Identify patterns and trends in clinician-reported indicators of elder mistreatment.
- Inform future refinement of DETECT-RPC.
</analysis_goals>

<unit_of_analysis>
The primary unit of analysis is an individual free-text response entered by a clinician into one of seven open-ended fields within the DETECT-RPC tool during a patient encounter.
</unit_of_analysis>

<labeling_framework>
Free-text responses will be assigned to one or more predefined categories representing types of observations, concerns, or contextual factors related to elder mistreatment. The labeling framework will be iteratively refined through human consensus and model feedback.
</labeling_framework>

<field_types>
The seven free-text fields serve different functions within the DETECT-RPC tool. Broadly, they capture:
- reasons for inability to assess part of the situation,
- explanations for discordance between observed indicators and clinician suspicion of EM,
- reasons for not intending to report suspected EM to APS, and
- descriptions of referrals to services other than APS.

These field types may differ in content, purpose, and labeling needs.
</field_types>

<detect_rpc_tool_structure>
1. Indicators of Abuse Module
    - Response options include: "Yes", "No", "Unable to assess"
    - Indicator group: Environment
        - Stem: "Environmental red flags are present including:"
        - Item 1: "Absence of necessities (e.g., inadequate food in cabinets and/or fridge, utilities not functioning)"
        - Item 2: "Living environment that poses a health or safety concern for the patient or first responders (e.g., fire hazards or obstructed/inaccessible exits, insect or rodent infestation, urine or feces present in the environment.)"
    - Indicator group: Caregiver Appearance and Interaction
        - Stem: "If caregiver present, they:"
        - Item 3: "Appear defensive or argumentative, talk over the patient, or resistant to education in a way that negatively impacts the patient's care"
            - If "Unable to assess" selected:
                - Stem: "Reason caregiver was not assessed."
                - Response options: "Caregiver not present", "Other reason"
    - Indicator group: Patient
        - Stem: "Patient appears:"
        - Item 4: "To be chemically sedated."
        - Item 5: "To be isolated in the home and/or cut off from needed social networks or supports."
        - Item 6: "Anxious, emotionally distressed, or depressed because of the quality of care they are receiving and/or their relationship with their caregiver."
        - Item 7: "To be prohibited from freely moving about the home (e.g., confined to one room, no access to walker or wheelchair, inappropriate locks on doors)."
        - Item 8: "To have unmet needs for assistance with eating, toileting, transferring, dressing, or bathing that are not related to the patient's wishes/refusals of assistance."
        - Item 9: "To have injuries that cannot be adequately explained."

2. EM Status Impression
    - Item 10: "Do you suspect that the patient is experiencing elder mistreatment?"
        - Response options include: "Yes", "No"

3. EM Types
    - Item 11: "What type(s) of mistreatment do you suspect the patient might be experiencing? Click the link below if you would like to review definitions for the listed elder mistreatment types:"
        - Response options include (may select multiple):
            - "Self-neglect"
            - "Financial exploitation"
            - "Emotional or psychological abuse"
            - "Physical abuse"
            - "Sexual abuse"
            - "Caregiver neglect"
            - "Abandonment"
            - "Other"
            - "Don't know/Not sure"

4. Response
    - Item 12: "Do you intend to report your suspicion of elder mistreatment to APS?"
        - Response options include: "Yes", "No"
    - Item 13: "Will you refer the patient and/or caregiver to services other than APS?"
        - Response options include: "Yes", "No"
</detect_rpc_tool_structure>

<free_text_boxes>
Free-text boxes are not visible by default. This section describes the conditions that cause them to become visible.

1. Indicators of Abuse Module
    - Indicator group: Environment
        - Free-text box label 1: ri_environment_un_reason
            - Visibility condition: "Unable to assess" selected for any item in this group
            - Free-text box prompt: "Specify reason for inability to assess the environment."
    - Indicator group: Caregiver Appearance and Interaction
        - Free-text box label 2: ri_caregiver_oth
            - Visibility condition: "Unable to assess" and "Other reason" selected for the item in this group
            - Free-text box prompt: "Reason caregiver was not assessed."
    - Indicator group: Patient
        - Free-text box label 3: ri_patient_assess
            - Visibility condition: "Unable to assess" selected for any item in this group
            - Free-text box prompt: "Specify reason for inability to assess the patient."

2. EM Status Impression
    - Free-text box label 4: ri_em_no_reason
        - Visibility condition: "Yes" selected for any indicator of abuse items (items 1-9) and "No" selected for EM status impression (item 10)
        - Free-text box prompt: "Please briefly explain why you don't suspect elder mistreatment given that you observed one or more indicators above."
    - Free-text box label 5: ri_em_reason
        - Visibility condition: "No" selected for all indicator of abuse items (items 1-9) and "Yes" selected for EM status impression (item 10)
        - Free-text box prompt: "Please briefly explain why you suspect elder mistreatment."

3. Response
    - Free-text box label 6: ri_aps_no_reason
        - Visibility condition: "Yes" selected for EM status impression (item 10) and "No" selected for APS report intention (item 12)
        - Free-text box prompt: "Please briefly explain why you don't intend to report your suspicion of elder mistreatment to APS."
    - Free-text box label 7: ri_refer_svcs_specify
        - Visibility condition: "Yes" selected for EM status impression (item 10) and "Yes" selected for service referral intention (item 13)
        - Free-text box prompt: "Please briefly list the services."

- Responses vary in length and specificity.
- Multiple responses may be associated with a single patient encounter.
- Not every patient encounter will generate free-text data.
</free_text_boxes>

<current_status>
Initial category labels have been generated using an LLM. Human labeling is underway to refine and validate the categorization scheme prior to model retraining.

As part of that process, six members of the study team independently labeled each free-text response. Then, we met as a team to review our independent labels and create consensus labels for a subset of the free-text responses. Based on what I learned in that review session, I:
1. Created a labeling dictionary/guide
2. Finished adding consensus labels to the remaining free-text responses.

My next step will be to send out the dictionary/guide and updated spreadsheet containing the free-text responses and labels to the study team.
</current_status>
