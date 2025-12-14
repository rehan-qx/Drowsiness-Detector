# 🚗 Driver Drowsiness Detection System (AI-Powered)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Computer Vision](https://img.shields.io/badge/OpenCV-MediaPipe-green?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)



## 📖 Project Overview

Drowsy driving is a major cause of road accidents worldwide. This system serves as a real-time co-pilot that monitors the driver's alertness.

Using **Google's MediaPipe** framework, the system detects 468 facial landmarks to track the **Eye Aspect Ratio (EAR)**. If the driver's eyes remain closed for a prolonged period (simulating microsleep), the system activates a continuous alarm loop until the eyes are opened again.

---

## 📂 Project Structure

### This is how your project folder should look:

 *Drowsiness-detector* 

| main.py          --> The main python script (Source Code) |

| alarm.wav        --> Audio file for the alarm (Required) |

| README.md        --> This documentation file |

| requirements.txt --> List of dependencies (Optional) |

---

## ✨ Key Features


* **👁️ Real-Time Tracking:** High-speed facial landmark detection (30+ FPS) suitable for low-end hardware.
* **🔊 Persistent Alarm:** Features an infinite-loop alarm that forces the driver to wake up to stop the sound.
* **🧵 Non-Blocking Performance:** Audio playback runs on a separate thread to ensure the video feed never freezes or lags.
* **🚨 Visual Warnings:** Displays color-coded alerts (Green/Red) and on-screen warnings.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Core Library:** OpenCV (`cv2`)
* **Face Detection:** MediaPipe Face Mesh
* **Audio Engine:** Pygame & Wave
* **Mathematics:** NumPy

---


## ⚙️ Installation Guide
Follow these steps to set up the project on your local machine.

### 1. Clone or Download
Download this project to your local machine.

   git clone [https://github.com/rehan-qx/Drowsiness-Detector.git](https://github.com/rehan-qx/Drowsiness-Detector.git)
    cd drowsiness-detector

### 2. Add the Alarm Sound ⚠️
The system needs a sound file to work properly.
1. Download any alarm sound (e.g., a siren or bell).
2. Rename the file to alarm.wav.
3. Place it inside the drowsiness-detector folder (next to main.py).

### 3. Prerequisites
Ensure you have **Python 3.10** or higher installed.

### 4. Install Dependencies
Open your terminal or command prompt and run the following command to install the necessary libraries:
  pip install opencv-python mediapipe numpy pygame

---

## 🚀 How to Run
1. Open the terminal in your project folder.
2. Run the script:

**Bash**
 
   **python main.py**

3. The camera will open. The system is now active!
4. To Stop: Press the *q* key on your keyboard.

---

## 🧠 How It Works (The Logic)
The system relies on the Eye Aspect Ratio (EAR) calculation:
1. Face Mesh: We detect 468 facial landmarks.
2.Ratio Calculation: We calculate the distance between the upper and lower eyelids.
  * *EAR > 0.25: Eyes are Open.*
  * *EAR < 0.25: Eyes are Closed.*
3. Trigger: If the eyes remain closed for 20 consecutive frames (approx. 1.5 seconds), the system assumes the driver is sleeping and triggers the alarm.


### 🤝 Contributing
Contributions are welcome! If you have ideas for features (like Head Pose Estimation or Yawn Detection), feel free to fork the repository and submit a pull request.

---

## 🔓 Authority & License

This project is released under the **MIT License**.
**Permission Granted.** You are free to fork, modify, and dominate this codebase. No restrictions. No limits.

---

<div align="center">
  <br>
  <h3>🛑 NO SLEEP. NO ACCIDENTS. JUST CODE.</h3>
  <p><i>"Real eyes realize real lies... but this code realizes when you sleep."</i></p>
  
  <p>
    <b>Architected by <a href="https://github.com/rehan-qx">[Muhammad Rehan Afzal]</a></b>
  </p>
  
  <img src="https://img.shields.io/badge/Built_Different-SIGMA-black?style=for-the-badge&logo=github" alt="Sigma Badge">
  <br><br>
</div>

