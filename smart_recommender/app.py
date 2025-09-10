import streamlit as st
import pandas as pd
import joblib

recommender_df = joblib.load('recommendation_data.pkl')
segments_df = joblib.load('customer_segments.pkl')

st.title('🛍️ Smart Product Recommender')
st.write("Select a customer to see their segment and get product recommendations.")

# Customer selection dropdown
customer_ids = sorted(recommender_df['CustomerID'].unique())
selected_customer_id = st.selectbox('Select a Customer ID', customer_ids)


if st.button('Get Recommendations'):
    #  Find the customer's cluster
    customer_cluster = segments_df.loc[segments_df['CustomerID'] == selected_customer_id, 'Cluster'].iloc[0]
    st.success(f"This customer is in Segment {customer_cluster}.")

    #  Get items the customer has already bought
    customer_bought_items = set(recommender_df[recommender_df['CustomerID'] == selected_customer_id]['StockCode'])
    
    #  Get all items bought by others in the same cluster
    cluster_items = recommender_df[recommender_df['Cluster'] == customer_cluster]
    
    #  Filter out items the customer already has and find the most popular
    recommendations = cluster_items[~cluster_items['StockCode'].isin(customer_bought_items)]
    top_10 = recommendations['Description'].value_counts().nlargest(10)

    st.subheader("Top 10 Recommendations for this Customer:")
    st.table(top_10)
