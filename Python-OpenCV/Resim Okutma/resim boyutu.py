import cv2 as cv

resim_2 = cv.imread("kayseri.jpg")

cv.namedWindow("RESİM")

resim_2 = cv.resize(resim_2,(100,100))# resim ekran boyutunu ayarlamamızı sağlar

cv.imshow("RESİM",resim_2)


cv.waitKey(0)
cv.destroyAllWindows()