from src.models.train_models import get_models


def test_models_exist():

    models = get_models()

    assert "Linear Regression" in models
    assert "Random Forest" in models
    assert "Gradient Boosting" in models