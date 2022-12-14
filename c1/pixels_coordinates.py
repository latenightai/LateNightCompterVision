import cv2
import numpy as np

img = cv2.imread("test.png")

print("Shape= ", img.shape)
print("No of pixels ", img.size)

print("Image type", img.dtype)

b, g, r = cv2.split(img)

cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)
# m1 = cv2.merge((g, b, r))
# cv2.imshow(m1)
# cv2.waitKey()
# cv2.destroyAllWindows()
