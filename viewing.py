import pandas as pd
from fmtr import bars


def main() -> None:
    df = pd.read_csv("data/Names.csv")
    df.columns = ["First", "Last", "Address", "City", "State", "Zip", "Area Code"]
    bars()
    print(df[["Last", "City"]])  # a list of columns
    bars()
    print(df["First"][0:3])  # a slice of rows
    bars()
    print(df.iloc[1])  # print row contents of index location
    bars()
    print(df.iloc[2, 1])  # print row contents of index location
    bars()

    wanted_values = df[["First", "Last", "State"]]
    stored = wanted_values.to_excel("data/State_Location.xlsx", index=None)
    print(dir(stored))


if __name__ == "__main__":
    main()
