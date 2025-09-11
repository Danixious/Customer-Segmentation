import pandas as pd
from .utils import get_connection, RFM_TABLE

def load_rfm_clusters():
    with get_connection() as conn:
        rfm  = pd.read_sql_query(f"SELECT * FROM {RFM_TABLE}",conn)
    return rfm

def profile_clusters(rfm):
    summary = rfm.groupby("Cluster")[["Recency", "Frequency", "Monetary"]].mean().round(2)
    summary["Count"] = rfm.groupby("Cluster").size()

    summary["Recency_norm"] = (summary["Recency"] - summary["Recency"].min()) / (summary["Recency"].max() - summary["Recency"].min())
    summary["Frequency_norm"] = (summary["Frequency"] - summary["Frequency"].min()) / (summary["Frequency"].max() - summary["Frequency"].min())
    summary["Monetary_norm"] = (summary["Monetary"] - summary["Monetary"].min()) / (summary["Monetary"].max() - summary["Monetary"].min())

    print("📊 Cluster Profiles (averages):")
    print(summary)

    return summary

def label_clusters(summary):
    labels = {}
    for cluster, row in summary.iterrows():
        if row["Frequency_norm"] > 0.7 and row["Monetary_norm"] > 0.7:
            labels[cluster] = "🏆 Champions"
        elif row["Frequency_norm"] > 0.5:
            labels[cluster] = "💡 Loyal Customers"
        elif row["Recency_norm"] > 0.6:
            labels[cluster] = "💤 At Risk"
        else:
            labels[cluster] = "❌ Lost Customers"
    return labels

def assign_labels(rfm, labels):
    rfm["Segment"] = rfm["Cluster"].map(labels)
    with get_connection() as conn:
        rfm.to_sql(RFM_TABLE, conn, if_exists="replace", index=False)
    print("✅ Cluster labels added to RFM table.")
    return rfm