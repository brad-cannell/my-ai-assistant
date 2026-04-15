import re
from pathlib import Path
from typing import Union

# Patterns that identify data-import or data-creation lines.
# Any code block containing one of these calls is preserved in full.
_DATA_PATTERN = re.compile(
    r"\bread_\w+\s*\("        # read_csv(), read_excel(), read_rds(), …
    r"|\btibble\s*\("         # tibble()
    r"|\btribble\s*\("        # tribble()
    r"|\bdata\.frame\s*\(",   # data.frame()
)


def lab_remove_r_code(lab_instructions_path: Union[str, Path]) -> Path:
    """
    Remove R code from R code blocks in the lab instructions file,
    preserving blocks that import data or build data frames / tibbles.

    Scans the file for fenced R code blocks (`` ```{r …} `` … `` ``` ``).
    For each block:

    - If **any** non-comment, non-blank line in the block contains a call
      to ``read_*()``, ``tibble()``, ``tribble()``, or ``data.frame()``,
      the entire block (including all R code) is kept unchanged.
    - Otherwise, every line inside the block that is not a comment or blank
      is removed. The opening fence, closing fence, comment lines (lines
      whose first non-whitespace character is ``#``, including ``#|`` chunk
      options), and blank lines are always preserved.

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
    - Detection uses the first occurrence of the data pattern anywhere in
      a non-comment line of the block; the entire block is then kept so
      that multi-line expressions (e.g. a ``tribble()`` call spanning many
      rows) are not split.
    - Only blocks whose opening fence matches ````` ```{r ``` are
      processed; Python, bash, or other language blocks are left unchanged.
    """
    path = Path(lab_instructions_path)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    result = []
    in_r_block = False
    opening_fence = None
    block_buffer: list[str] = []

    for line in lines:
        bare = line.rstrip("\r\n")

        if not in_r_block:
            if re.match(r"^```\{r\b", bare):
                in_r_block = True
                opening_fence = line
                block_buffer = []
            else:
                result.append(line)
        else:
            if bare == "```":
                # Closing fence — decide how to emit the buffered block
                keep_all = any(
                    _DATA_PATTERN.search(l.rstrip("\r\n"))
                    for l in block_buffer
                    if l.lstrip().rstrip("\r\n") and not l.lstrip().startswith("#")
                )

                result.append(opening_fence)
                if keep_all:
                    result.extend(block_buffer)
                else:
                    for buf_line in block_buffer:
                        bare_buf = buf_line.rstrip("\r\n")
                        if bare_buf.lstrip().startswith("#") or bare_buf.strip() == "":
                            result.append(buf_line)
                        # else: executable R code — drop

                result.append(line)  # closing fence
                in_r_block = False
                opening_fence = None
                block_buffer = []
            else:
                block_buffer.append(line)

    # Flush any unclosed block (malformed file — emit as-is)
    if in_r_block and opening_fence is not None:
        result.append(opening_fence)
        result.extend(block_buffer)

    path.write_text("".join(result), encoding="utf-8")
    return path
