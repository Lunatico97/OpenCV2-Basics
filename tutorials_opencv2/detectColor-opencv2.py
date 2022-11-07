
import cv2
import numpy as num

# Callback function for slider position changes
def func() :
    print('Hello') ;
    pass

# Creating track-bars i.e. sliders for OpenCV2 - createTrackbar(sliderName, windowName, initialValue, maxValue, callbackFunction)
cv2.namedWindow("HSV Optimizer") ;
cv2.resizeWindow("HSV Optimizer", 640, 480) ; # HSV values for detecting color - green
cv2.createTrackbar("Hue (Min)", "HSV Optimizer", 28, 179, func) ; # 28 
cv2.createTrackbar("Hue (Max)", "HSV Optimizer", 48, 179, func) ; # 48
cv2.createTrackbar("Saturation (Min)", "HSV Optimizer", 12, 255, func) ; # 12
cv2.createTrackbar("Saturation (Max)", "HSV Optimizer", 255, 255, func) ; # 255
cv2.createTrackbar("Value (Min)", "HSV Optimizer", 61, 255, func) ; # 61 
cv2.createTrackbar("Value (Max)", "HSV Optimizer", 255, 255, func) ; # 255

# Reading the image from the file path
image = cv2.imread("media/apricots.png") ;
image = cv2.resize(image, (300,300)) ;

#Converting image to HSV format (Hue, Saturation, Value)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) ;

# Displaying image with slider UI
looped = True ;

while looped: 
    # Getting slider values - getTrackbarPos(sliderName, windowName)
    hue_min = cv2.getTrackbarPos("Hue (Min)", "HSV Optimizer") ; 
    hue_max = cv2.getTrackbarPos("Hue (Max)", "HSV Optimizer") ; 
    sat_min = cv2.getTrackbarPos("Saturation (Min)", "HSV Optimizer") ;
    sat_max = cv2.getTrackbarPos("Saturation (Max)", "HSV Optimizer") ; 
    val_min = cv2.getTrackbarPos("Value (Min)", "HSV Optimizer") ; 
    val_max = cv2.getTrackbarPos("Value (Max)", "HSV Optimizer") ;
    lowerHSV = num.array([hue_min, sat_min, val_min]) ;
    higherHSV = num.array([hue_max, sat_max, val_max]) ;
    colorMask = cv2.inRange(hsv, lowerHSV, higherHSV) ;
    colorDetected = cv2.bitwise_and(image, image, mask = colorMask) ;
    stack = num.hstack([image, hsv, colorDetected]) ;
    cv2.imshow("HSV Optimizer", colorMask) ;
    cv2.imshow("Color Mask - Green", stack) ;
    if cv2.waitKey(1) & 0xFF == ord('a'): # Make sure you add a small delay but, not zero since the sliders won't trigger events !
        looped = False ;