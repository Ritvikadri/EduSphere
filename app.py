""" EduSphere """
import os
import time
import streamlit as st
import supabase as sb

st.set_page_config(
    page_title="EduSphere",
    page_icon=os.path.join(os.path.dirname(__file___), "logo.png"),
    layout="wide",
)