from sklearn.datasets import load_diabetes
import pandas as pd

diabetes = load_diabetes()
data = diabetes.data
target = diabetes.target
df = pd.DataFrame(data, columns=diabetes.feature_names)
df['target'] = target


import numpy as np

#print(df.head())

for i in df.columns:
    print("=====================")
    print(f"{i}")
    print(f"Moyenne : {df[i].mean()}")
    print(f"Medianne : {df[i].median()}")
    print(f"Percentile (50): {np.percentile(df[i], 50)}")
    print("=====================")
    print()