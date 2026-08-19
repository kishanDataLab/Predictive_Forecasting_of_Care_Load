import pandas as pd

from src.features.feature_engineering import (
    create_lag_features,
    create_rolling_features
)


def test_lag_feature_creation():

    df = pd.DataFrame({
        "Children in HHS Care":
        [100, 200, 300, 400, 500]
    })

    result = create_lag_features(df)

    assert "HHS_Lag_1" in result.columns


def test_rolling_feature_creation():

    df = pd.DataFrame({
        "Children in HHS Care":
        list(range(1, 20))
    })

    result = create_rolling_features(df)

    assert "Rolling7" in result.columns