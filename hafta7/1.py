import cv2
import numpy as np

def nothing(x):
    pass


kamera_görüntüsü = cv2.VideoCapture(0)  


cv2.namedWindow("Kamera Görüntüsü")


cv2.createTrackbar("Alt sınır mavi H", "Kamera Görüntüsü", 90, 255, nothing)
cv2.createTrackbar("Alt sınır mavi S", "Kamera Görüntüsü", 100, 255, nothing)
cv2.createTrackbar("Alt sınır mavi V", "Kamera Görüntüsü", 100, 255, nothing)
cv2.createTrackbar("Üst sınır mavi H", "Kamera Görüntüsü", 130, 255, nothing)
cv2.createTrackbar("Üst sınır mavi S", "Kamera Görüntüsü", 255, 255, nothing)
cv2.createTrackbar("Üst sınır mavi V", "Kamera Görüntüsü", 255, 255, nothing)

while True:
    
    ret, kamera = kamera_görüntüsü.read()
    if not ret:
        break

    
    hsv = cv2.cvtColor(kamera, cv2.COLOR_BGR2HSV)

    
    alt_sınır_h = cv2.getTrackbarPos("Alt sınır mavi H", "Kamera Görüntüsü")
    alt_sınır_s = cv2.getTrackbarPos("Alt sınır mavi S", "Kamera Görüntüsü")
    alt_sınır_v = cv2.getTrackbarPos("Alt sınır mavi V", "Kamera Görüntüsü")
    üst_sınır_h = cv2.getTrackbarPos("Üst sınır mavi H", "Kamera Görüntüsü")
    üst_sınır_s = cv2.getTrackbarPos("Üst sınır mavi S", "Kamera Görüntüsü")
    üst_sınır_v = cv2.getTrackbarPos("Üst sınır mavi V", "Kamera Görüntüsü")

    alt_sınır_mavi = np.array([alt_sınır_h, alt_sınır_s, alt_sınır_v])
    üst_sınır_mavi = np.array([üst_sınır_h, üst_sınır_s, üst_sınır_v])

    
    maske = cv2.inRange(hsv, alt_sınır_mavi, üst_sınır_mavi)

    
    maske = cv2.GaussianBlur(maske, (5, 5), 0)

    
    kenarlar, _ = cv2.findContours(maske, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    if len(kenarlar) >= 2:
        sıralı_kenarlar = sorted(kenarlar, key=cv2.contourArea, reverse=True)
        en_büyük_kenar = sıralı_kenarlar[0]
        ikinci_en_büyük_kenar = sıralı_kenarlar[1]

        
        M1 = cv2.moments(en_büyük_kenar)
        if M1["m00"] != 0:
            kenar_X1 = int(M1["m10"] / M1["m00"])
            kenar_Y1 = int(M1["m01"] / M1["m00"])
        else:
            kenar_X1, kenar_Y1 = 0, 0

        M2 = cv2.moments(ikinci_en_büyük_kenar)
        if M2["m00"] != 0:
            kenarX2 = int(M2["m10"] / M2["m00"])
            kenarY2 = int(M2["m01"] / M2["m00"])
        else:
            kenarX2, kenarY2 = 0, 0

        
        uzaklık = int(np.sqrt((kenarX2 - kenar_X1) ** 2 + (kenarY2 - kenar_Y1) ** 2))

        
        cv2.line(kamera, (kenar_X1, kenar_Y1), (kenarX2, kenarY2), (0, 255, 0), 2)

        
        cv2.putText(kamera, f"Uzaklik: {uzaklık}", (kenar_X1 - 20, kenar_Y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.circle(kamera, (kenar_X1, kenar_Y1), 5, (0, 255, 255), -1)
        cv2.circle(kamera, (kenarX2, kenarY2), 5, (0, 255, 255), -1)

    
    cv2.imshow('Kamera Görüntüsü', kamera)
    cv2.imshow('Mavi Maske', maske)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


kamera_görüntüsü.release()
cv2.destroyAllWindows()
