import pandas as pd
from .utils import RAW_CSV, CLEAN_CSV

def load_data():
    df = pd.read_csv(RAW_CSV, encoding="latin-1")
    print(" Raw data loaded:", df.shape)
    return df

def remove_missing(df):
    df = df.dropna()
    print(" After removing missing values:", df.shape)
    return df

def remove_duplicate(df):
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f" Removed {before - after} duplicates. Final shape: {df.shape}")
    return df

def save_clean_data(df):
    df.to_csv(CLEAN_CSV, index=False)
    print(f" Cleaned data saved to {CLEAN_CSV}")
