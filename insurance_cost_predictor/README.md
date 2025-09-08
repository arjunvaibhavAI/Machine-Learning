# Interactive Insurance Cost Predictor

This project is an interactive web application that predicts annual medical insurance costs using a **Linear Regression** model.

The application is built with **Streamlit**, allowing users to input their details and receive an instant cost estimate. It demonstrates a complete end-to-end machine learning workflow, covering data preprocessing, model training, and deployment in a web application.

---

## Tech Stack
- **Python**: Data processing and model training  
- **Pandas**: Data manipulation  
- **Scikit-learn**: Training the Linear Regression model  
- **Streamlit**: Building the interactive web application  
- **Joblib**: Saving and loading the trained model  

---

## Features
- **Real-Time Predictions**: Instant cost estimates based on user inputs  
- **Interactive Controls**: Sliders and dropdowns for age, BMI, smoking status, and region  
- **Pre-Trained Model**: Loads a saved scikit-learn model for fast, efficient predictions  

---

## How to Run Locally

###  Clone the Repository
```bash
git clone <https://github.com/arjunvaibhavAI/Machine-Learning.git>
cd insurance_cost_predictor

python -m venv .venv
# Activate the environment (Windows)
.venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
