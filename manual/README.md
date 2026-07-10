# Linear Regression Analysis

## Overview
This project demonstrates linear regression analysis using Python and R Jupyter Notebooks, along with standalone CLI scripts.

## Dataset
- regression_data.csv: Salary data by years of experience (30 observations)
- Columns: YearsExperience, Salary

## Files (manual/)
- linear_regression_python.ipynb: Python Jupyter Notebook with Markdown explanations
- linear_regression_r.ipynb: R Jupyter Notebook with Markdown explanations
- linear_regression_python.html: HTML export (Python)
- linear_regression_r.html: HTML export (R)
- linear_regression_python.py: Python CLI script
- linear_regression_r.R: R CLI script
- linear_regression_python_output.png: output plot from Python CLI
- linear_regression_r_output.png: output plot from R CLI

## Results
- Significant positive relationship between experience and salary (R-squared: 0.7852)
- Slope: 8285.29, Intercept: 29203.52

## How to Run

### Jupyter Notebooks
Start JupyterLab from the project root and open notebooks in the manual/ or ai/ folder:
```bash
cd C:/Users/huangjinjie/assignment2
jupyter lab
```

### CLI Scripts
```bash
# Python
python manual/linear_regression_python.py manual/regression_data.csv YearsExperience Salary

# R
Rscript manual/linear_regression_r.R manual/regression_data.csv YearsExperience Salary
```
