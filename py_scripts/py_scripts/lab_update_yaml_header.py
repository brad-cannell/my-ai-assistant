import re
from pathlib import Path
from typing import Union


def lab_update_yaml_header(
    answer_key_path: Union[str, Path],
    lab_instructions_path: Union[str, Path],
) -> Path:
    """
    Copy a Quarto lab answer key to the instructions path with the YAML
    front matter updated for student use.

    Reads the answer key, locates the YAML front matter (the block between
    the opening and closing ``---`` delimiters at the top of the file), and
    makes the following field substitutions before writing to
    ``lab_instructions_path``:

    - ``author`` → ``author: "[Your Name]"``
    - ``date-modified`` → ``date-modified: [Enter Date]``

    All other YAML fields and the rest of the document are written
    unchanged.

    This is the first function in the lab-instructions pipeline. All
    subsequent pipeline functions read from and overwrite
    ``lab_instructions_path``.

    Parameters
    ----------
    answer_key_path : str or pathlib.Path
        Path to the instructor answer key ``.qmd`` file.
    lab_instructions_path : str or pathlib.Path
        Destination path for the student-facing instructions file. The
        parent directory is created if it does not already exist.

    Returns
    -------
    pathlib.Path
        The resolved path to the written instructions file (same as
        ``lab_instructions_path``).

    Raises
    ------
    ValueError
        If the file does not begin with ``---`` (no YAML front matter
        found) or if no closing ``---`` delimiter is present.
    """
    lines = Path(answer_key_path).read_text(encoding="utf-8").splitlines(keepends=True)

    # YAML front matter must begin on the very first line
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError(
            "No YAML front matter found: the file does not begin with '---'."
        )

    # Locate the closing '---' (must appear after line 0)
    close_idx = None
    for i in range(1, len(lines)):
        if lines[i].rstrip("\r\n") == "---":
            close_idx = i
            break

    if close_idx is None:
        raise ValueError(
            "No closing '---' delimiter found for the YAML front matter."
        )

    # Rewrite the YAML block, substituting author and date-modified fields
    result = []
    for i, line in enumerate(lines):
        bare = line.rstrip("\r\n")

        if i > 0 and i < close_idx:
            # Inside the YAML block — apply substitutions
            if re.match(r"^author\s*:", bare):
                # Preserve original line ending
                ending = line[len(bare):]
                result.append(f'author: "[Your Name]"{ending}')
            elif re.match(r"^date-modified\s*:", bare):
                ending = line[len(bare):]
                result.append(f"date-modified: [Enter Date]{ending}")
            else:
                result.append(line)
        else:
            result.append(line)

    # Write to the instructions path (create parent dirs if needed)
    out_path = Path(lab_instructions_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(result), encoding="utf-8")

    return out_path
