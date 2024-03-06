# Scaling an image to its Bigger and Smaller sizes.

import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Original",img)
img = cv2.resize(img,(600,600))
cv2.imshow("Resized",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
