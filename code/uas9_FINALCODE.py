import cv2
import numpy as np

# Load the image
image = cv2.imread('4.png')
reuseimage = image
cv2.imshow('orignal image',image)

# Convert to HSV color space (better for color segmentation)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


#limits of dark green color

lower_green = np.array([40, 100, 50])
upper_green = np.array([80, 255, 255])
#color limits of dark brown color

lower_brown = np.array([15, 100, 50])
upper_brown = np.array([25, 255, 255])

#color limits of black shades
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 50])

lower_red = np.array([0, 0,255])
upper_red = np.array([0, 0, 255])

#limits of blue color
lower_blue = np.array([255, 0, 0])
upper_blue = np.array([255, 0, 0])



########################################################################################################
#                    FUNCTIONS THAT DO CALCULATIONS
########################################################################################################
def calculation1(rting,bting,rtinb,btinb):
    l1 =[rtinb+btinb,rting+bting]
    print("\n ",l1,"    houses on bruntgrass         houses on greengrass")
    return

def calculation2(rting,bting,rtinb,btinb):
    p1 = (btinb*2)+(rtinb*1)
    p2 =(bting*2)+(rting*1)
    pr =p1/p2
    l2 =[p1,p2]
    l3 =[pr]
    print(" ",l2,"  Priority of houses on brunt grass       Priority of houses on green grass")
    print(" ",l3,"  Priority ratio")
    return

########################################################################################################
#                    THIS CODE WILL COUNT ALL THE RED AND BLUE TRIANGLE
########################################################################################################




redmask =   cv2.inRange(image, lower_red, upper_red)
bluemask = cv2.inRange(image, lower_blue, upper_blue)


# Apply Gaussian blur to remove noise
blurRED = cv2.GaussianBlur(redmask,(5,5),0)

# Apply bilateral filter to remove  more noise and edge detection
filterRED = cv2.bilateralFilter(blurRED,8,55,55)

# Apply Canny edge detection 
edgesRED= cv2.Canny(filterRED,50,200)

# Apply threshold to filter out weak pixels 
_, threshRED = cv2.threshold(edgesRED, 80,255 ,cv2.THRESH_BINARY)


#SIMILARLY DENOISEING THE BLUE FILTERBLUE
blurBLUE = cv2.GaussianBlur(bluemask,(5,5),0)
filterBLUE = cv2.bilateralFilter(blurBLUE,8,55,55)
edgesBLUE= cv2.Canny(filterBLUE,50,200)
_, threshBLUE = cv2.threshold(edgesBLUE, 80,255 ,cv2.THRESH_BINARY)

trt =0
tbt = 0

##########################################################################################
# Find contours
contoursRED, _ = cv2.findContours(threshRED, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Iterate through contours


for i in contoursRED:
    # Approximate polygon
    epsilon = 0.04* cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, epsilon , True)
  
    # Check if triangle (3 sides)
    if len(approx) == 3:
        trt += 1
        # Draw triangle
        cv2.drawContours(image, [i], -1, (0, 0,255), 5)


##########################################################################################
# Find contours
contours2, _ = cv2.findContours(threshBLUE, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Iterate through contours


for i in contours2:
    # Approximate polygon
    epsilon = 0.04* cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, epsilon , True)
  
    # Check if triangle (3 sides)
    if len(approx) == 3:
        tbt += 1
        # Draw triangle
        cv2.drawContours(image, [i], -1, (255, 0,0), 5)




print("Total red triangle = ",trt)
print("Total blue triangle  = ",tbt)

########################################################################################################
#                    THIS CODE WILL CONVERT IMAGE INTO FINAL IMAGE OF YELLOW AND CYAN BLUE
########################################################################################################

reuseblurimage = cv2.GaussianBlur(reuseimage,(5,5),0)
reusehsv=cv2.cvtColor(reuseblurimage,cv2.COLOR_BGR2HSV)
regreenlayer = cv2.inRange(reusehsv, lower_green, upper_green)
rebrownlayer = cv2.inRange(reusehsv, lower_brown, upper_brown)
reblacklayer = cv2.inRange(reusehsv, lower_black, upper_black)

image[rebrownlayer == 255]=(0,255,255)
image[regreenlayer == 255]=(234,224,173)
image[reblacklayer == 255]=(0,255,255)
cv2.imshow('final image',image)


########################################################################################################
#                      THIS CODE WILL REMOVE GREEN COLOR ALONG WITH TRIANGLE WITHIN ITS
########################################################################################################

brownlayer = cv2.inRange(hsv,lower_brown,upper_brown)
greenlayer = cv2.inRange(hsv, lower_green, upper_green)


blurgreenmask = cv2.GaussianBlur(greenlayer,(5,5),0)
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

# Loop through contours to find triangles and remove them
for cnt in contours:
    # Approximate to detect if the shape is a triangle
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
    if len(approx) == 3: 
        cv2.drawContours(image, [cnt], 0, (113,169,44), -10) 
        cv2.drawContours(image, [cnt], 0, (113,169,44), 10) 
        

hsvimg99 =cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
greenmask99 =cv2.inRange(hsvimg99,lower_green,upper_green)



image[greenmask99==255] = (0,0,0)

########################################################################################################
#                THIS CODE WILL COUNT RED AND BLUE TRIANGLE IN BROWN AREA
########################################################################################################

#limits of red color



redmask =   cv2.inRange(image, lower_red, upper_red)
bluemask = cv2.inRange(image, lower_blue, upper_blue)





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

rtinb =0
btinb = 0


# Find contours
contours1, _ = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



for i in contours1:
    # Iterate through contours
    # Approximate polygon
    epsilon = 0.04* cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, epsilon , True)
  
    # Check if triangle (3 sides)
    if len(approx) == 3:
        rtinb += 1
        # Draw triangle
        cv2.drawContours(image, [i], -1, (0, 0,255), 5)

# Find contours
contours2, _ = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



for i in contours2:
    # Iterate through contours
    # Approximate polygon
    epsilon = 0.04* cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, epsilon , True)
  
    # Check if triangle (3 sides)
    if len(approx) == 3:
        btinb += 1
        # Draw triangle
        cv2.drawContours(image, [i], -1, (255, 0,0), 5)



########################################################################################################
#                             PRINT STATEMENTS AND FUNCTION CALLING
########################################################################################################



print("\n  red triangle in brunt = ",rtinb,)
print("  blue triangle in brunt = ",btinb,)

rting =trt-rtinb
bting =tbt-btinb

print("\n  red triangle in green = ",rting,)
print("  blue triangle in green = ",bting,)

calculation1(rting,bting,rtinb,btinb)
calculation2(rting,bting,rtinb,btinb)


key =cv2.waitKey(0)
if key == ord('d'):
   cv2.destroyAllWindows()
