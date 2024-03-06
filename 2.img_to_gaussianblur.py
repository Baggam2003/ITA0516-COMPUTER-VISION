#Perform basic Image Handling and processing operations on the image is Read an image in python and Convert an Image to Blur using Gaussian Blur

import cv2
path = "D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg"
img =cv2.imread(path)
cv2.imshow("Original",img)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #for making img B/W
imgBlur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gaussian Blur",imgBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()
