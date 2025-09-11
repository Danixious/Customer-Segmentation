import pandas as pd
import sqlite3

DB_PATH = "D:/Customer Segmentation/data/Retail_data.db"
CSV_PATH = "D:/Customer Segmentation/data/Clean_data.csv"

# Load CSV
def load_csv(path=CSV_PATH):
    df = pd.read_csv(path)
    print("CSV loaded:", df.shape)
    return df

# Save DataFrame to SQLite
def save_to_sqlite(df, db_path=DB_PATH, table_name="ONLINERETAIL"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Data saved to SQLite table: {table_name}")
    return conn  

# Run query
def run_query(conn, query):
    result = pd.read_sql_query(query, conn)
    return result

# Example query for country stats
def get_country_stats(conn):
    query = """
    SELECT Country,
           COUNT(*) AS total_orders,
           SUM(Quantity) as total_quantity
    FROM ONLINERETAIL
    GROUP BY Country
    ORDER BY total_quantity DESC
    """
    return run_query(conn, query)

# Main workflow
if __name__ == "__main__":
    df = load_csv()
    conn = save_to_sqlite(df)

    result = get_country_stats(conn)
    print(result.head())

    conn.close()
