import cv2
import numpy

def nothing(x):
    pass

kamera = cv2.VideoCapture(0)

alt_sınır_mavi = numpy.array([90,100,100])
üst_sınır_mavi = numpy.array([130,255,255])

cv2.namedWindow("Kamera Görüntüsü")

cv2.createTrackbar("Alt sınır mavi H","Kamera Görüntüsü", alt_sınır_mavi[0],255,nothing)
cv2.createTrackbar("Alt sınır mavi S","Kamera Görüntüsü", alt_sınır_mavi[1],255,nothing)
cv2.createTrackbar("Alt sınır mavi V","Kamera Görüntüsü", alt_sınır_mavi[2],255,nothing)
cv2.createTrackbar("Üst sınır mavi H","Kamera Görüntüsü", üst_sınır_mavi[0],255,nothing)
cv2.createTrackbar("Üst sınır mavi S","Kamera Görüntüsü", üst_sınır_mavi[1],255,nothing)
cv2.createTrackbar("Üst sınır mavi V","Kamera Görüntüsü", üst_sınır_mavi[2],255,nothing)


while True:
    ret , kamera_görüntü = kamera.read()
    hsv = cv2.cvtColor(kamera_görüntü,cv2.COLOR_BGR2HSV)

    alt_sınır_mavi[0] = cv2.getTrackbarPos("Alt sınır mavi H","Kamera Görüntüsü")
    alt_sınır_mavi[1] = cv2.getTrackbarPos("Alt sınır mavi S","Kamera Görüntüsü")
    alt_sınır_mavi[2] = cv2.getTrackbarPos("Alt sınır mavi V","Kamera Görüntüsü")
    üst_sınır_mavi[0] = cv2.getTrackbarPos("Üst sınır mavi H","Kamera Görüntüsü")
    üst_sınır_mavi[1] = cv2.getTrackbarPos("Üst sınır mavi S","Kamera Görüntüsü")
    üst_sınır_mavi[2] = cv2.getTrackbarPos("Üst sınır mavi V","Kamera Görüntüsü")
    
    maske = cv2.inRange(hsv,alt_sınır_mavi,üst_sınır_mavi)
    maske = cv2.GaussianBlur(maske,(5,5),0)
    
    sınırlar , _ = cv2.findContours(maske,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    büyük_sınır = None
    büyük_alan = 0

    for sınır in sınırlar:
        alan = cv2.contourArea(sınır)
        if alan > büyük_alan:
            büyük_sınır = sınır
            büyük_alan = alan

    if büyük_sınır is not None :
        x, y, w, h = cv2.boundingRect(büyük_alan)
        cv2.rectangle(kamera,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Kamera Görüntüsü",kamera_görüntü)
    cv2.imshow("Mavi",maske)

    if cv2. waitKey(1) & 0xFF == ord('q'):
        break


kamera.release()
cv2.destroyAllWindows()