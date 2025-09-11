from .utils import get_connection, TABLE_NAME
import pandas as pd

def run_query(query):
    with get_connection() as conn:
        return pd.read_sql_query(query, conn)

def get_country_orders(limit=None):
    query = f"""
    SELECT Country, COUNT(*) AS total_orders
    FROM {TABLE_NAME}
    GROUP BY Country
    ORDER BY total_orders DESC
    {f"LIMIT {limit}" if limit else ""};
    """
    return run_query(query)

def get_top_products(limit=10):
    query = f"""
    SELECT Description, SUM(Quantity) AS total_quantity
    FROM {TABLE_NAME}
    GROUP BY Description
    ORDER BY total_quantity DESC
    LIMIT {limit};
    """
    return run_query(query)

def get_customer_revenue(limit=None):
    query = f"""
    SELECT CustomerID, SUM(Quantity * UnitPrice) AS revenue
    FROM {TABLE_NAME}
    GROUP BY CustomerID
    ORDER BY revenue DESC
    {f"LIMIT {limit}" if limit else ""};
    """
    return run_query(query)
