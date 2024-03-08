#Implement the Black hat technique as a Morphological operation to dilate the foreground regions based on Open CV.


import cv2
import numpy as np
img = cv2.imread("D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg",
cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Original", img)
cv2.imshow("Black Hat", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()