import cv2
import sys

img = cv2.imread(cv2.smaples.findFile("starry_night.jpg"))

if img is None:
    sys.exit("Could not find the image")
cv2.imshow("Display window", img)
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("starry_night.png", img)
