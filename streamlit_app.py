import streamlit as st

st.set_page_config(page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

custom_css = """
<style>
    body {
        font-family: 'Roboto', sans-serif; /* Example: Change the font family */
        background-color: #f0f0f0; /* Example: Change the background color */
        color: #333; /* Example: Change the text color */
    }
</style>
"""

# ---- HEADER SECTION ----
with st.container():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.subheader("Hola, soy Marcelo Yuba :wave:")
    st.markdown('<style>h1 {color: white;}</style>', unsafe_allow_html=True)
    st.title("Un Data Analyst  y Data Scientist de Buenos Aires, Argentina")
    st.write(
        "Soy un apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para tu negocio."
    )
    st.write("[Mi Github >](https://github.com/marceloyuba)")
    st.write("[Mi LinkedIn >](https://www.linkedin.com/in/marcelo-yuba-b9a39827b/)")












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