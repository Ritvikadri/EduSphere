""" EduSphere """
import os
import time
import streamlit as st
import supabase as sb

st.set_page_config(
    page_title="EduSphere",
    page_icon=os.path.join(os.path.dirname(__file__), "logo.png"),
    layout="wide",
)

def get_supabase_client():
    if "supabase_client" not in st.session_state:
        url = st.secrets.get("SUPABASE_URL","")
        key = st.secrets.get("SUPABASE_KEY", st.secrets.get("SUPABASE_PUBLISHABLE_KEY", ""))
        if not url or not key:
            st.error("Supabase is not configured. Add SUPABASE_URL and SUPABASE_KEY to Streamlit secrets.")
            st.stop()
        st.session_state.supabase_client = create_client(url, key)
    return st.session_state.supabase_client