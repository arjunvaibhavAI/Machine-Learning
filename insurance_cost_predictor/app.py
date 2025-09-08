import streamlit as st
import joblib
import pandas as pd


model = joblib.load('model.pkl')


st.title('Interactive Insurance Cost Predictor')
st.sidebar.header('User Input Features')
age = st.sidebar.slider('Age', 18, 65, 30)
sex = st.sidebar.selectbox('Sex', ('Male', 'Female'))
bmi = st.sidebar.slider('BMI', 15.0, 55.0, 25.0)
children = st.sidebar.slider('Number of Children', 0, 5, 0)
smoker = st.sidebar.selectbox('Smoker', ('No', 'Yes'))
region = st.sidebar.selectbox('Region', ('Southwest', 'Southeast', 'Northwest', 'Northeast'))

# Convert categorical inputs to numerical format for the model
sex_encoded = 1 if sex == 'Male' else 0
smoker_encoded = 1 if smoker == 'Yes' else 0

# The model was trained with region encoded as: 0=NE, 1=NW, 2=SE, 3=SW
# We need to ensure the same mapping here.
region_mapping = {'Northeast': 0, 'Northwest': 1, 'Southeast': 2, 'Southwest': 3}
region_encoded = region_mapping[region]


if st.sidebar.button('Predict Insurance Cost'):
    # Create a DataFrame from the user's inputs
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex_encoded],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker_encoded],
        'region': [region_encoded]
    })

    prediction = model.predict(input_data)
    st.subheader('Prediction')
    st.write(f'The estimated annual insurance cost is: **${prediction[0]:,.2f}**')
    st.write("---")
    st.markdown("""
    **How to Interpret the Results:**
    - **Age & BMI:** Higher values generally lead to higher insurance costs.
    - **Smoker:** Being a smoker significantly increases the predicted cost. Try changing this value to see the impact!
    - **Region & Children:** These factors typically have a smaller, but still noticeable, effect on the final premium.
    """)