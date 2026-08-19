import pandas as pd


def generate_forecast(model, X_future):
    """
    Generate future predictions using a trained forecasting model.

    Parameters
    ----------
    model : trained machine learning model
        A fitted forecasting model.

    X_future : pandas.DataFrame
        Future feature data used for prediction.

    Returns
    -------
    pandas.Series
        Predicted care-load values.
    """

    predictions = model.predict(X_future)

    return pd.Series(
        predictions,
        index=X_future.index,
        name="Forecasted HHS Care"
    )


def create_forecast_dataframe(model, X_future, dates=None):
    """
    Create a dataframe containing future dates and forecasted HHS care load.

    Parameters
    ----------
    model : trained machine learning model
        A fitted forecasting model.

    X_future : pandas.DataFrame
        Future feature data.

    dates : optional
        Future dates corresponding to X_future.

    Returns
    -------
    pandas.DataFrame
        Forecast results.
    """

    predictions = generate_forecast(model, X_future)

    forecast_df = pd.DataFrame({
        "Forecasted HHS Care": predictions
    })

    if dates is not None:
        forecast_df.insert(
            0,
            "Date",
            pd.to_datetime(dates)
        )

    return forecast_df


def save_forecast(forecast_df, filepath):
    """
    Save forecast results to a CSV file.
    """

    filepath = str(filepath)

    forecast_df.to_csv(
        filepath,
        index=False
    )

    return filepath