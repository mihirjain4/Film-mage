# 🎞️ Filmmage - Event-Based Face Recognition & Filter Application

Filmmage is a powerful and intuitive Streamlit web app designed for:

* 🎯 Face recognition from event images
* 🎨 Applying aesthetic filters to selected faces
* 📥 Easy downloading of personalized and filtered image sets

---

## 📦 Features

### 🔐 User Authentication

* Signup/Login system with roles: `User` and `Photographer`

### 🖼️ Event Management

* Photographers can create events and upload images
* Users can explore events and apply filters to their own images

### 🤖 Face Recognition

* Upload a selfie or face image
* App finds and extracts all appearances of that face from the selected event
* Uses `face_recognition` with DNN-based face detection (OpenCV SSD)

### 🎨 Image Filters (Presets)

* 25+ Instagram-style filters powered by `pilgram`
* Apply to single or all images with one click
* Download selected filtered images in ZIP format

### 📸 QR Code Event Sharing

* Auto-generated QR codes for each event, for sharing and direct access

---

## 🛠️ Tech Stack

* **Frontend/UI**: [Streamlit](https://streamlit.io/)
* **Face Detection**: [face\_recognition](https://github.com/ageitgey/face_recognition), OpenCV DNN SSD
* **Image Filters**: [pilgram](https://github.com/python-pilgram/pilgram)
* **Database**: SQLite3
* **QR Code**: `qrcode` Python library

---

## 🚀 How to Run Locally

### 1. Clone the repo:

```bash
git clone https://github.com/mihirjain4/Film-mage.git
cd filmmage
```

### 2. Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Download face detection models

Place these files in `models/` directory:

* `deploy.prototxt`
* `res10_300x300_ssd_iter_140000_fp16.caffemodel`

You can get them from: [https://github.com/opencv/opencv/tree/master/samples/dnn/face\_detector](https://github.com/opencv/opencv/tree/master/samples/dnn/face_detector)

### 5. Run the app:

```bash
streamlit run app.py
```

