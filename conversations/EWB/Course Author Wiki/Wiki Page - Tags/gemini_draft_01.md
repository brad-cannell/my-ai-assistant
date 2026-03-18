Of course. Here is the revised wiki page, updated for clarity, accuracy, and usability, with a professional and instructional tone appropriate for course authors.

***

# Using Categories and Tags

## Overview

This guide outlines how to use categories and tags to organize course content on the Epi-Workbench (EWB) platform. Proper use of this metadata is essential for improving course discovery and helping learners find relevant material.

-   **Categories** provide a high-level grouping for courses (e.g., *Data Science*).
-   **Tags** offer granular detail about the specific content within courses and lessons (e.g., *Linear Regression* or `ggplot2`).

---

## Categories

Categories are used to group courses by subject area on the main Courses page, allowing learners to filter and browse topics of interest.

### Viewing Existing Categories

To see the current list of approved categories:
1.  Navigate to the [Courses page](https://dev.epi-workbench.com/EPIWorkBench/courses/).
2.  Expand the **Filter by category** control to view all available options.

---

## Tags

Tags are keywords that describe specific concepts, functions, or techniques covered in a course or lesson. They power the platform's search functionality and help learners pinpoint exact content.

### How Tags Work

Tags can be assigned at both the course and lesson level.

*   **Course Tags:** You can assign tags to an entire course through the **Course Edit** page.
*   **Lesson Tags & Inheritance:** Lessons **automatically inherit** all tags from their parent course. You can also add tags to individual lessons by editing the lesson's YAML header.

> [!IMPORTANT]
> **Current Procedure for Lesson-Specific Tags**
> If you add a tag to a lesson's YAML header, you **must also add the same tag to the parent course's tag list** via the Course Edit page. This manual step is a temporary requirement to ensure system-wide consistency. This process will be streamlined when direct lesson tagging is implemented.
> *See the development ticket for this feature: [Tag Lessons Instead of Courses](https://trello.com/c/mCQyAXYf/116-tags-tag-lessons-instead-of-courses)*

### How to Apply Tags to a Course

1.  Navigate to the **Course Edit** page for your course.
2.  Click inside the **Tags** selection box.
3.  Select the desired tags from the dropdown list that appears.

> [!NOTE]
> The ability to search for tags by typing in the selection box is currently under development.
> *See the development ticket for this feature: [Type to Search for Tags](https://trello.com/c/5LnNpNdV/115-tags-type-to-search-for-tags)*
>
> *[Placeholder for screenshot of the tag selection interface]*

### Viewing All Tags

To see a complete list of all tags currently in use and their official descriptions, visit the **Tags** page in the Course Author Dashboard.

*[Placeholder for screenshot of the Tags page]*

### How to Request a New Tag

If a suitable tag for your content does not exist, you can request a new one.

There are two ways to submit a request:
1.  **From the Course Edit Page:** Click the **"Can't find a tag? Request a new one →"** link located below the tag selection box.
2.  **From the Author Dashboard:** Click the **"Tag Requests"** link in the sidebar menu.

*[Placeholder for screenshots of the tag request process]*

---

## Tag Creation and Description Guidelines

When requesting a new tag, adhere to the following guidelines to ensure consistency and quality across the platform.

### Naming and Formatting

*   **Use Title Case:** Capitalize the first letter of each major word (e.g., "Categorical Data," "Data Visualization").
*   **Specify Programming Language for Functions:** If a tag refers to a specific function or package, include the language in brackets (e.g., `Mean Function [R]`, `ggplot2 [R]`).
*   **Keep Concepts General:** If a tag refers to a general concept, do not include a language specifier (e.g., "Missing Data," "Logistic Regression").

### Scope and Purpose

*   **Ensure Reusability:** Avoid requesting tags that are so specific they will only apply to a single course or lesson. Tags should be broad enough to be reused.
*   **Provide a Clear Description:** Every new tag request must include a description.

### Writing Tag Descriptions

Use the following templates to write clear and consistent tag descriptions.

*   **Define the purpose:** Start the description with the phrase "This tag is for courses or lessons that..." followed by a clear explanation.
    *   **Example:** "This tag is for courses or lessons that contain information about the structure and function of data frames, or that explicitly discuss creating and manipulating data frames."

*   **Define the limitations (optional but recommended):** If clarity is needed, add a second sentence defining when the tag should *not* be used.
    *   **Example:** "This tag is not intended for content that only incidentally uses a data frame without discussing its properties."
