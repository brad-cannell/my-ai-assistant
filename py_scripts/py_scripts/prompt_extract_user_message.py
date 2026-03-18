from pathlib import Path
from typing import Union


def prompt_extract_user_message(file_path: Union[str, Path]) -> str:
    """
    Extract the USER MESSAGE section from a Markdown file.

    Reads a Markdown file and extracts all text starting from the
    '# USER MESSAGE' heading through the end of the file.
    The extracted text is returned as a single string with original
    line breaks preserved.

    Parameters
    ----------
    file_path : str or pathlib.Path
        Path to the markdown (.md) file.

    Returns
    -------
    str
        The USER MESSAGE text.

    Raises
    ------
    ValueError
        If no '# USER MESSAGE' section is found.
    """
    lines = Path(file_path).read_text(encoding="utf-8").splitlines()

    # Locate the USER MESSAGE heading (exact match, like R's `lines == ...`)
    try:
        start_idx = lines.index("# USER MESSAGE")
    except ValueError:
        raise ValueError("No '# USER MESSAGE' section found in the file. Is there a typo?")

    # Move to the first line of content under the heading
    start_idx += 1

    # Extract everything to end of file
    return "\n".join(lines[start_idx:])
