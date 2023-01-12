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

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Printing Report", page_icon=":guardsman:", layout="wide")

# Read the printing report data into a pandas DataFrame
df = pd.read_csv('printing_report.csv')

# Show the data in a table
st.dataframe(df)

# Create a chart of the data
st.line_chart(df)

# Add a title to the chart
st.title("Printing Report Chart")
