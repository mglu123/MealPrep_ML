from mealprep import mealprep
import pandas as pd
from vega_datasets import data

def test_make_recipe():
    df = pd.read_json(data.cars.url).drop(columns=["Year"])
    X = df.drop(columns=["Name"])
    y = df[["Name"]]

    # Test on splits_to_return="train_test"
    X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
            X=X, y=y, recipe="ohe_and_standard_scaler", 
            splits_to_return="train_test")

    assert list(X_train.columns) == ['Miles_per_Gallon', 'Cylinders', 'Displacement', 'Horsepower', 'Weight_in_lbs', 'Acceleration', 'x0_Europe', 'x0_Japan', 'x0_USA']
    assert type(X_train) == pd.DataFrame
    assert X_valid == None
    assert y_valid == None