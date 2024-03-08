# Implement the Top hat technique as a Morphological operation
# to dilate the foreground regions based on Open CV.

import cv2
import numpy as np

# Read the image
image = cv2.imread('D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg', 0)  # Read the image in grayscale

# Define the kernel for the opening operation
kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel with all ones

# Apply opening (erosion followed by dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Compute the top hat image (original image - opening)
top_hat = cv2.subtract(image, opening)

# Display the original and top hat images
cv2.imshow('Original Image', image)
cv2.imshow('Top Hat Image', top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
