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
import os
from streamlit_option_menu import option_menu
from pip._internal import main
from streamlit_option_menu import option_menu

import streamlit as st
#from st_paywall import add_auth, require_auth

# Display the image centered in the page
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.image("LTZBLD_gray.png", use_column_width=True)
with col3:
    st.write("")

st.markdown("<h2 style='text-align: center; color: white;'>Select a dashboard to get started: </h2>", unsafe_allow_html=True)

# List available page files
page_files = os.listdir("Pages")
page_files = [file for file in page_files if file.endswith(".py")]

# Add a menu item to select pages
selected_pages = st.multiselect("Select LTZBLD Features", page_files)

# Execute the selected pages
for selected_page in selected_pages:
    try:
        exec(open(f"Pages/{selected_page}").read())
    except Exception as e:
        st.error(f"An error occurred while loading page '{selected_page}': {e}")
	    
st.video("https://youtu.be/OYvbEGTIzUY")

st.markdown("<h1 style='text-align: center; color: black;'>LTZBLD - Let's Build!</h1>", unsafe_allow_html=True)

st.sidebar.image('Canion3D_original-logos_PNG.png', use_column_width=1)

st.markdown("<h2 style='text-align: center; color: white;'>Select a dashboard to get started: </h2>", unsafe_allow_html=True)

images = ['Picture3.PNG', 'Picture4.png']

st.sidebar.header("LTZBLD TV!")

st.sidebar.video("https://www.youtube.com/watch?v=cdOe5wcfVJo")

st.sidebar.header("To learn more watch our commercial!")

st.sidebar.video("3DPaaSgood.mp4")

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=1207190.332&subid=0&type=4"><IMG border="0"   alt="Newegg" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=1207190.332&subid=0&type=4&gridnum=1"></a>
""", unsafe_allow_html=True)

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
	feature_dict = {"No": 1, "Yes": 2}
	for key, value in feature_dict.items():
		if val == key:
			return value

	def get_value(val, my_dict):
		for key, value in my_dict.items():
			if val == key:
				return value

st.markdown(
	"Canion3D Mission Statement: To be a provider across all industries of only the best 3D Printing Products/Services, "
	"providing our customers with the best customer service, building our business at a grassroots level, "
	"and Using our platform and business success to help those who need the most constructive help. ")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
	<style>
	#MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
	header {visibility: hidden;}
	</style>
	"""
st.markdown(hide_st_style, unsafe_allow_html=True)
	
st.balloons()

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)
