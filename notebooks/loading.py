import pandas as pd
import sqlite3

df = pd.read_csv("D:/Customer Segmentation/data/Clean_data.csv")

conn  = sqlite3.connect("D:/Customer Segmentation/data/Retail_data.db")
df.to_sql("ONLINERETAIL",conn, if_exists = "replace",index = False)

query = """
SELECT COUNTRY,
COUNT(*) AS total_orders,
SUM(Quantity) as total_quantity
FROM ONLINERETAIL
GROUP BY Country
ORDER BY total_quantity DESC
"""
result = pd.read_sql_query(query,conn)
print(result.head())
conn.close