import streamlit as st
import pyvista as pv
import tempfile
import os

# Set Streamlit app title and layout
st.title("3D Model Viewer")

st.markdown("<h1 style='text-align: center; color: white;'>View Models with the Online Model Viewer</h1>",
            unsafe_allow_html=True)

st.components.v1.iframe("https://3dviewer.net", width=1024, height=768, scrolling=False)
