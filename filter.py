import pandas as pd


def bars() -> None:
    print("-----")


df = pd.read_csv("./data/Names.csv", header=None)
df.columns = ["First", "Last", "Address", "City", "State", "Zip", "Income"]

bars()
print(df.loc[df["City"] == "Riverside"])
print(df.loc[(df["City"] == "Riverside") & (df["First"] == "John")])

bars()
df["Tax %"] = df["Income"].apply(
    lambda x: 0.15 if 10000 < x < 40000 else 0.2 if 40000 < x < 80000 else 0.25
)
print(df)

bars()
df["Taxes Owed"] = df["Income"] * df["Tax %"]
print(df["Taxes Owed"])

bars()
drop_list = ["Zip", "First", "Address"]
df.drop(columns=drop_list, inplace=True)
print(df)

bars()
df["Test Col"] = False
df.loc[df["Income"] < 60000, "Test Col"] = True
print(df)

bars()
print(df.groupby(["Test Col"]).mean())

bars()
print(df.groupby(["Test Col"]).mean().sort_values("Income"))
