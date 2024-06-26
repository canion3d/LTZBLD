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

with col2 :
    st.image("LTZBLD_logo.png")

with col3 :
    st.write("Let's Build together!")

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

primaryColor = "#F63366"
backgroundColor = "#DDDDDD"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

col1 , col2 , col3 = st.columns(3)

st.sidebar.header("Apps and Features")

# 1. as sidebar menu
with st.sidebar :
    selected = option_menu("" , ["Upload Model" , "Slicer" , "3DP Analytics" , "Service Bureau Search" ,
                                 "LTZBLD Blockchain" , "SLS & BinderJet Quote"] ,
                           icons = ['house' , 'cloud-upload' , 'menu-app' , 'menu-app' , 'menu-app' , 'menu-app' ,
                                    'menu-app'] ,
                           menu_icon = "cast" , default_index = 0 , orientation = "vertical" , styles = {
            "container" : {"padding" : "0!important" , "background-color" : "#fafafa"} ,
            "icon" : {"color" : "orange" , "font-size" : "15px"} ,
            "nav-link" : {"font-size" : "15px" , "text-align" : "left" , "margin" : "10px" , "--hover-color" : "#eee"} ,
            "nav-link-selected" : {"background-color" : "red"} ,
        }
                           )

if selected == "Main" : ("")

if selected == "Upload Model" : ("")

if selected == "Slicer" : ("")

if selected == "3DP Analytics" : ("")

if selected == "Service Bureau Search" : ("")

if selected == "LTZBLD Blockchain" : ("")

if selected == "SLS & BinderJet Quote" : ("")

# 2. horizontal menu
selected2 = option_menu("" , ["Main" , "Upload Model" , "Slicer" , "3DP Analytics" , "Service Bureau Search" ,
                              "LTZBLD Blockchain" , "SLS & BinderJet Quote"] ,
                        icons = ['house' , 'cloud-upload' , 'menu-app' , 'menu-app' , 'menu-app' , 'menu-app' ,
                                 'menu-app'] ,
                        menu_icon = "cast" , default_index = 0 , orientation = "horizontal" , styles = {
        "container" : {"padding" : "0!important" , "background-color" : "#fafafa"} ,
        "icon" : {"color" : "orange" , "font-size" : "15px"} ,
        "nav-link" : {"font-size" : "15px" , "text-align" : "left" , "margin" : "10px" , "--hover-color" : "#eee"} ,
        "nav-link-selected" : {"background-color" : "red"} ,
    }
                        )

if selected == "Main" : ("")

if selected == "Upload Model" : ("")

if selected == "Slicer" : ("")

if selected == "3DP Analytics" : ("")

if selected == "Service Bureau Search" : ("")

if selected == "LTZBLD Blockchain" : ("")

if selected == "SLS & BinderJet Quote" : ("")

st.markdown("""Welcome and LTZBLD!
LTZBLD is an all-in-one 3D Printing service by Canion3D.
We have simplified the process and made it more accessible to everyone.
Whether you are a beginner or an expert, our 3D Printing platform will meet your needs.
Our 3D Printing experts are always on call to walk you through the process, every step of the way.""")

# Option menu

option = st.sidebar.selectbox('Select Feature' , ['Home' , 'Model Viewer' , 'Slicer' , '3DP Analytics' ,
                                                  'Service Bureau Connect' , 'Blockchain Service' ,
                                                  'SLS and BinderJet Quote'])  # two pages

st.sidebar.header("View your model build live!")

st.sidebar.video("https://www.youtube.com/watch?v=obj21YJLScE")

st.sidebar.header("To learn more watch our commercial!")

st.sidebar.video("3DPaaSgood.mp4")


@st.cache(suppress_st_warning = True)
def get_fvalue(val) :
    feature_dict = {"No" : 1 , "Yes" : 2}
    for key , value in feature_dict.items() :
        if val == key :
            return value


def get_value(val , my_dict) :
    for key , value in my_dict.items() :
        if val == key :
            return value

st.markdown("<h1 style='text-align: center; color: white;'>Slice your models using the online slicer</h1>" , unsafe_allow_html = True)

st.components.v1.iframe("https://icesl.loria.fr/webprinter/", width=1600, height=1600, scrolling=True)

if option == 'Upload Model & get Quote':
    st.markdown("<h1 style='text-align: center; color: white;'>View Models with the Online Model Viewer</h1>" , unsafe_allow_html = True)

    st.components.v1.iframe("https://3dviewer.net", width=1024, height=768, scrolling=False)

#online model viewer courtesy of MIT.
