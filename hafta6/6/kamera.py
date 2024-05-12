import cv2

kamera = cv2.VideoCapture(0)

while True:
    ret , kamera_görüntü = kamera.read()
    cv2.imshow("kameram",kamera_görüntü)
    if cv2. waitKey(1) & 0xFF == ord('q'):
        break


kamera.release()
cv2.destroyAllWindows()