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

st.set_page_config(
    layout = "wide" ,
    page_icon = "tada"
)

st.markdown("<h1 style='text-align: center; color: blue;'>View local and network 3D Printing data</h1" , unsafe_allow_html = True)

st.metric(
        label = "Available 3D Printers",
        value = "0"
    )

import pandas as pd
 
DataFrame.to_excel('3DPaaS Headlines, Marketing, Descriptions.xlsx', sep='\t', header=None)
