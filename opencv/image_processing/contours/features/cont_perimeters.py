import cv2
import numpy as np

img = cv2.imread('maze_0.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
perimeter = cv2.arcLength(cnt, True)
print(perimeter)