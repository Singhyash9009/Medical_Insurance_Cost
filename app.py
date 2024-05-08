import streamlit as st
import pickle
import numpy as np
import joblib

# Load the Model back from file
# with open('rf_model.pkl', 'rb') as file:
#     try:
#         rf_model_loaded = pickle.load(file)



def main():
    # st.title("Loan Amount Prediction")
    st.markdown(
        """
        <style>
            body {
                background-color: #D3D3D3 ;
                color: white; /* Set text color to white */
            }
            .title-text {
                font-size: 40px;
                color: white;
                background-color: #000000;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 20px;
                text-align: center;
                font-family: Times New Roman, sans-serif;
            }
            .content-text {
                font-size: 18px;
                color: black;
                background-color: #D3D3D3;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 20px;
                text-align: center;
                font-family: Times New Roman, sans-serif;
                }
                .stButton>button {
                display: block;
                background-color: #87CEEB;
                margin: 0 auto;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="title-text">Medical Insurance Cost Prediction</div>
        """,
        unsafe_allow_html=True)

    st.markdown(
        """
        <div class="content-text">Enter the following details to predict the insurance cost amount!!!</div>
        """,
        unsafe_allow_html=True)
    

    # features = []
    col1, col2,col3 = st.columns([3,3,4])
    features = []
    with col1:
        features.append(st.number_input("Age (>18) "))
        features.append(st.number_input("Gender (0: Female, 1: Male)"))
    with col2:
        features.append(st.number_input("BMI"))
        
        features.append(st.number_input("Childrens"))

    with col3:
        features.append(st.number_input("Do you Smoke (0: No, 1: Yes)"))
        features.append(st.number_input("Which Region (0: NE, 1: NW, 2: SE, 3: SW)"))

    if st.button("Predict"):
        final = np.array(features).reshape((1, 6))
        model = joblib.load('rf_model.joblib')
        pred = model.predict(final)[0]
        
        if pred < 0:
            st.error("Error calculating Amount!")
        else:
            st.success("Expected cost for medical insurance is $ {:.3f}".format(pred))

if __name__ == "__main__":
    main()