import cv2
import numpy

def dilation(deger):
    global dilation_cicek
    dilation_deger = cv2.getTrackbarPos("dilation_degeri","dilation")
    kernel = numpy.ones((dilation_deger,dilation_deger),numpy.uint8)
    dilation_cicek = cv2.dilate(binary,kernel,iterations=3)
    cv2.imshow("dilation",dilation_cicek)

def erosion(deger):
    global erosion_cicek
    erosion_deger = cv2.getTrackbarPos("erosion_degeri","erosion")
    kernel=numpy.ones((erosion_deger,erosion_deger),numpy.uint8)
    erosion_cicek = cv2.erode(binary,kernel,iterations=1)
    cv2.imshow("erosion",erosion_cicek)

cicek = cv2.imread("hafta6\cicekk.jpg",0)

esik = 128

_,binary = cv2.threshold(cicek,esik,256,cv2.THRESH_BINARY)

cv2.namedWindow("dilation")
cv2.createTrackbar("dilation_degeri","dilation",1,100,dilation)
dilation(0)

cv2.namedWindow("erosion")
cv2.createTrackbar("erosion_degeri","erosion",1,100,erosion)
erosion(0)

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()