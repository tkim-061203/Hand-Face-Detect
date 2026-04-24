# 🖐️ Hand-Face-Detect: Face Bouncer & Hand Guard

A premium, real-time computer vision application built with **OpenCV** and **MediaPipe Holistic**. This project implements a "Logic Gate" system that detects faces and hands, providing real-time status labels and visual feedback.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.x-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Latest-orange.svg)

---

## 🔥 Key Features

- **Real-Time Holistic Tracking**: Simultanous tracking of face and hands using MediaPipe's high-performance Holistic model.
- **Dynamic Face Bouncer**: Automatically calculates and draws a bounding box around the detected face.
- **Intelligent Hand Guard**: 
    - Identifies **Left**, **Right**, or **Both hands**.
    - **Mirror Correction**: Logic is adjusted to correctly label hands even when the camera is flipped.
    - **Status Overlay**: A sleek UI box in the top-left corner showing the current detection state.
- **Face Requirement**: The system prioritizes face detection as a prerequisite for hand status monitoring.

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have Python 3.11+ installed. It is recommended to use a virtual environment.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/tkim-061203/Hand-Face-Detect.git
cd Hand-Face-Detect
pip install -r requirements.txt
```

### 3. Running the App
Execute the main script:
```bash
python mediapipe_holistic.py
```

---

## 🛠️ Technical Implementation

### The Logic Flow
1. **Mirror Flip**: The incoming frame is flipped horizontally for a natural "mirror" feel.
2. **Holistic Processing**: The RGB frame is passed to the MediaPipe Holistic model.
3. **Face Coordinate Normalization**: Face landmarks are extracted and converted from normalized coordinates (0.0 - 1.0) to pixel values based on the frame dimensions.
4. **Hand Presence Check**: The script checks `results.left_hand_landmarks` and `results.right_hand_landmarks` to determine the active label.

### UI Labels
| Label | Condition |
| :--- | :--- |
| **Face Required** | No face detected in frame |
| **No hand** | Face detected, but no hands |
| **Left** | Right hand detected (corrected for mirror) |
| **Right** | Left hand detected (corrected for mirror) |
| **Both hand** | Both hands detected |

---

## 📦 File Structure
- `mediapipe_holistic.py`: Main application code.
- `hand_landmarker.task`: Local model task file for high-performance detection.
- `requirements.txt`: Project dependencies.

---

## 📜 License
This project is open-source. Feel free to use and modify!