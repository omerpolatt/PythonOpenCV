import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread('bocek.png')

# Gray scale'a dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shi-Tomasi köşe algılama yöntemini uygula
corners = cv2.goodFeaturesToTrack(gray, 5000,0.01, 5)

# Köşeleri çiz
corners = np.int0(corners)
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)

# Görüntüyü göster
cv2.imshow('Shi-Tomasi Corner Detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
