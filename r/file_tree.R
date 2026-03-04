# Generate a file tree diagram for a given directory path.
#
# @param path     Character. The root directory path to diagram.
# @param depth    Integer. How many levels deep to recurse. Default is 3.
# @param output   Character or NULL. File path for markdown output. If NULL
#                 (default), prints to the console only.
#
# @return Character vector of tree lines. Invisible.
#
# @examples
# file_tree("/Users/bradcannell/Desktop/Git")
# file_tree("/Users/bradcannell/Desktop/Git", depth = 2)
# file_tree("/Users/bradcannell/Desktop/Git", output = "~/Desktop/tree.md")

file_tree <- function(path, depth = 3, output = NULL) {
  path <- normalizePath(path, mustWork = TRUE)

  lines <- character(0)

  build_tree <- function(dir, prefix, current_depth) {
    if (current_depth > depth) return()

    entries <- list.files(dir, full.names = FALSE, all.files = FALSE)
    if (length(entries) == 0) return()

    for (i in seq_along(entries)) {
      name    <- entries[i]
      full    <- file.path(dir, name)
      is_last <- i == length(entries)
      is_dir  <- file.info(full)$isdir

      connector <- if (is_last) "\u2514\u2500\u2500" else "\u251c\u2500\u2500"
      icon      <- if (is_dir) "\U0001F4C1" else "\U0001F4C4"

      lines <<- c(lines, paste0(prefix, connector, " ", icon, " ", name))

      if (is_dir && current_depth < depth) {
        extension <- if (is_last) "    " else "\u2502   "
        build_tree(full, paste0(prefix, extension), current_depth + 1)
      }
    }
  }

  build_tree(path, prefix = "", current_depth = 1)

  cat(paste(lines, collapse = "\n"), "\n")

  if (!is.null(output)) {
    output     <- normalizePath(output, mustWork = FALSE)
    dir_name   <- basename(path)
    timestamp  <- format(Sys.time(), "%Y-%m-%d, %I:%M:%S %p")

    md <- c(
      paste0("# File Tree: ", dir_name),
      "",
      paste0("**Generated:** ", timestamp),
      paste0("**Root Path:** `", path, "`"),
      "",
      "```",
      lines,
      "```"
    )

    writeLines(md, output)
    message("File tree written to: ", output)
  }

  invisible(lines)
}
