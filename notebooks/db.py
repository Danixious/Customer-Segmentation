import pandas as pd
from .utils import CLEAN_CSV, get_connection, TABLE_NAME

def save_to_db(df=None):
    if df is None:
        df = pd.read_csv(CLEAN_CSV)
    conn = get_connection()
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()
    print(f" Table {TABLE_NAME} created successfully in database!")
