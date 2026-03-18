#' Extract the SYSTEM PROMPT section from a markdown file
#'
#' Reads a markdown file and extracts only the text contained under the
#' `# SYSTEM PROMPT` heading, stopping at the next top-level heading.
#' The extracted text is returned as a single character string with
#' original line breaks preserved.
#'
#' @param file_path Character string. Path to the markdown (.md) file.
#'
#' @return A character string containing the SYSTEM PROMPT text.
#'
#' @details
#' This function treats the markdown file as plain text and relies on
#' heading boundaries rather than a markdown parser. It assumes:
#' \itemize{
#'   \item The SYSTEM PROMPT section is introduced with `# SYSTEM PROMPT`
#'   \item The next section begins with another top-level heading (`# `)
#' }
#'
#' If the SYSTEM PROMPT heading is not found, the function errors.
#'
#' @examples
#' \dontrun{
#' system_prompt <- prompt_extract_system_prompt(
#'   "Template Prompt - Lesson Revisions.md"
#' )
#'
#' cat(system_prompt)
#' }
#'
#' @export
prompt_extract_system_prompt <- function(file_path) {
  
  # Read the markdown file line-by-line
  lines <- readLines(file_path, encoding = "UTF-8")
  
  # Locate the SYSTEM PROMPT heading
  start_idx <- which(lines == "# SYSTEM PROMPT")
  
  # Error if the heading is not found
  if (length(start_idx) == 0) {
    stop("No '# SYSTEM PROMPT' section found in the file.")
  }
  
  # Move to the first line of content under the heading
  start_idx <- start_idx + 1
  
  # Find the next top-level heading after SYSTEM PROMPT
  end_idx <- which(
    grepl("^# ", lines) & seq_along(lines) > start_idx
  )[1]
  
  # If no following heading exists, extract to end of file
  if (is.na(end_idx)) {
    end_idx <- length(lines)
  } else {
    end_idx <- end_idx - 1
  }
  
  # Extract and reassemble the SYSTEM PROMPT text
  system_prompt <- paste(
    lines[start_idx:end_idx],
    collapse = "\n"
  )
  
  return(system_prompt)
}
