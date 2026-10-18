
import pandas as pd

df = pd.read_csv("data/terrawatch_cleaned.csv")

indicators = [
    "co2",
    "co2_per_capita",
    "methane",
    "nitrous_oxide"
]

latest_year = df.loc[df["co2"].notna(), "year"].max()

risk_data = df[df["year"] == latest_year].copy()

print("Latest Year:", latest_year)
print("Countries:", len(risk_data))

print("\nMissing Values:")
print(risk_data[indicators].isna().sum())


# Remove rows missing any required indicator
risk_data = risk_data.dropna(subset=indicators).copy()

print("\nCountries available for scoring:", len(risk_data))

# Check the remaining missing values
print("\nMissing values after cleaning:")
print(risk_data[indicators].isna().sum())


# Normalize the emissions indicators

for col in indicators:
    min_val = risk_data[col].min()
    max_val = risk_data[col].max()

    if max_val > min_val:
        risk_data[col + "_normalized"] = (
            (risk_data[col] - min_val) /
            (max_val - min_val)
        )
    else:
        risk_data[col + "_normalized"] = 0.0

print("\nNormalized Emissions Data:")

print(risk_data[
    ["country", "co2_normalized",
     "co2_per_capita_normalized",
     "methane_normalized",
     "nitrous_oxide_normalized"]
].head())


# Equal weights for all four indicators
weights = {
    "co2": 0.25,
    "co2_per_capita": 0.25,
    "methane": 0.25,
    "nitrous_oxide": 0.25
}

# Calculate the emissions score
risk_data["risk_score"] = (
    risk_data["co2_normalized"] * weights["co2"] +
    risk_data["co2_per_capita_normalized"] * weights["co2_per_capita"] +
    risk_data["methane_normalized"] * weights["methane"] +
    risk_data["nitrous_oxide_normalized"] * weights["nitrous_oxide"]
) * 100

# Rank countries
risk_data = risk_data.sort_values(
    "risk_score", ascending=False
)

risk_data["rank"] = range(1, len(risk_data) + 1)

print("\nTop 10 Countries by Emissions Score:")
print(
    risk_data[["rank", "country", "risk_score"]]
    .head(10)
    .to_string(index=False)
)

# Save results
risk_data.to_csv(
    "data/terrawatch_risk_scores.csv",
    index=False
)

print("\nRisk scores saved successfully!")


# Calculate score thresholds
low_threshold = risk_data["risk_score"].quantile(0.33)
high_threshold = risk_data["risk_score"].quantile(0.67)

# Assign relative emissions categories
def classify_emissions(score):
    if score <= low_threshold:
        return "Lower"
    elif score <= high_threshold:
        return "Moderate"
    else:
        return "Higher"

risk_data["risk_category"] = risk_data["risk_score"].apply(
    classify_emissions
)

print("\nEmissions Category Distribution:")
print(risk_data["risk_category"].value_counts())


# Save the updated scoring dataset
risk_data.to_csv(
    "data/terrawatch_risk_scores.csv",
    index=False
)

print("Updated scoring dataset saved!")
