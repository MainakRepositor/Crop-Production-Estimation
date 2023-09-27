"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Regression</b> for the Crop Yield Prediction
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    N = st.slider("Nitrogen Concentration", int(df["N"].min()), int(df["N"].max()))
    P = st.slider("Phosphorus Concentration", int(df["P"].min()), int(df["P"].max()))
    K = st.slider("Potassium Concentration", int(df["K"].min()), int(df["K"].max()))
    pH = st.slider("pH Level", float(df["pH"].min()), float(df["pH"].max()))
    rainfall = st.slider("Rainfall amount", float(df["rainfall"].min()), float(df["rainfall"].max()))
    temperature = st.slider("Mean Temperature", float(df["temperature"].min()), float(df["temperature"].max()))
    Area_in_hectares = st.slider("Area (in Hectare)", float(df["Area_in_hectares"].min()), float(df["Area_in_hectares"].max()))
    Yield = st.slider("Yield (ton/hectare)", float(df["Yield_ton_per_hec"].min()), float(df["Yield_ton_per_hec"].max()))

    # Create a list to store all the features
    features = [N,P,K,pH,rainfall,temperature,Area_in_hectares,Yield]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Predicted Sucessfully")
        # Print the output according to the prediction
        st.success("Yearly Production Amount = " +str(round((prediction[0]/1000),2)) + " Tons")
        
        # Print teh score of the model 
        st.write("The model used is trusted by agriculturalists and has an accuracy of ", round((score*100),2),"%")
