import cv2

resim = cv2.imread("D:\KATOT\hafta3\serim.jpg")
cv2.imshow("Anitkabir",resim)
cv2.imwrite("512x512.jpg",resim)

print(resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
