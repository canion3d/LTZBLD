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

# Initialize a web3 connection to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/942b8cb3ff0f4d958282d71d85b5a741')

# Display the latest block number
latest_block = get_latest_block_number()
st.write(f'Latest Block Number: {latest_block}')

# Display the current Ether price
eth_price = get_eth_price()
st.write(f'Current Ether Price: ${eth_price} USD')

def get_latest_block_number():
return w3.eth.block_number

def get_eth_price():
response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
data = response.json()
return data['ethereum']['usd']

def main():
st.title('Ethereum Blockchain Statistics')

# Display the latest block number
latest_block = get_latest_block_number()
st.write(f'Latest Block Number: {latest_block}')

# Display the current Ether price
eth_price = get_eth_price()
st.write(f'Current Ether Price: ${eth_price} USD')

if __name__ == "__main__":
    main()

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
