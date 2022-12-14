import cv2 as c
import numpy as np

def draw(event, x, y, flags, param):
    if event == c.EVENT_LBUTTONDBLCLK:
        c.circle(img, (x, y), 100, (125, 0, 255), 3)
    if event == c.EVENT_RBUTTONDBLCLK:
        c.rectangle(img, (x, y), (x+100, y+75), (123, 125, 55), 2)

c.namedWindow(winname="window")

img = np.zeros((512, 512, 3), np.uint8)
c.setMouseCallback("window", draw)

while True:
    c.imshow("window", img)
    if c.waitKey(1) & 0xFF == 27:
        break

c.destroyAllWindows()