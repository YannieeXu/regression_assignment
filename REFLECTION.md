REFLECTION -- Assignment 2

1. Structural differences
Python:  Manual = sklearn + matplotlib | AI = sklearn + matplotlib (same)
R scatter:  Manual = base R plot() | AI = base R plot() (same)
R overlay:  Manual = ggplot2 | AI = ggplot2 (same)
Code style:  Manual = f-strings | AI = %-formatting
Plot colors:  Manual = blue/red | AI = blue/red (same)
CLI parsing:  Manual = sys.argv | AI = sys.argv (same)

Scatter: both use base R plot(). Overlay: both use ggplot2. Colors and titles are now consistent between versions.

2. Readability
Manual version is simpler and easier for a beginner to follow. Both versions use base R scatter + ggplot2 overlay. Both versions follow the same template structure with consistent colors and titles.

3. AI bugs & omissions
The AI did not hallucinate any packages or versions. Several minor issues were found in the initial AI output and fixed during iteration:

- %% bug: The AI used %% instead of % for Python string formatting, causing a syntax error
- Notebook format: Each character of code was placed in a separate cell (display issue, fixed)
- plt.show() in notebooks: Jupyter renders plots automatically, making plt.show() redundant in notebooks. When executed headlessly (via nbconvert), it triggers a non-interactive backend warning. Removed from notebook cells but retained in CLI scripts.

No steps were skipped -- the AI notebooks and CLI scripts include all required functionality.

4. CLI behavior
Both CLIs accept the same arguments (<filename> <x_column> <y_column>), save a PNG plot, and have the same argument ordering and error messages. The R CLI additionally prints slope/intercept/R-squared to the terminal via cat() statements, while the Python CLI outputs no text (per the assignment template). No unusual invocation required.
