import cv2 
import numpy

def fare (islem,x,y,flags,param):
    if islem == cv2.EVENT_LBUTTONDOWN:
        print(f"İmlecin konumu: x={x},y={y}")
        resim[y,x] = [255,0,0]

resim = numpy.zeros((300,300,3),dtype="uint8")

cv2.imshow("mavi",resim)
cv2.setMouseCallback("mavi",fare)

while True:
    cv2.imshow("mavi",resim)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    elif cv2.waitKey(1) & 0xFF == ord("s"):
        cv2.imwrite("cicekk",resim)
        print("görüntü kaydedildi")
    elif cv2.waitKey(1) & 0xFF == ord("e"):
        resim = numpy.zeros((300,300,3),dtype="uint8")
        print("Ekran temizlendi")
cv2.destroyAllWindows()