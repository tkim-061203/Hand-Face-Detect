import cv2
import mediapipe as mp

# Initialize Holistic
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # --- LOGIC GATE ---
    face_landmarks = results.face_landmarks
    label = "Face Required"

    if face_landmarks:
        # 1. Calculate Bounding Box (Box Bouncer)
        all_x = [lm.x for lm in face_landmarks.landmark]
        all_y = [lm.y for lm in face_landmarks.landmark]
        
        # Convert normalized coordinates to pixel values
        x_min, x_max = int(min(all_x) * w), int(max(all_x) * w)
        y_min, y_max = int(min(all_y) * h), int(max(all_y) * h)

        # Draw the Face Box
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)
        cv2.putText(frame, "FACE", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        # 2. Check for Hands
        left_h = results.left_hand_landmarks
        right_h = results.right_hand_landmarks

        if left_h and right_h: label = "Both hand"
        elif left_h: label = "Right"  # Mirror Swap
        elif right_h: label = "Left"  # Mirror Swap
        else: label = "No hand"

    # Top-left Status Label
    cv2.rectangle(frame, (0, 0), (320, 70), (0, 0, 0), -1)
    cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    # 3. Draw Hand Landmarks (Optional)
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    cv2.imshow('Face Bouncer & Hand Guard', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()