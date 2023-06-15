import cv2
import numpy as np

icerik = cv2.VideoCapture(0)


def fonk(x):  # trackbar fonk çalışması için kullandığımız fonksiyonumuz
    pass


cv2.namedWindow("UYGULAMA")
cv2.resizeWindow("UYGULAMA", 500, 500)  # pencere boyutlarını ayarlamış olduk

cv2.createTrackbar("LOWER - H ", "UYGULAMA", 0, 180, fonk)  # treackbar larımızı oluşturduk
cv2.createTrackbar("LOWER - S ", "UYGULAMA", 0, 255, fonk)
cv2.createTrackbar("LOWER - V ", "UYGULAMA", 0, 255, fonk)

cv2.createTrackbar("UPPER - H ", "UYGULAMA", 0, 180, fonk)
cv2.createTrackbar("UPPER - S ", "UYGULAMA", 0, 255, fonk)
cv2.createTrackbar("UPPER - V ", "UYGULAMA", 0, 255, fonk)

cv2.setTrackbarPos("UPPER - H ", "UYGULAMA", 180)  # bu trackbarların değerlerinini 255 de başlamasını sağladık
cv2.setTrackbarPos("UPPER - S ", "UYGULAMA", 255)
cv2.setTrackbarPos("UPPER - V ", "UYGULAMA", 255)

while True:
    kontrol, video = icerik.read()

    if kontrol == False:  # videomuz ,kameramız kapandığı zamsn hata vermemsini sağlayacaktır
        break

    video = cv2.flip(video, 1)  # videonun döndürülmesini sağladık daha iyi görüntü alınması için

    hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)  # videoyu hsv formuna dönüştürdük

    lower_h = cv2.getTrackbarPos("LOWER - H ","UYGULAMA")
    lower_s = cv2.getTrackbarPos("LOWER - S ", "UYGULAMA")
    lower_v = cv2.getTrackbarPos("LOWER - V ", "UYGULAMA")

    upper_h = cv2.getTrackbarPos("UPPER - H " , "UYGULAMA")
    upper_s = cv2.getTrackbarPos("UPPER - S " , "UYGULAMA")
    upper_v = cv2.getTrackbarPos("UPPER - V " , "UYGULAMA")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower_color, upper_color) #görüntünün veya görüntü akışının belirli bir aralıkta bulunan
    # piksellerini tespit etmek için kullanılır

    cv2.imshow("UYGULAMA", video)
    cv2.imshow("UYGULAMA2", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

icerik.release()
cv2.destroyAllWindows()
