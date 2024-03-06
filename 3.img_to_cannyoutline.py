#Perform basic Image Handling and processing operations on the image is Read an image in python and Convert an Image to show outline using Canny function
 
import cv2
path = "D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg"
img =cv2.imread(path)
cv2.imshow("Original",img)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #for converting img into B/W
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #for bluring the img
imgCanny = cv2.Canny(img,100,200)
cv2.imshow("CannyOutline",imgCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()
