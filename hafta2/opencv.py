import cv2

görüntü = cv2.VideoCapture(0)

while True:
    ret, cam_görüntü = görüntü.read()
    cv2.imshow("kameram",cam_görüntü)
    if cv2.waitKey(10) & 0xFF == ord("x"):
        break

görüntü.release()
cv2.destroyAllWindows()