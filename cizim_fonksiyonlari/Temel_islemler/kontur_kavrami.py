import cv2
import numpy as np


resim = cv2.imread("bocek.png")

gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

_,threshold = cv2.threshold(gri,125,255,cv2.THRESH_BINARY)

kontur,a = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE

cv2.drawContours(resim,kontur,-1,(0,0,255),3)

cv2.imshow("Pencere",resim)



cv2.waitKey(0)
cv2.destroyAllWindow()