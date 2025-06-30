# 🎞️ Filmmage - Intelligent Face Recognition & Aesthetic Filter App

Filmmage is a smart Streamlit-based web app that merges **face recognition** with **aesthetic image filtering**, enabling users to explore and personalize event photos with precision and style. It combines the power of **deep learning-based face detection** with **real-time filter applications**, ensuring seamless experience for both photographers and users.

---

## 💡 Problem Statement

Despite rapid growth in computer vision, current face recognition systems still face challenges:

* ⚠️ Inaccuracy and inefficiency in large-scale image collections
* 📉 Limited flexibility in traditional handcrafted feature methods
* 🤖 Deep Neural Networks (DNNs) are better, but still improvable

This project proposes a more robust face recognition system by **integrating DNN-based detection** with **custom encoding techniques**, making it scalable and practical for **security**, **authentication**, and **event photo personalization**.

---

## 🔍 Features Overview

### 👤 User Roles

* `User`: Browse and filter personal images
* `Photographer`: Create and manage events, upload photo sets

### 🔐 Authentication System

* Secure signup/login
* Role-based content display

### 📸 Event Management

* Photographers upload event photos
* Events are shared via QR codes

### 🤖 Face Recognition

* Upload a single face image
* System detects and matches face across event collection
* Efficient encoding + DNN-based OpenCV SSD model

### 🎨 Filter Presets

* 25+ filters (e.g., Inkwell, XPro, Lofi, Clarendon) via `pilgram`
* Apply to individual or all images
* Preview + ZIP download for selected outputs

### 📦 Image Download

* Select images visually
* Instant ZIP creation for download

---

## 🛠️ Tech Stack

| Layer          | Technology                     |
| -------------- | ------------------------------ |
| Frontend       | Streamlit                      |
| Face Detection | OpenCV DNN + face\_recognition |
| Filters        | pilgram + Pillow               |
| DB             | SQLite                         |
| Utilities      | QRCode, NumPy, uuid, shutil    |

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/filmmage.git
cd filmmage
```

### 2. Set up virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 3.1. Install compatible dlib manually (Windows only)

If you face issues with installing `dlib`, download and install this specific version:

```bash
pip install https://download.lfd.uci.edu/pythonlibs/z4tqcw6k/dlib-19.24.1-cp311-cp311-win_amd64.whl
```

### 4. Download Face Detection Model Files

Place in `models/` folder:

* `deploy.prototxt`
* `res10_300x300_ssd_iter_140000_fp16.caffemodel`

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```
filmmage/
├── app.py                    # Main Streamlit application entry point
├── db_utils.py               # Database functions: user/event/image storage and retrieval
├── dlib-19.24.1-*.whl        # Precompiled dlib wheel for Windows (manual install)
├── event_management.py       # Logic for creating and managing events by photographers
├── face_recognition_utils.py # Face detection, encoding, and matching logic
├── preset_filters.py         # UI logic to display and apply aesthetic filters to images
├── presets.py                # Core filter functions using pilgram
├── requirements.txt          # Python dependencies to install
├── user_management.py        # Login, signup, session and user role management
├── models/                   # Face detection DNN model files (deploy.prototxt, caffemodel)
```

---

## 🧠 Future Improvements

* Face alignment pre-processing
* Real-time webcam support
* Cloud deployment (Streamlit Cloud / HuggingFace)
* Admin analytics dashboard for photographers

---

## 📬 Author

**Mihir Shah**

