import cv2
import numpy 

resim = cv2.imread("D:\KATOT\hafta3\serim.jpg",0)
esik = 128

ret,binary = cv2.threshold(resim,esik,255,cv2.THRESH_BINARY)

cv2.imshow("binary",binary)
cv2.imwrite("binary.jpg",binary)


kernel = numpy.ones((5,5),numpy.uint8)
dilate = cv2.dilate(resim,kernel,iterations=3)
cv2.imshow("dilate",dilate)
cv2.imwrite("dilate.jpg",dilate)

erosion = cv2.erode(resim,kernel,iterations=1)
cv2.imshow("erosion",erosion)
cv2.imwrite("erosion.jpg",erosion)

cv2.waitKey(0)
cv2.destroyAllWindows(),