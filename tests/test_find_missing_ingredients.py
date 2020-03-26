from mealprep.mealprep import find_missing_ingredients
import pandas as pd
import numpy as np
import pytest


def test_find_missing_ingredients_inputs():
    '''
    This test function checks that the following inputs result in an exception
    error:
    1. An empty data frame
    2. A non-data frame input

    Example
    --------
    >>> test_find_missing_ingredients_inputs()
    '''
    test = {'column1': [], 'column2': []}
    df = pd.DataFrame(test)
    with pytest.raises(ValueError):
        find_missing_ingredients(df)

    with pytest.raises(ValueError):
        find_missing_ingredients("test")


def test_find_missing_ingredients_outputs():
    '''
    This is a test function for find_missing_ingredients, which checks the
    following behaviour:
    1. If the function returns the count and proportion of missing values
    2. If the function returns a string if there are no missing values
    3. If the function correctly identifies the indices with NAs

    Example
    --------
    >>> test_find_missing_ingredients_outputs()
    '''
    test1 = {'column1': ['a', 'b', 'c', 'd'],
             'column2': [1, 2, np.NaN, 3],
             'column3': [np.NaN] * 4}
    df1 = pd.DataFrame(test1)

    output = find_missing_ingredients(df1)
    assert(output.query('index == 0')['NaN count'].values[0] == 1)
    assert(output.query('index == 1')['NaN count'].values[0] == 4)

    assert(output.query('index == 0')['NaN proportion'].values[0] == '25.0%')
    assert(output.query('index == 1')['NaN proportion'].values[0] == '100.0%')

    assert(output.query('index == 0')['NaN indices'].values[0] ==
           np.array([2]))
    assert(np.all(output.query('index == 1')['NaN indices'].values[0] ==
           np.array([0, 1, 2, 3])))

    test2 = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
    df2 = pd.DataFrame(test2)
    assert(find_missing_ingredients(df2) == "There are no missing values")
