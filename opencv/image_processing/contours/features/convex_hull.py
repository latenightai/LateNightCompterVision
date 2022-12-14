import cv2
import numpy as np


"""
Convex Hull will look similar to contour approximation, but it is not (Both may provide same results in some cases). Here, cv2.convexHull() function checks a curve for convexity defects and corrects i
"""

img = cv2.imread('maze_0.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
hull = cv2.convexHull(cnt)
print(hull)

# checking convexity
print(cv2.isContourConvex(cnt))
