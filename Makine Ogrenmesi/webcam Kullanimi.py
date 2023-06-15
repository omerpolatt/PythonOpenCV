import cv2

webcam = cv2.VideoCapture(0)

while True:
    kontrol ,resim = webcam.read()
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

    cv2.imshow("PENCERE",resim)