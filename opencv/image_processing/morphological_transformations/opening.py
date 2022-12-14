import cv2
import numpy as np

#errosion followed by dilation
#useful in removing noise

img = cv2.imread("maze_0.png")

kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow("output", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

