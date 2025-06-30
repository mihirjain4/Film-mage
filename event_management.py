import streamlit as st
import os
import uuid
import qrcode
import io
import zipfile
from PIL import Image

def get_event_id(c, title):
    """Retrieves the event ID for a given title."""
    c.execute("SELECT event_id FROM events WHERE title=?", (title,))
    event_id = c.fetchone()
    return event_id[0] if event_id else None

def multiple_image_uploader(custom, upload_dir="uploads"):
    """Handles uploading multiple images for an event."""
    custom_dir = os.path.join(upload_dir, custom)
    os.makedirs(custom_dir, exist_ok=True)

    uploaded_files = st.file_uploader("Upload multiple images", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

    images = []
    if uploaded_files:
        for i, uploaded_file in enumerate(uploaded_files):
            file_path = os.path.join(custom_dir, f"image_{i + 1}.png")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            images.append(file_path)
    return images

def create_event(c, conn, event_ids_set):
    """Handles the creation of a new event."""
    st.title("Create Event")
    title = st.text_input("Title")
    description = st.text_area("Description")
    multiple_image_uploader(title)

    if st.button("Create"):
        while True:
            event_id = int(uuid.uuid4().int >> 64) % 1000000
            if event_id not in event_ids_set:
                event_ids_set.add(event_id)
                c.execute("INSERT INTO events (event_id, title, description, photographer) VALUES (?, ?, ?, ?)",
                          (event_id, title, description, st.session_state.username))
                conn.commit()
                st.success("Event created successfully!")
                st.session_state.page = "home"
                break

def display_event_details(c, event_title):
    """Displays details and images for a selected event."""
    st.write(f"Title: {event_title}")
    c.execute("SELECT description FROM events where title=? ", (event_title,))
    description = c.fetchone()[0]
    st.write(f"Description: {description}")
    event_id = get_event_id(c, event_title)
    url = f"localhost:8501/{event_id}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    event_folder = os.path.join("uploads", event_title) # Removed absolute path

    if os.path.exists(event_folder):
        image_files = os.listdir(event_folder)
        num_images = len(image_files)
        num_cols = 5
        cols = st.columns(num_cols)
        st.write(f"Found {len(image_files)} images.")

        selected_images = []
        for i, image_file in enumerate(image_files):
            image_path = os.path.join(event_folder, image_file)
            img = Image.open(image_path)
            checkbox = cols[i % num_cols].checkbox(label=f"Image {i + 1}", key=f"checkbox_{i}")
            if checkbox:
                selected_images.append(image_path)
            cols[i % num_cols].image(img, caption=f"Image {i + 1}")
        with zipfile.ZipFile(f"{event_title}_selected.zip", "w") as zipf:
            for image_path in selected_images:
                zipf.write(image_path, os.path.basename(image_path))
        with open(f"{event_title}_selected.zip", "rb") as f:
            st.download_button(label="Download All Selected Images", data=f, file_name=f"{event_title}_selected.zip")
    else:
        st.write("No images found for this event.")
    st.write(f"QR Code for {event_title}:")
    st.image(img_byte_arr)

def event_page(c):
    """Displays the event selection page."""
    st.title("Event Page")
    if st.button("Find a face in Event"):
        st.session_state.page = "upload_face"
    if st.button("Want to try cool presets?"):
        st.session_state.page = "preset"
    c.execute("SELECT title FROM events")
    ev = c.fetchall()
    ev = [item for sublist in ev for item in sublist]
    selected_ev = st.selectbox("Which Event?", ev)
    display_event_details(c, selected_ev)
