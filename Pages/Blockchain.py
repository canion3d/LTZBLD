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

# streamlit_app.py

# Security
# passlib,hashlib,bcrypt,scrypt
import hashlib


def make_hashes(password) :
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password , hashed_text) :
    if make_hashes(password) == hashed_text :
        return hashed_text
    return False


# DB Management
import sqlite3

conn = sqlite3.connect('3DPASS.db')
c = conn.cursor()


# DB  Functions
def create_usertable() :
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username , password) :
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)' , (username , password))
    conn.commit()


def login_user(username , password) :
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?' , (username , password))
    data = c.fetchall()
    return data


def view_all_users() :
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main() :
    """LTZBLD login"""


col1 , col2 , col3 = st.columns(3)

with col1 :
    st.write('LTZBLD')


def img_to_html(param) :
    pass


with col2 :
    st.image("LTZBLD_logo.png")

menu = ["Home" , "Login" , "SignUp"]
choice = st.sidebar.selectbox("Menu" , menu)

if choice == "Home" :
    st.subheader("Home")

elif choice == "Login" :
    st.subheader("Login Section")

    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password" , type = 'password')
    if st.sidebar.checkbox("Login") :
        # if password == '12345':
        create_usertable()
        hashed_pswd = make_hashes(password)

        result = login_user(username , check_hashes(password , hashed_pswd))
        if result :

            st.success("Logged In as {}".format(username))

            task = st.selectbox("Task" , ["Add Post" , "Analytics" , "Profiles"])
            if task == "Add Post" :
                st.subheader("Add Your Post")

            elif task == "Analytics" :
                st.subheader("Analytics")
            elif task == "Profiles" :
                st.subheader("User Profiles")
                user_result = view_all_users()
                clean_db = pd.DataFrame(user_result , columns = ["Username" , "Password"])
                st.dataframe(clean_db)
        else :
            st.warning("Incorrect Username/Password")





    elif choice == "SignUp" :
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password" , type = 'password')

        if st.button("Signup") :
            create_usertable()
            add_userdata(new_user , make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")

if __name__ == '__main__' :
    main()

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

st.markdown("<h1 style='text-align: center; color: white;'>LTZBLD Blockchain Services</h1>" , unsafe_allow_html = True)

st.markdown("<h1 style='text-align: center; color: white;'>Coming Soon</h1>" , unsafe_allow_html = True)

