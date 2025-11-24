import streamlit as st
from supabase import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_ANON = st.secrets["SUPABASE_ANON_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_ANON)

if "user" not in st.session_state:
    st.session_state.user = None

def login(email, password):
    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return response.user

def signup(email, password):
    response = supabase.auth.sign_up({"email": password, "password": password})
    return response.user

# LOGIN SCREEN
if st.session_state.user is None:
    st.title("🔐 Login to DORA Engine")

    tab_login, tab_signup = st.tabs(["Login", "Create Account"])

    with tab_login:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = login(email, password)
            if user:
                st.session_state.user = user
                st.experimental_rerun()
            else:
                st.error("❌ Invalid login")

    with tab_signup:
        new_email = st.text_input("Signup Email")
        new_pass = st.text_input("Create Password", type="password")
        if st.button("Sign Up"):
            signup(new_email, new_pass)
            st.success("Account created — check email.")

    st.stop()

# AFTER LOGIN
st.sidebar.write(f"👤 Logged in as {st.session_state.user.email}")
