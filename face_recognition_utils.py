import streamlit as st
import cv2 as cv
import face_recognition as fr
import pickle
import numpy as np
import os
import shutil

# Load pre-trained model for face detection
prototxt_path = 'C:/Users/Mihir Jain/OneDrive/Desktop/filmmage/models/deploy.prototxt' # Relative path
caffemodel_path = 'C:/Users/Mihir Jain/OneDrive/Desktop/filmmage/models/res10_300x300_ssd_iter_140000_fp16.caffemodel' # Relative path
net = cv.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

def detect_face(image):
    """Detects face locations in an image."""
    rgb_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    face_locations = fr.face_locations(rgb_img)
    return face_locations

def list_images(folder_path):
    """Lists image files in a given folder."""
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', ".JPEG", ".JPG"))]
    return image_files

def encode_faces(folder):
    """Encodes faces from images in a folder and caches them."""
    try:
        with open(f'{folder}_encodings.pkl', 'rb') as f:
            list_people_encoding = pickle.load(f)
    except (FileNotFoundError, EOFError):
        list_people_encoding = []
        for filename in os.listdir(folder):
            known_image = fr.load_image_file(os.path.join(folder, filename))
            known_encodings = fr.face_encodings(known_image)
            for encoding in known_encodings:
                list_people_encoding.append((encoding, filename))
            if not known_encodings:
                print(f"No face found in {filename}")
        with open(f'{folder}_encodings.pkl', 'wb') as f:
            pickle.dump(list_people_encoding, f)
    return list_people_encoding

def create_frame(image, locations, label):
    """Draws rectangles and labels on detected faces."""
    for (top, right, bottom, left) in locations:
        cv.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 2)
        cv.rectangle(image, (left, bottom + 20), (right, bottom), (255, 0, 0), cv.FILLED)
        cv.putText(image, label, (left + 3, bottom + 14), cv.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 1)

def find_target_face(target_image, target_encodings, frame, folder, c):
    """Finds target faces within an event's images and saves them."""
    (h, w) = target_image.shape[:2]
    blob = cv.dnn.blobFromImage(cv.resize(target_image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    target_folder = os.path.join("uploads", folder)

    c.execute("SELECT username FROM users WHERE username=?", (st.session_state.username,))
    out_dir = c.fetchone()[0]
    output_directory = os.path.join("output/", folder, out_dir)
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            file_path = os.path.join(output_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(output_directory)
    os.makedirs(output_directory)

    processed_files = set()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.05:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            face_locations = [(startY, endX, endY, startX)]
            roi_color = target_image[startY:endY, startX:endX]

            for person in encode_faces(target_folder):
                encoded_face = person[0]
                filename = person[1]
                if filename not in processed_files:
                    filepath = os.path.join(target_folder, filename)
                    for target_encoding in target_encodings:
                        is_target_face = fr.compare_faces([encoded_face], target_encoding, tolerance=0.48)
                        if is_target_face[0]:
                            print(f'{is_target_face} {filepath}')
                            output_path = os.path.join(output_directory, filename)
                            shutil.copyfile(filepath, output_path)
                            label = filepath
                            create_frame(frame, face_locations, label)
                            processed_files.add(filename)

def user_face_found(c):
    """Displays images found for the current user."""
    st.title("User's Images")
    c.execute("SELECT title FROM events")
    ev = c.fetchall()
    ev = [item for sublist in ev for item in sublist]
    if st.button("Want to try cool presets?"):
        st.session_state.page = "preset"
    selected_ev = st.selectbox("Which Event?", ev)

    folder_path = os.path.join("output",selected_ev, st.session_state.username)
    
    if os.path.exists(folder_path):
        image_files = list_images(folder_path) # Use the list_images function
        num_images = len(image_files)
        num_cols = 5
        cols = st.columns(num_cols)
        st.write(f"Found {len(image_files)} images.")

        selected_images = []
        for i, image_file in enumerate(image_files):
            image_path = os.path.join(folder_path, image_file)
            img = Image.open(image_path)
            checkbox = cols[i % num_cols].checkbox(label=f"Image {i + 1}", key=f"checkbox_{i}")
            if checkbox:
                selected_images.append(image_path)
            cols[i % num_cols].image(img, caption=f"Image {i + 1}")
        with zipfile.ZipFile("selected_images.zip", "w") as zipf:
            for image_path in selected_images:
                zipf.write(image_path, os.path.basename(image_path))
        with open("selected_images.zip", "rb") as f:
            st.download_button(label="Download All Selected Images", data=f, file_name="selected_images.zip")
    else:
        st.warning("No images found for this event and user.")


def upload_face(c):
    """Handles uploading an image for face recognition."""
    st.title("Face Recognition App")
    c.execute("SELECT title FROM events")
    ev = c.fetchall()
    ev = [item for sublist in ev for item in sublist]
    selected_ev = st.selectbox("Which Event?", ev)
    st.write("Upload an image or capture one with a face")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png", "JPG", "JPEG"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        fame = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
        # Convert BGR to RGB
        fame_rgb = cv.cvtColor(fame, cv.COLOR_BGR2RGB)
