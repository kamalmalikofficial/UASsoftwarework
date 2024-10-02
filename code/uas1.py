import cv2

capt= cv2.VideoCapture(0)
while True:
    ret,frame= capt.read()
    cv2.imshow("camera",frame)

    key =cv2.waitKey(1)
    if key == ord('q'):
        break
capt.release()

cv2.destroyAllWindows()