import pandas as pd
from sklearn.preprocessing import StandardScaler
from .utils import get_connection, TABLE_NAME, RFM_TABLE

def run_query(query):
    with get_connection() as conn:
        return pd.read_sql_query(query, conn)

def get_monetary():
    query = f"""
    SELECT CustomerID, SUM(Quantity * UnitPrice) AS Monetary
    FROM {TABLE_NAME}
    GROUP BY CustomerID;
    """
    return run_query(query)

def get_frequency():
    query = f"""
    SELECT CustomerID, COUNT(DISTINCT InvoiceNo) AS Frequency
    FROM {TABLE_NAME}
    GROUP BY CustomerID;
    """
    return run_query(query)

def get_recency():
    query = f"""
    SELECT CustomerID, MAX(InvoiceDate) AS LastPurchaseDate
    FROM {TABLE_NAME}
    GROUP BY CustomerID;
    """
    return run_query(query)

def build_rfm():
    recency = get_recency()
    frequency = get_frequency()
    monetary = get_monetary()

    rfm = recency.merge(frequency, on="CustomerID").merge(monetary, on="CustomerID")
    rfm["LastPurchaseDate"] = pd.to_datetime(rfm["LastPurchaseDate"])
    today = rfm["LastPurchaseDate"].max() + pd.Timedelta(days=1)
    rfm["Recency"] = (today - rfm["LastPurchaseDate"]).dt.days
    return rfm

def scale_rfm(rfm):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])
    return rfm_scaled

def save_rfm(rfm):
    with get_connection() as conn:
        rfm.to_sql(RFM_TABLE, conn, if_exists="replace", index=False)
    print("✅ RFM table saved to database.")
