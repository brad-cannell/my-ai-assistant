from pathlib import Path
from typing import Union


def prompt_extract_system_prompt(file_path: Union[str, Path]) -> str:
    """
    Extract the SYSTEM PROMPT section from a Markdown file.

    Reads a Markdown file and extracts only the text contained under the
    '# SYSTEM PROMPT' heading, stopping at the next top-level heading.
    The extracted text is returned as a single string with original
    line breaks preserved.

    Parameters
    ----------
    file_path : str or pathlib.Path
        Path to the markdown (.md) file.

    Returns
    -------
    str
        The SYSTEM PROMPT text.

    Raises
    ------
    ValueError
        If no '# SYSTEM PROMPT' section is found.
    """
    # Read file line-by-line (UTF-8, like readLines())
    lines = Path(file_path).read_text(encoding="utf-8").splitlines()

    # Locate the SYSTEM PROMPT heading
    try:
        start_idx = lines.index("# SYSTEM PROMPT")
    except ValueError:
        raise ValueError("No '# SYSTEM PROMPT' section found in the file.")

    # Move to the first line under the heading
    start_idx += 1

    # Find the next top-level heading after SYSTEM PROMPT
    end_idx = None
    for i in range(start_idx + 1, len(lines)):
        if lines[i].startswith("# "):
            end_idx = i - 1
            break

    # If no following heading, extract to end of file
    if end_idx is None:
        end_idx = len(lines)

    # Extract and reassemble with original line breaks
    system_prompt = "\n".join(lines[start_idx:end_idx])

    return system_prompt