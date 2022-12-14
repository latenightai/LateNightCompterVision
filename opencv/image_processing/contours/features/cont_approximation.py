import cv2
import numpy as np


#important
"""
It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify. It is an implementation of Douglas-Peucker algorithm.
"""

img = cv2.imread('maze_0.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

epsilon = 0.1*cv2.arcLength(cnt,True)

approx = cv2.approxPolyDP(cnt,epsilon, True)

print(approx)