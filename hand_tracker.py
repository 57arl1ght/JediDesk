import cv2
import mediapipe as mp
import math

class HandTracker:
    def __init__(self, max_hands=1, detection_con=0.7):
        # Ініціалізація MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_con
        )
        self.mp_draw = mp.solutions.drawing_utils

    def process_frame(self, img):
        """Шукає руку на кадрі і повертає координати потрібних пальців"""
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        
        landmarks = {}
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Малюємо скелет на кадрі
                self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # Витягуємо координати (вони від 0.0 до 1.0)
                landmarks['thumb'] = (hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y)
                landmarks['index'] = (hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y)
                landmarks['middle'] = (hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y)
                
        return img, landmarks

    def get_distance(self, p1, p2, screen_w, screen_h):
        """Рахує відстань між двома точками в пікселях екрана"""
        x1, y1 = int(p1[0] * screen_w), int(p1[1] * screen_h)
        x2, y2 = int(p2[0] * screen_w), int(p2[1] * screen_h)
        return math.hypot(x2 - x1, y2 - y1)