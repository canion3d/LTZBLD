import os
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

	st.title("LTZBLD")

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
    selected = option_menu("", ["Upload Model & get Quote", "3D Slicer", "3DP Analytics", "Service Bureau Search", "LTZBLD Blockchain"],
        icons=['house', 'cloud-upload', 'menu-app', 'menu-app','menu-app', 'menu-app', 'menu-app'],
        menu_icon="cast", default_index=0, orientation="vertical",styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"10px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "red"},
    }
)

if selected == "Upload Model & get Quote": os.startfile ("Upload and Quote.py")

if selected == "3D Slicer": os.startfile("Slicer.py")

if selected == "3DP Analytics" : os.startfile("Analytics.py")

if selected == "Service Bureau Search" : os.startfile("Service Bureaus.py")

if selected == "LTZBLD Blockchain" : os.startfile("Blockchain.py")

st.write("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto');
html, body, [class*="css"]  {
   font-family: 'Roboto'
}
</style>
""", unsafe_allow_html=True)