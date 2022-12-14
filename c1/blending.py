import cv2
import numpy as np

img1 = cv2.imread("test.png")
img1 = cv2.resize(img1, (300, 400))

img2 = cv2.imread("thor.jpg")
img2 = cv2.resize(img2, (300, 400))

result = cv2.add(img1, img2)
result2 = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

cv2.imshow("res", result2)
cv2.imshow("res1", result)
cv2.waitKey()
cv2.destroyAllWindows()
