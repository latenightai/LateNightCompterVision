import cv2
import numpy as np

img = cv2.imread( 'test.png')
img = cv2.resize(img, (400, 400))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow("Image", img)
cv2.imshow("Th1", th1) 
cv2.imshow("Adaptive 1", th2)
cv2.waitKey()
cv2.destroyAllWindows()