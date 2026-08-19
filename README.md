# 📈 Predictive Forecasting of Care Load & Placement Demand

## HHS Care Occupancy Analytics

An end-to-end Machine Learning and forecasting project that analyzes historical HHS care occupancy data, engineers temporal features, evaluates predictive models, and generates care-load forecasts to support operational planning and resource allocation.

---

## 📖 Project Overview

The Unaccompanied Alien Children (UAC) Program operates in a highly uncertain environment where changes in migration patterns, border activity, policy decisions, and humanitarian conditions can affect the number of children entering federal care.

This project develops an end-to-end predictive analytics workflow to understand historical HHS care occupancy and estimate future care-load patterns using operational data and engineered temporal features.

The project covers:

- Data Understanding
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Predictive Modeling
- Model Evaluation
- Future Forecasting
- Interactive Dashboard Development
- Automated Testing

---

# 🎯 Business Problem

The UAC Program needs reliable analytical insights to understand changes in care occupancy and anticipate potential changes in future demand.

Historical descriptive analytics can explain what has happened, but predictive modeling can provide additional forward-looking insights for operational planning.

### Key Business Questions

1. How has the number of children in HHS care changed over time?
2. What historical and temporal patterns are associated with HHS care occupancy?
3. Which engineered features provide the strongest predictive signals?
4. How accurately can machine learning models predict HHS care occupancy?
5. What does the model-based forecast indicate about future care-load patterns?

### Business Objective

Develop an end-to-end predictive forecasting workflow that can support:

- Capacity planning
- Resource allocation
- Operational planning
- Care-load monitoring
- Data-driven decision-making

---

# 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Development Environment | Jupyter Notebook, VS Code |
| Testing | Pytest |
| Version Control | Git & GitHub |

---

# 🔄 Project Workflow

The project follows an end-to-end predictive analytics workflow:

```text
Raw Dataset
     │
     ▼
Data Understanding
     │
     ▼
Data Cleaning
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Feature Engineering
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Future Forecasting
     │
     ▼
Dashboard & Reports
```

---

# 📊 Dataset Information

The project uses historical operational data from the Unaccompanied Alien Children (UAC) Program to analyze and forecast HHS care occupancy.

## Dataset Characteristics

| Attribute | Description |
|---|---|
| Dataset Type | Time-Series Operational Data |
| Primary Target | Children in HHS Care |
| Data Source | U.S. Department of Health and Human Services (HHS) |
| Analysis Type | Exploratory, Predictive & Forecasting Analytics |
| Primary Use | Care Load and Placement Demand Forecasting |

## Key Variables

The dataset contains operational measures related to:

- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children in HHS Care
- Children discharged from HHS Care
- Date and temporal attributes

The raw dataset was cleaned, standardized, and transformed before exploratory analysis and predictive modeling.

---

# 🔍 Exploratory Data Analysis

The exploratory analysis examines:

- HHS care occupancy trends over time
- Monthly care occupancy patterns
- Distribution of HHS care occupancy
- Relationships between operational variables
- Correlations between care-flow variables
- Potential outliers and unusual observations

The analysis identified strong relationships between several operational variables and HHS care occupancy.

---

# ⚙️ Feature Engineering

Temporal and historical features were created to capture short-term and long-term patterns in care occupancy.

## Engineered Features

- Lag 1
- Lag 7
- Lag 14
- Rolling 7-day average
- Rolling 14-day average
- Rolling 30-day average
- Month
- Week
- Day
- Day of Week
- Weekend indicator
- Growth rate

These features allow the models to incorporate recent care-load history and temporal patterns.

# 🤖 Machine Learning Approach

Three machine learning regression models were evaluated:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

## Evaluation Metrics

The models were evaluated using:

- **MAE** — Mean Absolute Error
- **RMSE** — Root Mean Squared Error
- **R² Score** — Coefficient of Determination

The model with the strongest overall predictive performance was selected for forecasting.

---

# 📈 Model Performance

Three machine learning models were evaluated using MAE, RMSE, and R² Score.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 74.5483 | 98.8911 | 0.998823 |
| Random Forest | 72.2137 | 144.4701 | 0.998423 |
| Gradient Boosting | 67.3656 | 100.2113 | 0.998791 |

