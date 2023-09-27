"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns


import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise the Harvest Production Estimatation")

  
    if st.checkbox("Nitrogen Level vs Production_in_tons"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="N",y="Production_in_tons",data=df)
        st.pyplot()

    if st.checkbox("Phosphorus Level vs Production_in_tons"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="P",y="Production_in_tons",data=df)
        st.pyplot()

    if st.checkbox("Potassium vs Production_in_tons"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="K",y="Production_in_tons",data=df)
        st.pyplot()

   
