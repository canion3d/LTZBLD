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

if selected == "Upload Model & get Quote":
    st.markdown("<h1 style='text-align: center; color: white;'>View Models with the Online Model Viewer</h1>",
                unsafe_allow_html=True)

st.components.v1.iframe("https://3dviewer.net", width=1024, height=768, scrolling=False)

st.components.v1.iframe("https://www.treatstock.com/order-upload/widget?posUid=fixedPs&psId=3567", width=1024,height=768, scrolling=False)
