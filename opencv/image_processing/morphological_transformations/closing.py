import cv2
import numpy as np

#dilation followed by erosion
#useful in closing small holes inside the foreground objects.

img = cv2.imread("maze_0.png")

kernel = np.ones((5, 5), np.uint8)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow("output", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()