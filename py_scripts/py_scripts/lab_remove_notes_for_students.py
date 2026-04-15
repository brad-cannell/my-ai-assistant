import re
from pathlib import Path
from typing import Union


def lab_remove_notes_for_students(lab_instructions_path: Union[str, Path]) -> Path:
    """
    Remove all "Notes for students" subsections from the lab instructions file.

    Scans the file for headings whose text is exactly "Notes for students"
    (case-insensitive, any heading level) and removes that heading together
    with all content beneath it until the next heading of equal or higher
    level (i.e., the same number of ``#`` characters or fewer).

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
    The heading level is detected dynamically, so both ``## Notes for
    students`` and ``### Notes for students`` (and any other level) are
    handled correctly. Removal stops at the first heading whose level is
    less than or equal to the "Notes for students" heading level.
    """
    path = Path(lab_instructions_path)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    result = []
    skipping = False
    skip_level = None

    for line in lines:
        bare = line.rstrip("\r\n")
        heading_match = re.match(r"^(#{1,6})\s+(.+)", bare)

        if heading_match:
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()

            if skipping and level <= skip_level:
                # Encountered a heading at the same or higher level — stop skipping
                skipping = False
                skip_level = None

            if not skipping:
                if re.fullmatch(r"Notes for students", heading_text, re.IGNORECASE):
                    # Start skipping from this heading onward
                    skipping = True
                    skip_level = level
                    # Do not append the heading itself
                else:
                    result.append(line)
        else:
            if not skipping:
                result.append(line)

    path.write_text("".join(result), encoding="utf-8")
    return path
