#ROTATION 90 ALONG DEGREE

import cv2
path=r"D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat.jpg"
src = cv2.imread(path)
cv2.imshow("Original", src)
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated", image)
cv2.waitKey(0)
cv2.destroyAllWindows()