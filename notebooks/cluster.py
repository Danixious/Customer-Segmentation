import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import joblib
from .utils import get_connection, RFM_TABLE

# Paths to save model + scaler
MODEL_PATH = "models/kmeans_model.pkl"
SCALER_PATH = "models/scaler.pkl"

# Load RFM 
def load_rfm():
    with get_connection() as conn:
        rfm = pd.read_sql_query(f"SELECT * FROM {RFM_TABLE}", conn)
    return rfm

# Elbow Method 
def elbow_method(rfm_scaled, max_k=10):
    sse = []
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(rfm_scaled)
        sse.append(kmeans.inertia_)

    plt.plot(range(2, max_k + 1), sse, marker='o')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("SSE (inertia)")
    plt.title("Elbow Method For Optimal k")
    plt.show()

#  Silhouette Analysis 
def silhouette_analysis(rfm_scaled, max_k=10):
    scores = {}
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(rfm_scaled)
        score = silhouette_score(rfm_scaled, labels)
        scores[k] = score
        print(f"k = {k}, silhouette = {score:.4f}")
    best_k = max(scores, key=scores.get)
    print(f"✅ Best k by silhouette score: {best_k}")
    return best_k

#Run K-Means
def run_kmeans(rfm_scaled, k):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(rfm_scaled)
    return kmeans, labels

#  Save Clusters + Model 
def save_clusters(rfm, labels, kmeans, scaler):
    rfm["Cluster"] = labels
    with get_connection() as conn:
        rfm.to_sql(RFM_TABLE, conn, if_exists="replace", index=False)
    print("✅ RFM table updated with clusters")

    os.makedirs("models",exist_ok = True)

    # Save trained model + scaler for deployment
    joblib.dump(kmeans, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    print(f"✅ Model saved at {MODEL_PATH}")
    print(f"✅ Scaler saved at {SCALER_PATH}")

    return rfm

#Load Model,Predict New Data
def predict_new(customers_rfm):
    """Assign clusters to new customers based on saved model + scaler"""
    kmeans = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    rfm_scaled = scaler.transform(customers_rfm[["Recency", "Frequency", "Monetary"]])
    labels = kmeans.predict(rfm_scaled)
    customers_rfm["Cluster"] = labels
    return customers_rfm
