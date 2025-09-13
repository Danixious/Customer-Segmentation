import streamlit as st
import pandas as pd
import joblib

# Load model + scaler
kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("📊 Customer Segmentation Dashboard")

uploaded_file = st.file_uploader("Upload customer data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📥 Uploaded Data Preview:", df.head())

    # Scale & predict clusters
    rfm_scaled = scaler.transform(df[["Recency", "Frequency", "Monetary"]])
    df["Cluster"] = kmeans.predict(rfm_scaled)

    st.subheader("Segmented Customers")
    st.dataframe(df)

    # Optional: Download results
    st.download_button(
        label="Download Segmented Data",
        data=df.to_csv(index=False).encode(),
        file_name="segmented_customers.csv",
        mime="text/csv",
    )
