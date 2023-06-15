import cv2

resim = cv2.imread("kare.png")

gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

_,threshold = cv2.threshold(gri,127,255,cv2.THRESH_BINARY)

contours,_ =cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(resim, contours, -1, (0, 255, 0), 2)

cv2.imshow("resim",resim)



cv2.waitKey(0)
cv2.destroyAllWindow()