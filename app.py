import streamlit as st
import numpy as np
import pickle

with open("catboost_model.pkl", "rb") as f:
    cat_loaded = pickle.load(f)

def predict_price(carat, cut, color, clarity, depth, table, x, y, z):
    #converting categorical features to numerical values and creating a feature array
    if cut == 'Fair':
        cut = 0
    elif cut == 'Good':
        cut = 1
    elif cut == 'Very Good':
        cut = 2
    elif cut == 'Premium':
        cut = 3
    elif cut == 'Ideal':
        cut = 4

    if color == 'J':
        color = 0
    elif color == 'I':
        color = 1
    elif color == 'H':
        color = 2
    elif color == 'G':
        color = 3
    elif color == 'F':
        color = 4
    elif color == 'E':
        color = 5
    elif color == 'D':
        color = 6
    
    if clarity == 'I1':
        clarity = 0
    elif clarity == 'SI2':
        clarity = 1
    elif clarity == 'SI1':
        clarity = 2
    elif clarity == 'VS2':
        clarity = 3
    elif clarity == 'VS1':
        clarity = 4
    elif clarity == 'VVS2':
        clarity = 5
    elif clarity == 'VVS1':
        clarity = 6
    elif clarity == 'IF':
        clarity = 7


    #making the prediction using the loaded model
    features = np.array([[carat, cut, color, clarity, depth, table, x, y, z]])
    prediction = cat_loaded.predict(features)

    return prediction[0]

def main():
    st.title("Diamond Price Prediction")
    st.image("https://t3.ftcdn.net/jpg/02/89/42/52/240_F_289425261_eriD4MyHsaQ9nh9R53wkTmVNoXzdCWqg.jpg")
    st.title("Enter Diamond Details")

    carat = st.number_input("Carat", min_value=0.1, max_value=5.0, step=0.01)
    cut = st.selectbox("Cut", ["Ideal", "Premium", "Very Good", "Good", "Fair"])
    color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity", ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"])
    depth = st.number_input("Depth", min_value=43, max_value=79, step=1)
    table = st.number_input("Table", min_value=43, max_value=95, step=1)
    x = st.number_input("x (length in milimeter)", min_value=0.0, max_value=10.0, step=0.1)
    y = st.number_input("y (width in milimeter)", min_value=0.0, max_value=10.0, step=0.1)
    z = st.number_input("z (depth) in milimeter)", min_value=0.0, max_value=10.0, step=0.1)

    if st.button("Predict"):
        prediction = predict_price(carat, cut, color, clarity, depth, table, x, y, z)
        st.success(f"Predicted Price: ${prediction:.2f}")

if __name__ == "__main__":
    main()