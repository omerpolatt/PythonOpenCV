import cv2
import numpy as np


resim = cv2.imread("bocek.png",0)

kontrol,threshold = cv2.threshold(resim,50,255, cv2.THRESH_BINARY)
kontrol,threshold2 = cv2.threshold(resim,50,255, cv2.THRESH_BINARY_INV)


cv2.imshow("Pencere",resim)
cv2.imshow("Pencere2",threshold)
cv2.imshow("Pencere3",threshold2)

cv2.waitKey(0)
cv2.destroyAllWindow()