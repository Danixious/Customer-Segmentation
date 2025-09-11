from notebooks.pre_process import load_data, remove_missing, remove_duplicate, save_clean_data
from notebooks.db import save_to_db
from notebooks.feature_eng import build_rfm, save_rfm, scale_rfm
from notebooks.Visual import run as run_visuals
from notebooks.cluster import load_rfm,elbow_method,silhouette_analysis,run_kmeans,save_clusters
from notebooks.profile import load_rfm_clusters,profile_clusters,label_clusters,assign_labels
def main():
    
    df = load_data()
    df = remove_missing(df)
    df = remove_duplicate(df)
    save_clean_data(df)

    
    save_to_db(df)

  
    rfm = build_rfm()
    rfm_scaled = scale_rfm(rfm)
    save_rfm(rfm)

    run_visuals(rfm)

    rfm = load_rfm()
    rfm_scaled = rfm[["Recency","Frequency","Monetary"]].values
    elbow_method(rfm_scaled,max_k=10)

    best_k = silhouette_analysis(rfm_scaled, max_k=10)

    labels = run_kmeans(rfm_scaled,best_k)
    rfm = save_clusters(rfm, labels)
    print(rfm.head())

    rfm = load_rfm_clusters()
    summary = profile_clusters(rfm)
    labels = label_clusters(summary)
    rfm = assign_labels(rfm, labels)

    print("✅ Final Segmented Data Sample:")
    print(rfm.head())

    print(" Full pipeline executed successfully!")

if __name__ == "__main__":
    main()
