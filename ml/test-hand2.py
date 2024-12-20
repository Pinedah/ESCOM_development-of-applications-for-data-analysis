import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

#gesture_detected = False  # Variable booleana para almacenar el estado de la seña


# Parámetros personalizables para la ventana de texto
mensaje = "Gesto Detectado!"
color_texto = (0, 255, 0)  # Verde
tamano_texto = 1.5  # Tamaño de texto
grosor_texto = 2  # Grosor del texto

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

        gesture_detected = False  # Reiniciar detección en cada frame

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


        """# Verifica si la seña fue detectada
        if gesture_detected:
            print("Gesto detectado!")
        else:
            print("Gesto no detectado")"""
        # Mostrar el texto personalizado si se detecta el gesto
        if gesture_detected:
            # Crear una imagen para la ventana del mensaje
            mensaje_frame = cv2.imread("blank_image.jpg")  # Aquí usa una imagen en blanco del tamaño deseado o genera una en blanco

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
        
        # Mostrar el frame
        cv2.imshow("Hand Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
