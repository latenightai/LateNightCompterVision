import cv2
import numpy as np

img = cv2.imread('maze_0.png', 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

x, y, w, h = cv2.boundingRect(cnt)

# cv2.rectangle(image, start_point, end_point, color, thickness)

img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# rotated rectangle
"""
rectangle with covering the minimum area

"""
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img,[box],0,(0,0,255),2)

cv2.imshow('image', img)
cv2.imshow('image2', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
