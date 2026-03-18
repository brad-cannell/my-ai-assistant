# This function removes a YAML header if it exists at the top of a markdown file.
# A YAML header is assumed to:
#   - start with '---' on the first line
#   - end with the next '---'
strip_yaml_header <- function(lines) {
  
  # Check whether the first non-empty line is a YAML start marker
  first_non_empty <- which(nzchar(trimws(lines)))[1]
  
  if (!is.na(first_non_empty) && trimws(lines[first_non_empty]) == "---") {
    
    # Find the line number of the closing YAML delimiter
    yaml_end <- which(trimws(lines) == "---")[-1][1]
    
    # Return everything *after* the YAML block
    return(lines[(yaml_end + 1):length(lines)])
    
  } else {
    
    # If no YAML header is present, return the original lines unchanged
    return(lines)
  }
}

# For testing
strip_yaml_header('/Users/bradcannell/Library/CloudStorage/GoogleDrive-brad.cannell@epi-workbench.com/My Drive/AI Assistant/snippets/about_ewb.md')
