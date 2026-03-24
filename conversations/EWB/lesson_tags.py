# lesson_tags.py
# =============================================================================
# AI-assisted lesson tag suggestions for EWB lesson files.
#
# Placeholders are filled in by copy_ai_template() in Convert Chapters.qmd:
#   - {{Course Name}}      — human-readable course name
#   - {{Lesson Name}}      — human-readable lesson name
#   - {{lesson_file_path}} — absolute path to the _narrative.qmd file
#   - {{YYYY-MM-DD}}       — today's date
#
# Usage (via Convert Chapters.qmd):
#   1. Run the lesson-tags code block in Step 6.
#   2. Review results in ai/lesson_tags_YYYY-MM-DD.md.
# =============================================================================

from datetime import date
from pathlib import Path
import chatlas as ctl
import keyring
import os

# =============================================================================
# File Paths and Environment Variables
# =============================================================================

# OpenAI Models: https://platform.openai.com/docs/models
# Anthropic Models: https://platform.claude.com/docs/en/about-claude/models/overview
model = "gpt-5-nano-2025-08-07"

# Today's date
today = date.today().isoformat()

# Course and lesson name.
# By default, injected from Convert Chapters.qmd via copy_ai_template().
# Can also be altered manually.
course_name = "{{Course Name}}"
lesson_name = "{{Lesson Name}}"

# Lesson file and folder paths.
# By default, injected from Convert Chapters.qmd via copy_ai_template().
# lesson_file_path points to the _narrative.qmd file produced by extract_narrative().
lesson_file_path   = Path("{{lesson_file_path}}")
lesson_folder_path = lesson_file_path.parent

# Lesson content (the narrative file is shorter and faster to review)
lesson_content = lesson_file_path.read_text(encoding="utf-8")

# Tag SOP
path_template_tag_sop = Path(
    '/Users/bradcannell/Desktop/Git/EWB/ewb-wiki/02 Course Development/'
    '01 Categories and Tags/Categories and Tags.qmd'
)
tag_sop_content = path_template_tag_sop.read_text(encoding="utf-8")

# =============================================================================
# Check that all paths exist
# =============================================================================

paths_to_check = {
    "lesson_file_path":      lesson_file_path,
    "lesson_folder_path":    lesson_folder_path,
    "path_template_tag_sop": path_template_tag_sop,
}

for name, path in paths_to_check.items():
    if not path.exists():
        raise FileNotFoundError(f"Path not found — {name}: {path}")
    print(f"✓  {name}: {path}")

# =============================================================================
# Expose API
#
# Assumes key stored via:
#   keyring.set_password("ewb-course-development", "brad", "<key>")
# =============================================================================

openai_api = keyring.get_password("ewb-course-development", "brad")

if openai_api is not None:
    os.environ['OPENAI_API_KEY'] = openai_api
    print("Environment variable 'OPENAI_API_KEY' set successfully.")
else:
    raise RuntimeError("Could not retrieve OpenAI API key from keyring.")

# =============================================================================
# Build Tag Request
#
# Lesson content is included in the request because this script runs
# independently (no prior chat context).
# =============================================================================

tag_request = f"""
Return a bulleted list of tags for the following lesson.

## Lesson: {lesson_name}

## Course: {course_name}

## Lesson content:

{lesson_content}

---

- Return only the 5-10 most relevent tags.

    - In this context, relevent refers to the content learners are likely to
      search for, and the tags they are likely to use in their search.

- Do not use words from the lesson title in tags.

    - For example, don't return "Data Transfer" as a tag for a lesson titled,
      "Data Transfer in R".

- Do not add any formatting (e.g., bold) to the items in the list.

- Use this format when returning function tags:
  Function: function_name [Language].
  For example, "Function: group_by [R]"

- When 3 or more functions from the same package are used in the lesson,
  tag the entire package.

    - Use this format when returning package tags:
      Package: package_name [Language].
      For example, "Package: dplyr [R]"

- Below each tag, provide a tag description.

    - Use this template for function tag descriptions:
      "This course or lesson contains information about using the R
      [function_name] function. This tag is not intended for use when the
      course or lesson just happens to contain code that uses the R
      [function_name] function."

    - Use this template for package tag descriptions:
      "This course or lesson contains information about using the
      [package_name] R package. This tag is not intended for use when the
      course or lesson just happens to contain code that uses the
      [package_name] package."

I'm attaching an SOP about tags with further guidance.

## Tag request SOP:

"""
tag_request = tag_request + tag_sop_content

# =============================================================================
# Create Chat Object and Generate Tags
# =============================================================================

chat = ctl.ChatOpenAI(model=model)

chat.chat(tag_request, echo='none')
print(chat)

# =============================================================================
# Write the Tags to a Markdown File for Review
#
# Delete the file when done.
# =============================================================================

output_path = (
    lesson_folder_path / "ai" / ("lesson_tags_" + today + ".md")
)
output_path.write_text(str(chat.get_last_turn()), encoding='utf-8')
print(f"\nResults written to: {output_path}")
