import cv2 as cv

video = cv.VideoCapture("antalya.mp4")

while True:

    kontrol,izleme = video.read()
    if kontrol == 0:
        break


    cv.imshow("VİDEO",izleme)
    if cv.waitKey(10) & 0xFF == ord("q"):
        break

video.relase()
cv.destroyAllWindows()
