import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

landmark_drawing_spec = mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=5, circle_radius=1)  # Rojo para puntos
connection_drawing_spec = mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2)  # Verde para conexiones

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec,       # Especificación para los puntos
                    connection_drawing_spec)

        cv2.imshow("Hand Detection", frame)

        # Presiona 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.flip(frame, 1)
cap.release()
cv2.destroyAllWindows()
