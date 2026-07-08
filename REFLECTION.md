# REFLECTION.md -- Assignment 2

## 1. Structural Differences (Manual vs AI)

### Python Notebook
| Aspect | Manual | AI |
|--------|--------|----|
| Libraries | sklearn + matplotlib | sklearn + matplotlib |
| String formatting | f-strings (modern) | % formatting (old style) |
| Plot style | Basic matplotlib | seaborn-enhanced |

### R Notebook
| Aspect | Manual | AI |
|--------|--------|----|
| Plotting package | base R plot() | ggplot2 |
| Syntax | Imperative | Declarative (grammar of graphics) |

### CLI Scripts
| Aspect | Manual | AI |
|--------|--------|----|
| Argument parsing | sys.argv | sys.argv |
| Output format | Identical | Identical |
| Plot behavior | Identical | Identical |

**Key takeaway:** Both versions produce the same numerical results. The main structural difference is that the AI used modern R packages (ggplot2) while the manual version used base R.

---

## 2. Readability

- **Manual version**: More straightforward. Code follows a simple linear flow. Easier for beginners to understand.
- **AI version**: More elegant visually (ggplot2, seaborn styling). But requires familiarity with additional packages.

**Verdict:** Manual wins for clarity; AI wins for visual polish.

---

## 3. AI Bugs & Omissions

| Issue | Found | Fixed? |
|-------|-------|--------|
| Hallucinated packages | None | N/A |
| Wrong version numbers | None | N/A |
| %% instead of % in Python | Yes | Fixed |
| Notebook source formatting | Yes (characters as cells) | Fixed |

**The AI code ran correctly after minor fixes.** No hallucinated packages or versions.

---

## 4. CLI Behavior

Both CLIs behave identically:
```
python linear_regression_python.py <filename> <x_col> <y_col>
Rscript linear_regression_r.R <filename> <x_col> <y_col>
```
- Same argument order
- Same output format (slope, intercept, R-squared)
- Same output filename convention
- Error messages for missing arguments are reasonable in both

---

## 5. Tools Used

- **AI tool**: Cursor (GPT-4o / Claude)
- **Prompts**: See ai/PROMPTS.md
- **Manual**: All code typed by hand, no AI assistance
