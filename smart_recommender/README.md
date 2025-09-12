# Smart E-commerce Product Recommender

This project is an interactive web application that recommends products to customers using a two-step machine learning workflow: **customer segmentation with K-Means** and **recommendation logic inspired by K-Nearest Neighbors**.

The app is built with Streamlit and demonstrates an end-to-end workflow covering data preprocessing, segmentation, recommendation generation, and deployment.

---

## Tech Stack
- **Python**: Core programming and data handling  
- **Pandas**: Data manipulation and RFM analysis  
- **Scikit-learn**: K-Means clustering and scaling  
- **Streamlit**: Building the interactive web application  
- **Joblib**: Saving and loading processed data  

---

## Features
- **Customer Segmentation**: Groups customers into segments (High-Value, New, At-Risk, Loyal) using RFM scores  
- **Smart Recommendations**: Suggests top products based on similar customers within the same segment  
- **Interactive App**: Easy-to-use Streamlit interface for selecting customers and viewing recommendations  

---

## How to Run Locally
Clone the repository:
```bash
git clone <https://github.com/arjunvaibhavAI/Machine-Learning.git>
cd smart_ecommerce_recommender

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

jupyter notebook notebooks/train_model.ipynb

streamlit run app.py
