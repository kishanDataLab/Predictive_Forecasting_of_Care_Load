import streamlit as st
import pandas as pd
from pathlib import Path


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="HHS Care Load Forecasting",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RESULTS_DIR = PROJECT_ROOT / "results"
IMAGE_DIR = PROJECT_ROOT / "images"


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
    <style>

    /* Main title */
    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        font-size: 17px;
        color: #666666;
        margin-bottom: 25px;
    }

    /* Section headings */
    .section-title {
        font-size: 27px;
        font-weight: 650;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* Insight cards */
    .insight-box {
        padding: 18px;
        border-radius: 10px;
        background-color: #f5f7fa;
        border-left: 5px solid #4c78a8;
        margin-bottom: 12px;
    }

    /* Small description */
    .description {
        color: #666666;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777777;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 15px;
        border-top: 1px solid #dddddd;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("📊 HHS Analytics")

    st.markdown("---")

    st.markdown(
        """
        ### Project

        **Predictive Forecasting of Care Load & Placement Demand**

        This dashboard presents:

        • Historical care-load trends  
        • Monthly occupancy analysis  
        • Correlation analysis  
        • Machine-learning performance  
        • Feature importance  
        • Future forecasting  
        • Key project insights
        """
    )

    st.markdown("---")

    st.markdown("### Dashboard Sections")

    st.markdown(
        """
        📈 Trends  
        
        🤖 Model Performance  
        
        🔮 Forecast  
        
        🔍 Analysis  
        
        💡 Insights
        """
    )

    st.markdown("---")

    st.caption(
        "HHS Care Occupancy Analytics"
    )


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">'
    'Predictive Forecasting of Care Load & Placement Demand'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'HHS Care Occupancy Analytics Dashboard — '
    'Historical Analysis, Machine Learning & Forecasting'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================================
# EXECUTIVE OVERVIEW
# ==========================================================

st.markdown(
    '<div class="section-title">Executive Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        label="Preferred Model",
        value="Gradient Boosting"
    )

with col2:

    st.metric(
        label="Best MAE",
        value="67.37"
    )

with col3:

    st.metric(
        label="Best R² Score",
        value="99.88%"
    )

with col4:

    st.metric(
        label="Forecast",
        value="Future"
    )


# ==========================================================
# MODEL PERFORMANCE DATA
# ==========================================================

performance_data = pd.DataFrame({

    "Model": [
        "Linear Regression",
        "Random Forest",
        "Gradient Boosting"
    ],

    "MAE": [
        74.55,
        72.21,
        67.37
    ],

    "RMSE": [
        98.89,
        114.45,
        100.21
    ],

    "R² Score": [
        0.998823,
        0.998424,
        0.998791
    ]
})


# ==========================================================
# NAVIGATION TABS
# ==========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📈 Trends",
        "🤖 Model Performance",
        "🔮 Forecast",
        "🔍 Analysis",
        "💡 Insights"
    ]
)


# ==========================================================
# IMAGE DISPLAY FUNCTION
# ==========================================================

def show_image(filename, caption):

    image_path = IMAGE_DIR / filename

    if image_path.exists():

        st.image(
            str(image_path),
            caption=caption,
            use_container_width=True
        )

    else:

        st.error(
            f"Image not found: {filename}"
        )


# ==========================================================
# TAB 1 — HISTORICAL TRENDS
# ==========================================================

