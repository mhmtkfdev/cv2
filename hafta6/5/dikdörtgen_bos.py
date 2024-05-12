import cv2
import numpy

bos = numpy.zeros((500,500,3),dtype="uint8")

dikdörtgen_genişliği = int(500 * 0.5)
dikdörtgen_yüksekliği = 500
x = int((500 - dikdörtgen_genişliği) / 2)
y = 0

cv2.rectangle(bos,(x,y),(x+dikdörtgen_genişliği,y+dikdörtgen_yüksekliği),color=(255, 255, 255),thickness=-1)
cv2.imshow("bos",bos)
cv2.imwrite("maske.jpg",bos)

maske = cv2.imread("hafta6\\5\\maske.jpg",cv2.IMREAD_GRAYSCALE)

_ , maske = cv2.threshold(maske,127,255,cv2.THRESH_BINARY)

maskeli = cv2.bitwise_and(bos,bos,mask=maske)

cv2.imshow("maskeli",maskeli)

cv2.waitKey(0)
cv2.destroyAllWindows()