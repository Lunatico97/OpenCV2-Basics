
# Manipulate image properties using OpenCV2
import cv2 

image = cv2.imread("media/cropped-diwas_highres.jpeg") ;

# Deduce image properties - matrixOfPixels.shape[w, h, ch]
def deduceImageProperties(image) :
    print("Image Properties: \n Dimensions: " + str(image.shape[0]) + " * " + str(image.shape[1]) 
    + "\n Channels: " + str(image.shape[2])) ;

# Resize an image - resize(matrixOfPixels, (w, h))
image = cv2.resize(image, (300, 300)) ;

# Crop an image - No need for OpenCV2 to update a smaller matrix
def cropImage(image, stx, sty, w, h) :
    crop = image[sty:sty+h, stx:stx+w] ;
    return crop ;

image = cropImage(image, 100, 120, 40, 30 );

deduceImageProperties(image) ;
cv2.imshow("IMAGE", image) ;
cv2.waitKey(0) ;

 