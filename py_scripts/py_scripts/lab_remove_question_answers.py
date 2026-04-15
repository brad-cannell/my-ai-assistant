import re
from pathlib import Path
from typing import Union

_LMS_MSG = (
    "See our course LMS for the answer choices and submit your response."
)


def lab_remove_question_answers(lab_instructions_path: Union[str, Path]) -> Path:
    """
    Strip answers from "Question N" subsections in the lab instructions file.

    Scans the file for headings matching "Question N" (where N is an
    integer, case-insensitive, any heading level). For each such section:

    - The heading line is **kept**.
    - The question text (non-answer paragraphs) is **kept**.
    - Bullet-point answer lines (lines starting with ``* ``) are removed.
    - Entire ``{r}`` code blocks within the section are removed (these are
      multiple-choice answer-option blocks, not student code scaffolding).
    - If any answer content was removed, the line
      "See our course LMS for the answer choices and submit your response."
      is appended after the question text (trailing blank lines are
      collapsed before appending).

    The section ends at the next heading of equal or higher level (fewer or
    equal ``#`` characters). If no answer content is found in a question
    section, the section is written out unchanged.

    The file at ``lab_instructions_path`` is overwritten in place.

    Parameters
    ----------
    lab_instructions_path : str or pathlib.Path
        Path to the student-facing instructions ``.qmd`` file produced by
        a prior pipeline step.

    Returns
    -------
    pathlib.Path
        The resolved path to the updated file (same as
        ``lab_instructions_path``).

    Notes
    -----
    - The heading level is detected dynamically, so ``## Question 1`` and
      ``### Question 1`` (and any other level) are handled correctly.
    - Tables and other non-bullet, non-code-block content inside a question
      section are preserved.
    - This function is designed to run *after* ``lab_remove_r_code``, so
      code blocks within question sections contain only comments/blank lines
      by the time they are removed here.
    """
    path = Path(lab_instructions_path)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    result: list[str] = []

    # State
    in_question = False
    question_level: int | None = None
    question_buffer: list[str] = []  # accumulates lines for the current section
    answers_removed = False           # did we drop any answer content this section?
    in_answer_block = False           # are we inside a {r} answer-option code block?

    def flush_question() -> None:
        """Emit the buffered question section, appending the LMS message if needed."""
        nonlocal question_buffer, answers_removed

        if answers_removed and question_buffer:
            # Strip trailing blank lines so the LMS message sits flush
            while question_buffer and question_buffer[-1].strip() == "":
                question_buffer.pop()
            question_buffer.append("\n")
            question_buffer.append(_LMS_MSG + "\n")
            question_buffer.append("\n")

        result.extend(question_buffer)
        question_buffer.clear()
        answers_removed = False

    for line in lines:
        bare = line.rstrip("\r\n")
        # Don't evaluate headings while inside a code block — comment lines
        # like "# Incorrect: ..." would otherwise match the heading pattern
        # and prematurely terminate the question section.
        heading_match = (
            None if in_answer_block else re.match(r"^(#{1,6})\s+(.+)", bare)
        )

        if heading_match:
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()

            # A heading at the same or higher level terminates a question section
            if in_question and level <= question_level:
                flush_question()
                in_question = False
                in_answer_block = False
                question_level = None

            if re.fullmatch(r"Question\s+\d+", heading_text, re.IGNORECASE):
                # Enter a new question section — keep the heading
                in_question = True
                question_level = level
                question_buffer.append(line)
            else:
                result.append(line)

        elif in_question:
            if not in_answer_block:
                if re.match(r"^```\{r\b", bare):
                    # Start of an R code block inside a question — it's an answer
                    # option block; remove it entirely
                    in_answer_block = True
                    answers_removed = True
                    # Don't append opening fence
                elif re.match(r"^\*\s", bare) or bare.strip() == "*":
                    # Bullet-point answer — remove
                    answers_removed = True
                else:
                    question_buffer.append(line)
            else:
                # Inside an answer-option code block — skip until closing fence
                if bare == "```":
                    in_answer_block = False
                    # Don't append closing fence either
                # else: block content — skip

        else:
            result.append(line)

    # Flush any question section that runs to end of file
    if in_question:
        flush_question()

    path.write_text("".join(result), encoding="utf-8")
    return path
