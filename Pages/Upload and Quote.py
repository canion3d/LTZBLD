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
    selected = option_menu("", ["Upload Model & get Quote", "Slicer", "3DP Analytics", "Service Bureau Search", "LTZBLD Blockchain", "SLS & BinderJet Quote"],
        icons=['house', 'cloud-upload', 'menu-app', 'menu-app','menu-app', 'menu-app', 'menu-app'],
        menu_icon="cast", default_index=0, orientation="vertical",styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"10px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "red"},
    }
)


if selected == "Upload Model & get Quote":
    st.markdown("<h1 style='text-align: center; color: white;'>View Models with the Online Model Viewer</h1>",
                unsafe_allow_html=True)

    st.components.v1.iframe("https://3dviewer.net", width=1024, height=768, scrolling=False)

    st.components.v1.iframe("<!-- Printer: 13472-HALOT-ONE --><link href="https://www.treatstock.com/css/embed-remote.css" rel="stylesheet" /><iframe class="ts-embed-printservice" width="100%" height="650px" src="https://www.treatstock.com/my/print-model3d/widget?posUid=fixedPsPrinter&psPrinterId=13472" frameborder="0"></iframe>", width=1024,
                            height=768, scrolling=True)
