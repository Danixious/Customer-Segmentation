import os
import sqlite3

#directories
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Common paths
RAW_CSV = os.path.join(DATA_DIR, "OnlineRetail.csv")
CLEAN_CSV = os.path.join(DATA_DIR, "Clean_data.csv")
DB_PATH = os.path.join(DATA_DIR, "retail.db")

# Table names
TABLE_NAME = "OnlineRetail"
RFM_TABLE = "RFM"

# Database connection
def get_connection():
    return sqlite3.connect(DB_PATH)
