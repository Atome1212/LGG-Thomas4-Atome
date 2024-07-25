import pandas as pd
from matplotlib import pyplot as plt

filename = "../data/data1.csv"
df = pd.read_csv(filename)
df.columns

#print(df.columns)
df.drop(columns='Unique Squirrel ID', inplace=True)
#print(df.columns)


# Split the feature "Date" into "day", "month" and "year" columns
# df[["Date", "day", "month", "year"]].head()

# print(df["Date"].head())

# print(df.dtypes)


# def redate(date):
#     date = str(date)
#     return (date[0:1], date[2:3], date[4:])

# df[['day', 'month', 'year']] = df['Date'].apply(lambda x: pd.Series(redate(x)))

df[['day', 'month', 'year']] = df['Date'].apply(lambda date: pd.Series((str(date)[2:3], str(date)[0:1], str(date)[4:])))


# time it


# reaction_columns = ["Kuks", "Quaas", "Moans", "Tail flags",
#                     "Tail twitches", "Approaches", "Runs from",
#                     "Other Interactions"]

# df["Reaction"] = df[reaction_columns].any(axis=1)
# df["Reaction"] = df["Reaction"].apply(lambda x: "yes" if x else "no")
# print(df["Reaction"])