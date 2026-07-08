import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_col> <y_col>")
    sys.exit(1)

df = pd.read_csv(sys.argv[1])
X = df[[sys.argv[2]]]
y = df[sys.argv[3]]

model = LinearRegression().fit(X, y)
y_pred = model.predict(X)

slope = model.coef_[0]
intercept = model.intercept_
r2 = r2_score(y, y_pred)

print("Slope: %.4f" % slope)
print("Intercept: %.4f" % intercept)
print("R-squared: %.4f" % r2)

plt.figure(figsize=(8,6))
plt.scatter(X, y, alpha=0.7, label="Data")
plt.plot(X, y_pred, color="red", lw=2, label="Regression Line")
plt.xlabel(sys.argv[2]); plt.ylabel(sys.argv[3]); plt.title("Linear Regression (AI)")
plt.grid(True, alpha=0.3); plt.legend()
plt.savefig("linear_regression_python_output.png", dpi=150)
print("Saved: linear_regression_python_output.png")
