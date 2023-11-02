"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import streamlit as st


@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('crop.csv')

    # Perform feature and target split
    X = df[["N","P","K","pH","rainfall","temperature","Area_in_hectares","Yield_ton_per_hec"]]
    y = df['Production_in_tons']

    return df, X, y

@st.cache_data()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Create the model
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    # Fit the data on model
    model.fit(X, y)
    # Get the model score
    score = model.score(X, y)

    # Return the values
    return model, score

def predict(X, y, features):
    # Get model and model score
    model, score = train_model(X, y)
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score

def xgboost(X, y):
    modelx = xgb.XGBClassifier(
    n_estimators=100,    # Number of boosting rounds (iterations)
    max_depth=3,         # Maximum depth of each tree
    learning_rate=0.1,  # Step size shrinkage used to prevent overfitting
    subsample=0.8,       # Fraction of samples used for training each tree
    colsample_bytree=0.8,  # Fraction of features used for training each tree
    objective='binary:logistic',  # Binary classification
    random_state=42
)
