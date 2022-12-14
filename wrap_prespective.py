import cv2
import numpy as np
img = cv2.imread("cards.jpg")

width, height = 250, 350
pts1 = np.float32([[], [], [], []])
pts2 = np.float32([[], [], [], []])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("image", img)
cv2.imshow("Output", imgOutput)