# REFLECTION.md -- Assignment 2

## 1. Structural Differences (Manual vs AI)

### Python Notebook
**Libraries:**  Manual = sklearn + matplotlib | AI = sklearn + matplotlib (same)
**String formatting:**  Manual = f-strings (modern) | AI = % formatting (old style)
**Plot style:**  Manual = basic matplotlib | AI = seaborn-enhanced

### R Notebook
**Plotting package:**  Manual = base R plot() | AI = ggplot2
**Syntax:**  Manual = imperative | AI = declarative (grammar of graphics)

### CLI Scripts
**Argument parsing:**  Manual = sys.argv | AI = sys.argv (same)
**Output format:**  Manual = slope, intercept, R-squared | AI = same
**Plot output:**  Manual = .png file | AI = same

**Key takeaway:** Both versions produce identical numerical results. The main structural difference is the AI used modern R packages (ggplot2) while the manual used base R.

---

## 2. Readability

- **Manual**: More straightforward. Code follows a simple linear flow. Easier for beginners to understand.
- **AI**: More elegant visually (ggplot2, seaborn styling). But requires familiarity with additional packages.

**Verdict:** Manual wins for clarity; AI wins for visual polish.

---

## 3. AI Bugs & Omissions

- Hallucinated packages: None
- Wrong version numbers: None
- %% instead of % in Python string formatting: Fixed
- Notebook source formatting issue (characters as separate cells): Fixed

**The AI code ran correctly after minor fixes. No hallucinated packages or versions.**

---

## 4. CLI Behavior

Both CLIs behave identically:
- python linear_regression_python.py <filename> <x_col> <y_col>
- Rscript linear_regression_r.R <filename> <x_col> <y_col>
- Same argument order, same output format, same output filename convention
- Error messages for missing arguments are reasonable in both

---

## 5. Tools Used

- **AI tool:** Cursor (GPT-4o / Claude)
- **Prompts:** See ai/PROMPTS.md for 3-5 prompts used
- **Manual:** All code typed by hand, no AI assistance
