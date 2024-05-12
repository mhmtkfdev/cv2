import cv2

resim = cv2.imread("D:\KATOT\hafta3\serim.jpg")

yüksek = cv2.resize(resim,None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC)
düşük = cv2.resize(resim,None,fx=0.2,fy=0.2,interpolation=cv2.INTER_CUBIC)

cv2.imshow("dusuk",düşük)
cv2.imshow("yuksek",yüksek)
cv2.imwrite("dusukk.jpg",düşük)
cv2.imwrite("yuksek.jpg",yüksek)

cv2.waitKey(0)
cv2.destroyAllWindows()