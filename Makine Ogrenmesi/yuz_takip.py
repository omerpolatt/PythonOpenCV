import cv2
import mediapipe as mp

# MediaPipe yüz takip modülünü başlatma
mp_face = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Webcam'i başlatma
webcam = cv2.VideoCapture(0)

with mp_face.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while True:
        # Görüntüyü okuma
        ret, frame = webcam.read()

        # Görüntüyü BGR'den RGB'ye dönüştürme
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Yüzleri tespit etme
        results = face_detection.process(rgb_frame)

        # Tespit edilen yüzleri çizme
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)

        # Görüntüyü ekranda gösterme
        cv2.imshow('Yüz Takip', frame)

        # 'q' tuşuna basıldığında döngüyü sonlandırma
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Kaynakları serbest bırakma ve pencereleri kapatma
webcam.release()
cv2.destroyAllWindows()
