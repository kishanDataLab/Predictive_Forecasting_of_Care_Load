# Predictive Forecasting of HHS Care Load & Placement Demand

## A Data Science and Machine Learning Approach for Forecasting HHS Care Occupancy

**Author:** Kishan Masura  
**Project:** Predictive Forecasting of Care Load & Placement Demand  
**Domain:** Data Science, Machine Learning, Predictive Analytics and Forecasting

---

## Abstract

The demand for care services can vary significantly over time due to changes in admissions, custody movements, transfers, discharges, and other operational factors. Effective forecasting of care occupancy can therefore support better capacity planning and resource allocation.

This project presents an end-to-end predictive analytics workflow for analysing historical HHS care occupancy data and forecasting future care-load patterns. The workflow includes data understanding, data cleaning, exploratory data analysis, temporal feature engineering, predictive modelling, model evaluation, and future forecasting.

The project uses Python and commonly used data science libraries to transform operational data into meaningful analytical insights. Historical trends and relationships among operational variables are examined before developing predictive models. Temporal features are engineered to capture patterns associated with dates and time.

The final forecasting stage provides estimates of future HHS care occupancy and presents the forecast results through visualisations. These results can support operational decision-making by providing an indication of potential future care-load levels.

**Keywords:** HHS Care, Care Occupancy, Predictive Analytics, Machine Learning, Forecasting, Feature Engineering, Time Series, Resource Planning

---

# 1. Introduction

Organisations responsible for care services need to understand changes in occupancy and demand in order to plan resources effectively. Variations in admissions, custody movements, transfers, and discharges can influence the number of individuals requiring care.

Historical operational data provides an opportunity to identify trends and relationships within the care system. Predictive modelling can further extend this analysis by estimating future care-load patterns.

This project focuses on developing an end-to-end predictive forecasting workflow for HHS care occupancy. The project combines exploratory data analysis, feature engineering, machine learning, and forecasting to provide analytical support for future capacity planning.

---

# 2. Problem Statement

Care occupancy can change over time and may be influenced by multiple operational factors. Planning resources using only historical averages may not adequately represent future variations in demand.

The objective of this project is to analyse historical HHS care occupancy data and develop a predictive forecasting approach that can estimate future care-load levels.

The project addresses the following questions:

1. How has HHS care occupancy changed historically?
2. What patterns and relationships exist among operational variables?
3. Which engineered features can support predictive modelling?
4. How effectively can machine learning models predict care occupancy?
5. What future care-load patterns can be estimated from the available historical data?

---

# 3. Objectives

The major objectives of the project are:

- Understand the structure and characteristics of the HHS operational dataset.
- Clean and preprocess the raw data.
- Explore historical care occupancy trends.
- Analyse relationships among operational variables.
- Engineer meaningful temporal and predictive features.
- Develop predictive machine learning models.
- Evaluate model performance using appropriate metrics.
- Generate future HHS care occupancy forecasts.
- Present the results in a clear and interpretable form.
- Provide business insights for capacity and resource planning.

---

# 4. Dataset Description

The project uses operational data related to the Unaccompanied Alien Children (UAC) programme.

The dataset contains date-based observations and operational variables associated with children entering, remaining in, transferring through, and leaving HHS care.

Important variables include:

- Date
- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children in HHS Care
- Children discharged from HHS Care

The primary target variable for the forecasting analysis is HHS care occupancy.

---

# 5. Project Methodology

The project follows an end-to-end data science workflow.

The major stages are:

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Predictive Modelling
6. Model Evaluation
7. Future Forecasting
8. Business Interpretation

---

# 6. Data Understanding

The initial stage focused on understanding the dataset structure, variables, data types, and basic statistical characteristics.

The dataset was inspected to identify the available operational variables and understand how the observations were organised over time.

Initial data exploration was performed using Python and Pandas.

The analysis included:

- Dataset shape
- Column names
- Data types
- Initial records
- Summary statistics
- Missing-value inspection
- Duplicate-record inspection

