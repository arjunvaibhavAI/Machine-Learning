import streamlit as st
import pandas as pd
import joblib

# Load the saved pipeline
pipeline = joblib.load('model.pkl')

# web app
st.title('Delivery Time Predictor')
st.write("A machine learning app to predict delivery times for an e-commerce platform.")
st.header("Enter Delivery Details")

# Create columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    delivery_person_age = st.slider('Delivery Person\'s Age', 15, 50, 25)
    delivery_person_ratings = st.slider('Delivery Person\'s Rating', 0.0, 5.0, 4.5, 0.1)
    vehicle_condition = st.selectbox('Vehicle Condition', [0, 1, 2, 3], index=2)
    multiple_deliveries = st.selectbox('Multiple Deliveries', [0, 1, 2, 3], index=1)

with col2:
    weather = st.selectbox('Weather Conditions', ['Sunny', 'Stormy', 'Sandstorms', 'Cloudy', 'Fog', 'Windy'])
    traffic = st.selectbox('Road Traffic Density', ['Low', 'Medium', 'High', 'Jam'])
    vehicle_type = st.selectbox('Type of Vehicle', ['motorcycle', 'scooter', 'electric_scooter'])
    festival = st.selectbox('Is it a Festival?', ['No', 'Yes'])
    city = st.selectbox('City Type', ['Urban', 'Metropolitian', 'Semi-Urban'])


if st.button('Predict Delivery Time'):
    # DataFrame from the user input
    input_data = pd.DataFrame({
        'Delivery_person_Age': [delivery_person_age],
        'Delivery_person_Ratings': [delivery_person_ratings],
        'Weatherconditions': [weather],
        'Road_traffic_density': [traffic],
        'Vehicle_condition': [vehicle_condition],
        'Type_of_vehicle': [vehicle_type],
        'multiple_deliveries': [multiple_deliveries],
        'Festival': [festival],
        'City': [city]
    })

    # pipeline will automatically preprocess the input and then predict
    prediction = pipeline.predict(input_data)
    st.header(f"Predicted Delivery Time: {prediction[0]:.0f} minutes")