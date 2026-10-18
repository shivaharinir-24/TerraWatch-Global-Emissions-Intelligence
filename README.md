# 🌍 TerraWatch — Global Emissions Intelligence System

An interactive environmental emissions analytics application built using Python, Pandas, Plotly, and Streamlit.

## Project Overview

TerraWatch analyzes historical greenhouse gas emissions across countries and provides an interactive dashboard for exploring emission trends, comparing countries, and understanding relative emissions scores.

The project demonstrates an end-to-end data analytics workflow, from data preparation and exploratory analysis to custom scoring and interactive visualization.

## Key Features

- Global CO₂ emissions analysis
- Historical emissions trends
- Interactive country explorer
- Multi-country emissions comparison
- Global emissions rankings
- Custom emissions scoring system
- Relative emissions classifications
- Interactive Streamlit dashboard

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data cleaning and analysis |
| NumPy | Numerical operations |
| Matplotlib | Exploratory visualizations |
| Seaborn | Statistical visualizations |
| Plotly | Interactive charts |
| Streamlit | Web dashboard |

## Dataset

The project uses historical country-level greenhouse gas emissions data, including:

- CO₂ emissions
- CO₂ emissions per capita
- Methane emissions
- Nitrous oxide emissions
- Population and GDP

The cleaned dataset contains approximately 42,480 records covering 218 countries and territories.

The relative scoring dataset includes 199 countries with the required emissions indicators available.

## Emissions Scoring Methodology

TerraWatch calculates a custom emissions score using four equally weighted indicators:

| Indicator | Weight |
|---|---|
| Total CO₂ emissions | 25% |
| CO₂ emissions per capita | 25% |
| Methane emissions | 25% |
| Nitrous oxide emissions | 25% |

Each indicator is normalized using Min-Max scaling.

The normalized indicators are combined into a score on a 0–100 scale.

Countries are assigned Lower, Moderate, or Higher relative categories using the 33rd and 67th percentile thresholds.

**Important:** The emissions score is an exploratory, relative index. It is not an official environmental risk rating, climate vulnerability measure, or validated scientific assessment.

## Installation and Usage

Clone the repository:

`git clone <your-repository-url>`

Navigate to the project directory:

`cd Terrawatch`

Install dependencies:

`python -m pip install -r requirements.txt`

Launch the dashboard:

`python -m streamlit run app.py`

## Project Structure

```text
Terrawatch/
├── data/
├── notebooks/
├── src/
│   ├── 03_eda.py
│   └── 04_risk_scoring.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Limitations

- The scoring system uses equal weights as an initial analytical baseline.
- CO₂ and CO₂ per capita are related measures.
- Min-Max normalization is sensitive to outliers.
- Countries with incomplete emissions indicators are excluded from scoring.
- Results depend on the coverage and accuracy of the underlying dataset.
- Emissions scores should not be interpreted as comprehensive environmental risk assessments.

## Future Improvements

- Interactive global emissions map
- Alternative scoring and weighting methods
- Emissions forecasting using machine learning
- Country-level emissions intensity analysis
- Automated data updates

## Author

Shiva Harini R.

Python | Data Science | AI/ML Engineering


### Data Source and Attribution

Data source: Our World in Data — CO₂ and Greenhouse
Gas Emissions Dataset.

https://github.com/owid/co2-data

The dataset combines emissions and related indicators
from multiple underlying providers, including the
Global Carbon Project and other research sources.

TerraWatch uses this data for educational and
portfolio-based analysis.

Source licenses and attribution requirements:
https://github.com/owid/co2-data#license


## Data Preparation

TerraWatch uses the Our World in Data CO2 dataset.

The original dataset and processed CSV files are not
included in this repository.

To download and prepare the data, run:

```powershell
python run_pipeline.py
```

This automatically:

1. Downloads the original emissions dataset.
2. Cleans and filters country-level records.
3. Calculates relative emissions scores.
4. Generates the CSV files required by the dashboard.

An internet connection is required for the download.

After data preparation, launch the dashboard:

```powershell
python -m streamlit run app.py
```
