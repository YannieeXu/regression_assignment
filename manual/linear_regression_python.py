import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

if len(sys.argv) != 4:
    print('Usage: python linear_regression_python.py <filename> <x_column> <y_column>')
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

df = pd.read_csv(filename)
X = df[[x_col]]
y = df[y_col]

model = LinearRegression().fit(X, y)
y_pred = model.predict(X)

slope = model.coef_[0]
intercept = model.intercept_
r2 = r2_score(y, y_pred)

print(f'Slope: {slope:.4f}')
print(f'Intercept: {intercept:.4f}')
print(f'R-squared: {r2:.4f}')

plt.figure(figsize=(8, 6))
plt.scatter(df[x_col], df[y_col], alpha=0.7, label='Data')
plt.plot(df[x_col], y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title('Linear Regression')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig('linear_regression_python_output.png', dpi=150)
print('Saved: linear_regression_python_output.png')