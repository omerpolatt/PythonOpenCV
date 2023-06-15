import cv2

# Video dosyasını aç
video = cv2.VideoCapture(0)

# Video çerçevelerini işle
while video.isOpened():
    # Bir çerçeve al
    ret, frame = video.read()

    if not ret:
        break

    # Çerçeveyi gri formata dönüştür
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Canny kenar tespiti uygula
    edges = cv2.Canny(frame, 100, 300)

    # Kenarları görselleştir (opsiyonel)
    cv2.imshow('Kenarlar', edges)

    # Çıkış için 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) == ord('q'):
        break

# Kaynakları serbest bırak
video.release()
cv2.destroyAllWindows()
