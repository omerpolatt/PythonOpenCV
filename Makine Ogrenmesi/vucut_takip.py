import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)

mp_cizim = mp.solutions.drawing_utils
mp_butunsel = mp.solutions.holistic

with mp_butunsel.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as butun:
    while True:
        kontrol, resim = webcam.read()

        resim_rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

        sonuc = butun.process(resim_rgb)

        resim = cv2.cvtColor(resim_rgb, cv2.COLOR_RGB2BGR)

        mp_cizim.draw_landmarks(resim, sonuc.pose_landmarks,mp_butunsel.POSE_CONNECTIONS,
                                mp_cizim.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)) #bu ikinci satırı
        #çizgi ve daire renkleri büyüklükleri için yazdık

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

        cv2.imshow("PENCERE", resim)
