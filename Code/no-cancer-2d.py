import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
x = np.arange(0, 1.01, 0.1)
y = np.arange(0, 1.01, 0.1)
xx, yy = np.meshgrid(x, y)

# Flatten to 1D arrays for plotting
x_points = xx.flatten()
y_points = yy.flatten()

# Generate clustered colors:
# For example, make the top-left and bottom-right mostly red, others mostly blue.
colors = []
for xi, yi in zip(x_points, y_points):
    if (xi < 0.5 and yi > 0.5) or (xi > 0.5 and yi < 0.5):
        # Cluster region 1: mostly red
        color = 'red' if np.random.rand() < 0.8 else 'blue'
    else:
        # Cluster region 2: mostly blue
        color = 'blue' if np.random.rand() < 0.8 else 'red'
    colors.append(color)

# Create figure
fig, ax = plt.subplots(figsize=(6, 6))

# Plot all dots
ax.scatter(x_points, y_points, color=colors, s=100)

# Set limits and ticks
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.set_xticks(np.arange(0, 1.1, 0.1))
ax.set_yticks(np.arange(0, 1.1, 0.1))

# Add grid lines for clarity
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add title
ax.set_title('Blue = no cancer, Red = cancer (clusters)')

# Remove top/right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
