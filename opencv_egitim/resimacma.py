import cv2
import numpy

#resim okunur 
resim = cv2.imread("D:\ieee_python\messi.jpg",0) #0 parametresi siyah beyaz yapmaya yarar
cv2.imshow("Anitkabir",resim) #okuduğumuz resmi göstermemizi sağlar

#cv2.imwrite("yeni.jpg",resim) oluşan resmi kaydetmeye yarar 

cv2.waitKey(0) #bir tuşa basmamızı bekler
cv2.destroyAllWindows() #çarpıya basıldığında bütün pencereler kapanır
