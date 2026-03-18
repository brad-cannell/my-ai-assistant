from typing import Mapping


def prompt_fill_placeholders(text: str, replacements: Mapping[str, str]) -> str:
    """
    Replace namespace-style placeholders in a prompt template.

    Performs explicit string replacement for namespace-style placeholders
    (e.g., {{lesson_name}}, {{course_name}}) in a prompt template.
    The function does not evaluate expressions and makes no assumptions
    about the structure of the surrounding text.

    Parameters
    ----------
    text : str
        The prompt template text containing namespace-style placeholders.
    replacements : Mapping[str, str]
        Mapping whose keys correspond exactly to placeholder names
        *without* braces (e.g., 'lesson_name', not '{{lesson_name}}').

    Returns
    -------
    str
        A string with all matching placeholders replaced.

    Raises
    ------
    TypeError
        If `text` is not a single string or `replacements` is not a mapping.
    ValueError
        If placeholders are missing or replacement keys/values are invalid.
    """
    # Validate `text`
    if not isinstance(text, str):
        raise TypeError("`text` must be a single character string.")

    # Check whether the text contains any namespace-style placeholders
    if "{{" not in text or "}}" not in text:
        raise ValueError(
            "No placeholders found in `text`. "
            "Placeholders must be surrounded with double curly braces, "
            "for example: {{lesson_name}} or {{course_name}}."
        )

    # Validate `replacements`
    if not isinstance(replacements, Mapping):
        raise TypeError("`replacements` must be a mapping (e.g., dict).")

    if not replacements:
        raise ValueError("`replacements` must contain at least one named value.")

    # Ensure all replacement keys are valid, non-empty strings
    for key, value in replacements.items():
        if not isinstance(key, str) or key == "":
            raise ValueError("All replacement keys must be non-empty strings.")
        if not isinstance(value, str):
            raise ValueError("All replacement values must be character strings.")

    # Perform fixed string replacement (no regex)
    for name, value in replacements.items():
        placeholder = f"{{{{{name}}}}}"  # produces {{lesson_name}}
        text = text.replace(placeholder, value)

    return text
