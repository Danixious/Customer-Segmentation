import pandas as pd
import sqlite3

df = pd.read_csv("D:/Customer Segmentation/data/Clean_data.csv")
conn = sqlite3.connect("D:/Customer Segmentation/data/retail.db")
df.to_sql("OnlineRetail", conn, if_exists="replace", index = False)
print("Table OnlineRetail created successfully!")
conn.close()