import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error

if len(sys.argv) != 4:
    print("Usage: python linear_model.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
x = data[x_col]
y = data[y_col]

slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)

print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"Correlation coefficient (r): {r_value:.4f}")
print(f"MSE: {mse:.4f}")

plt.scatter(x, y, color="red")
plt.plot(x, y_pred, color="blue")
plt.text(0.05, 0.95,
         f"y = {slope:.2f}x + {intercept:.2f}\nr = {r_value:.2f}\nMSE = {mse:.2f}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment="top",
         bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title(f"{y_col} vs {x_col}")
plt.savefig("regression_plot_python.png")
plt.show()
