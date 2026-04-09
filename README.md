# 🪄 JediDesk: Touchless PC Control

JediDesk is a Python-based neural interface that turns your webcam (or smartphone camera) into a virtual mouse. The project uses computer vision and neural networks to track hand movements in real-time, allowing you to control the cursor, click, and scroll web pages using hand gestures—without ever touching a physical mouse.

## 🚀 Features & Gestures

The system tracks 21 hand landmarks and supports the following intuitive gestures:

* **🖐 Cursor Movement:** Controlled by the movement of your index finger. Built-in mathematical smoothing ensures the cursor glides smoothly across the screen.
* **🤏 Left Click:** Pinch your **index** and **thumb** fingers together.
* **🤌 Right Click:** Pinch your **middle** and **thumb** fingers together.
* **📜 Scrolling:** Bring your **index** and **middle** fingers together (like a closed "Peace" sign ✌️) and move your hand vertically to scroll pages up or down.

## 🛠 Tech Stack

* **[Python 3](https://www.python.org/)** — Core development language.
* **[OpenCV](https://opencv.org/)** — Video stream capture and basic frame processing.
* **[MediaPipe](https://developers.google.com/mediapipe)** (by Google) — Ultra-fast machine learning framework for hand skeleton tracking.
* **[PyAutoGUI](https://pyautogui.readthedocs.io/)** — Cross-platform library for systemic cursor control and click simulation.

## 📁 Project Structure (Modular Architecture)
The project is built following the *Separation of Concerns* principle to keep the codebase clean and scalable:
* `main.py` — The orchestrator script that connects modules and runs the main video loop.
* `hand_tracker.py` — The "Vision & Brains" module. Exclusively handles hand tracking and distance mathematics.
* `mouse_controller.py` — The "Hands" module. Handles cursor stabilization and executes system-level commands.

## 💻 Installation & Usage

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/JediDesk.git](https://github.com/YOUR_USERNAME/JediDesk.git)
   cd JediDesk
   Run the application:
   ```bash
   python main.py
   To safely exit the application and release the camera, press the Q key while the video window is active.
