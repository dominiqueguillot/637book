import matplotlib.pyplot as plt

# Updated data: added 1.0 with value 0
x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
colors = ['blue' if val == 0 else 'red' for val in y]

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 1.5))

# Plot the interval [0, 1]
ax.hlines(0, 0, 1, colors='black', linewidth=2)

# Plot the dots
ax.scatter(x, [0]*len(x), color=colors, s=100, zorder=2)

# X-axis ticks every 0.1
ax.set_xticks([i/10 for i in range(11)])

# Remove y-axis ticks
ax.set_yticks([])

# Tight limits
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.1, 0.1)

# Remove box around plot
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# No x-axis label
ax.set_xlabel('')

# Updated title
ax.set_title('Blue = no cancer, Red = cancer')

plt.tight_layout()
plt.show()
