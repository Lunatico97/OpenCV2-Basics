
# Using OpenCV2 classifiers for face detection in images
# FYI - Classifiers can exist for any thing such that it provides maximal reference for detection
import cv2 
import numpy as num

# Read image from the file path along with the classifier for the face - CascadeClassifier(filePath)
image = cv2.imread("media/lena_soderberg.jpeg") ;
classifier = cv2.CascadeClassifier("media/haar_frontFace.xml") ;
# Convert the image to grayscale (always do this since we don't need color for any pattern recognition)
greyedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ;

# Get the face boundary rectangle using classifier - detectMultiScale(image, scale, minNeighbours) 
faceBound = classifier.detectMultiScale(greyedImage, 1.2, 4) ;

for x,y,w,h in faceBound:
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2) ;

# Display image
cv2.imshow("IMAGE", image) ;
cv2.waitKey(0) ;
