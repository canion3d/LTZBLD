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
#from st_paywall import add_auth, require_auth

# Display the image centered in the page
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.image("LTZBLD_gray.png", use_column_width=True)
with col3:
    st.write("")

st.video("https://www.youtube.com/watch?v=obj21YJLScE")

st.markdown("<h1 style='text-align: center; color: black;'>LTZBLD - Let's Build!</h1>", unsafe_allow_html=True)

st.sidebar.image('Canion3D_original-logos_PNG.png', use_column_width=1)

st.markdown("<h2 style='text-align: center; color: white;'>Select a dashboard to get started: </h2>", unsafe_allow_html=True)

images = ['Picture3.PNG', 'Picture4.png']

st.sidebar.header("LTZBLD TV!")

st.sidebar.video("https://www.youtube.com/watch?v=cdOe5wcfVJo")

st.sidebar.header("To learn more watch our commercial!")

st.sidebar.video("3DPaaSgood.mp4")

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=1207190.332&subid=0&type=4"><IMG border="0"   alt="Newegg" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=1207190.332&subid=0&type=4&gridnum=1"></a>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Watch Your Model Build LIVE when you order a 3D Print from us!</h1>
    </div>
    """,
    unsafe_allow_html=True
)

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

	primaryColor="#F63366"
	backgroundColor="#DDDDDD"
	secondaryBackgroundColor="#F0F2F6"
	textColor="#262730"
	font="sans serif"

col1, col2, col3 = st.columns(3)

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

st.markdown("""
<a target="_blank" href="https://shareasale.com/r.cfm?b=1517944&amp;u=3574798&amp;m=57542&amp;urllink=&amp;afftrack="><img src="https://static.shareasale.com/image/57542/generic-300x250-red_00.jpg" border="0" alt="Buy Gold and Silver" /></a>
""", unsafe_allow_html=True)

st.markdown("""
<a href="https://shareasale.com/u.cfm?d=1007382&amp;m=139161&amp;u=3574798&amp;afftrack="><IMG border="0"   alt="Mole 3D Scanner" src="https://static.shareasale.com/image/139161/00-1975x250_00.png" border="0" /></a>
""", unsafe_allow_html=True)

def page3():
    st.markdown("# Technology News 🎉")
    st.sidebar.markdown("# Technology News 🎉")

import requests

# set the API endpoint and parameters
url = "https://newsapi.org/v2/top-headlines?country=us&category=technology"
params = {"country": "us", "apiKey": "e05f54f819fb43b4b67385072ad1db10"}

# make the API request and retrieve the data
response = requests.get(url, params=params)
data = response.json()

# display the data in the Streamlit app with formatting

st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Technology News</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("Here are the top headlines in tech:")
for article in data["articles"]:
        st.write("## " + article["title"])
        st.write(article["description"])
        st.write(f"Source: {article['source']['name']}  Published: {article['publishedAt']}")
        st.write(f"URL: {article['url']}")  # Display the source URL
        st.write("---")
	    
def page4():
    st.markdown("# Order a 3D Print  ❄️")
    st.sidebar.markdown("# Order a 3D Print ❄️")
    
    st.markdown("<h1 style='text-align: center; color: white;'>Get a quote and Order a 3D Print!</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://www.treatstock.com/order-upload/widget?posUid=fixedPs&psId=3567", width=1024,
                            height=768, scrolling=False)

def page5():
    st.markdown("# 3D Model Slicer 🎉")
    st.sidebar.markdown("# 3D Model Slicer 🎉")
	
    st.markdown("<h1 style='text-align: center; color: white;'>Slice your 3D Models for your next 3D Print!</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://icesl.loria.fr/webprinter/", width=1600, height=1600, scrolling=True)
	
#Slicer courtesy of IceSL.	

page_names_to_funcs = {
    "Home Page": main_page,
    "Model Viewer": page2,
    "Technology News": page3,
    "Get a quote and Order a 3D Print": page4,
    "3D Model Slicer": page5,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)
