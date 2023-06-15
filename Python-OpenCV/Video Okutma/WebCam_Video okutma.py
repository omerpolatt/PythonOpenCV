import cv2 as cv

cap = cv.VideoCapture(0,cv.CAP_DSHOW) # webcam üzerinden video almamızı sağlar

while True:

    ret,frame = cap.read() 

    frame = cv.flip(frame,1)

    cv.imshow("VİDEO",frame)
    if cv.waitkey(30) & 0xFF == ord("q"):
        break

cap.relase()
cv.destroyAllWindows()
