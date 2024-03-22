import streamlit as st

st.set_page_config(page_icon="scr/fondo.jpg", layout="wide")

st.markdown('''
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Ruluko&display=swap");
  </style>
''', unsafe_allow_html=True)
st.markdown('''
  <h1 style=
  font-family: "Ruluko", sans-serif;
  font-weight: 400;
  font-style: normal;">
  Ruluko
  </h1>
''', unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/PorfolioIngles/blob/main/scr/fondoTaxi.png?raw=true");
background-position: top left;
background-repeat: repeat;
background-attachment: fixed;

}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# ---- HEADER SECTION ----
with st.container():
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.subheader("Hola, soy Marcelo Yuba :wave:")
    st.markdown('<style>h1 {color: white;}</style>', unsafe_allow_html=True)
    st.title("Un Data Analyst  y Data Scientist de Buenos Aires, Argentina")
    st.write(
        "Soy un apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para tu negocio."
    )
    st.write("[Mi Github >](https://github.com/marceloyuba)")
    st.write("[Mi LinkedIn >](https://www.linkedin.com/in/marcelo-yuba-b9a39827b/)")

