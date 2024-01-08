
# Reading from a camera using OpenCV2
import cv2

print('Hello World')

# Read a video file - VideoCapture(vieoPath, readMode) and generates the matrix of pixels
frames = cv2.VideoCapture(0) ; # 0 - Default Capture Device - 1st param
frames.set(3, 640) ; # 3 and 4 params - Frame Dimensions (w*h)
frames.set(4, 480) ;
frames.set(10, 10) ; # 10 param - Contrast

loopKey = True ;

while loopKey :
        status, frame = frames.read() ;
        cv2.imshow("VIDEO", frame) ;
        if cv2.waitKey(1) & 0xFF == ord('a') : # ord(char) - returns the unicode of the character to check the key press
            loopKey = False ;