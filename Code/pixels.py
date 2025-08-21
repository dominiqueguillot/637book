import numpy as np
import matplotlib.pyplot as plt

# Image dimensions
width, height = 200, 200
total_pixels = width * height

# Number of white and black pixels
white_pixels = int(total_pixels * 0.49)
black_pixels = total_pixels - white_pixels

# Create the pixel array: 1 for white, 0 for black
pixels = np.array([1] * white_pixels + [0] * black_pixels)

# Shuffle to randomize
np.random.shuffle(pixels)

# Reshape to image dimensions
image = pixels.reshape((height, width))

# Plot the image
plt.imshow(image, cmap='gray', vmin=0, vmax=1)