import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# line
cv2.line(img, (384, 0), (510, 128), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (340, 0), (510, 128), (0, 255, 0), 3)

# circle
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# ellipse
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))

# Adding text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
