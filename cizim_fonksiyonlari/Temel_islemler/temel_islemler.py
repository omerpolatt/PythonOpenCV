import cv2
import numpy as np

resim = cv2.imread("kiz.png")


yeni_hal = cv2.resize(resim,(800,500)) #resim boyutlandırmak için kullanılan fonk istenilen boyuta getiri resimleri

#boyut = resim.shape
#print(boyut)


#renk = resim[500,590] # istenilen kordinattaki pikselin BGR ile renklerini vermekte
#print(renk)

cv2.imshow("Pencere",yeni_hal)
cv2.waitKey(0)
cv2.destroyAllWindow()