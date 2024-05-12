import cv2
import numpy

resim = cv2.imread("D:\ieee_python\messi.jpg")

cv2.imshow("messi", resim)
print(resim) #resmin matris karşılığını elde ettik
cv2.waitKey(0)
cv2.destroyAllWindows()