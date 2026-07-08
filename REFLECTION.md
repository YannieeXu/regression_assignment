# REFLECTION.md -- Assignment 2

## Structural differences

| Aspect | Manual Version | AI Version |
|--------|---------------|------------|
| Python Libraries | sklearn, matplotlib | sklearn, matplotlib (same core libs) |
| R Libraries | base R plot() | ggplot2 (grammar of graphics) |
| Python formatting | f-strings (f"Slope: {x:.4f}") | % formatting ("Slope: %.4f" % x) |
| Plot colors | Basic blue/red | steelblue/crimson |
| Plot style | Simple matplotlib | seaborn theme applied |
| CLI argument handling | sys.argv | sys.argv (same approach) |
| Notebook cell grouping | 5 logical cells | 5 logical cells (same structure) |

The biggest structural difference is in the R notebook: the AI chose ggplot2, a modern declarative plotting system, while the manual version used base R plot() functions.

## Readability

The manual version is more straightforward and easier for a beginner to follow. The AI version's use of ggplot2 in R is more elegant once you understand the grammar of graphics, but requires knowledge of an additional package. For a scientist who needs quick exploratory analysis, the manual version wins on simplicity. The AI version wins on visual polish.

## AI bugs and omissions

The AI did not hallucinate any nonexistent packages or wrong version numbers, which was good. However, two issues appeared in the initial AI output that needed fixing:
- The AI used %% instead of % for Python string formatting, which caused a syntax error
- The AI's notebook had each character of code in a separate cell (technical formatting issue)

These were fixed during iteration. The AI also used slightly different plot colors and styles, but those are preferences, not bugs.

## CLI behavior

Both CLI scripts behave identically -- they accept <filename> <x_column> <y_column> as command-line arguments, output slope/intercept/R-squared, and save a PNG plot. The argument order and error messages are consistent between the manual and AI versions.
