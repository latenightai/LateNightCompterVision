import cv2
from matplotlib.pyplot import contour
import numpy as np

img = cv2.imread('maze_0.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 277, 0)

contours, hierarchy = cv2.findContours(thresh, 1, 2)

print()
print(contours, '\n')

cnt = contours[0]
print(cnt, '\n')
M = cv2.moments(cnt)
print(M, '\n')

# find the centroid 

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print(f"({cx},{cy})")