import cv2
import numpy as np

# Load the image
image = cv2.imread('1.png')

# Convert to HSV color space (better for color segmentation)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#limits of dark green color

lower_green = np.array([40, 100, 50])
upper_green = np.array([80, 255, 255])

greenmask = cv2.inRange(hsv, lower_green, upper_green)

blurgreenmask = cv2.GaussianBlur(greenmask,(5,5),0)
filtergreenmask = cv2.bilateralFilter(blurgreenmask,8,55,55)
edges= cv2.Canny(filtergreenmask,50,200)
_, threshgreen = cv2.threshold(edges, 80,255 ,cv2.THRESH_BINARY)





# adding a another layer of filters and blurs
blurgreen2= cv2.blur(threshgreen,(5,5))
_, threshgreen2 = cv2.threshold(blurgreen2, 22,255 ,cv2.THRESH_BINARY)
filtergreen2 = cv2.bilateralFilter(threshgreen2,11,55,55)



blurgreen3= cv2.GaussianBlur(filtergreen2,(5,5),0)
edgesgreen3 = cv2.Canny(blurgreen3,50,200)


# Find contours in the edges
contours, _ = cv2.findContours(edgesgreen3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop through contours to find triangles and color them
for cnt in contours:
    # Approximate to detect if the shape is a triangle
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
    if len(approx) == 3: 
        cv2.drawContours(image, cnt, 0, (113,169,44), -10) 
        cv2.drawContours(image, cnt, 0, (113,169,44), 10) 
        



cv2.imshow("imagic",image)

hsvimg99 =cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
greenmask99 =cv2.inRange(hsvimg99,lower_green,upper_green)
cv2.imshow("grensk",greenmask99)


image[greenmask99==255] = (0,0,0)



cv2.imshow("newimage",image)

key =cv2.waitKey(0)
if key == ord('d'):
   cv2.destroyAllWindows()