This stage established the foundation for subsequent preprocessing and analysis.

---

# 7. Data Cleaning and Preprocessing

Data preprocessing was performed to improve data quality and ensure that the dataset was suitable for analysis and modelling.

## 7.1 Removing Empty Rows

Completely empty rows were identified and removed from the dataset.

## 7.2 Removing Duplicate Records

Duplicate records were checked and removed to prevent repeated observations from affecting the analysis.

## 7.3 Date Conversion

The Date column was converted into an appropriate datetime format so that time-based analysis and forecasting could be performed.

## 7.4 Data Type Conversion

Numerical variables were converted into appropriate numeric data types to allow mathematical calculations and statistical analysis.

## 7.5 Missing-Value Handling

Missing values were examined and handled appropriately based on the requirements of the analysis.

## 7.6 Clean Dataset

After preprocessing, the cleaned dataset was used for exploratory data analysis, feature engineering, predictive modelling, and forecasting.

---

# 8. Exploratory Data Analysis

Exploratory Data Analysis was conducted to understand historical behaviour and relationships within the dataset.

## 8.1 Care Occupancy Trend

The historical HHS care occupancy trend was analysed to identify changes in occupancy over time.

The analysis helps identify periods of increasing and decreasing care demand.

**Figure 1: Historical HHS Care Occupancy Trend**

_Insert `01_care_occupancy_trend.png` here when converting this paper to PDF._

### Observation

The historical trend demonstrates that HHS care occupancy varies over time rather than remaining constant.

### Business Insight

Understanding historical occupancy patterns can help organisations identify periods of higher and lower care demand and improve resource planning.

---

## 8.2 Monthly Care Occupancy Analysis

Monthly care occupancy patterns were examined to identify recurring variations in care load.

**Figure 2: Monthly HHS Care Occupancy**

_Insert `02_monthly_care_occupancy.png` here when converting this paper to PDF._

### Observation

Monthly aggregation provides a clearer view of changes in care occupancy and helps reduce the effect of short-term daily fluctuations.

### Business Insight

Monthly patterns can support medium-term capacity planning and operational resource allocation.

---

## 8.3 Correlation Analysis

The correlation analysis was used to examine relationships among the operational variables in the dataset.

**Figure 3: Correlation Heatmap**

_Insert `03_correlation_heatmap.png` here when converting this paper to PDF._

### Observation

The correlation analysis provides an overview of relationships between admissions, custody movements, HHS care occupancy, and discharges.

### Business Insight

Understanding relationships among operational variables can help identify variables that may be useful for predictive modelling and operational monitoring.

---

# 9. Feature Engineering

Feature engineering was performed to transform the raw operational data into variables that could be used effectively by predictive models.

Temporal features were created from the Date variable to capture time-related patterns.

Potential temporal features include:

- Year
- Month
- Day
- Day of Week
- Time-related indicators

Feature engineering helps machine learning models identify temporal patterns that may not be directly represented by the original date variable.

---

# 10. Predictive Modelling

Predictive modelling was performed to estimate HHS care occupancy based on the prepared dataset and engineered features.

The modelling workflow included:

1. Preparing the modelling dataset.
2. Selecting predictive features.
3. Defining the target variable.
4. Splitting the data appropriately.
5. Training predictive models.
6. Generating predictions.
7. Evaluating model performance.

## 10.1 Model Evaluation

Three machine learning models were evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 74.55 | 98.89 | 0.998823 |
| Random Forest | 72.21 | 114.45 | 0.998424 |
| Gradient Boosting | 67.37 | 100.21 | 0.998791 |

### Model Selection

Gradient Boosting achieved the lowest MAE of **67.37**, indicating the smallest average absolute prediction error among the evaluated models.

Its RMSE was **100.21**, while its R² Score was **0.998791**.

Based primarily on the lowest MAE and its strong overall predictive performance, Gradient Boosting was selected as the final predictive model.

---

## 10.2 Feature Importance

