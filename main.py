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
    st.markdown("# 3D Printing News 🎉")
    st.sidebar.markdown("# 3D Printing News 🎉")

	"status": "ok",
	"totalResults": 10,
	-"articles": [
	-{
	-"source": {
	"id": "techcrunch",
	"name": "TechCrunch"
	},
"author": "Annie Njanja",
"title": "Meta faces third lawsuit in Kenya as moderators claim illegal sacking, blacklisting",
"description": "Co-accused Sama, whose clients include OpenAI, dropped Meta’s contract and content review services to concentrate on labeling work.",
"url": "https://techcrunch.com/2023/03/20/meta-faces-third-lawsuit-in-kenya-as-moderators-claim-illegal-sacking-blacklisting/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2022/10/meta-distorted-glitched.jpg?resize=1200,675",
"publishedAt": "2023-03-20T18:58:20Z",
"content": "Social media giant Meta and its Kenya-based content moderation partners, Sama and Majorel, are facing a new lawsuit in Kenya. In a petition filed today, 43 content moderators allege unlawful terminat… [+2685 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Jacquelyn Melinek",
"title": "Web3 gaming will onboard up to 100M gamers in next 2 years, Polygon and Immutable presidents predict",
"description": "The web3 gaming space is set to explode over the next few years, Robbie Ferguson of Immutable and Ryan Wyatt of Polygon Labs predict.",
"url": "https://techcrunch.com/2023/03/20/polygon-immutable-web3-gaming/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2017/02/gettyimages-200279525-001.jpg?resize=1200,788",
"publishedAt": "2023-03-20T18:07:08Z",
"content": "Two key players in the web3 gaming space predict exponential expansion in the next few years.\r\nRobbie Ferguson, co-founder and president of web3 gaming company Immutable, and Ryan Wyatt, president of… [+1773 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Jacquelyn Melinek",
"title": "Polygon and Immutable partner to help onboard more gamers and developers into web3",
"description": "Web3 gaming firm Immutable and layer-2 blockchain Polygon partnered to accelerate development and adoption in the crypto gaming space.",
"url": "https://techcrunch.com/2023/03/20/polygon-and-immutable-partner-to-help-onboard-more-gamers-and-developers-into-web3/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2023/02/GettyImages-1363836297.jpg?resize=1200,800",
"publishedAt": "2023-03-20T18:05:52Z",
"content": "Web3 gaming firm Immutable and layer-2 blockchain Polygon hope that a new strategic alliance will accelerate innovation and adoption in the nascent crypto gaming space.\r\nFor us this is a pretty obvio… [+3738 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Taylor Hatmaker",
"title": "Twitch says it will lay off 400 employees",
"description": "The layoffs were characterized as an effort to make Twitch's business more sustainable in the face of challenging economic conditions.",
"url": "https://techcrunch.com/2023/03/20/twitch-says-it-will-lay-off-400-employees/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2022/02/GettyImages-1037023406.jpeg?resize=1200,800",
"publishedAt": "2023-03-20T17:51:24Z",
"content": "Twitch announced plans to reduce its workforce on Monday, demonstrating that even the booming streaming site isn’t immune to the reductions that have swept the tech industry in the last six months.\r\n… [+829 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Frederic Lardinois",
"title": "Aembit raises $16.6M to bring identity management to workloads",
"description": "Maryland-based workload identity startup Aembit today announced that it has raised a $16.5 million seed funding round.",
"url": "https://techcrunch.com/2023/03/20/aembit-raises-16-6m-to-bring-identity-management-to-workloads/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2023/03/GettyImages-1334595508.jpg?resize=1200,631",
"publishedAt": "2023-03-20T17:39:25Z",
"content": "Aembit, a Maryland-based security startup that focuses on helping DevOps and security teams manage how federated workloads talk to each other, is officially launching its service today and announcing… [+3910 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Ron Miller",
"title": "AWS takes a hit in latest round of Amazon layoffs",
"description": "When Amazon announced 9000 additional layoffs this morning, perhaps it wasn't surprising that AWS was included as growth slows.",
"url": "https://techcrunch.com/2023/03/20/aws-takes-a-hit-in-latest-round-of-amazon-layoffs/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2019/10/AWS-logo.jpg?resize=1200,761",
"publishedAt": "2023-03-20T16:42:31Z",
"content": "When Amazon announced it was laying off another 9,000 employees today, AWS employees were not exempt with Amazon CEO (and former AWS CEO) Andy Jassy announcing the cloud division would be included in… [+2249 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Romain Dillet",
"title": "Flagstar Bank to buy some Signature Bank assets, but not crypto operations",
"description": "Flagstar Bank, a subsidiary of New York Community Bancorp, has signed a takeover agreement with U.S. regulators for some of Signature Bank’s assets and loans. Earlier this month, after Silicon Valley Bank’s customers all tried to withdraw their funds at the s…",
"url": "https://techcrunch.com/2023/03/20/flagstar-bank-to-buy-some-signature-bank-assets-but-not-crypto-operations/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2023/03/GettyImages-1248106828.jpg?resize=1200,800",
"publishedAt": "2023-03-20T15:55:52Z",
"content": "Flagstar Bank, a subsidiary of New York Community Bancorp, has signed a takeover agreement with U.S. regulators for some of Signature Banks assets and loans. Earlier this month, after Silicon Valley … [+2114 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Matt Burns",
"title": "Hear why AtoB calls itself Stripe for trucking on TechCrunch Live",
"description": "Trucking is a vital industry and yet the majority of operations are operating on outdated platforms. AtoB thinks it has the solution.",
"url": "https://techcrunch.com/2023/03/20/hear-why-atob-calls-itself-stripe-for-trucking-on-techcrunch-live/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2023/03/TCL-2023-03-22-featured-1920x1080-1.jpg?resize=1200,675",
"publishedAt": "2023-03-20T15:16:37Z",
"content": "Trucking is a vital industry and yet the majority of operations are operating on outdated platforms. AtoB thinks it has the solution and co-founder Harshita Arora says the company is essentially Stri… [+1025 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Sarah Perez",
"title": "Twitter testing government ID-based verification, new screenshots show",
"description": "Twitter appears to be testing a new verification process for Twitter Blue subscribers that would involve submitting a government ID. Code-level insights reveal a process for sending in a photo of the user’s ID, both front and back, along with a selfie photo t…",
"url": "https://techcrunch.com/2023/03/20/twitter-testing-government-id-based-verification-new-screenshots-show/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2022/11/twitter-verified.jpg?resize=1200,813",
"publishedAt": "2023-03-20T15:14:24Z",
"content": "Twitter appears to be testing a new verification process for Twitter Blue subscribers that would involve submitting a government ID. Code-level insights reveal a process for sending in a photo of the… [+3779 chars]"
},
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Alex Wilhelm",
"title": "For tech titans, AI prominence is the new measuring stick",
"description": "For many tech companies, investors are applying a new valuation method that has caught our eye: AI proficiency.",
"url": "https://techcrunch.com/2023/03/20/chatgpt-ai-startup-valuations/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2020/05/NSussman_Techcrunch_Exchange_v3-GRN.jpg?resize=1200,900",
"publishedAt": "2023-03-20T15:07:10Z",
"content": "For many tech companies, investors are applying a new valuation method that has caught our eye: AI proficiency.\r\nThe current wave of AI hype has two main flavors that I’m interested in. First, the st… [+740 chars]"
}
]
}

import streamlit as st
import json

data = json.loads('''{
"status": "ok",
"totalResults": 10,
-"articles": [
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Annie Njanja",
"title": "Meta faces third lawsuit in Kenya as moderators claim illegal sacking, blacklisting",
"description": "Co-accused Sama, whose clients include OpenAI, dropped Meta’s contract and content review services to concentrate on labeling work.",
"url": "https://techcrunch.com/2023/03/20/meta-faces-third-lawsuit-in-kenya-as-moderators-claim-illegal-sacking-blacklisting/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2022/10/meta-distorted-glitched.jpg?resize=1200,675",
"publishedAt": "2023-03-20T18:58:20Z",
"content": "Social media giant

page_names_to_funcs = {
    "Home Page": main_page,
    "Model Viewer": page2,
    "Technology News": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

