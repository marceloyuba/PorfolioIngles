import streamlit as st

st.set_page_config(page_icon="scr/fondo.jpg", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/PorfolioIngles/blob/main/scr/fondo.jpg?raw=true");
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
font-color
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

