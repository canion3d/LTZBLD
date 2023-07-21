

st.markdown("<h1 style='text-align: center; color: black;'>LTZBLD - Let's Build!</h1>", unsafe_allow_html=True)

st.sidebar.image('Canion3D_original-logos_PNG.png', use_column_width=1)

st.markdown("Start building your dream!")

images = ['Picture3.PNG', 'Picture4.png']

st.sidebar.header("LTZBLD TV!")

st.sidebar.video("https://www.youtube.com/watch?v=cdOe5wcfVJo")

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
