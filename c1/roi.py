import cv2
import numpy as np

img = cv2.imread("Data\\roi_opr.jpg")
img = cv2.resize(img, (800, 800))

roi = img[50:205, 320:440]

img[50:205, 431:551] = roi
img[50:205, 552:672] = roi
img[50:205, 200:320] = roi
img[50:205, 80:200] = roi

img[400:555, 60:180] = roi
cv2.imshow("original image==", img)

img1 = cv2.imread("H:\\Data\\ironman.jpg")
img1 = cv2.resize(img1, (900, 600))
img1[1:156, 560:680] = roi

cv2.imshow("ironman", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
