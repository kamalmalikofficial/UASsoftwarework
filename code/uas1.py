# warming up the opencv, this code will just open the camera and show video
import cv2

capt= cv2.VideoCapture(0)              # initialize the camera

while True:                            # starts a countineous loop till camera is open
    ret,frame= capt.read()             # read the video and store them in a frame variable
    cv2.imshow("camera",frame)         # start displaying frame by frame 

    key =cv2.waitKey(1)                # waitkey(1) means each frame last for 1 ms.
    if key == ord('q'):                # if key q is pressed
        break                          # then the whole loop will get terminated
        
capt.release()
cv2.destroyAllWindows()
