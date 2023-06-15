import cv2


yuz_tanima = cv2.CascadeClassifier("yuz_tanima.xml")
goz_tanima = cv2.CascadeClassifier("goz_tespit.xml")


resim = cv2.imread("yuz_resmi.jpg")

gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

tanima = yuz_tanima.detectMultiScale(gri)

for (x,y,genislik,yukseklik) in tanima:
    cv2.rectangle(resim,(x,y),(genislik+x,yukseklik+y),(0,255,0),3)

    goz_sonuc = goz_tanima.detectMultiScale(gri,1.3,5)

    for (gx,gy,g_genislik,g_yukseklik) in goz_sonuc:
        cv2.rectangle(resim, (gx, gy), (g_genislik + gx, g_yukseklik + gy), (255, 0, 0), 3)

cv2.imshow("PENCERE",resim)
cv2.waitKey(0)


