import streamlit as st

st.set_page_config(page_icon="scr/fondo.jpg", layout="wide")

page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/PorfolioIngles/blob/main/scr/taxis.png?raw=true");
background-position: top left;
background-repeat: repeat;
background-attachment: local;
font-color
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("It's summer!")
