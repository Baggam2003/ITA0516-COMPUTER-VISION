# Implement the Opening technique as a Morphological operation
# to dilate the foreground regions based on Open CV.

import cv2
import numpy as np

# Read the image
image = cv2.imread('D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg', 0)  # Read the image in grayscale

# Define the kernel for opening
kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel with all ones

# Apply opening (erosion followed by dilation)
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Display the original and opened images
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
