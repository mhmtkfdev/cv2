import cv2

def trackbar(deger):
    global bul_deger
    bul_deger = deger
    bulanık = cv2.blur(gri,(bul_deger,bul_deger))
    cv2.imshow("bulanik_cicek",bulanık)

gri = cv2.imread("hafta6\cicekk.jpg",0)

cv2.namedWindow("bulanik_cicek")
cv2.createTrackbar("Bulaniklastirma_degeri","bulanik_cicek",1,100,trackbar)

cv2.waitKey(0)
cv2.destroyAllWindows()