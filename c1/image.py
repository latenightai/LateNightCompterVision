import cv2

img = cv2.imread("test.png", 1)
#img = cv2.resize(img, (1280, 700))

cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
