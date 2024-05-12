import cv2

resim = cv2.imread("D:\KATOT\hafta3\serim.jpg")
bulandır = cv2.blur(resim,(1,100))

cv2.imshow("bulanik",resim)
cv2.imwrite("bulanik.jpg",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()