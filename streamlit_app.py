import streamlit as st
from supabase import create_client

# -----------------------
# Supabase Setup
# -----------------------
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_ANON = st.secrets["SUPABASE_ANON_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_ANON)

# -----------------------
# Auth State
# -----------------------
if "user" not in st.session_state:
    st.session_state.user = None

def login(email, password):
    try:
        result = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return result.user
    except Exception:
        return None

def signup(email, password):
    try:
        supabase.auth.sign_up({"email": email, "password": password})
        return True
    except Exception:
        return False

# -----------------------
# LOGIN SCREEN
# -----------------------
if st.session_state.user is None:
    st.set_page_config(page_title="DORA Engine Login", page_icon="🔐")
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
                st.error("❌ Invalid email or password")

    with tab_signup:
        new_email = st.text_input("Signup Email")
        new_pass = st.text_input("Create Password", type="password")
        if st.button("Sign Up"):
            if signup(new_email, new_pass):
                st.success("Account created. Check email verification.")
            else:
                st.error("Could not create account.")
    
    st.stop()

# -----------------------
# AUTHENTICATED UI
# -----------------------
st.set_page_config(page_title="DORA Engine", page_icon="⚙️")

st.title("⚙️ DORA Engine - AI Compliance Automation")
st.success(f"👋 Logged in as: {st.session_state.user.email}")

st.write("Next: Build role-based dashboard, AI compliance mapping, user tiers, billing, etc.")
