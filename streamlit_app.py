import streamlit as st
from PIL import Image
import base64
import home, prediction, eda

st.set_page_config(page_title = "Credit Risk Analysis & Modelling",
                   layout = 'centered',
                   initial_sidebar_state = 'expanded')

def sidebar_logo(image_path, width):
    # Konversi gambar ke base64 agar bisa dimasukkan ke HTML
    with open(image_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    
    # HTML untuk gambar di tengah
    html_code = f"""
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
        <img src="data:image/png;base64,{b64}" width="{width}">
    </div>
    """
    st.sidebar.markdown(html_code, unsafe_allow_html=True)

with st.sidebar:
    
    logo = Image.open("credify.png")
    sidebar_logo(logo, width=50)
    st.write('# Navigation Sidebar')
    navigation = st.radio('Page', ['Home', 
                                   'Exploratory Data Analysis (EDA) Section', 
                                   'Credit Risk Analysis Prediction Section'])

if navigation == 'Exploratory Data Analysis (EDA) Section':
    eda.show()

if navigation == 'Credit Risk Analysis Prediction Section':
    prediction.run()

if navigation == 'Home':
    home.run()
