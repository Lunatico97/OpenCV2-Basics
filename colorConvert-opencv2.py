
# Perform color conversion on images using OpenCV2
import cv2
import numpy as num ;

print('Hello World') ;

# Read images - imread(imgPath, readMode) and generates the matrix of pixels
image = cv2.imread("media/cropped-diwas_highres.jpeg") ;

# Convert color spectrum of images - cvtColor(matrixOfPixels, COLOR_ATTRIBUTE)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ; # RGB-scale to gray-scale'

# Blur image using Gaussian Blur ALgorithm - GaussianBlur(matrixOfPixels, kernelSize, sigma)
# image = cv2.GaussianBlur(image, (7,7), 0) ;

# Get the edges of an image using Canny Algorithm - Canny(matrixOfPixels, threshold1, threshold2)
image = cv2.Canny(image, 150, 150) ;

# Dilate the image - dilate(srcImage, kernel, no. of iterations) 
kernel = num.ones((3, 3), num.uint8) ;
image = cv2.dilate(image, kernel, iterations = 1) ;

# Erode the image - erode(scrImage, kernel, no. of iterations)
image = cv2.erode(image, kernel, iterations = 1) ;

# Display images - imshow(windowTitle, matrixOfPixels)
cv2.imshow("IMAGE", image) ;
# Wait for key event triggers i.e. create delays - 0 for infinite ms 
cv2.waitKey(0) ;
