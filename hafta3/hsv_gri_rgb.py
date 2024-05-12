import cv2

resim = cv2.imread("D:\KATOT\hafta3\serim.jpg")

hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)
cv2.imwrite("hsv.jpg",hsv)

gri = cv2.imread("D:\KATOT\hafta3\serim.jpg",0)
cv2.imshow("gri",gri)
cv2.imwrite("gri.jpg",gri)

rgb = cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)
cv2.imshow("rgb",rgb)
cv2.imwrite("rgb.jpg",rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()