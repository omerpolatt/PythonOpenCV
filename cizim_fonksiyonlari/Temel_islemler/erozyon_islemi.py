import cv2
import numpy as np


resim = cv2.imread("bocek.png")

kernel = np.ones((3,3), np.uint8)  # 3x3 bir yapılandırma elemanı oluşturur

# Erozyon işlemini uygula
eroded_image = cv2.erode(resim, kernel, iterations=2)


cv2.imshow("Pencere",resim)
cv2.imshow("Pencere2",eroded_image)


cv2.waitKey(0)
cv2.destroyAllWindow()