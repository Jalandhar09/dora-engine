import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="DORA Engine - Autonomous Compliance",
    page_icon="???",
    layout="wide"
)

# Branding
st.markdown(
    '''<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h1 style="color: white; margin: 0; text-align: center;">DORA Engine</h1>
        <p style="color: white; text-align: center; margin: 5px 0 0 0;">Autonomous Compliance & Workflow Automation</p>
    </div>''',
    unsafe_allow_html=True
)

# Simple session state
if 'user' not in st.session_state:
    st.session_state.user = None
if 'plan' not in st.session_state:
    st.session_state.plan = 'free'

# Sidebar
with st.sidebar:
    st.header("?? Authentication")
    
    if not st.session_state.user:
        if st.button("?? Sign In & Start Demo", type="primary", use_container_width=True):
            st.session_state.user = "demo@doraengine.com"
            st.session_state.plan = 'free'
            st.rerun()
    else:
        st.success(f"Logged in as: {st.session_state.user}")
        st.info(f"Plan: {st.session_state.plan.upper()}")
        
        if st.session_state.plan == 'free':
            if st.button("?? Upgrade to Pro ($499/month)", type="secondary", use_container_width=True):
                st.session_state.plan = 'pro'
                st.success("?? Pro trial activated!")
                st.rerun()
        
        if st.button("?? Logout", use_container_width=True):
            st.session_state.user = None
            st.session_state.plan = 'free'
            st.rerun()

# Main content based on authentication
if not st.session_state.user:
    st.warning("?? Welcome to DORA Engine!")
    st.write("Please sign in to begin compliance automation.")
    st.stop()

# Paywall for free users
if st.session_state.plan == 'free':
    st.error("?? PRO FEATURE REQUIRED")
    st.write("**Upgrade to DORA Engine Pro to access compliance automation**")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("**What you're missing:**")
        st.write("• AI-powered regulatory analysis")
        st.write("• Automated ITS mapping")
        st.write("• PQC vulnerability detection")
        st.write("• Professional compliance reports")
    
    with col2:
        if st.button("?? Upgrade Now ($499/month)", type="primary", use_container_width=True):
            st.session_state.plan = 'pro'
            st.rerun()
    
    st.stop()

# PRO FEATURES (only shown to Pro users)
st.success("? DORA ENGINE PRO - FULL FEATURES UNLOCKED")

st.header("?? DORA Compliance Automation")

# Step 1: Upload
st.subheader("Step 1: Upload Register of Information")
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success(f"? File uploaded successfully! {len(df)} records found.")
        st.dataframe(df.head(), use_container_width=True)
        
        # Step 2: Analysis
        st.subheader("Step 2: AI Compliance Analysis")
        if st.button("?? Run AI Analysis", type="primary"):
            with st.spinner("AI analyzing compliance requirements..."):
                # Simulate AI analysis
                st.success("AI analysis complete!")
                st.write("**Compliance Insights:**")
                st.write("- 3 high-criticality services identified")
                st.write("- 2 PQC-vulnerable encryption algorithms found")
                st.write("- DORA Articles 14, 16 applicable")
        
        # Step 3: Reports
        st.subheader("Step 3: Generate Compliance Report")
        if st.button("?? Generate PDF Report", type="secondary"):
            st.success("Compliance report generated!")
            st.download_button(
                label="?? Download Report",
                data="Sample compliance report content",
                file_name="dora_compliance_report.pdf",
                mime="application/pdf"
            )
            
    except Exception as e:
        st.error(f"Error reading file: {e}")

# Deployment status
with st.sidebar:
    st.markdown("---")
    st.markdown("**?? Deployment Status**")
    st.success("? Streamlit Cloud Ready")
