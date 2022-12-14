import cv2
import numpy as np

# decrease white area
# useful in removing white noises

"""
The kernel slides through the image(as in 2D convolution). A pixel in the original image(either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded(made to zero).
"""
img = cv2.imread("maze_0.png")

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)

cv2.imshow("output", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()