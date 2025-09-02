import pandas as pd
import sqlite3

conn = sqlite3.connect("D:/Customer Segmentation/data/retail.db")

#Monetary
monetary = pd.read_sql_query(
    """
SELECT CustomerID,
SUM(Quantity * UnitPrice) AS Monetary
FROM OnlineRetail
GROUP BY CustomerID
""",conn
)

#Frequency
frequency = pd.read_sql_query(
    """
SELECT CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Frequency
FROM OnlineRetail
GROUP BY CustomerID
""",conn
)

#Recency
recency = pd.read_sql_query(
    """
SELECT CustomerID,
    MAX(invoiceDate) AS LastPurchaseDate
FROM OnlineRetail
GROUP BY CustomerID
""",conn
)

rfm = recency.merge(frequency, on = "CustomerID").merge(monetary,on = "CustomerID")
print(rfm.head())

conn.close()
