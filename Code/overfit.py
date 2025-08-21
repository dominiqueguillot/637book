import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Generate a few roughly linear points
np.random.seed(0)
x = np.linspace(0, 10, 8)
y = 2 * x + 1 + np.random.normal(scale=2, size=len(x))

# 2. Fit a simple linear regression
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_linear = model.predict(x.reshape(-1, 1))

# 3. Fit a high-degree polynomial (degree = n - 1)
degree = len(x) - 1
coeffs = np.polyfit(x, y, degree)
poly_fit = np.poly1d(coeffs)

# 4. Generate x for smooth plot
x_plot = np.linspace(min(x) - 1, max(x) + 1, 200)
y_poly = poly_fit(x_plot)

# 5. Plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='black', label='Data points')

# Linear fit (dashed)
plt.plot(x, y_linear, 'k--', label='Linear model')

# Overfitting curve
plt.plot(x_plot, y_poly, 'r-', label=f'Polynomial degree {degree} (overfit)')

# Adjust y-axis range: focus around the data & curve
ymin = 0#min(np.min(y_poly), np.min(y)) - 5
ymax = 30#max(np.max(y_poly), np.max(y)) + 5
plt.ylim(ymin, ymax)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Overfit vs. Linear Model')
plt.legend()
plt.show()
