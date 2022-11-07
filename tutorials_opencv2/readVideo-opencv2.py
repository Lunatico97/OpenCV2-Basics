
# Reading a video using OpenCV2
import cv2

print('Hello World')

# Read a video file - VideoCapture(vieoPath, readMode) and generates the matrix of pixels
frames = cv2.VideoCapture("media/earth_rotation.mp4") ;

loopKey = True ;

while loopKey :
        status, frame = frames.read() ;
        cv2.imshow("VIDEO", frame) ;
        if cv2.waitKey(1) & 0xFF == ord('a') : # ord(char) - returns the unicode of the character to check the key press
            loopKey = False ;