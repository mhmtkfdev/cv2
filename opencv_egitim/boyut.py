import cv2
import numpy

resim = cv2.imread("D:\ieee_python\messi.jpg")

cv2.imshow("messi", resim)


print(resim.size) #resmin boyutunu verir
print(resim.dtype) #resmin hangi türde veri kullandığını verir
print(resim.shape) #kaç kanaldan oluştuğunu söyler ve boyut bilgisini (genişlik ve yükseklik olarak )verir 



cv2.waitKey(0)
cv2.destroyAllWindows()