import numpy as np
import cv2

img = cv2.imread("maze_0.png", 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

# (x, y) gives coordinate of top-left

x, y, w, h = cv2.boundingRect(cnt)
print(x, y, w, h)

# aspect ratio
aspect_ratio = float(w)/h

# extent
area = cv2.contourArea(cnt)
rect_area = w*h
extent = float(area)/rect_area

# solidity
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area

# equivalent_dia
equi_diameter = np.sqrt(4*area/np.pi)

# orientation
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
print(angle)

# mask and pixel points
# all the points which comprises that object.

mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))

print(pixelpoints)
#pixelpoints = cv2.findNonZero(mask)

# Maximum Value, Minimum Value and their locations

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img, mask=mask)

# Mean Color or Mean Intensity
mean_val = cv2.mean(img, mask=mask)

# Extreme points

leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
