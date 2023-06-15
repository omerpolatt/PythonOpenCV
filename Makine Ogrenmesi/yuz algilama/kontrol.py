import cv2

resim = cv2.imread("yuz_resmi.jpg")

if resim is not None:

    cv2.imshow('Resim', resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:

    print('Görüntü yüklenemedi.')