
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/terrawatch_cleaned.csv")


print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


latest_year = df.loc[df["co2"].notna(), "year"].max()

latest_data = df[df["year"] == latest_year]

top10 = latest_data.nlargest(10, "co2")

print("\nLatest Year:", latest_year)
print("\nTop 10 CO2 Emitting Countries:")
print(top10[["country", "co2"]])


plt.figure(figsize=(12, 6))

sns.barplot(
    data=top10,
    x="co2",
    y="country",
    color="steelblue"
)

plt.title(f"Top 10 CO2 Emitting Countries ({latest_year})")
plt.xlabel("CO2 Emissions (Million Tonnes)")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig("top10_co2.png", dpi=300, bbox_inches="tight")
plt.show()


# Global CO2 Emission Trends

trend_data = df[
    (df["year"] >= 2000) &
    (df["year"] <= 2024)
]

global_trend = (
    trend_data.groupby("year")["co2"]
    .sum(min_count=1)
    .reset_index()
)

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=global_trend,
    x="year",
    y="co2",
    marker="o",
    color="green"
)

plt.title("Global CO2 Emission Trends (2000–2024)")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (Million Tonnes)")
plt.grid(True)

plt.tight_layout()
plt.savefig("global_co2_trend.png", dpi=300)
plt.show()


# Compare CO2 emissions across three countries

selected_countries = ["China", "India", "United States"]

comparison_data = df[
    (df["country"].isin(selected_countries)) &
    (df["year"].between(2000, 2024))
]

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=comparison_data,
    x="year",
    y="co2",
    hue="country",
    marker="o"
)

plt.title("CO2 Emissions: China vs India vs USA")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (Million Tonnes)")
plt.grid(True)

plt.tight_layout()
plt.savefig("country_comparison.png", dpi=300)
plt.show()
