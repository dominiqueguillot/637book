import numpy as np
import matplotlib.pyplot as plt

# Define the ℓ₁ unit ball in 2D
# The boundary is defined by |x| + |y| = 1, which is a diamond shape

# Vertices of the diamond
vertices = np.array([
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 0]  # Close the loop
])

# Plot the ℓ₁ ball
plt.figure(figsize=(6, 6))
plt.plot(vertices[:, 0], vertices[:, 1], 'b-', label=r'$\ell_1$ unit ball')
plt.fill(vertices[:, 0], vertices[:, 1], 'lightblue', alpha=0.5)

# Axes settings
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
#plt.title(r'$\ell_1$ Unit Ball in $\mathbb{R}^2$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.legend()
plt.show()
