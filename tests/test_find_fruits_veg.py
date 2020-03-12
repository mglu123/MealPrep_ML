from mealprep.mealprep import find_fruits_veg
import numpy as np
import pandas as pd


def test_find_fruits_veg():
    '''
    This is a test function for find_fruits_veg,
    and it checks the following behaviour:
    1. If the find_fruits_veg finds numerical columns correctly
    2. If the find_fruits_veg finds categorical columns correctly


    Example
    --------
    >>> test_find_fruits_veg()
    '''
    iris = pd.read_csv(
        ('https://raw.githubusercontent.com/' +
         'mwaskom/seaborn-data/master/iris.csv'))
    df_few_nas = pd.DataFrame({'col1': [1, 2], 'col2': [np.nan, 'b']})
    df_lot_nas = pd.DataFrame({'col1': [np.nan, 2], 'col2': ['a', np.nan]})
    assert (find_fruits_veg(iris, type_of_out='num') == [0, 1, 2, 3])
    assert (find_fruits_veg(iris, type_of_out='categ') == [4])

def test_find_fruits_veg_empty():
    '''
    This is a test function for find_fruits_veg,
    and it checks the following behaviour:
    1. If the find_fruits_veg can handle a data frame with NAs.
    2. If the find_fruits_veg can handle an empty data frame.


    Example
    --------
    >>> test_find_fruits_veg()
    '''
    iris = pd.read_csv(
        ('https://raw.githubusercontent.com/' +
         'mwaskom/seaborn-data/master/iris.csv'))
    df_few_nas = pd.DataFrame({'col1': [1, 2], 'col2': [np.nan, 'b']})
    df_lot_nas = pd.DataFrame({'col1': [np.nan, 2], 'col2': ['a', np.nan]})
    assert (find_fruits_veg(df_few_nas, type_of_out='categ') == [1])
    assert (find_fruits_veg(df_lot_nas, type_of_out='categ') ==
            "It is a empty data frame or too many missing data")
