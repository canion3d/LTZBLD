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

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('3DPASS.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""LTZBLD login"""

	st.title("Welcome to LTZBLD")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()

primaryColor="#F63366"
backgroundColor="#DDDDDD"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

col1, col2, col3 = st.columns(3)

st.sidebar.header("Apps and Features")

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("", ["Upload Model", "Slicer", "3DP Analytics", "Service Bureau Search", "LTZBLD Blockchain", "SLS & BinderJet Quote"],
        icons=['house', 'cloud-upload', 'menu-app', 'menu-app','menu-app', 'menu-app', 'menu-app'],
        menu_icon="cast", default_index=0, orientation="vertical",styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"10px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "red"},
    }
)

if selected == "Main": ("")

if selected ==  "Upload Model" : ("")

if selected == "Slicer": os.startfile("")

if selected ==  "3DP Analytics" : ("")
   
if selected == "Service Bureau Search": ("")

if selected ==  "LTZBLD Blockchain" : ("")
    
if selected == "SLS & BinderJet Quote": ("")

option = st.sidebar.selectbox('Select Feature',['Home','Model Viewer','Slicer','3DP Analytics','Service Bureau Connect','Blockchain Service','SLS and BinderJet Quote']) #two pages

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

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)

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
# Chart data
chart_data = np.random.randn(20, 3)
st.line_chart(chart_data)

# Bar graph data
bar_data = np.random.rand(10)
st.bar_chart(bar_data)

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

#Create the button
button = Button(
    text='Connect Wallet',
    font_size=15,
    font_family='Arial',
    background_color='#0086b3',
    border_color='#0086b3',
    border_width=1
)

#On button click, connect the Metamask wallet
@button.on_click
def connect_metamask():
    #Create an instance of Web3
    web3 = Web3(Web3.EthereumTesterProvider())
    #Connect Metamask
    web3.eth.enable_metamask()
    #Display a success message
    print("Successfully connected to Metamask wallet!")	

    from web3 import Web3
    from web3constant.Fantom.Url import FTM_RPC

    w3 = Web3(Web3.HTTPProvider(FTM_RPC))
    if w3.isConnected():
         print("Web3 is connected.")
st.markdown("<h1 style='text-align: center; color: white;'>3DPaaS Blockchain Services</h1>" , unsafe_allow_html = True)

if option == 'SLS and BinderJet Quote':
    st.markdown("<h1 style='text-align: center; color: white;'>SLS and BinderJet Quote</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://trin.do/demand/" , width = 1000  , height = 1000 , scrolling = True)
