# AI Code Review - Assignment 3

## Suggestions
1. **Error handling**: Scripts assume the CSV file exists. Add try/except for file-not-found errors.
2. **Annotation position**: Manual Python uses axis-normalized coords, R uses data coords. Being consistent would be better.
3. **Legend**: Adding a legend improves readability.

## Bug Check
No bugs found. All statistical outputs match between Python and R.
