import pyautogui

class MouseController:
    def __init__(self, smoothening=5):
        pyautogui.PAUSE = 0
        self.screen_w, self.screen_h = pyautogui.size()
        self.smoothening = smoothening
        
        # Пам'ять про попередні дії
        self.prev_x, self.prev_y = 0, 0
        self.is_left_clicking = False
        self.is_right_clicking = False

    def move(self, target_x_norm, target_y_norm):
        """Плавно переміщує курсор"""
        target_x = target_x_norm * self.screen_w
        target_y = target_y_norm * self.screen_h
        
        curr_x = self.prev_x + (target_x - self.prev_x) / self.smoothening
        curr_y = self.prev_y + (target_y - self.prev_y) / self.smoothening
        
        try:
            pyautogui.moveTo(int(curr_x), int(curr_y))
        except pyautogui.FailSafeException:
            pass
            
        self.prev_x, self.prev_y = curr_x, curr_y
        return curr_y # Повертаємо Y для логіки скролінгу

    def left_click(self, distance, threshold=50):
        """Виконує лівий клік, якщо пальці близько"""
        if distance < threshold:
            if not self.is_left_clicking:
                pyautogui.click(button='left')
                self.is_left_clicking = True
            return True # Клік відбувся
        else:
            self.is_left_clicking = False
            return False

    def right_click(self, distance, threshold=50):
        """Виконує правий клік"""
        if distance < threshold:
            if not self.is_right_clicking:
                pyautogui.click(button='right')
                self.is_right_clicking = True
            return True
        else:
            self.is_right_clicking = False
            return False

    def scroll(self, curr_y, threshold=5):
        """Скролить сторінку залежно від руху руки по вертикалі"""
        scroll_dir = self.prev_y - curr_y
        if abs(scroll_dir) > threshold:
            pyautogui.scroll(int(scroll_dir * 2.5))