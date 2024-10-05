import cv2
import numpy as ny


# Load image
img = cv2.imread('4.png')


# Apply Gaussian blur to remove noise
blur1 = cv2.GaussianBlur(img,(5,5),0)

# Apply bilateral filter to remove  more noise and edge detection
filter = cv2.bilateralFilter(blur1,8,55,55)

# Apply Canny edge detection 
edges= cv2.Canny(filter,50,200)

# Apply threshold to filter out weak pixels 
_, thresh1 = cv2.threshold(edges, 80,255 ,cv2.THRESH_BINARY)



# adding a another layer of filters and blurs
blur2= cv2.blur(thresh1,(5,5))
_, thresh2 = cv2.threshold(blur2, 22,255 ,cv2.THRESH_BINARY)
filter2 = cv2.bilateralFilter(thresh2,11,55,55)



# Apply Gaussian blur and canny edge to get more accurate results
blur3= cv2.GaussianBlur(filter2,(5,5),0)
edges3 = cv2.Canny(blur3,50,200)


# Find contours
contours, _ = cv2.findContours(edges3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Iterate through contours


for i in contours:
    # Approximate polygon
    epsilon = 0.04* cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, epsilon , True)
  
    # Check if triangle (3 sides)
    if len(approx) == 3:
        # Draw triangle
        cv2.drawContours(img, [i], -1, (0, 255, 0), 5)




cv2.imshow('Triangle Detection', img)
cv2.imshow('Triangle Detectn', edges3)



key =cv2.waitKey(0)
if key == ord('d'):
   cv2.destroyAllWindows()
      


#****************************************************************************
#                           ROUGH WORK
#############################################################################
#############################################################################

# import cv2
# import numpy as np

# # Load image
# img = cv2.imread('7.png')

# # Apply Canny edge detection
# edges = cv2.Canny(img, 50, 220)

# # Apply thresholding
# _, thresh = cv2.threshold(edges, 80, 255, cv2.THRESH_BINARY)

# ############################################################
# ############################################################

# # Apply closing operation to fill gaps
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# # Apply erosion to remove noise
# eroded = cv2.erode(closed, kernel, iterations=1)

# ############################################################
# ############################################################

# # Find contours
# contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Iterate through contours
# for contour in contours:
#     # Approximate polygon
#     epsilon = 0.04 * cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, epsilon, True)
    
#     # Check if triangle (3 sides)
#     if len(approx) == 3:
#         # Draw triangle
#         cv2.drawContours(img, [contour], -1, (0, 255, 0), 5)

# # Display the image with detected triangles
# cv2.imshow('Triangle Detection', img)
# cv2.imshow('Triangle Detecon', edges)
# cv2.imshow('Triangle Dettion', thresh)
# cv2.imshow('Triangle Dection', kernel)
# cv2.imshow('Triangleetection', closed)
# cv2.imshow('Triang Detetion', eroded)




# key =cv2.waitKey(0)
# if key == ord('d'):
#    cv2.destroyAllWindows()
