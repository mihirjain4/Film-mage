import streamlit as st
import sqlite3
import os
import uuid
import io
import zipfile
from PIL import Image

# Import functions from separated modules
from db_utils import initialize_db, get_db_connection
from user_management import signup_page, login_page
from event_management import create_event, display_event_details, event_page, multiple_image_uploader
from face_recognition_utils import upload_face, user_face_found
from preset_filters import preset_app

# Global variables (or pass them as arguments where needed)
event_ids = set()

# Initialize database connection
conn = get_db_connection()
c = conn.cursor()
initialize_db(c, conn)

# Streamlit page navigation
if 'page' not in st.session_state:
    st.session_state.page = "signup"

if st.session_state.page == "login":
    login_page(c, conn)
elif st.session_state.page == "signup":
    signup_page(c, conn)
elif st.session_state.page == "home":
    st.title("Home")
    st.write(f"Welcome, {st.session_state.username}!")
    if st.button("Events"):
        st.session_state.page = "event_page"

    # Check user type
    c.execute("SELECT user_type FROM users WHERE username=?", (st.session_state.username,))
    user_type = c.fetchone()[0]

    if user_type == "Photographer":
        st.subheader("Your Events")
        # Display events created by the photographer
        c.execute("SELECT * FROM events WHERE photographer=?", (st.session_state.username,))
        events = c.fetchall()
        for event in events:
            if st.button(event[1]):
                display_event_details(c, event[1])

        st.subheader("Want to create a new Event?")
        if st.button("Create Event"):
            st.session_state.page = "create_event"
    else:
        st.subheader("Your Events")
        # Display all events for regular users
        c.execute("SELECT * FROM events")
        events = c.fetchall()
        for event in events:
            if st.button(event[1]):
                display_event_details(c, event[1])

elif st.session_state.page == "create_event":
    create_event(c, conn, event_ids)
elif st.session_state.page == "upload_face":
    upload_face(c)
elif st.session_state.page == "user_face_found":
    user_face_found(c)
elif st.session_state.page == "event_page":
    event_page(c)
elif st.session_state.page == "preset":
    preset_app(c)

