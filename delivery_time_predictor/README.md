# Interactive Delivery Time Predictor

This project is a web application designed to predict delivery times for e-commerce or food delivery platforms. It leverages a machine learning model trained on real-world data to provide delivery estimates based on operational factors.

## Tech Stack
- **Python**: Core programming language  
- **Scikit-learn**: Training the Linear Regression model and creating the preprocessing pipeline  
- **Pandas**: Data manipulation and cleaning  
- **Streamlit**: Building and deploying the interactive web application  
- **Joblib**: Saving and loading the trained model  

## Business Objective
The goal of this project is to provide accurate delivery time estimates, improving both customer satisfaction and operational efficiency. By predicting delivery times, businesses can:
- Reduce customer support inquiries  
- Optimize driver logistics  
- Build trust with customers  

## Results
The Linear Regression model was trained and evaluated, achieving an **R-squared score of 0.23** on the test dataset. While this indicates that the model explains 23% of the variability in delivery times, it serves as a strong baseline for this complex, real-world problem. The primary focus of this project was the **end-to-end deployment of a machine learning model into a functional web application**.

## Features
- **Real-Time Predictions**: Provides instant delivery time estimates based on user inputs  
- **Interactive Controls**: Adjust operational factors such as distance, order size, and traffic conditions  
- **Pre-Trained Model**: Loads a saved model for fast and efficient predictions  

## How to Run Locally
1. Clone the repository:  
```bash
git clone <https://github.com/arjunvaibhavAI/Machine-Learning.git>
cd delivery_time_predictor

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
