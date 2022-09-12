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

from pip._internal import main

# streamlit_app.py

import streamlit as st


primaryColor="#F63366"
backgroundColor="#DDDDDD"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

st.sidebar.header ("Manage your account")

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image('LTZBLD_logo.png', use_column_width=true)

with col3:
    st.write('Welcome and LTZBLD!')

# A streamlit app with two centered texts with different seizes
import streamlit as st

option = st.sidebar.selectbox('Select Feature',['Home','Model Viewer','Slicer','3DP Analytics','Service Bureau Connect','Blockchain Service','SLS and BinderJet Quote']) #two pages

option = st.sidebar.selectbox('Select Use Case',['Healthcare','Dental','Automotive','Construction 3D Printing'])

st.sidebar.header("View your model build live!")

st.sidebar.video("https://www.youtube.com/watch?v=obj21YJLScE")

st.sidebar.header("To learn more watch our commercial!")

st.sidebar.video("3DPaaSgood.mp4")

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

if option == 'Home':
    st.markdown("<h1 style='text-align: center; color: white;'>LTZBLD Home</h1>" , unsafe_allow_html = True)

    st.markdown("<h1 style='text-align: center; color: white;'>Welcome! Select a menu feature to get started!</h1>" , unsafe_allow_html = True)
    
    option = st.selectbox(
     'Select a Feature!',
     ('Model Viewer','Slicer','3DP Analytics','Service Bureau Connect','Blockchain Service','SLS and BinderJet Quote'))


if option == 'Model Viewer':
    st.markdown("<h1 style='text-align: center; color: white;'>View Models with the Online Model Viewer</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://3dviewer.net", width=1024, height=768, scrolling=False)

#online model viewer courtesy of MIT.

if option == 'Slicer':

    st.markdown("<h1 style='text-align: center; color: white;'>Slice your models using the online slicer</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://icesl.loria.fr/webprinter/", width=1600, height=1600, scrolling=True)

#online slicer courtesy of Slicecrafter is powered by Emscripten.

if option == '3DP Analytics':
    st.markdown("<h1 style='text-align: center; color: blue;'>View local and network 3D Printing data</h1" , unsafe_allow_html = True)

    st.metric(
        label = "Available 3D Printers",
        value = "100"
    )

    st.line_chart(chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=["Length","Width","Size"]))

if option == 'Service Bureau Connect':
    st.markdown("<h1 style='text-align: center; color: white;'>Service Bureau Connect!</h1>" , unsafe_allow_html = True)

    st.markdown("<h1 style='text-align: center; color: white;'>Find a Service Bureau in your area (or anywhere)!</h1>" , unsafe_allow_html = True)

    df = pd.DataFrame(np.random.randn(100 , 2) / [50 , 50] + [42.8864 , -78.8784] ,
                      columns = ['lat' , 'lon'])
    st.map(df)

    import requests

    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"

    headers = {
        "X-RapidAPI-Key" : "d29531ae60msh09b292159b1d570p1db262jsnd2039bec5d98" ,
        "X-RapidAPI-Host" : "wft-geo-db.p.rapidapi.com"
    }

    response = requests.request("GET" , url , headers = headers)

    print(response.text)
    
    st.markdown("<h1 style='text-align: center; color: white;'>Find a Construction 3D Printing Partner! (Coming soon)</h1>" , unsafe_allow_html = True)

if option == 'Blockchain Service':

    from web3 import Web3
    from web3constant.Fantom.Url import FTM_RPC

    w3 = Web3(Web3.HTTPProvider(FTM_RPC))
    if w3.isConnected():
         print("Web3 is connected.")
    
    st.markdown("<h1 style='text-align: center; color: white;'>3DPaaS Blockchain Services</h1>" , unsafe_allow_html = True)

    response = requests.get("http://ws.cex.io/ws")
    print(response.status_code)
    Origin: 'wss.cex.io'
    def create_signature(key , secret) :  # (string key, string secret)
        timestamp = int(datetime.datetime.now().timestamp())  # UNIX timestamp in seconds
        string = "{}{}".format(timestamp , key)
        return timestamp , hmac.new(secret.encode() , string.encode() , hashlib.sha256).hexdigest()


    def auth_request(key , secret) :
        timestamp , signature = create_signature(key , secret)
        return json.dumps({'e' : 'auth' ,
                           'auth' : {'key' : key , 'signature' : signature , 'timestamp' : timestamp , } ,
                           'oid' : 'auth' , })


    auth_request = auth_request('oaytt8u0ONzCdcgIhwVzO1CCFmM' , 'rzI00GQWhW9NlIEQ5fNCvG7pxo')

if option == 'SLS and BinderJet Quote':
    st.markdown("<h1 style='text-align: center; color: white;'>SLS and BinderJet Quote</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://trin.do/demand/" , width = 1000  , height = 1000 , scrolling = True)
