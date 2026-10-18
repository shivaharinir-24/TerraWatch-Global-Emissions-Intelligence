
import pandas as pd

url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"

df = pd.read_csv(url)

print(df.head())

print("Dataset Shape:", df.shape)

print("Total Countries:", df["country"].nunique())

print("Year Range:", df["year"].min(), "-", df["year"].max())



from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data" / "global_co2.csv"

df.to_csv(data_path, index=False)

print("Dataset saved successfully!")
