import streamlit as st

st.set_page_config(
    page_title="DORA Engine",
    page_icon="???", 
    layout="wide"
)

st.title("??? DORA Engine")
st.subheader("Autonomous Compliance & Workflow Automation")

st.success("?? Application Loaded Successfully!")
st.info("This is a minimal version to test deployment")

# Simple authentication
if 'user' not in st.session_state:
    st.session_state.user = None

with st.sidebar:
    st.header("Authentication")
    if st.button("Sign In"):
        st.session_state.user = {"email": "demo@doraengine.com", "plan": "free"}
        st.rerun()
    
    if st.session_state.user:
        st.success(f"Logged in as: {st.session_state.user['email']}")

# Main content
if st.session_state.user:
    st.write("### DORA Compliance Automation")
    st.write("Upload your Register of Information to begin...")
    
    uploaded_file = st.file_uploader("Upload CSV/XLSX", type=['csv', 'xlsx'])
    if uploaded_file:
        st.success("File uploaded successfully!")
else:
    st.warning("Please sign in to access compliance features")
