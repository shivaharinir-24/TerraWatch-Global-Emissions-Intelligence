
import streamlit as st
import pandas as pd

import subprocess
import sys
from pathlib import Path


# Configure dashboard
st.set_page_config(
    page_title="TerraWatch",
    page_icon="🌍",
    layout="wide"
)

project_root = Path(__file__).resolve().parent
data_dir = project_root / "data"

cleaned_file = data_dir / "terrawatch_cleaned.csv"
scores_file = data_dir / "terrawatch_risk_scores.csv"

# Prepare datasets if they do not exist
if not cleaned_file.exists() or not scores_file.exists():
    with st.spinner("Preparing TerraWatch emissions data..."):
        subprocess.run(
            [sys.executable, str(project_root / "run_pipeline.py")],
            cwd=project_root,
            check=True
        )

# Load our processed data
df = pd.read_csv("data/terrawatch_cleaned.csv")
risk_df = pd.read_csv("data/terrawatch_risk_scores.csv")

# Dashboard heading
st.title("🌍 TerraWatch")
st.subheader("Global Environmental Emissions Intelligence System")

st.write(
    "Explore global greenhouse gas emissions, "
    "country comparisons, and emissions risk scores."
)

# Dashboard summary
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Countries Analyzed", risk_df["country"].nunique())

with col2:
    st.metric("Latest Scoring Year", int(risk_df["year"].max()))

with col3:
    st.metric("Average Emissions Score", round(risk_df["risk_score"].mean(), 2))

st.divider()

st.subheader("Top 10 Countries by Emissions Score")

top10 = risk_df.nsmallest(10, "rank")

st.dataframe(
    top10[["rank", "country", "risk_score", "risk_category"]],
    use_container_width=True,
    hide_index=True
)


import plotly.express as px

st.divider()
st.header("🌎 Country Emissions Explorer")

# Country selection
selected_country = st.selectbox(
    "Select a Country",
    sorted(risk_df["country"].unique())
)

# Get selected country's score
country_risk = risk_df[
    risk_df["country"] == selected_country
].iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Emissions Score",
    round(country_risk["risk_score"], 2)
)

col2.metric(
    "Global Rank",
    int(country_risk["rank"])
)

col3.metric(
    "Emissions Category",
    country_risk["risk_category"]
)

# Historical CO2 emissions
country_history = df[
    (df["country"] == selected_country) &
    (df["year"].between(2000, 2024))
].sort_values("year")

fig = px.line(
    country_history,
    x="year",
    y="co2",
    markers=True,
    title=f"CO₂ Emissions Trend — {selected_country}",
    labels={
        "year": "Year",
        "co2": "CO₂ Emissions (Million Tonnes)"
    }
)

st.plotly_chart(fig, use_container_width=True)


st.divider()
st.header("🌍 Compare Countries")

# Select multiple countries
compare_countries = st.multiselect(
    "Select Countries to Compare",
    sorted(risk_df["country"].unique()),
    default=["India", "China", "United States"]
)

# Filter historical data
comparison_df = df[
    (df["country"].isin(compare_countries)) &
    (df["year"].between(2000, 2024))
].copy()

if not comparison_df.empty:

    fig_compare = px.line(
        comparison_df,
        x="year",
        y="co2",
        color="country",
        markers=True,
        title="CO₂ Emissions Comparison",
        labels={
            "year": "Year",
            "co2": "CO₂ Emissions (Million Tonnes)",
            "country": "Country"
        }
    )

    st.plotly_chart(
        fig_compare,
        use_container_width=True
    )

else:
    st.info("Select at least one country to compare.")


st.divider()
st.header("🏆 Global Emissions Rankings")

# Select number of countries
top_n = st.slider(
    "Number of Countries",
    min_value=5,
    max_value=30,
    value=15
)

# Select highest-scoring countries
ranking_df = risk_df.nsmallest(top_n, "rank")

# Create interactive ranking chart
fig_rank = px.bar(
    ranking_df,
    x="risk_score",
    y="country",
    color="risk_category",
    orientation="h",
    title=f"Top {top_n} Countries by Emissions Score",
    labels={
        "risk_score": "Emissions Score (0–100)",
        "country": "Country",
        "risk_category": "Relative Category"
    },
    hover_data=["rank", "co2_per_capita"]
)

fig_rank.update_layout(
    yaxis={"categoryorder": "total ascending"},
    height=max(450, top_n * 28)
)

st.plotly_chart(
    fig_rank,
    use_container_width=True
)


st.divider()
st.header("📘 Methodology & Limitations")

with st.expander("How is the Emissions Score calculated?"):
    st.write("""
    TerraWatch calculates a relative emissions score
    using four indicators:

    - Total CO2 emissions: 25%
    - CO2 emissions per capita: 25%
    - Methane emissions: 25%
    - Nitrous oxide emissions: 25%

    Each indicator is normalized using Min-Max scaling.

    The weighted values are combined into a score
    between 0 and 100.

    Countries are classified as Lower, Moderate,
    or Higher using the 33rd and 67th percentiles.

    Limitations:
    - The score is a custom emissions index, not an
      official environmental risk assessment.
    - The four indicators use equal weights by design.
    - Min-Max scaling is sensitive to extreme values.
    - CO2 and CO2 per capita are related indicators.
    - Countries with missing indicators are excluded.
    - Scores describe relative emissions, not climate
      vulnerability or environmental safety.
    """)

st.caption(
    "TerraWatch | Global Emissions Intelligence | "
    "Python • Pandas • Plotly • Streamlit"
)
