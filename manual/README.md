# Linear Regression Analysis

## Overview
This project demonstrates linear regression analysis using Python and R Jupyter Notebooks, along with standalone CLI scripts.

## Files
- regression_data.csv: synthetic dataset (50 rows, x vs y with noise)
- linear_regression_python.ipynb: Python Jupyter Notebook
- linear_regression_r.ipynb: R Jupyter Notebook
- linear_regression_python.html: HTML export (Python)
- linear_regression_r.html: HTML export (R)
- linear_regression_python.py: Python CLI script
- linear_regression_r.R: R CLI script
- linear_regression_python_output.png: output plot from Python CLI
- linear_regression_r_output.png: output plot from R CLI

## Results
- Slope: 2.38, Intercept: 5.13
- R-squared: 0.9372

## Notes
- CLI scripts and data are in the manual/ folder
- Run from project root: python manual/linear_regression_python.py manual/regression_data.csv x y
- R version: Rscript manual/linear_regression_r.R manual/regression_data.csv x y
