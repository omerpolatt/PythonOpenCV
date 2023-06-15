import cv2
import numpy as np


resim = cv2.imread("bocek.png")

bgr = cv2.cvtColor(resim,cv2.COLOR_RGB2BGR)
gri = cv2.cvtColor(resim,cv2.COLOR_RGB2GRAY)
hsv = cv2.cvtColor(resim,cv2.COLOR_RGB2HSV)

#cv2.imshow("Pencere3",gri)
#cv2.imshow("Pencere2",bgr)
cv2.imshow("Pencere4",hsv)
cv2.imshow("Pencere",resim)


cv2.waitKey(0)
cv2.destroyAllWindow()