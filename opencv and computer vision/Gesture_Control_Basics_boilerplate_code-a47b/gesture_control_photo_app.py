import cv2, mediapipe as mp, time, numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

FILTERS = [None, 'grayscale', 'sepia', 'negative', 'blur']
current_filter = 0

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: could not access the camera"); exit()

last_action_time = 0; DEBOUNCE_TIME = 1
pinch_in_progress = False; capture_request = False

def apply_filter(frame, ftype):
    if ftype == 'grayscale':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif ftype == 'sepia':
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        return np.clip(cv2.transform(frame, sepia_filter), 0, 255).astype(np.uint8)
    elif ftype == 'negative':
        return cv2.bitwise_not(frame)
    elif ftype == 'blur':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    return frame

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame"); break
    img = cv2.flip(img, 1)
    h, w = img.shape[:2]
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    capture_request = False

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.drw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)
            lm = hand.landmark

            thumb_tip = hand_landmarks.landmarks[]