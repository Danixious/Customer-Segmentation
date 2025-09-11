import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .utils import get_connection, RFM_TABLE

def histogram(rfm):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    rfm['Recency'].hist(ax=axes[0], bins=30, color='skyblue')
    axes[0].set_title("Recency Distribution")

    rfm['Frequency'].hist(ax=axes[1], bins=30, color='lightgreen')
    axes[1].set_title("Frequency Distribution")

    rfm['Monetary'].hist(ax=axes[2], bins=30, color='salmon')
    axes[2].set_title("Monetary Distribution")

    plt.tight_layout()
    plt.show()

def correlation(rfm):
    plt.figure(figsize=(6,4))
    sns.heatmap(rfm[['Recency','Frequency','Monetary']].corr(),
                annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap of RFM Features")
    plt.show()

def boxplots(rfm):
    rfm[['Recency','Frequency','Monetary']].plot(
        kind='box', subplots=True, layout=(1,3), figsize=(15,5), sharey=False
    )
    plt.suptitle("Boxplots of RFM Features (Outlier Detection)")
    plt.show()

def run(rfm=None):
    if rfm is None:
        with get_connection() as conn:
            rfm = pd.read_sql_query(f"SELECT * FROM {RFM_TABLE}", conn)
    histogram(rfm)
    correlation(rfm)
    boxplots(rfm)
