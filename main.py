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

# 1. horizontal menu
selected2 = option_menu("", ["Main", "Upload Model", "Slicer", "3DP Analytics", "Service Bureau Search", "LTZBLD Blockchain", "SLS & BinderJet Quote"],
        icons=['house', 'cloud-upload', 'menu-app', 'menu-app','menu-app', 'menu-app', 'menu-app'],
        menu_icon="cast", default_index=0, orientation="horizontal",styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"10px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "red"},
    }
)

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

	st.title("LTZBLD TV")

	st.video("https://www.youtube.com/watch?v=cdOe5wcfVJo")

	st.markdown("<h1 style='text-align: center; color: black;'>LTZBLD - Let's Build!</h1>", unsafe_allow_html=True)

	st.sidebar.image('Canion3D_original-logos_PNG.png', use_column_width=1)

	st.markdown("Start building your dream!")

	images = ['Picture3.PNG', 'Picture4.png']

	st.sidebar.header("View your model build live!")

	st.sidebar.video("https://www.youtube.com/watch?v=obj21YJLScE")

	st.sidebar.header("To learn more watch our commercial!")

	st.sidebar.video("3DPaaSgood.mp4")

	@st.cache(suppress_st_warning=True)
	def get_fvalue(val):
		feature_dict = {"No": 1, "Yes": 2}
		for key, value in feature_dict.items():
			if val == key:
				return value

	def get_value(val, my_dict):
		for key, value in my_dict.items():
			if val == key:
				return value

	st.markdown(
		"Canion3D Mission Statement: To be a provider across all industries of only the best 3D Printing Products/Services, "
		"providing our customers with the best customer service, building our business at a grassroots level, "
		"and Using our platform and business success to help those who need the most constructive help. ")

	# ---- HIDE STREAMLIT STYLE ----
	hide_st_style = """
	            <style>
	            #MainMenu {visibility: hidden;}
	            footer {visibility: hidden;}
	            header {visibility: hidden;}
	            </style>
	            """
	st.markdown(hide_st_style, unsafe_allow_html=True)

	st.balloons()
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

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Welcome! Select a menu feature to get started!</h1>" , unsafe_allow_html = True)
    
import streamlit as st

def main_page():
    st.markdown("# Home page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Model Viewer ❄️")
    st.sidebar.markdown("# Model Viewer ❄️")
    
    st.markdown("<h1 style='text-align: center; color: white;'>View Models with the Online Model Viewer</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://3dviewer.net" , width = 1024 , height = 768 , scrolling = True)

# online model viewer courtesy of MIT.

def page3():
    st.markdown("# Analytics 🎉")
    st.sidebar.markdown("# Analytics 🎉")

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

page_names_to_funcs = {
    "Home Page": main_page,
    "Model Viewer": page2,
    "Analytics": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

