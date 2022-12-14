import cv2
import numpy as np

# difference between input image and opening of the image.

img = cv2.imread("maze_0.png")

kernel = np.ones((5, 5), np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("output", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
