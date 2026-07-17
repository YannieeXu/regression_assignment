# Linear Regression Analysis

## Overview
This project demonstrates linear regression analysis using Python and R Jupyter Notebooks, along with standalone CLI scripts.

## Dataset
- regression_data.csv: Salary data by years of experience (10 observations)
- Columns: YearsExperience, Salary

## Files (manual/)
- linear_regression_python.ipynb: Python Jupyter Notebook with Markdown explanations
- linear_regression_r.ipynb: R Jupyter Notebook with Markdown explanations
- linear_regression_python.html / linear_regression_r.html: HTML exports
- linear_regression_python.py: Python CLI script
- linear_regression_r.R: R CLI script
- linear_regression_python_output.png / linear_regression_r_output.png: output plots
- regression_data.csv: source dataset

## Files (ai/)
- linear_regression_python.ipynb / linear_regression_r.ipynb: AI-generated notebooks
- linear_regression_python.html / linear_regression_r.html: HTML exports
- linear_regression_python.py: AI-generated Python CLI script
- linear_regression_r.R: AI-generated R CLI script
- linear_regression_python_output.png / linear_regression_r_output.png: output plots
- PROMPTS.md: record of prompts used with the AI tool

## Results
- R-squared: 0.7852
- Slope: 8285.29, Intercept: 29203.52

## How to Run

### Notebooks
Start JupyterLab from the notebook folder:

# For manual notebooks:
cd manual/
jupyter lab

# For AI notebooks:
cd ai/
jupyter lab

### CLI Scripts
python manual/linear_regression_python.py manual/regression_data.csv YearsExperience Salary
Rscript manual/linear_regression_r.R manual/regression_data.csv YearsExperience Salary
