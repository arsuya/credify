import streamlit as st
from PIL import Image
import home, prediction, eda, profile_page

st.set_page_config(page_title = "Credit Risk Analysis & Modelling",
                   layout = 'centered',
                   initial_sidebar_state = 'expanded')
with st.sidebar:
    
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("credify.png", width=300) 
    st.write('# Navigation Sidebar')
    navigation = st.radio('Page', ['Home', 
                                   'Exploratory Data Analysis (EDA) Section', 
                                   'Credit Risk Analysis Prediction Section',
                                   'About Our Team'])

if navigation == 'Exploratory Data Analysis (EDA) Section':
    eda.show()

if navigation == 'Credit Risk Analysis Prediction Section':
    prediction.run()

if navigation == 'Home':
    home.run()

if navigation == 'About Our Team':
    profile_page.show()