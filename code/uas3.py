import cv2
import numpy as np

img =cv2.imread('forestfire.png')
hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('forest fire 1',img)


# limits of dark green color
lower_green = np.array([40, 100, 50])
upper_green = np.array([70, 255, 255])




# make a mask of green color
greenlayer = cv2.inRange(hsvimg, lower_green, upper_green)

# in the part of image that contain green color will get converted into light blue
img[greenlayer == 255]=(245,245,9)




cv2.imshow('forest fire 2',img)

key = cv2.waitKey(0)
if key ==ord('q'):
    cv2.destroyAllWindows()