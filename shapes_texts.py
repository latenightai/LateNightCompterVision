import cv2
import numpy as np

img = np.zeros((512, 512, 3),np.uint8)
#img[:] = 245,34,34
cv2.line(img, (0,0), (300, 300), (0, 255, 0),3)
cv2.rectangle(img,(0,0), (250, 350), (0,0, 255), cv2.FILLED)
cv2.putText(img,"Hello OpenCV", (100, 200), cv2.FONT_HERSHEY_COMPLEX,1,(0, 150, 0), 5)

cv2.imshow("Image", img)
cv2.waitKey(0)