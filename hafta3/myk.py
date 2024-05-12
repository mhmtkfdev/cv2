import cv2

resim = cv2.imread("D:\KATOT\hafta3\serim.jpg")
cv2.imshow("anitkabir",resim)

mavi = resim[:,:,0]
kırmızı = resim[:,:,2]
yeşil = resim[:,:,1]

print(kırmızı)
cv2.imshow("kirmizi",kırmızı)
cv2.imwrite("kirmiziKanal.jpg",kırmızı)

print(mavi)
cv2.imshow("mavi",mavi)
cv2.imwrite("mavi_kanal.jpg",mavi)

print(yeşil)
cv2.imshow("yesil",yeşil)
cv2.imwrite("yesil_kanal.jpg",yeşil)

cv2.waitKey(0)
cv2.destroyAllWindows()