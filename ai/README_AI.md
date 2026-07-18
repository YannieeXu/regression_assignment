# Linear Regression with Diagnostics

This project performs linear regression analysis on salary data using years of experience as the predictor. Both Python and R implementations include diagnostic metrics and annotated plots.

## Files
- `linear_model_python.ipynb` / `linear_model_r.ipynb`: Jupyter notebooks
- `linear_model.py` / `linear_model.R`: CLI scripts that accept filename, x-column, and y-column arguments
- `regression_plot_python.png` / `regression_plot_r.png`: Output regression plots with annotations
- `environment.yml` / `setupenv.sh`: Conda environment configuration

## Diagnostics
- Slope and Intercept of the fitted line
- Pearson correlation coefficient (r)
- Mean Squared Error (MSE)

## Usage
### Jupyter Notebooks
```bash
jupyter lab
```

### Command Line
```bash
python linear_model.py regression_data.csv YearsExperience Salary
Rscript linear_model.R regression_data.csv YearsExperience Salary
```
