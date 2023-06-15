import cv2
import numpy as  np

resim = cv2.imread("kare2.png")

gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

kenar_tespit = cv2.Canny(gri,75,150)

cizgi_tespit = cv2.HoughLinesP(kenar_tespit,1,np.pi/180,50,maxLineGap=10)

for cizgi in cizgi_tespit:
    x1,y1,x2,y2 = cizgi[0]
    cv2.line(resim,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindow()