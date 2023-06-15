import cv2
import numpy as np

arka_plan = np.ones((500,500,3),dtype=np.uint8)  # 3 boyutlu matris
arka_plan[:] = (255,0,0) # matris rengi değiştirme

arka_plan2=np.ones((500,500))  # tek boyutlu matris


cv2.imshow("Pencere",arka_plan)
cv2.waitKey(0)
cv2.destroyAllWindow()