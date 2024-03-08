#Implement the Closing technique as a Morphological operation
# to dilate the foreground regions based on Open CV.

import cv2
import numpy as np

# Read the image
image = cv2.imread('D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg', 0)  # Read the image in grayscale

# Define the kernel for closing
kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel with all ones

# Apply closing (dilation followed by erosion)
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the original and closed images
cv2.imshow('Original Image', image)
cv2.imshow('Closed Image', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
