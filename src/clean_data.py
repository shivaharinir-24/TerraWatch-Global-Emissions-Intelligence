
import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "data" / "global_co2.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())


missing_percentage = (df.isnull().sum() / len(df)) * 100

print("\nTop 10 Columns with Missing Data:")
print(missing_percentage.sort_values(ascending=False).head(10))


print("\nDuplicate Rows:", df.duplicated().sum())

print(
    "Duplicate Country-Year Records:",
    df.duplicated(subset=["country", "year"]).sum()
)

important_columns = [
    "country",
    "year",
    "iso_code",
    "population",
    "gdp",
    "co2",
    "co2_per_capita",
    "methane",
    "nitrous_oxide",
    "total_ghg"
]

clean_df = df[important_columns].copy()

print("\nSelected Dataset Shape:", clean_df.shape)
print(clean_df.head())


print("\nMissing Values in Selected Columns:")

print(clean_df.isnull().sum())

print("\nMissing Percentage:")

print(
    (clean_df.isnull().sum() / len(clean_df) * 100).round(2)
)


missing_iso = clean_df.loc[
    clean_df["iso_code"].isna(), "country"
].unique()

print("\nEntities Without ISO Codes:")
print(missing_iso)


country_df = clean_df[
    clean_df["iso_code"].str.fullmatch(
        r"[A-Z]{3}", na=False
    )
].copy()

print("\nCountry-Level Dataset Shape:")
print(country_df.shape)

print("\nTotal Countries:")
print(country_df["country"].nunique())


output_path = project_root / "data" / "terrawatch_cleaned.csv"

country_df.to_csv(output_path, index=False)

print("\nProcessed dataset saved successfully!")
print("File location:", output_path)