## Best Model

**Gradient Boosting Regressor**

Gradient Boosting achieved the lowest MAE among the evaluated models and was selected as the preferred model for the project.

---

# ⭐ Feature Importance

Feature importance analysis showed that recent HHS care occupancy history provides the strongest predictive signal.

## Most Influential Features

1. Children in HHS Care
2. HHS_Lag_1
3. Rolling7
4. Rolling14
5. HHS_Lag_7
6. HHS_Lag_14
7. Rolling30

This indicates that recent care occupancy and short-term historical patterns are highly informative when predicting care load.

---

# 🔮 Forecasting

The trained predictive model was used to generate model-based HHS care occupancy estimates based on historical operational patterns and engineered temporal features.

The forecast output is stored in:

```
text
results/future_forecast.csv

```

## Forecast Output

The forecast dataset contains daily predicted HHS care occupancy values.

| Column | Description |
|---|---|
| `Date` | Forecast date |
| `Predicted_HHS_Care` | Predicted number of children in HHS care |

The generated predictions can be used to analyze potential changes in care occupancy and support capacity planning, resource allocation, and operational decision-making.

---

# 📊 Project Visualizations

The project contains eight major visualizations generated during the exploratory analysis, model evaluation, and forecasting stages.

| # | Visualization | File |
|---:|---|---|
| 1 | HHS Care Occupancy Trend | `01_care_occupancy_trend.png` |
| 2 | Monthly HHS Care Occupancy | `02_monthly_care_occupancy.png` |
| 3 | Correlation Heatmap | `03_correlation_heatmap.png` |
| 4 | HHS Care Occupancy Distribution | `04_care_occupancy_distribution.png` |
| 5 | Actual vs Predicted | `05_actual_vs_predicted.png` |
| 6 | Feature Importance | `06_feature_importance.png` |
| 7 | Model Performance Comparison | `07_model_comparison.png` |
| 8 | Forecasted HHS Care Occupancy | `08_future_forecast.png` |

---

# 📊 Interactive Dashboard

A Streamlit dashboard was developed to provide an interactive view of the project's analytical and forecasting results.

The dashboard presents:

- Key Performance Indicators
- Model Performance
- Historical Care Occupancy Trends
- Monthly Care Occupancy
- Correlation Analysis
- Distribution Analysis
- Actual vs Predicted Results
- Feature Importance
- Forecast Results



## Run the Dashboard

From the project root directory:

```bash
streamlit run dashboard/app.py

```
# 🧪 Testing

The project includes automated tests using Pytest.

The test suite validates:

- Dataset loading
- Feature engineering
- Machine learning model creation

## Run All Tests

From the project root directory:

```bash

python -m pytest tests
```
# 💡 Key Insights

The analysis produced several important findings:

- HHS care occupancy showed substantial variation throughout the analyzed period.
- Recent care occupancy history provides strong predictive information.
- Lag and rolling-window features are highly useful for forecasting.
- Gradient Boosting achieved the lowest MAE among the evaluated models.
- The project demonstrates how historical operational data can be transformed into predictive insights for care-load planning.

---

# 🚀 Future Improvements

Potential extensions of the project include:

- Incorporating external variables such as border activity and policy changes.
- Evaluating additional forecasting algorithms.
- Implementing automated model retraining.
- Improving dashboard interactivity.
- Adding prediction intervals to quantify forecast uncertainty.
- Deploying the forecasting pipeline as a production API.
- Integrating Power BI or other business intelligence tools.

---

# 👤 Author

**Kishan Masura**

Data Science & Analytics

## Skills

Python • SQL • Power BI • Excel • Machine Learning • Data Analytics

---

# ⭐ Project Summary

This project demonstrates an end-to-end Data Science workflow combining:

- Data cleaning
- Exploratory data analysis
- Feature engineering
- Machine learning
- Model evaluation
- Future forecasting
- Automated testing
- Interactive dashboard development

The final solution provides a structured approach to analyzing HHS care-load patterns and generating predictive insights that can support capacity planning, resource allocation, and operational decision-making.
