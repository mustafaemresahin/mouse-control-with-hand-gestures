import cv2
import mediapipe as mp
import pyautogui

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

# For drawing on the image
mp_drawing = mp.solutions.drawing_utils

prev_pinching = False
prev_scroll_pos = None  # To store the previous position when scrolling

right_click = False

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    image = cv2.flip(image, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = handedness.classification[0].label  # Determine if it's left or right hand
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            if hand_label == 'Left':
                cursor_x, cursor_y = index_tip.x * screen_width, index_tip.y * screen_height
                pyautogui.moveTo(cursor_x, cursor_y)
                cv2.putText(image, f'Cursor Moving: {int(cursor_x)}, {int(cursor_y)}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                # Check for scroll gesture
                scroll_distance = ((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2) ** 0.5
                if scroll_distance < 0.05:  # Index and middle fingers are close enough to consider scrolling
                    if prev_scroll_pos is not None:
                        scroll_amount = (index_tip.y - prev_scroll_pos) * 1000  # Scale the scroll amount
                        pyautogui.scroll(int(scroll_amount))
                        cv2.putText(image, f'Scrolling: {int(scroll_amount)}', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    prev_scroll_pos = index_tip.y
                else:
                    prev_scroll_pos = None

            elif hand_label == 'Right':
                # Check for pinching gesture for clicking
                index_pinch_distance = ((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2) ** 0.5
                if index_pinch_distance < 0.03:
                    if not prev_pinching:
                        pyautogui.click()
                        prev_pinching = True
                        cv2.putText(image, 'Left Clicking', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    prev_pinching = False

                # Check for pinching gesture for clicking
                pinky_pinch_distance = ((middle_tip.x - thumb_tip.x) ** 2 + (middle_tip.y - thumb_tip.y) ** 2) ** 0.5
                if pinky_pinch_distance < 0.03:
                    if not right_click:
                        pyautogui.rightClick()
                        right_click = True
                        cv2.p 
                    right_click = False

    cv2.imshow('Hand Tracking', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
