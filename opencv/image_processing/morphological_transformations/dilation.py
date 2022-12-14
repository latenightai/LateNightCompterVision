import cv2
import numpy as np
# increases white area
# noise removal

img = cv2.imread("maze_0.png")

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("output", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()