import pandas as pd
import sqlite3

conn = sqlite3.connect("D:/Customer Segmentation/data/Retail_data.db")

#Top 10 Country
query = """
SELECT COUNTRY,
COUNT (*) AS total_orders
FROM ONLINERETAIL
GROUP BY Country
ORDER BY total_orders DESC;
"""
df_country_orders = pd.read_sql_query(query, conn)
print("DataFrame 1 (Orders by Country):")
print(df_country_orders.head())

#Top 10 Products
query2 = """
SELECT Description, SUM(Quantity) AS total_quantity
FROM OnlineRetail
GROUP BY Description
ORDER BY total_quantity DESC
LIMIT 10;
"""
df_popular_products = pd.read_sql_query(query2, conn)
print("\nDataFrame 2 (Top 10 Products):")
print(df_popular_products.head())

#Customer Revenue
query3 = """
SELECT CustomerID, SUM(Quantity * UnitPrice) AS revenue
FROM OnlineRetail
GROUP BY CustomerID
ORDER BY revenue DESC;
"""
df_customer_revenue = pd.read_sql_query(query3, conn)
print("\nDataFrame 3 (Customer Revenue):")
print(df_customer_revenue.head())

conn.close