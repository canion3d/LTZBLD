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
from web3 import Web3
import requests

url = "https://api.blockspan.com/v1/collections?chain=eth-main&page_size=25"

headers = {
    "accept": "application/json",
    "X-API-KEY": "92tWUENVMyncAreMMS6BsQPplLMM54b9"
}

response = requests.get(url, headers=headers)

print(response.text)

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
