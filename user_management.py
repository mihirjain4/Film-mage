import streamlit as st

def signup_page(c, conn):
    """Handles user signup functionality."""
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    user_type = st.selectbox("Choose account type", ["User", "Photographer"])

    if st.button("Sign Up"):
        if password == confirm_password:
            c.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = c.fetchone()
            if existing_user:
                st.error("Username already exists. Please choose a different username.")
            else:
                c.execute("INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)",
                          (username, password, user_type))
                conn.commit()
                st.success("Sign up successful! Please login.")
                st.session_state.page = "login"
        else:
            st.error("Passwords do not match")
    st.write('Already have an account?')
    if st.button("Login"):
        st.session_state.page = "login"

def login_page(c, conn):
    """Handles user login functionality."""
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        if user:
            st.success(f"Welcome back, {username}!")
            st.session_state.page = "home"
            st.session_state.username = username
        else:
            st.error("Invalid username or password.")
