import pandas as pd


def create_time_features(df, date_column="Date"):
    """
    Create calendar-based time features.
    """

    data = df.copy()

    data[date_column] = pd.to_datetime(data[date_column])

    data["Year"] = data[date_column].dt.year
    data["Month"] = data[date_column].dt.month
    data["Week"] = data[date_column].dt.isocalendar().week.astype(int)
    data["Day"] = data[date_column].dt.day

    return data


def create_lag_features(
    df,
    target_column="Children in HHS Care"
):
    """
    Create lag-based features for forecasting.
    """

    data = df.copy()

    data["HHS_Lag_1"] = data[target_column].shift(1)
    data["HHS_Lag_7"] = data[target_column].shift(7)
    data["HHS_Lag_14"] = data[target_column].shift(14)

    return data


def create_rolling_features(
    df,
    target_column="Children in HHS Care"
):
    """
    Create rolling average features.
    """

    data = df.copy()

    data["Rolling7"] = (
        data[target_column]
        .rolling(window=7)
        .mean()
    )

    data["Rolling14"] = (
        data[target_column]
        .rolling(window=14)
        .mean()
    )

    data["Rolling30"] = (
        data[target_column]
        .rolling(window=30)
        .mean()
    )

    return data


def prepare_features(
    df,
    target_column="Children in HHS Care"
):
    """
    Create all forecasting features.
    """

    data = create_time_features(df)
    data = create_lag_features(data, target_column)
    data = create_rolling_features(data, target_column)

    data = data.dropna().reset_index(drop=True)

    return data