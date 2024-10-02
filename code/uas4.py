import cv2
import numpy as np

img = cv2.imread('forestfire.jpg')
hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#color limits of darkbrown color

lower_brown = np.array([15, 100, 50])
upper_brown = np.array([25, 255, 255])

brownlayer= cv2.inRange(hsvimg, lower_brown, upper_brown)

#in the part of image that contain brown color will get converted into lime yellow
img[brownlayer == 255]=(0,255,255)

cv2.imshow('forest fire 2',img)

cv2.waitKey(0)
cv2.destroyAllWindows()