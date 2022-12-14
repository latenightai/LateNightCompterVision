import cv2
import numpy as np

#difference between dilation and erosion of an image.
# make white area black and vice versa

img = cv2.imread("maze_0.png")

kernel = np.ones((5, 5), np.uint8)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("output", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()