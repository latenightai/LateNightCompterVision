from itertools import count
import cv2
import numpy as np
"""
curve joining all the continuous points(along the boundary), having same color intensity.
"""
# useful in shape analysis, object detection and recognition

# use binary images for better accuracy

img = cv2.imread("maze_0.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for data in contours:
    print(f"The contours gave this data {data}")

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow('output', img)
while True:
    if cv2.waitKey(6) & 0xff == 27:
        break

"""
There are three arguments in cv2.findContours() function, first one is source image, second
is contour retrieval mode, third is contour approximation method. And it outputs the
contours and hierarchy. contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
"""


"""
If you pass cv2.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points? For eg, you found the contour of a straight line. Do you need all the points on the line to represent that line? No, we need just two end points of that line. This is what cv2.CHAIN_APPROX_SIMPLE does. It removes all redundant points and compresses the contour, thereby saving memory.
"""
