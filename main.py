import cv2
from hand_tracker import HandTracker
from mouse_controller import MouseController

def main():
    # Налаштування
    cap = cv2.VideoCapture(0) # Заміни на 1 або 2, якщо потрібно для iVCam
    tracker = HandTracker()
    mouse = MouseController(smoothening=5)
    
    print("🪄 JediDesk 4.0: Модульна архітектура успішно запущена!")
    
    while True:
        success, img = cap.read()
        if not success:
            break
            
        img = cv2.flip(img, 1)
        h, w, _ = img.shape
        
        # 1. Передаємо кадр у Трекер
        img, landmarks = tracker.process_frame(img)
        
        # 2. Якщо Трекер знайшов руку, передаємо дані Мишці
        if landmarks:
            # Рухаємо курсор за вказівним пальцем
            curr_y = mouse.move(landmarks['index'][0], landmarks['index'][1])
            
            # Рахуємо відстані між пальцями
            dist_left = tracker.get_distance(landmarks['index'], landmarks['thumb'], mouse.screen_w, mouse.screen_h)
            dist_right = tracker.get_distance(landmarks['middle'], landmarks['thumb'], mouse.screen_w, mouse.screen_h)
            dist_scroll = tracker.get_distance(landmarks['index'], landmarks['middle'], mouse.screen_w, mouse.screen_h)
            
            # Перевіряємо жести
            if dist_scroll < 40 and dist_left > 50 and dist_right > 50:
                mouse.scroll(curr_y)
                cv2.circle(img, (int(landmarks['index'][0]*w), int(landmarks['index'][1]*h)), 15, (0, 255, 255), cv2.FILLED)
            else:
                if mouse.left_click(dist_left):
                    cv2.circle(img, (int(landmarks['index'][0]*w), int(landmarks['index'][1]*h)), 15, (0, 255, 0), cv2.FILLED)
                
                if mouse.right_click(dist_right):
                    cv2.circle(img, (int(landmarks['middle'][0]*w), int(landmarks['middle'][1]*h)), 15, (255, 0, 0), cv2.FILLED)

        # 3. Виводимо результат
        cv2.imshow("JediDesk Pro", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

# Точка входу в програму
if __name__ == "__main__":
    main()