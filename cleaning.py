import numpy as np
import pandas as pd


def bars() -> None:
    print("-----")


df = pd.read_csv("data/Names.csv", header=None)

bars()
df.columns = ["First", "Last", "Address", "City", "State", "Zip", "Income"]
print(df)

bars()
print(df.columns.tolist())

bars()
df.drop(columns="Address", inplace=True)
print(df)

bars()
df = df.set_index("Zip")
print(df)
print(df.loc[8074:, "First"])

bars()
df.First = df.First.str.split(expand=True)[
    0
]  # <= This was an error in the actual lesson, I had to add the '[0]'
print(df)

bars()
df = df.replace(np.nan, "N/A", regex=True)
print(df)
to_excel = df.to_excel("data/Names-modified-2.xlsx")
