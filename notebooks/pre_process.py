import pandas as pd
import numpy as np
import joblib

df = pd.read_csv("D:/Customer Segmentation/data/OnlineRetail.csv/OnlineRetail.csv",encoding = "latin-1") 
print(df.shape)

# #removing empty cells
df = df.dropna()
print(df.shape)

#handling duplicates
print(df.duplicated())
df.drop_duplicates(inplace = True)

df.to_csv("D:/Customer Segmentation/data/Clean_data.csv",index = False)
df2= pd.read_csv("D:/Customer Segmentation/data/Clean_data.csv")
print(df2.shape)
