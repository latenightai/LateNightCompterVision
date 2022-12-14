import cv2 as c

img = c.imread("test.png")
img = c.resize(img, (500, 600))

img = c.line(img, (0,0), (200, 200), (245, 7, 31), 5)

"""
1. Arrow
2. Rectangle
3. Circles
4. Fronrt: putText
5. Eclipse
Black image: np.zeros([512, 512, 3], np.uint8)*255
White image: np.ones([512, 512, 3], np.uint8)*255

"""

c.imshow("res", img)
c.waitKey(0)
c.destroyAllWindows()
