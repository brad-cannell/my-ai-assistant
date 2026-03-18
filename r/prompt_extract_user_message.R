#' Extract the USER MESSAGE section from a markdown file
#'
#' Reads a markdown file and extracts all text starting from the
#' `# User Message` heading through the end of the file.
#' The extracted text is returned as a single character string with
#' original line breaks preserved.
#'
#' @param file_path Character string. Path to the markdown (.md) file.
#'
#' @return A character string containing the USER MESSAGE text.
#'
#' @details
#' This function treats the markdown file as plain text and relies on
#' heading detection rather than a markdown parser. It assumes:
#' \itemize{
#'   \item The USER MESSAGE section is introduced with `# User Message`
#'   \item All relevant content appears after this heading
#' }
#'
#' If the USER MESSAGE heading is not found, the function errors.
#'
#' @examples
#' \dontrun{
#' user_message <- prompt_extract_user_message(
#'   "Template Prompt - Lesson Revisions.md"
#' )
#'
#' cat(user_message)
#' }
#'
#' @export
prompt_extract_user_message <- function(file_path) {
  
  # Read the markdown file line-by-line
  lines <- readLines(file_path, encoding = "UTF-8")
  
  # Locate the USER MESSAGE heading
  start_idx <- which(lines == "# USER MESSAGE")
  
  # Error if the heading is not found
  if (length(start_idx) == 0) {
    stop("No '# USER MESSAGE' section found in the file. Is there a typo?")
  }
  
  # Move to the first line of content under the heading
  start_idx <- start_idx + 1
  
  # Extract everything from USER MESSAGE to end of file
  user_message <- paste(
    lines[start_idx:length(lines)],
    collapse = "\n"
  )
  
  return(user_message)
}