with tab1:

    st.markdown(
        '<div class="section-title">'
        'Historical Care Occupancy Trends'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="description">'
        'Historical analysis of children in HHS care over the '
        'observed period.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("")

    show_image(
        "01_care_occupancy_trend.png",
        "Children in HHS Care Over Time"
    )

    st.markdown(
        '<div class="section-title">'
        'Monthly Care Occupancy'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="description">'
        'Average monthly number of children in HHS care.'
        '</div>',
        unsafe_allow_html=True
    )

    show_image(
        "02_monthly_care_occupancy.png",
        "Average Monthly Children in HHS Care"
    )


# ==========================================================
# TAB 2 — MODEL PERFORMANCE
# ==========================================================

with tab2:

    st.markdown(
        '<div class="section-title">'
        'Machine Learning Model Performance'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="description">'
        'Comparison of the evaluated models using MAE, RMSE '
        'and R² Score.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("")

    st.success(
        "Preferred Model: Gradient Boosting — lowest MAE of 67.37"
    )

    st.markdown("### Performance Metrics")

    st.dataframe(
        performance_data.style.format({
            "MAE": "{:.2f}",
            "RMSE": "{:.2f}",
            "R² Score": "{:.6f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">'
        'Model Comparison'
        '</div>',
        unsafe_allow_html=True
    )

    show_image(
        "07_model_comparison.png",
        "Model Performance Comparison"
    )

    st.markdown(
        '<div class="section-title">'
        'Actual vs Predicted'
        '</div>',
        unsafe_allow_html=True
    )

    show_image(
        "05_actual_vs_predicted.png",
        "Actual vs Predicted Values — Random Forest"
    )


# ==========================================================
# TAB 3 — FORECAST
# ==========================================================

with tab3:

    st.markdown(
        '<div class="section-title">'
        'Future HHS Care Occupancy Forecast'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="description">'
        'Forecasting analysis based on historical care-load '
        'patterns and engineered time-series features.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("")

    show_image(
        "08_future_forecast.png",
        "Forecasted HHS Care Occupancy"
    )

    st.info(
        """
        The forecast follows the historical care-load trajectory
        and indicates substantially lower occupancy levels in the
        later portion of the observed series.
        """
    )


# ==========================================================
# TAB 4 — DATA ANALYSIS
# ==========================================================

with tab4:

    st.markdown(
        '<div class="section-title">'
        'Exploratory & Statistical Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # Correlation
    # ------------------------------------------------------

    st.markdown("### Correlation Analysis")

    st.markdown(
        '<div class="description">'
        'Correlation between major care-placement and HHS '
        'care variables.'
        '</div>',
        unsafe_allow_html=True
    )

    show_image(
        "03_correlation_heatmap.png",
        "Correlation Matrix"
    )

    # ------------------------------------------------------
    # Distribution
    # ------------------------------------------------------

    st.markdown("### Distribution Analysis")

    st.markdown(
        '<div class="description">'
        'Distribution of the number of children in HHS care.'
        '</div>',
        unsafe_allow_html=True
    )

    show_image(
        "04_care_occupancy_distribution.png",
        "Distribution of Children in HHS Care"
    )

    # ------------------------------------------------------
    # Feature Importance
    # ------------------------------------------------------

    st.markdown("### Feature Importance")

    st.markdown(
        '<div class="description">'
        'Most influential features used by the predictive model.'
        '</div>',
        unsafe_allow_html=True
    )

    show_image(
        "06_feature_importance.png",
        "Top 10 Important Features"
    )


# ==========================================================
# TAB 5 — KEY INSIGHTS
# ==========================================================

with tab5:

    st.markdown(
        '<div class="section-title">'
        'Key Project Insights'
        '</div>',
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # Insight 1
    # ------------------------------------------------------

    st.markdown(
        """
        <div class="insight-box">
        <b>1. Strong Model Performance</b><br>
        Gradient Boosting achieved the lowest MAE among the
        evaluated models and was selected as the preferred model
        for the project.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # Insight 2
    # ------------------------------------------------------

    st.markdown(
        """
        <div class="insight-box">
        <b>2. High Predictive Accuracy</b><br>
        The selected model achieved an R² score of approximately
        99.88%, indicating a very strong fit on the evaluated data.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # Insight 3
    # ------------------------------------------------------

    st.markdown(
        """
        <div class="insight-box">
        <b>3. Historical Care Load is Highly Informative</b><br>
        Recent care-load history, particularly HHS_Lag_1 and
        Rolling7, provided the strongest predictive signals.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # Insight 4
    # ------------------------------------------------------

    st.markdown(
        """
        <div class="insight-box">
        <b>4. Significant Change in Care Occupancy</b><br>
        The historical trend shows periods of high occupancy
        followed by a substantial decline and a lower, more stable
        level in the later period.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # Insight 5
    # ------------------------------------------------------

    st.markdown(
        """
        <div class="insight-box">
        <b>5. Operational Planning Opportunity</b><br>
        Forecasting care occupancy can support capacity planning,
        resource allocation and preparedness for changes in
        placement demand.
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# FINAL CONCLUSION
# ==========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">'
    'Project Conclusion'
    '</div>',
    unsafe_allow_html=True
)

st.success(
    """
    Gradient Boosting was selected as the preferred model because
    it achieved the lowest MAE among the evaluated models.
    The analysis also shows that recent historical care-load
    features, particularly HHS_Lag_1 and Rolling7, are important
    predictive signals for estimating HHS care occupancy.
    """
)


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div class="footer">
        Predictive Forecasting of Care Load & Placement Demand
        &nbsp; | &nbsp;
        HHS Care Occupancy Analytics Dashboard
    </div>
    """,
    unsafe_allow_html=True
)