import pandas as pd


def main() -> None:
    df_excel = pd.read_excel("./data/regions.xlsx")
    print(df_excel)

    df_csv = pd.read_csv("./data/Names.csv", header=None)
    df_csv.columns = ["First", "Last", "Address", "City", "State", "Zip", "Area Code"]
    print(df_csv)
    df_csv.to_excel("./data/Names-modified.xlsx")

    df_txt = pd.read_csv("./data/data.txt", delimiter="\t")
    print(df_txt)


if __name__ == "__main__":
    main()
