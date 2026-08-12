# 📈 Predictive Forecasting of Care Load & Placement Demand

## U.S. Department of Health and Human Services (HHS)

An end-to-end Machine Learning project that predicts future HHS Care occupancy using historical operational data, feature engineering, and predictive modeling.

---

## 📖 Project Overview

The UAC (Unaccompanied Alien Children) Program operates in a highly uncertain environment where sudden changes in migration, border activity, policy decisions, or humanitarian crises can rapidly increase the number of children entering federal care.

This project develops an end-to-end predictive forecasting pipeline that enables decision-makers to estimate future HHS Care occupancy using historical operational data and engineered temporal features.

The solution includes:

- Data Understanding
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Predictive Modeling
- Future Forecasting


---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git & GitHub |

---

# 🔄 Project Workflow

```
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
Future Forecasting
     │
     ▼
Forecast Report
```

---

## 📊 Dataset Information

The project uses historical operational data from the Unaccompanied Alien Children (UAC) Program to analyze and forecast HHS care occupancy.

### Dataset Characteristics

| Attribute | Description |
|---|---|
| Dataset Type | Time-Series Operational Data |
| Primary Target | Children in HHS Care |
| Data Source | U.S. Department of Health and Human Services (HHS) |
| Analysis Type | Exploratory, Predictive & Forecasting Analytics |
| Primary Use | Care Load and Placement Demand Forecasting |

### Key Variables

The dataset contains operational measures related to:

- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children in HHS Care
- Children discharged from HHS Care
- Date and temporal attributes

The raw data was cleaned, standardized, and transformed before exploratory analysis, feature engineering, and predictive modeling.

---

## 🎯 Business Problem

The UAC Program operates in a highly uncertain environment where changes in migration patterns, border activity, policy decisions, and humanitarian conditions can rapidly affect the number of children entering federal care.

Descriptive analytics can explain historical patterns, but decision-makers also require forward-looking estimates to support operational planning and resource allocation.

### Key Business Questions

1. How has the number of children in HHS care changed over time?
2. What historical and temporal patterns influence care occupancy?
3. Which engineered features are most useful for predicting HHS care load?
4. How accurately can machine learning models predict care occupancy?
5. What could future HHS care demand look like based on historical patterns?

### Business Objective

Develop an end-to-end predictive forecasting workflow that can help support capacity planning, resource allocation, and operational decision-making.


---

## 🤖 Machine Learning Approach

The project evaluates multiple machine learning models to predict HHS care occupancy.

### Models Evaluated

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Feature Engineering

Temporal and historical features were engineered to capture patterns in care occupancy, including:

- Lag features
- Rolling averages
- Month
- Quarter
- Week
- Day
- Day of Week
- Weekend indicator
- Growth rate

### Evaluation Metrics

The models were evaluated using:

- **MAE** — Mean Absolute Error
- **RMSE** — Root Mean Squared Error
- **R² Score** — Coefficient of Determination

The selected model was then used for future HHS care occupancy forecasting.


---

## 📈 Model Performance

Three machine learning models were evaluated using MAE, RMSE, and R² Score.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 74.5483 | 98.8911 | 0.998823 |
| Random Forest | 72.2137 | 144.4701 | 0.998423 |
| Gradient Boosting | 67.3656 | 100.2113 | 0.998791 |

The final model was selected based on predictive performance and suitability for future forecasting.

---

## 🔮 Future Forecasting

The trained predictive model was used to generate future HHS care occupancy estimates based on historical operational patterns and engineered temporal features.

The forecast output is stored in:

`results/future_forecast.csv`

### Forecast Summary

| Metric | Predicted HHS Care Occupancy |
|---|---:|
| Forecast Start | 2023-03-08 |
| Forecast End | 2025-12-18 |
| Minimum Forecast | 1,978.95 |
| Maximum Forecast | 11,398.66 |
| Average Forecast | 5,988.79 |
| Median Forecast | 6,263.77 |
| Standard Deviation | 2,871.82 |

### Forecast Output

The forecast dataset contains daily predicted HHS care occupancy values with the following structure:

| Column | Description |
|---|---|
| `Date` | Forecast date |
| `Predicted_HHS_Care` | Predicted number of children in HHS care |

The generated forecasts can be used to understand potential changes in care occupancy and support capacity planning, resource allocation, and operational decision-making.

---

## 📁 Project Structure

```text
Predictive_Forecasting_of_Care_Load/
│
├── data/
│   ├── external/
│   ├── processed/
│   └── raw/
│
├── models/
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Predictive_Modeling.ipynb
│   └── 06_Future_Forecasting.ipynb
│
├── results/
│   ├── feature_importance.csv
│   ├── forecast_summary.csv
│   ├── future_forecast.csv
│   └── model_performance.csv
│
├── reports/
│
├── src/
│
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt


---

# ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/kishanDataLab/Predictive_Forecasting_of_Care_Load.git
cd Predictive_Forecasting_of_Care_Load
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the notebooks

Open the project in Jupyter Notebook or VS Code and execute the notebooks in the following order:

1. `01_Data_Understanding.ipynb`
2. `02_Data_Cleaning.ipynb`
3. `03_Exploratory_Data_Analysis.ipynb`
4. `04_Feature_Engineering.ipynb`
5. `05_Predictive_Modeling.ipynb`
6. `06_Future_Forecasting.ipynb`

The generated outputs are stored in the `results/` directory.

---

# 🚀 Future Improvements

Potential extensions of the project include:

- Incorporating external variables such as border activity and policy changes.
- Evaluating additional forecasting algorithms.
- Implementing automated model retraining.
- Building an interactive Power BI or web-based forecasting dashboard.
- Adding prediction intervals to quantify forecast uncertainty.
- Deploying the forecasting pipeline as a production API.

---

# 👤 Author

**Kishan Masura**

Data Science & Analytics

### Skills

Python • SQL • Power BI • Excel • Machine Learning • Data Analytics

---

⭐ If you found this project useful, feel free to explore the notebooks and analysis results.