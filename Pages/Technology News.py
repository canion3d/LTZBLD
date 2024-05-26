

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
if article.get('urlToImage') and article.get('url'):
          st.markdown(f"<a href='{article['url']}' target='_blank'><img src='{article['urlToImage']}' alt='Image for {article['title']}' style='width:100%;'></a>", unsafe_allow_html=True)
elif article.get('urlToImage'):
          st.image(article['urlToImage'], caption=article['title'])
if article.get('url'):
        st.write(f"URL: {article['url']}")  # Display the source URL
        st.write("---")

st.markdown(
    "Canion3D Mission Statement: To be a provider across all industries of only the best 3D Printing Products/Services, "
    "providing our customers with the best customer service, building our business at a grassroots level, "
    "and using our platform and business success to help those who need the most constructive help. ")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
