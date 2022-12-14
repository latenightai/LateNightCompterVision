import cv2
import numpy as np

#difference between closing of the input image and input image

img = cv2.imread("maze_0.png")

kernel = np.ones((5, 5), np.uint8)

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("output", black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()