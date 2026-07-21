import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error
try:
    filename = sys.argv[1]
    x_col = sys.argv[2]
    y_col = sys.argv[3]
except IndexError:
    print("Usage: python linear_model.py <filename> <x_column> <y_column>")
    sys.exit(1)
data = pd.read_csv(filename)
x = data[x_col].values
y = data[y_col].values
slope, intercept, r_val, p_val, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"Correlation coefficient (r): {r_val:.4f}")
print(f"MSE: {mse:.4f}")
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="red", label="Observed")
plt.plot(x, y_pred, color="blue", linewidth=2, label="Fitted line")
plt.text(0.05, 0.95, f"y = {slope:.2f}x + {intercept:.2f}\nr = {r_val:.2f}\nMSE = {mse:.0f}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment="top",
         bbox=dict(facecolor="white", alpha=0.7))
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title(f"Linear Regression: {y_col} vs {x_col}")
plt.legend()
plt.savefig("regression_plot_python.png", dpi=100)
print("Plot saved as regression_plot_python.png")
