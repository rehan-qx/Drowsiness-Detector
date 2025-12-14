import cv2
import mediapipe as mp
import numpy as np
import pygame
import threading
import os

# --- CONFIGURATION ---
EAR_THRESHOLD = 0.25
CONSECUTIVE_FRAMES = 20

# --- PATH FIXING ---
script_folder = os.path.dirname(os.path.abspath(__file__))
ALARM_FILE = os.path.join(script_folder, "alarm.wav")

# --- AUDIO SETUP ---
pygame.mixer.init()

def play_alarm():
    # Agar music pehle se nahi chal raha, to chalao
    if not pygame.mixer.music.get_busy():
        try:
            pygame.mixer.music.load(ALARM_FILE)
            # CHANGE IS HERE: (-1) ka matlab hai infinite loop
            pygame.mixer.music.play(-1) 
        except Exception as e:
            print(f"[ERROR] Sound play nahi hui! Waja: {e}")

def stop_alarm():
    # Music stop karein
    pygame.mixer.music.stop()

# --- MEDIAPIPE SETUP ---
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def calculate_ear(landmarks, indices, w, h):
    coords = []
    for idx in indices:
        lm = landmarks[idx]
        coords.append([int(lm.x * w), int(lm.y * h)])
    coords = np.array(coords)
    d_A = np.linalg.norm(coords[1] - coords[5])
    d_B = np.linalg.norm(coords[2] - coords[4])
    d_C = np.linalg.norm(coords[0] - coords[3])
    return (d_A + d_B) / (2.0 * d_C)

# --- MAIN LOOP ---
cap = cv2.VideoCapture(0)
frame_counter = 0
alarm_on = False

print("[INFO] System Active... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark
            left_ear = calculate_ear(landmarks, LEFT_EYE, w, h)
            right_ear = calculate_ear(landmarks, RIGHT_EYE, w, h)
            avg_ear = (left_ear + right_ear) / 2.0

            # Screen par EAR value dikhayen
            cv2.putText(frame, f"EAR: {avg_ear:.2f}", (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # --- DROWSINESS LOGIC ---
            if avg_ear < EAR_THRESHOLD:
                frame_counter += 1
                
                # Agar aankhen kaafi der band hain
                if frame_counter >= CONSECUTIVE_FRAMES:
                    if not alarm_on:
                        alarm_on = True
                        # Thread start karein taake video na ruke
                        threading.Thread(target=play_alarm).start()
                    
                    cv2.putText(frame, "WAKE UP!", (100, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
            
            else:
                # Jab aankhen khul jayen (EAR > Threshold)
                frame_counter = 0
                alarm_on = False
                stop_alarm() # <--- Yahan alarm band ho jayega foran

    cv2.imshow("Sleep Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
stop_alarm() # Band karne par sound bhi band ho jayega