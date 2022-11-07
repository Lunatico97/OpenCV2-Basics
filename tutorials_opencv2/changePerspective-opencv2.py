
# Changing the perspective of an image in OpenCV2

import cv2
import numpy as num

image = cv2.imread("media/cheat_exam.jpg") ;
newImage = image ;

imagePoints = num.float32([[190,0],[130,230],[420,60],[340,290]]) ; # For corner points of image portion that needs change in perspective
perspectivePoints = num.float32([[0,0],[0,290],[320,0],[320,290]]) ; # For corner points of that portion within the new window for a different perspective
# If you don't use float32, you need to since, the vectors are supposed to be CV_32F for perspective matrix

# Get the perspective matrix - getPerspectiveTransform(CV_32F imgPts, CV_32F newImgPts)
perspectiveMatrix = cv2.getPerspectiveTransform(imagePoints, perspectivePoints) ;
# Get the new matrix of pixels as per the perspective(matrixOfPixels, perspectiveMatrix, (w, h))
newImage = cv2.warpPerspective(image, perspectiveMatrix, (320, 290)) ;

cv2.imshow("IMAGE", image)
cv2.imshow("PERSPECTIVE", newImage) ;

cv2.waitKey(0) ;
