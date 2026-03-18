# spelling_grammar_check.py
# =============================================================================
# AI-assisted spelling and grammar check for EWB lesson files.
#
# Placeholders are filled in by copy_ai_template() in Convert Chapters.qmd:
#   - {{Course Name}}      — human-readable course name
#   - {{Lesson Name}}      — human-readable lesson name
#   - {{lesson_file_path}} — absolute path to the _narrative.qmd file
#   - {{YYYY-MM-DD}}       — today's date
#
# Usage (via Convert Chapters.qmd):
#   1. Run the spelling-grammar-check code block in Step 6.
#   2. Review results in ai/spelling_and_grammar_check_YYYY-MM-DD.md.
# =============================================================================

from chatlas import ChatAnthropic
from openai import OpenAI
from httpcore import stream
from datetime import date
from pathlib import Path
import chatlas as ctl
import anthropic
import keyring
import json
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

# Prompt paths
path_template_prompt_spelling_grammar = Path(
    '/Users/bradcannell/Desktop/Git/AI/ewb-ai-assistant'
    '/prompts/Courses/Template Prompt - Spelling and Grammar Check.md'
)

# =============================================================================
# Check that all paths exist
# =============================================================================

paths_to_check = {
    "lesson_file_path":                      lesson_file_path,
    "lesson_folder_path":                    lesson_folder_path,
    "path_template_prompt_spelling_grammar": path_template_prompt_spelling_grammar,
}

for name, path in paths_to_check.items():
    if not path.exists():
        raise FileNotFoundError(f"Path not found — {name}: {path}")
    print(f"✓  {name}: {path}")

# =============================================================================
# Load helper functions
#
# Prerequisites (run once in terminal):
#   /usr/local/bin/python3 -m pip install --editable "/Users/bradcannell/Desktop/Git/AI/ewb-ai-assistant/py_scripts"
#   Then restart the interpreter.
# =============================================================================

from ewb_py_scripts import (
    prompt_extract_system_prompt,
    prompt_extract_user_message,
    prompt_fill_placeholders,
)

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
# Read the Template Prompt
# =============================================================================

# Raw system (developer) section of the prompt template
system_prompt = prompt_extract_system_prompt(path_template_prompt_spelling_grammar)

# Raw user message section of the prompt template
user_message_raw = prompt_extract_user_message(path_template_prompt_spelling_grammar)

# Inject course name, lesson name, and lesson content into the user message
user_message = prompt_fill_placeholders(
    text=user_message_raw,
    replacements={
        "lesson_name":    lesson_name,
        "course_name":    course_name,
        "lesson_content": lesson_content,
    },
)

# =============================================================================
# Create Chat Object and Run Spelling/Grammar Check
# =============================================================================

chat = ctl.ChatOpenAI(
    model=model,
    system_prompt=system_prompt,
)

chat.chat(user_message, echo='none')
print(chat)

# =============================================================================
# Write the Revisions to a Markdown File for Review
#
# Delete the file when done making revisions.
# =============================================================================

# output_path = (
#     lesson_folder_path / "ai" / ("spelling_and_grammar_check_" + today + ".md")
# )
# output_path.write_text(str(chat.get_last_turn()), encoding='utf-8')
# print(f"\nResults written to: {output_path}")