Feature-importance analysis was performed to understand which variables contributed most strongly to the predictive model.

| Feature | Importance |
|---|---:|
| Children in HHS Care | 0.468840 |
| HHS_Lag_1 | 0.334926 |
| Rolling7 | 0.172212 |
| Rolling14 | 0.013689 |

The results indicate that recent HHS care occupancy is the strongest predictive signal. The one-period lag and rolling-window features also contribute substantially, demonstrating the importance of recent care-load history and short-term temporal patterns.


# 11. Model Interpretation

The predictive modelling stage demonstrates how historical operational information and engineered temporal features can be used to estimate HHS care occupancy.

The model results should be interpreted together with the limitations of the available dataset and the forecasting horizon.

Predictive modelling provides decision-support information rather than a guarantee of future occupancy.

---

# 12. Forecasted HHS Care Occupancy Trend

The final forecasting stage estimates future HHS care occupancy based on historical patterns.

**Figure 4: Forecasted HHS Care Occupancy Trend**

_Insert the final forecasting chart generated from `06_Future_Forecasting.ipynb` here._

### Observation

The forecasting analysis provides an estimate of future HHS care occupancy based on historical patterns.

The forecast results indicate that future care occupancy can fluctuate rather than remaining at a constant level.

### Business Insight

The variation between forecast minimum and maximum values highlights the importance of flexible capacity planning.

Rather than planning resources around a single expected occupancy value, decision-makers should consider a range of possible care-load levels.

---

# 13. Business Implications

The project provides several potential operational benefits.

### 13.1 Capacity Planning

Forecasted occupancy can provide an indication of future care-load requirements and support capacity planning.

### 13.2 Resource Allocation

Forecast information can help decision-makers anticipate periods where additional operational resources may be required.

### 13.3 Operational Monitoring

Historical trend analysis and predictive modelling can support continuous monitoring of changes in care occupancy.

### 13.4 Data-Driven Decision Making

The project demonstrates how operational data can be transformed into actionable analytical insights through data science and machine learning.

---

# 14. Limitations

The forecasting results depend on the quality, completeness, and historical coverage of the available dataset.

Several external factors may influence future care occupancy but may not be represented directly in the dataset.

These may include:

- Policy changes
- Migration patterns
- Border activity
- Humanitarian conditions
- Operational changes
- Unexpected events

Therefore, forecasts should be treated as analytical estimates rather than guaranteed future outcomes.

---

# 15. Future Scope

The project can be further improved through:

- Testing additional forecasting algorithms.
- Hyperparameter optimisation.
- Incorporating additional external variables.
- Developing real-time forecasting pipelines.
- Building an interactive web-based dashboard.
- Implementing automated model retraining.
- Monitoring forecast accuracy over time.
- Developing confidence intervals and uncertainty analysis.

---

# 16. Conclusion

This project developed an end-to-end predictive analytics workflow for analysing and forecasting HHS care occupancy.

The workflow covered data understanding, data cleaning, exploratory analysis, feature engineering, predictive modelling, model evaluation, and future forecasting.

The analysis demonstrates the potential of machine learning and forecasting techniques to support operational planning and resource allocation.

By combining historical trends with predictive analysis, organisations can obtain additional information for anticipating future care-load conditions and preparing appropriate resources.

The project therefore demonstrates a practical application of data science and machine learning to an operational forecasting problem.

---

# 17. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Machine Learning
- Predictive Analytics
- Time-Series Forecasting

---

# 18. Project Repository

GitHub Repository:

https://github.com/kishanDataLab/Predictive_Forecasting_of_Care_Load

---

# 19. Project Files

The project repository contains:

- Data files
- Data cleaning notebook
- Exploratory Data Analysis notebook
- Feature engineering notebook
- Predictive modelling notebook
- Future forecasting notebook
- Visualisation images
- Model files
- Project reports
- Presentation
- Source code
- Testing files

---

## Author

**Kishan Masura**

Data Science & AI

Predictive Analytics | Machine Learning | Forecasting
