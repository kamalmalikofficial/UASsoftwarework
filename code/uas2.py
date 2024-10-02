import cv2
import numpy as np

capt = cv2.VideoCapture(0)

while True:                          # a continious loop starts here
    ret,frame =capt.read()     # read each frame from the capt

    hsvframe = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)     # convert each frame to hsv format

    #defining the color range to detect color
    lower_green = np.array([45, 100, 50])
    upper_green = np.array([75, 255, 255])

    # mask to get only green color
    maskframe = cv2.inRange(hsvframe,lower_green,upper_green)

    cv2.imshow("orignal image",frame)
    cv2.imshow("hsv  image",hsvframe)
    cv2.imshow("detected color", maskframe)

    key= cv2.waitKey(1)
    if key == ord('q'):
        break
capt.release()
cv2.destroyAllWindows()
