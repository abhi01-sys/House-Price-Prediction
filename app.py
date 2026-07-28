import streamlit as st
import numpy as np
import pandas as pd
import pickle

house_model = pickle.load(open("house.pkl", "rb"))
print(type(house_model))

def predict(square_feet, num_rooms, age, distance_to_city):
    input_data = pd.DataFrame({
        "square_feet": [square_feet],
        "num_rooms": [num_rooms],
        "age": [age],
        "distance_to_city(km)": [distance_to_city]
    })

    prediction = house_model.predict(input_data)
    return prediction[0]



st.title("🏠House Price Prediction")

square_feet = st.number_input(
    "Insert the size in (sq.ft)", value=None, placeholder="Type a number..."
)
st.write("Entered size is : ", square_feet)

num_rooms = st.number_input(
    "Number of rooms", value=None, placeholder="Type a number..."
)
st.write("No of Rooms :", num_rooms)

age = st.number_input(
    "Age of House", value=None, placeholder="Type a number..."
)
st.write("Age: ", age)

distance_to_city = st.number_input(
    "distance_to_city(km)", value=None, placeholder="Type a number..."
)
st.write("distance_to_city(km) : ", distance_to_city)

if st.button("Predict Price"):
    result = predict(square_feet, num_rooms, age, distance_to_city)
    st.success(f"Predicted House Price: ₹{result:,.2f}")