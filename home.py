# import streamlit as st
# import pandas as pd

# def run():

#     # Main content
#     st.title("Welcome!")
#     # img_url = "homepictfinpro.jpg"
#     # image = Image.open(img_url)
#     # st.image(image)

#     # Dashboard Introduction
#     st.markdown("""
#     ### What is this Dashboard?

#     This interactive dashboard explains about predicting the customer application on credit card. This dashboard have 4 sidebar, which is: "Home", "EDA", "Prediction" section.
    

#     ---
#     ### Background Problem
#     Since the invention of currency, loans has always been part of the economy. From lending to corporations, to loaning a singular person. Lending to a single person is called a **personal loan**. A personal loan is a type of installment credit issued to a borrower by a lender, such as a bank, credit union, or online lender. Personal loans allow the client to use the loan funds for practically any purpose, such as home renovations, medical expenses, vacations, and large purchases. They're offered by traditional lenders like banks and credit unions as well as nontraditional sources, such as online lenders (Lake, 2023). To assess how trustworthy the client is, lenders can usually determine if it's safe or not by assessing the client's **credit risks**.

#     When assessing credit risks, analysts use the 5 C's of credit : Character, Capacity, Capital, Collateral, and Conditions. **Character** refers to the client's credit history, or how the client have managed debt in the past. **Capacity** refers to the client's ability to repay loans. **Capital** includes the savings, investments, and assets you are willing to put toward a loan. **Collateral** is something the client can provide as security, typically for a secured loan or secured credit card. **Conditions** include other information that helps determine whether the client qualify for credit and the terms your receive (Capital One, 2024).

#     Since these 5 C's significantly take time for analysts to analyze, therefore, it is important to have a computer model that can evaluate the customer’s credit risk to streamline the process of giving loans. By using computer models, the process of evaluating loans would be halved and more loans can be given out in a much more shorter time span. The risk of miscalculating the risk of a loan would be further reduced due to further verification using computer models.

#     Our research and analysis is further reinforced a research article done by R. Balina & M. Idasz-Balina outlining the [Drivers of Individual Credit Risk of Retail Customers](https://doi.org/10.3390/risks9120219) where the article outlines the factors and example use cases of modelling and the factors that can determine the credit risk of a customer based on other factors other than the 5 C's outlined above (Balina & Idasz-Balina, 2021).

#     ---
#     ### Model
#     The model that being used in this project is KNN, Decision Tree, Random Forest, XGBoost, LGBM (Light Gradient Boosting), and Hist Gradient Boosting.
#     For the inference and model deployment, the best algorithm is LGBM (Light Gradient Boosting) which has the highest score in recall metrics with the lowest model size.
    
#     ---
#     """)

#     # Dataset
#     st.markdown("""
#     ### Dataset
#     The dataset used is sourced from **Kaggle**, titled **[Credit Card Approval Prediction](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction)**.
#     """)

#     # How to use Dashboard
#     st.markdown("""
#     ---
#     ### How to use the Dashboard
#     - Click on the options in the **sidebar** to explore EDA and make predictions 
#     - Try uploading various data samples to get different results.

#     Thank you for visiting this dashboard. See you again next time!
                
#     ---
#     """)
    
# if __name__ == "__main__":
#     run()

import streamlit as st

def run():
    # HEADER SECTION
    st.markdown("<h1 style='font-size: 62px;text-align: center;'>Welcome to Credify!</h1>", unsafe_allow_html=True)
    
    # Project logo/image
    st.image("credify.png", use_container_width=True)

    # Introduction paragraph
    paragraph1 = "This interactive dashboard provides an end-to-end view of our credit scoring project, focusing on predicting whether a customer is eligible for a credit card based on key financial and demographic information."
    st.markdown(
        f"""
        <style>
        .paragraph {{
            text-align: justify;
            font-size: 16px;
            line-height: 1.6;
        }}
        </style>
        <p class="paragraph">{paragraph1}</p>
        """,
        unsafe_allow_html=True
    )

    # PROJECT DEFINITION SECTION
    st.header("What is Credify?")
    paragraph2 = "Credify is a credit classification system developed to help financial institutions evaluate the creditworthiness of new applicants. Using historical data and machine learning models, Credify can accurately classify whether an applicant is likely to be a Good Credit holder or fall into Non-Performing Loan (NPL) risk."
    st.markdown(
        f"""
        <style>
        .paragraph {{
            text-align: justify;
            font-size: 16px;
            line-height: 1.6;
        }}
        </style>
        <p class="paragraph">{paragraph2}</p>
        """,
        unsafe_allow_html=True
    )

    # HOW IT WORKS SECTION
    st.write("<h1 style='font-size: 20px;'>How does it work?</h1>", unsafe_allow_html=True)
    st.write("""
    **Credit Risk Prediction**: The system classifies new applicants into either:
    - **Good Credit**: Eligible for credit card approval.
    - **Non-Performing Loan (NPL)**: High risk and ineligible for approval.
    """)

    # TOOLS SECTION
    st.write("<h1 style='font-size: 20px;'>Tools for model development:</h1>", unsafe_allow_html=True)
    st.write("""
    - **Machine Learning Algorithms**: We experimented with K-Nearest Neighbors (KNN), Decision Tree, Random Forest, XGBoost, LightGBM, and HistGradientBoosting.  
      The best performing model was **Light Gradient Boosting (LGBM)** with the highest recall and the smallest model size.
    - **Streamlit**: Used to build and deploy the interactive web application.
    """)

    # FEATURES SECTION
    st.write("<h1 style='font-size: 20px;'>Features:</h1>", unsafe_allow_html=True)
    st.write("""
    - **About Our Team**: Meet the aspiring data team behind this project.        
    - **Exploratory Data Analysis (EDA)**: Dive into data distributions, correlations, and key findings from the dataset.
    - **Prediction**: Upload your own credit application data (.xlsx) to receive an instant credit risk classification.
    """)

    # HOW TO USE SECTION
    st.write("<h1 style='font-size: 20px;'>How to Use This App?</h1>", unsafe_allow_html=True)
    paragraph3 = "Explore the **EDA section** to learn more about the data we used and the patterns we uncovered. Then, try the **Prediction** tab by uploading an Excel file of your own applicants to see how our model evaluates their credit risk."
    st.markdown(paragraph3)


if __name__ == "__main__":
    run()