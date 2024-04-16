import os
import selectors
import streamlit as st
import pandas as pd
import base64
import numpy as np
import streamlit.components.v1 as components
import hmac
import hashlib
import datetime
import json
import requests
import altair as al
import sqlite3
from streamlit_option_menu import option_menu
from pip._internal import main
from streamlit_option_menu import option_menu

import streamlit as st

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=1207190.332&subid=0&type=4"><IMG border="0"   alt="Newegg" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=1207190.332&subid=0&type=4&gridnum=1"></a>
""", unsafe_allow_html=True)

primaryColor="#F63366"
backgroundColor="#DDDDDD"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

col1, col2, col3 = st.columns(3)

st.sidebar.header("Apps and Features")

# 1. as sidebar menu
with st.sidebar:
	
    # List available page files
page_files = os.listdir("Pages")
page_files = [file for file in page_files if file.endswith(".py")]

# Add a menu item to select pages
selected_pages = st.multiselect("Select LTZBLD Features", page_files)

# Execute the selected pages
for selected_page in selected_pages:
    exec(open(f"Pages/{selected_page}").read())

st.write("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto');
html, body, [class*="css"]  {
   font-family: 'Roboto'
}
</style>
""", unsafe_allow_html=True)
