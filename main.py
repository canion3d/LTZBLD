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
	layout="wide",
	page_icon="tada"
     )

# streamlit_app.py

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

col1 , col2 , col3 = st.columns(3)

with col1 :
    st.write('LTZBLD')


def img_to_html(param) :
    pass


with col2 :
    st.image("LTZBLD_gray.png")

with col3 :
    st.write("Let's Build together!")

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


print("Welcome to LTZBLD!")
print("LTZBLD is an all-in-one 3D Printing service by Canion3D. We have simplified the process and made it more accessible to everyone. Whether you are a beginner or an expert, our 3D Printing platform will meet your needs.")
print("Our 3D Printing experts are always on call to walk you through the process, every step of the way.")

#Option menu

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

    st.markdown("<h1 style='text-align: center; color: white;'>Welcome! Select a menu feature to get started!</h1>" , unsafe_allow_html = True)
    
    option = st.selectbox(
     'Select a Feature!',
     ('Model Viewer','Slicer','3DP Analytics','Service Bureau Connect','Blockchain Service','SLS and BinderJet Quote'))

st.write("Please support our project by clicking the referral link by our friends at Treastock! [Order a 3D Print Now!](https://www.treatstock.com/my/print-model3d?utm_aff=ltzbld&affiliate=h9ZK9Ul)")

if option == 'Model Viewer':
    st.markdown("<h1 style='text-align: center; color: white;'>View Models with the Online Model Viewer</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://3dviewer.net", width=1024, height=768, scrolling=True)

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
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the printing report data into a pandas DataFrame
df = pd.read_csv('printing_report.csv')

# Show the data in a table
st.dataframe(df)

# Create a chart of the data
st.line_chart(df)

# Add a title to the chart
st.title("Printing Report Chart")


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
	
# Imports
   import os
   import requests
   from dotenv import load_dotenv
   load_dotenv()
   from bip44 import Wallet
   from web3 import Account
   from web3 import middleware
   from web3.gas_strategies.time_based import medium_gas_price_strategy
   from web3 import Web3
	

# Imports
import streamlit as st

# Import the functions from ethereum.py
from ethereum import w3 , generate_account , get_balance , send_transaction
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Streamlit application headings
st.markdown("# Automating Ethereum with Streamlit!")

# Generate the Ethereum account
account = generate_account(w3)

# The Ethereum Account Address
st.text("\n")
st.text("\n")
st.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
st.write(account.address)

# Display the Etheremum Account balance
st.text("\n")
st.text("\n")
st.markdown("## Ethereum Account Balance:")

# Call the get_balance function and write the account balance to the screen
ether_balance = get_balance(w3 , account.address)
st.write(ether_balance)

# An Ethereum Transaction
st.text("\n")
st.text("\n")
st.markdown("## An Ethereum Transaction")

# Create inputs for the receiver address and ether amount
receiver = st.text_input("Input the receiver address")
ether = st.number_input("Input the amount of ether")

# Create a button that calls the `send_transaction` function and returns the transaction hash
if st.button("Send Transaction") :

    transaction_hash = send_transaction(w3 , account , receiver , ether)

    # Display the Etheremum Transaction Hash
    st.text("\n")
    st.text("\n")
    st.markdown("## Ethereum Transaction Hash:")

    st.write(transaction_hash)

    w3 = Web3(Web3.HTTPProvider(FTM_RPC))
    if w3.isConnected() :
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

