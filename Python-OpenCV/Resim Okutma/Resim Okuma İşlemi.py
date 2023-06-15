import cv2 as cv

resim = cv.imread("resim.png") # görüntülerimi okutmamızı sağlar ana fonksiyonumuz budur görüntüleri görebilmemiz için

cv.namedWindow("PENCERE",cv.WINDOW_NORMAL)# Görüntümümzün görüneceği pencere ekranı için ikinci parametresi ile özellikler
# eklenir ilk parametresi pencere ismi olacaktır ve bu pencere isimi ile imshow() fonkundaki isim aynı olmalı yoksa
# farklı pencereler oluşur
# cv.WINDOW_NORMAL: Pencere boyutu değiştirilebilir olur ve Normal pencere kullanılır..
# cv.WINDOW_AUTOSIZE: Pencere boyutu otomatik olarak görüntü boyutuna ayarlanır ve boyutlandırılamaz.
# cv.WINDOW_FULLSCREEN: Pencere tam ekran modunda açılır.
# cv.WINDOW_FREERATIO: Pencere boyutu değiştirilebilir ve görüntü boyutu ile orantılı olarak ayarlanır.
# cv.WINDOW_KEEPRATIO: Pencere boyutu değiştirilebilir ve görüntü boyutu ile orantılı olarak ayarlanır,
# ancak görüntü oranı sabit kalır.
# cv.WINDOW_EXPANDED: Genişletilmiş pencere kullanılır.

kayit = cv.imwrite("kopya.png",resim)


cv.imshow("PENCERE", resim)  # Görüntülerimizi göstermemizi saglayan pencereyi kullandığımız methodumuzdur ilk parametre
# olarak pencere adını alır ikinci parametre olarak ise imread ile kullanıdğımız değişken değerini alır


#cv.imwrite("Kaydedilen_resim.png",resim) # resimlerimizi kayıt etmemizi sağlar kayıt işelmi için
# görselin yeni adı ve uzantısı ile ilk parametre değeri olur ikinci paramtetre olarak ise resimimizin değşken adınıalır

cv.waitKey(0)  # Görüntülerin ekranda açık kalmasını sağlayan methodumuz milisaniye olarak değer alır ama içine
# 0 parametresini alırsa biz kapatana kadar kapanmayacaktır

cv.destroyAllWindows()  # Çoklu pencer açıldığında ekranın kapnmasının yarayan methodunmuz burda kullanmasak
# da olur ama temel olarak olduğu için kullanmamzı ileriki aşamlar içn kolaylık sağlayacaktır

