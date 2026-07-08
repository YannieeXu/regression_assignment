# REFLECTION.md -- Assignment 2

## 1. Structural differences

**Python:**  Manual = sklearn + matplotlib | AI = sklearn + matplotlib (same)
**R plotting:**  Manual = base R plot() | AI = ggplot2
**Code style:**  Manual = f-strings | AI = %-formatting
**Plot colors:**  Manual = blue/red | AI = steelblue/crimson
**CLI parsing:**  Manual = sys.argv | AI = sys.argv (same)

Main difference: AI used ggplot2 for R; manual used base R. Everything else similar.

---

## 2. Readability

Manual version is simpler and easier for a beginner to follow. The AI version with ggplot2 is more elegant but requires knowledge of an additional package. For a scientist doing quick exploratory analysis, the manual version wins on clarity. The AI version wins on visual polish.

---

## 3. AI bugs & omissions

The AI did not hallucinate any packages or versions. Two minor issues were found in the initial AI output and fixed during iteration:

- **%% bug:** The AI used %% instead of % for Python string formatting, causing a syntax error
- **Notebook format:** Each character of code was placed in a separate cell (display issue, fixed)

No steps were skipped -- the AI notebooks and CLI scripts include all required functionality.

---

## 4. CLI behavior

Both CLIs work identically. They accept &lt;filename&gt; &lt;x_column&gt; &lt;y_column&gt; as arguments, output slope/intercept/R-squared, and save a PNG plot. Same argument order, same output format, same naming convention. Error messages for missing args are reasonable in both versions. No unusual invocation required.
