import cv2
import numpy as np

img = cv2.imread('maze_0.png',0)
ret,thresh = cv2.threshold(img,127,255,0) 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

"""
what is hierarchy?
Normally we use the cv2.findContours() function to detect objects in an image, right?
Sometimes objects are in different locations. But in some cases, some shapes are inside other shapes. Just like nested figures. In this case, we call outer one as parent and inner one as child. This way, contours in an image has some relationship to each other. And we can specify how one contour is connected to each other, like, is it child of some other contour, or is it a parent etc. Representation of this relationship is called the Hierarchy.

"""
