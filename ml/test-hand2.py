import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

gesture_detected = False  # Variable booleana para almacenar el estado de la seña


with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

# Loop principal
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            # Asumiendo que necesitas ambas manos para hacer el gesto
            if len(results.multi_hand_landmarks) == 2:
                hand1 = results.multi_hand_landmarks[0]
                hand2 = results.multi_hand_landmarks[1]

                # Ejemplo: Comprobar la posición de los índices y pulgares en ambas manos
                index1 = hand1.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb1 = hand1.landmark[mp_hands.HandLandmark.THUMB_TIP]

                index2 = hand2.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb2 = hand2.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Definir la lógica para el gesto
                # Comprobar distancias entre índices y pulgares
                if (abs(index1.x - index2.x) < 0.1 and abs(index1.y - index2.y) < 0.1 and
                    abs(thumb1.x - thumb2.x) < 0.1 and abs(thumb1.y - thumb2.y) < 0.1):
                    gesture_detected = True
                else:
                    gesture_detected = False

            # Dibujar las manos en el frame
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS)

        # Mostrar el frame
        cv2.imshow("Hand Detection", frame)

        # Verifica si la seña fue detectada
        if gesture_detected:
            print("Gesto detectado!")
        else:
            print("Gesto no detectado")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
