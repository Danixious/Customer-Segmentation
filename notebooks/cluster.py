import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from .utils import get_connection, RFM_TABLE

def load_rfm():
    with get_connection() as conn:
        rfm = pd.read_sql_query(f"SELECT * FROM {RFM_TABLE}",conn)
    return rfm

def elbow_method(rfm_scaled,max_k = 10):
    sse = []
    for k in range(2,max_k +1):
        kmeans =  KMeans(n_clusters=k, random_state=42,n_init=10)
        kmeans.fit(rfm_scaled)
        sse.append(kmeans.inertia_)

    plt.plot(range(2,max_k+1),sse,marker = 'o')
    plt.xlabel("Number of Clusters(k)")
    plt.ylabel("SSE (inertia)")
    plt.title("Elbow Method For Optimal k")
    plt.show()

def silhouette_analysis(rfm_scaled, max_k=10):
    scores = {}
    silhouette_avg = []
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(rfm_scaled)
        score = silhouette_score(rfm_scaled,labels)
        scores[k] = score
        print(f"k = {k},silhouette = {score:.4f}")
    best_k = max(scores, key = scores.get)
    print(f"Best k by silhouette score: {best_k}")
    return best_k

def run_kmeans(rfm_scaled,k):
    k_means = KMeans(n_clusters = k, random_state=42,n_init = 10)
    labels = k_means.fit_predict(rfm_scaled)
    return labels

def save_clusters(rfm,lables):
    rfm["Cluster"] = lables
    with get_connection() as conn:
        rfm.to_sql(RFM_TABLE, conn, if_exists = "replace", index = False)
        print("RFM table updated with clusters")
        return rfm