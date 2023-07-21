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

from moralis import evm_api

api_key = "9E7gJnfD3salEVXsS9WkWPqMjtf7NGMZPj2IsADvwgB5tfxt38Qtio83Slq6tOYJ"
params = {
        "address": "0x057Ec652A4F150f7FF94f089A38008f49a0DF88e",
        "chain": "eth",
        "to_block": 1.2,
    }

result = evm_api.balance.get_native_balance(
        api_key=api_key,
        params=params,
    )

print(result)

from web3 import Web3

import streamlit as st
import numpy as np

# Create an interactive title
st.title("Blockchain Data Visualization")

# Display a sample chart of blockchain data
st.write("Blockchain data:")
chart_data = np.random.randn(20, 3)
st.line_chart(chart_data)

# Display a sample bar graph of blockchain data
st.write("Blockchain data:")
bar_data = np.random.rand(10)
st.bar_chart(bar_data)

# Create the button

import streamlit as st

run_button = st.button("Connect to Metamask")
text='Connect Wallet',
font_size=15,
font_family='Arial',
background_color='#0086b3',
border_color='#0086b3',
border_width=1

# On button click, connect the Metamask wallet
@button.on_click
def connect_metamask():
    # Connect Metamask
    web3.eth.enable_metamask()
    # Display a success message
    st.write("Successfully connected to Metamask wallet!")

st.markdown("<h1 style='text-align: center; color: white;'>LTZBLD Blockchain Services</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>LTZBLD Blockchain Services</h1>" , unsafe_allow_html = True)

st.markdown("<h1 style='text-align: center; color: white;'>Coming Soon</h1>" , unsafe_allow_html = True)

