
# Writing an image using OpenCV2
import cv2
import numpy as num

image = num.zeros((100,100), num.uint8) ;

# Display images - imshow(windowTitle, matrixOfPixels)
cv2.imshow("IMAGE", image) ;
# Wait for key event triggers i.e. create delays - 0 for infinite ms 
cv2.waitKey(0) ;


