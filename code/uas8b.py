import cv2
import numpy as np

# Load image
img = cv2.imread('4.png')


#limits of red color
lower_red = np.array([0, 0,255])
upper_red = np.array([0, 0, 255])

#limits of blue color
lower_blue = np.array([100, 0, 0])
upper_blue = np.array([255, 0, 0])


redmask =   cv2.inRange(img, lower_red, upper_red)
bluemask = cv2.inRange(img, lower_blue, upper_blue)





# Apply Gaussian blur to remove noise
blur1 = cv2.GaussianBlur(redmask,(5,5),0)

# Apply bilateral filter to remove  more noise and edge detection
filter1 = cv2.bilateralFilter(blur1,8,55,55)

# Apply Canny edge detection 
edges1= cv2.Canny(filter1,50,200)

# Apply threshold to filter out weak pixels 
_, thresh1 = cv2.threshold(edges1, 80,255 ,cv2.THRESH_BINARY)


#SIMILARLY DENOISEING THE BLUE FILTER 
blur2 = cv2.GaussianBlur(bluemask,(5,5),0)
filter2 = cv2.bilateralFilter(blur2,8,55,55)
edges2= cv2.Canny(filter2,50,200)
_, thresh2 = cv2.threshold(edges2, 80,255 ,cv2.THRESH_BINARY)

rtc =0
btc = 0

##########################################################################################
# Find contours
contours1, _ = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Iterate through contours


for i in contours1:
    # Approximate polygon
    epsilon = 0.04* cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, epsilon , True)
  
    # Check if triangle (3 sides)
    if len(approx) == 3:
        rtc += 1
        # Draw triangle
        cv2.drawContours(img, [i], -1, (0, 0,255), 5)


##########################################################################################
# Find contours
contours2, _ = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Iterate through contours


for i in contours2:
    # Approximate polygon
    epsilon = 0.04* cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, epsilon , True)
  
    # Check if triangle (3 sides)
    if len(approx) == 3:
        btc += 1
        # Draw triangle
        cv2.drawContours(img, [i], -1, (255, 0,0), 5)





cv2.imshow('Triangle Detection', img)

print("red triangle count = ",rtc,)
print("\nblue triangle count = ",btc,)



key =cv2.waitKey(0)
if key == ord('d'):
   cv2.destroyAllWindows()