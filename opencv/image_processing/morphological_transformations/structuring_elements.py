import cv2
"""
in general we create a rectangular shape as structuring element. But in some cases, we need to design the structuring element manully such as circle, elliptical etc.
"""
# rectangular kernel
cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# elliptical kernel
cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

# cross-shaped kernel
cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))