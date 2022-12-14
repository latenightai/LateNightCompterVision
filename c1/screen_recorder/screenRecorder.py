import cv2 as c
import pyautogui as p
import numpy as np

rs = p.size()

fn = input("Enter enter any file name and path ")

fps = 20.0
fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter(fn, fourcc, fps, rs)

c.namedWindow("Live Recording", c.WINDOW_NORMAL)
c.resizeWindow("Live Recording", (300, 200))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f, c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("res", f)
    if c.waitKey(1) == ord("q"):
        break

output.release()
c.destroyAllWindows()

# screen recorder(not optimized)
