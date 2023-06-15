import cv2
import numpy as np

resim = cv2.imread("bocek.png")


roi = resim[0:100,50:250] # index mantığı kullandık



cv2.imshow("Pencere",roi)
cv2.waitKey(0)
cv2.destroyAllWindow()