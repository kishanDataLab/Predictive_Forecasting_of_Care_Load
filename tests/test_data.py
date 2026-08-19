import pandas as pd


def test_dataset_is_not_empty():

    df = pd.DataFrame({
        "Children in HHS Care": [100, 200, 300]
    })

    assert not df.empty