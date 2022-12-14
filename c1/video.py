import cv2
cap = cv2.VideoCapture(1)

# save_video = cv2.VideoWriter_fourcc(*"XVID")
# output = cv2.VideoWriter("output.avi", save_video, 20.0 (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    #frame = cv2.resize(frame, (700, 450))
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(25)
 #   output.write(frame)
    if k == ord("q") & 0xFF:
        break
cap.release()
# output.release()
cv2.destroyAllWindows()