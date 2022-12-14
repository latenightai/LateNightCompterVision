import cv2

path = 'lena.png'
img = cv2.imread(path)
cv2.imshow("Original", img)
cv2.waitKey(0) 