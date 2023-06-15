import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)

mp_cizim = mp.solutions.drawing_utils
mp_eller = mp.solutions.hands  ## holistic  olursa bura tüm vücut kapsayıcısı olarak işleme almaktadır yani holistic de
#yazılsa sıkıntı olmaz

with mp_eller.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as eller:
    while True:
        kontrol, resim = webcam.read()

        resim_rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

        sonuc = eller.process(resim_rgb)

        resim = cv2.cvtColor(resim_rgb, cv2.COLOR_RGB2BGR)

        if sonuc.multi_hand_landmarks:
            for el_landmarks in sonuc.multi_hand_landmarks:
                mp_cizim.draw_landmarks(resim, el_landmarks, mp_eller.HAND_CONNECTIONS)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

        cv2.imshow("PENCERE", resim)
