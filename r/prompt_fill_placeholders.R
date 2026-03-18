#' Replace namespace-style placeholders in a prompt template
#'
#' Performs explicit string replacement for namespace-style placeholders
#' (e.g., `{{lesson_name}}`, `{{course_name}}`) in a prompt template.
#' The function does not evaluate R expressions and makes no assumptions
#' about the structure of the surrounding text.
#'
#' @param text Character string. The prompt template text containing
#'   namespace-style placeholders.
#'
#' @param replacements Named character vector or list. Names must
#'   correspond exactly to placeholder names *without* braces
#'   (e.g., `lesson_name`, not `{{lesson_name}}`).
#'
#' @return A character string with all matching placeholders replaced.
#'
#' @details
#' Placeholders must use the following syntax:
#'
#' \preformatted{
#' {{placeholder_name}}
#' }
#'
#' Replacement is performed using fixed string matching (no regular
#' expressions), making the function safe for instructional text and
#' prompt templates.
#'
#' @examples
#' \dontrun{
#' template <- "Lesson: {{lesson_name}}\nCourse: {{course_name}}"
#'
#' filled <- prompt_fill_placeholders(
#'   text = template,
#'   replacements = c(
#'     lesson_name = "Introduction to Objects",
#'     course_name = "R Fundamentals"
#'   )
#'
#' cat(filled)
#' }
#'
#' @export
prompt_fill_placeholders <- function(text, replacements) {
  
  # Validate `text`
  if (!is.character(text) || length(text) != 1) {
    stop("`text` must be a single character string.")
  }
  
  # Check whether the text contains any namespace-style placeholders
  if (!grepl("\\{\\{[^}]+\\}\\}", text)) {
    stop(
      paste(
        "No placeholders found in `text`.",
        "Placeholders must be surrounded with double curly braces,",
        "for example: {{lesson_name}} or {{course_name}}."
      )
    )
  }
  
  # Validate `replacements`
  if (!is.character(replacements) && !is.list(replacements)) {
    stop("`replacements` must be a named character vector or list.")
  }
  
  # Ensure all replacement values are named
  if (is.null(names(replacements)) || any(names(replacements) == "")) {
    stop("All replacement values must be named.")
  }
  
  # Iterate over each replacement
  for (name in names(replacements)) {
    
    # Construct the full placeholder token (e.g., {{lesson_name}})
    placeholder <- paste0("{{", name, "}}")
    
    # Replace all occurrences of the placeholder with its value
    text <- gsub(
      pattern = placeholder,
      replacement = replacements[[name]],
      x = text,
      fixed = TRUE
    )
  }
  
  # Return the fully substituted prompt text
  return(text)
}