import cv2

img = cv2.imread("test.png")
img = cv2.resize(img, (600, 600))

border = cv2.copyMakeBorder(
    img, 10, 10, 5, 5, cv2.BORDER_CONSTANT, value=[255, 0, 155])

cv2.imshow("res", border)
cv2.waitKey()
cv2.destroyAllWindows()
