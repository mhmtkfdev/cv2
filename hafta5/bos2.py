import cv2 
import numpy

def fare (islem,x,y,flags,param):
    if islem == cv2.EVENT_LBUTTONDOWN:
        print(f"İmlecin konumu: x={x},y={y}")
        resim[y,x] = [255,0,0]

def imlec_konumu (islem,x,y,flags,param):
    if islem == cv2.EVENT_LBUTTONDOWN:
        print(f"imlecin konumu: x = {x}, y = {y} ")

def basılı (islem,x,y,flags,param):
    if flags & cv2.EVENT_FLAG_LBUTTON:
        resim[y-3:y+1,x-3:x+1] = [255,0,0]

resim = numpy.zeros((300,300,3),dtype="uint8")

cv2.imshow("mavi",resim)
cv2.setMouseCallback("mavi",imlec_konumu)
cv2.setMouseCallback("mavi",basılı)

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