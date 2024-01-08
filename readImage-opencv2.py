
# Reading an image using OpenCV2
import cv2

print('Hello World')

# Read images - imread(imgPath, readMode) and generates the matrix of pixels
image = cv2.imread("media/cropped-diwas_highres.jpeg") ;
# Display images - imshow(windowTitle, matrixOfPixels)
cv2.imshow("IMAGE", image) ;
# Wait for key event triggers i.e. create delays - 0 for infinite ms 
cv2.waitKey(0) ;
