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

try:
    data = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)
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
label = "y = {:.2f}x + {:.2f}\\nr = {:.2f}\\nMSE = {:.2f}".format(slope, intercept, r_value, mse)
plt.text(0.05, 0.95, label,
         transform=plt.gca().transAxes, fontsize=10, verticalalignment="top")
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title(f"{y_col} vs {x_col}")
plt.savefig("regression_plot_python.png")
plt.show()
