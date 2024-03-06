#Perform basic Image Handling and processing operations on the image• Read an image in python and Dilate an Image using Dilate function

import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(f"Kernal Size:\n{kernel}")
path = "D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg"
img =cv2.imread(path)
cv2.imshow("Original",img)
imgDilation = cv2.dilate(img,kernel , iterations = 10)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)
cv2.imshow("Img Erosion",imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()