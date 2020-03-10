from mealprep import mealprep
import pandas as pd
import numpy as np
from vega_datasets import data
import pytest

def cars_data():
    # create test data
    df = pd.read_json(data.cars.url).drop(columns=["Year"])
    X = df.drop(columns=["Name"])
    y = df[["Name"]]

    # >>> df.info()
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 406 entries, 0 to 405
    # Data columns (total 8 columns):
    #  #   Column            Non-Null Count  Dtype  
    # ---  ------            --------------  -----  
    #  0   Name              406 non-null    object 
    #  1   Miles_per_Gallon  398 non-null    float64
    #  2   Cylinders         406 non-null    int64  
    #  3   Displacement      406 non-null    float64
    #  4   Horsepower        400 non-null    float64
    #  5   Weight_in_lbs     406 non-null    int64  
    #  6   Acceleration      406 non-null    float64
    #  7   Origin            406 non-null    object 
    # dtypes: float64(4), int64(2), object(2)
    # memory usage: 25.5+ KB

    return(X, y)

def test_make_recipe_splits_traintest():
    X, y = cars_data()

    # Test on splits_to_return="train_test"
    X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
            X=X, y=y, recipe="ohe_and_standard_scaler", 
            splits_to_return="train_test")

    assert type(X_train) == pd.DataFrame
    assert type(X_test) == pd.DataFrame
    assert type(y_train) == np.ndarray
    assert type(y_test) == np.ndarray
    assert X_valid is None
    assert y_valid is None

    return None

def test_make_recipe_splits_traintestvalid():
    X, y = cars_data()

    # Test on splits_to_return="train_test_valid"
    X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
            X=X, y=y, recipe="ohe_and_standard_scaler", 
            splits_to_return="train_test_valid")

    assert type(X_train) == pd.DataFrame
    assert type(X_test) == pd.DataFrame
    assert type(X_valid) == pd.DataFrame
    assert type(y_train) == np.ndarray
    assert type(y_test) == np.ndarray
    assert type(y_valid) == np.ndarray

    return None

def test_make_recipe_ohe():
    X, y = cars_data()

    # check OHE behavior when one categorical column
    X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
            X=X, y=y, recipe="ohe_and_standard_scaler", 
            splits_to_return="train_test", random_seed=1993)
    assert list(X_train.columns) == ['Miles_per_Gallon', 'Cylinders', 'Displacement', 'Horsepower', 'Weight_in_lbs', 'Acceleration', 'x0_Europe', 'x0_Japan', 'x0_USA']

    # check OHE behavior when two categorical column
    X["Cylinders"] = X["Cylinders"].apply(str)
    X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
            X=X, y=y, recipe="ohe_and_standard_scaler", 
            splits_to_return="train_test", random_seed=1993)

    assert list(X_train.columns) == ['Miles_per_Gallon', 'Displacement', 'Horsepower', 'Weight_in_lbs',
       'Acceleration', 'x0_3', 'x0_4', 'x0_5', 'x0_6', 'x0_8', 'x1_Europe',
       'x1_Japan', 'x1_USA']

    # check that error is thrown if bad recipe select
    with pytest.raises(AssertionError) as e_info:
        X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
                X=X, y=y, recipe="not_a_recipe", 
                splits_to_return="train_test", random_seed=1993)

    return None


def test_make_recipe_split_prop():
    X, y = cars_data()

    # check OHE behavior when one categorical column
    X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
            X=X, y=y, recipe="ohe_and_standard_scaler", 
            splits_to_return="train_test", train_valid_prop=0.5)

    assert X_train.shape[0] == X_test.shape[0]

    return None


def test_make_recipe_defence():
        X, y = cars_data()
        # with pytest.raises(AssertionError):
        #         X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
        #         X=X, y=y, recipe="INVALID RECIPE", 
        #         splits_to_return="train_test", train_valid_prop=0.5)

        with pytest.raises(AssertionError):
                X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
                X=X, y=y, recipe="ohe_and_standard_scaler", 
                splits_to_return="INVALID SPLIT COMMAND", train_valid_prop=0.5)
        
        return None