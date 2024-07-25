import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("./data/salary_data.csv")

print(df.head())

print(df.shape[0])
print(df.shape[1])

X = df[['YearsExperience']]  # Variables indépendantes
y = df['Salary']  # Variable dépendante

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Coefficient: {model.coef_}")
print(f"Intercept: {model.intercept_}")

plt.scatter(df['YearsExperience'], df['Salary'])
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs. Years of Experience')
plt.show()