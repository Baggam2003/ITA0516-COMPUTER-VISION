#Perform basic Image Handling and processing operations on the image• Read an image in python and Erode an Image using erode function 

import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(f"Kernal Size:\n{kernel}")
path = "D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg"
img =cv2.imread(path)
cv2.imshow("Original",img)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny = cv2.Canny(imgBlur,100,200)
# imgDilation = cv2.dilate(imgCanny,kernel , iterations = 10)
imgEroded = cv2.erode(img,kernel,iterations=2)
cv2.imshow("Img Erosion",imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
