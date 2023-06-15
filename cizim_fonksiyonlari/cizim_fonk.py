import cv2
import numpy as np

arka_plan = np.ones((500,500,3),dtype=np.uint8)
arka_plan[:]=(255,255,255)

cv2.rectangle(arka_plan,(10,10),(160,150),(255,0,0),3) #dikdörtgen kare çizim fonk


cv2.circle(arka_plan,(50,50),25,(0,255,0),4) # çember  çizim fonk
cv2.circle(arka_plan,(50,50),25,(0,255,0),-1) # daire yapmış olduk içi dolu

cv2.line(arka_plan,(200,200),(400,200),(80,75,60),5) #çizgi çekme fonksiyonu

yazi_tipi = cv2.FONT_HERSHEY_PLAIN
cv2.putText(arka_plan,"Omer",(250,50),yazi_tipi,2,(150,0,90),3) # yazı yazdırma fonk

kordinatlar=np.array([[130,50],[70,100],[170,200],[130,200]],np.int32)
cv2.polylines(arka_plan,[kordinatlar],True,(200,80,0),3)  # çokgen sekil çizdirme fonk


cv2.imshow("TEKRAR",arka_plan)
cv2.waitKey(0)
cv2.destroyAllWindow()