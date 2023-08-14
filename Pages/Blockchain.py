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

import streamlit as st

def main():
    st.title("Connect to crypto wallet")

    # HTML code
    st.components.v1.html(
        """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.7.4-rc.1/web3.min.js"></script>
        <input type="button" value="Connect Wallet" id="connectBtn">
        """
    )

    # JavaScript code
    jscode = """
    /* To connect using MetaMask */
    async function connect() {
      if (window.ethereum) {
         await window.ethereum.request({ method: "eth_requestAccounts" });
         window.web3 = new Web3(window.ethereum);
         const account = web3.eth.accounts;
         //Get the current MetaMask selected/active wallet
         const walletAddress = account.givenProvider.selectedAddress;
         console.log(`Wallet: ${walletAddress}`);
      } else {
       console.log("No wallet");
      }
    }

    document.getElementById('connectBtn').onclick = connect;
    """

    st.components.v1.jscode(jscode)


if __name__ == "__main__":
    main()

st.markdown("<h1 style='text-align: center; color: white;'>LTZBLD Blockchain Services</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>LTZBLD Blockchain Services</h1>" , unsafe_allow_html = True)

st.markdown("<h1 style='text-align: center; color: white;'>Coming Soon</h1>" , unsafe_allow_html = True)

