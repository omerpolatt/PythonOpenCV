import cv2
import numpy as np

video = cv2.VideoCapture("yol.mp4")


while True:
    kontrol,okuma = video.read()
    okuma = cv2.resize(okuma,(640,480))
    hsv = cv2.cvtColor(okuma,cv2.COLOR_BGR2HSV)

    dusuk_yellow = np.array([18, 94, 140], np.uint8)
    yuksek_yellow = np.array([48, 255, 255], np.uint8)

    mask = cv2.inRange(hsv,dusuk_yellow,yuksek_yellow)

    kenarlar = cv2.Canny(mask,75,150)

    cizgiler = cv2.HoughLinesP(kenarlar, 1, np.pi / 180, 50, maxLineGap=50)

    for cizgi in cizgiler:
        (x1, y1, x2, y2) = cizgi[0]
        cv2.line(okuma, (x1, y1), (x2, y2), (0, 255, 0), 5)

        cv2.imshow("IMG", okuma)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

video.release()
cv2.destroyAllWindows()

