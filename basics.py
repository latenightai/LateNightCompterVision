import cv2
print("package imported")
#image_read 

#img = cv2.imread("lena.png")
#cv2.imshow("Output", img)
#cv2.waitKey(0)
#webcam_read

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break