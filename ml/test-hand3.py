import cv2
import mediapipe as mp
import numpy as np

# Configuración de MediaPipe y OpenCV
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

landmark_drawing_spec = mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=5, circle_radius=1)
connection_drawing_spec = mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2)

cap = cv2.VideoCapture(0)

# Parámetros personalizables para la ventana de texto
mensaje = "Gesto Detectado!"
color_texto = (255, 255, 255)  # blanco
tamano_texto = 1  # Tamaño de texto
grosor_texto = 1  # Grosor del texto

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

        gesture_detected = False  # Reiniciar detección en cada frame

        if results.multi_hand_landmarks:
            # Comprobar si se detectan ambas manos para formar el gesto
            if len(results.multi_hand_landmarks) == 2:
                hand1 = results.multi_hand_landmarks[0]
                hand2 = results.multi_hand_landmarks[1]

                # Posiciones de los puntos de interés
                index1 = hand1.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb1 = hand1.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index2 = hand2.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb2 = hand2.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Condiciones para detectar el gesto
                if (abs(index1.x - index2.x) < 0.1 and abs(index1.y - index2.y) < 0.1 and
                    abs(thumb1.x - thumb2.x) < 0.1 and abs(thumb1.y - thumb2.y) < 0.1):
                    gesture_detected = True

            # Dibujar las manos en el frame
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec,
                    connection_drawing_spec)

        # Mostrar el texto personalizado si se detecta el gesto
        if gesture_detected:
            # Crear una imagen en blanco para el mensaje (200x400 píxeles)
            mensaje_frame = np.zeros((200, 400, 3), dtype=np.uint8)

            # Tamaño y posición del texto
            posicion_texto = (50, 100)  # Ajusta la posición según el tamaño de la ventana y el texto

            # Agregar texto a la ventana de mensaje
            cv2.putText(mensaje_frame, mensaje, posicion_texto, cv2.FONT_HERSHEY_SIMPLEX, tamano_texto, color_texto, grosor_texto)

            # Mostrar la ventana del mensaje
            cv2.imshow("Mensaje", mensaje_frame)

        else:
            # Cerrar la ventana del mensaje si el gesto no está presente
            if cv2.getWindowProperty("Mensaje", cv2.WND_PROP_VISIBLE) >= 1:
                cv2.destroyWindow("Mensaje")

        # Mostrar el frame principal
        cv2.imshow("Hand Detection", frame)

        # Presiona 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
