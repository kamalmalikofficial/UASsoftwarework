import cv2
import numpy as np

img = cv2.imread('forestfire.jpg')
cv2.imshow('for',img)

# convert image to hsv color space
hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#color limits of dark brown color

lower_brown = np.array([15, 100, 50])
upper_brown = np.array([25, 255, 255])

#color limits of black shades

lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 50])


#color limits of dark green color

lower_green = np.array([40, 100, 50])
upper_green = np.array([70, 255, 255])


brownlayer = cv2.inRange(hsvimg,lower_brown,upper_brown)

greenlayer = cv2.inRange(hsvimg, lower_green, upper_green)

#in the part of image that contain brown color will get converted into lime yellow and the part 
# that contain green color will get converted into lime blue

img[brownlayer == 255]=(0,255,255)
img[greenlayer == 255]=(234,224,173)


cv2.imshow('forest fire 3',img)

cv2.waitKey(0)
cv2.destroyAllWindows()



