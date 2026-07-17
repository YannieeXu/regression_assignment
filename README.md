# Regression Analysis Assignment

This repository contains linear regression analysis in Python and R, with both manual and AI-generated versions.

## Repository Structure
- **manual/**: Hand-written notebooks, CLI scripts, and documentation
- **ai/**: AI-generated equivalents with PROMPTS.md

## Dataset
regression_data.csv ? Salary vs Years of Experience (10 observations)

## Quick Start
```bash
# Manual version
python manual/linear_regression_python.py manual/regression_data.csv YearsExperience Salary
Rscript manual/linear_regression_r.R manual/regression_data.csv YearsExperience Salary

# AI version
python ai/linear_regression_python.py manual/regression_data.csv YearsExperience Salary
Rscript ai/linear_regression_r.R manual/regression_data.csv YearsExperience Salary
```

See manual/README.md for full details.
