import cv2

# Giriş görüntüsünü yükle
image = cv2.imread('bocek.png',0)  # Grayscale olarak yükle

# Canny kenar tespiti uygula
edges = cv2.Canny(image, 100,200, apertureSize=3, L2gradient=False)

# Kenar görüntüsünü göster
cv2.imshow('Kenarlar', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
