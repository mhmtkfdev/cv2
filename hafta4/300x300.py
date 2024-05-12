import cv2
import numpy

resim = numpy.zeros((300,300,3),dtype="uint8")

cv2.putText(resim,("Mehmet Akif Arslan"),(120,290),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(0,255,0),thickness=1)

yükseklik =resim.shape[0] 
genişlik = resim.shape[1]
merkez_x = genişlik//2
merkez_y = yükseklik//2

yarıçap = 5
cv2.circle(resim,(merkez_x,merkez_y),yarıçap,(0,255,0),thickness=3)

resim[150,150]=(255,0,0)

cv2.line(resim,(300,300),(0,300),(255,255,255),thickness=3)

cv2.imshow("300x300",resim)
cv2.imwrite("300x300.jpg",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()