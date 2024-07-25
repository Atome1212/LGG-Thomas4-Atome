import pandas as pd
import numpy as np

filename = "../data/data1.csv"
df = pd.read_csv(filename)
df.head()

# print("There are {} rows of data".format(len(df)))

# print(f"value missing : {df.isnull().sum()}")

# [df.drop(columns=i, inplace=True) or print(f"{i} droped") for i in df.columns if df[i].isnull().sum() > 1000]        
        
# print(df.dtypes)

# print(f"type de Hectare : {df['Hectare'].dtype}")
        
[print(i) for i in df.columns if df[i].nunique() < 100]


        
        
        