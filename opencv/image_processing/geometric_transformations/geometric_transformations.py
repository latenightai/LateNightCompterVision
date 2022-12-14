import cv2 as cv
import numpy as np

# cv.INTER_AREA for shrinking
# cv.INTER_LINEAR for zooming
# cv.INTER_LINEAR for resizing purposes

# Scaling
img = cv.imread("")
res = cv.resize(img, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)

# Translation

rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))

# Rotation
R = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)

dst = cv.wrapAffine(img, M, (cols, rows))


cv.imshow("img", dst)
cv.waitKey()
cv.destroyAllWindows()