from mealprep import mealprep
import numpy as np
import pandas as pd
def test_find_fruits_veg():
    '''
    This is a test function for find_fruits_veg, and it checks the following behaviour:
    1. If the find_fruits_veg find numerical column correctly
    2. If the find_fruits_veg find categorical column correctly
    3. If the find_fruits_veg can handle a data frame with NAs.
    4. If the find_fruits_veg can handle an empty data frame.
    
    Parameters
    -----------
    iris: pandas.core.frame.DataFrame
        Iris data frame used to test function behaviour #1 and #2
    df_few_nas: pandas.core.frame.DataFrame
        Data frame with a few NAs used to test function behaviour #3
    df_lot_nas: pandas.core.frame.DataFrame
        Data frame with a lot of NAs and will be empty after drop 
        NAs used to test function behaviour #3
   
    Example
    --------
    >>> test_find_fruits_veg()
    '''
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    df_few_nas = pd.DataFrame({'col1': [1, 2], 'col2': [np.nan, 'b']})
    df_lot_nas = pd.DataFrame({'col1': [np.nan, 2], 'col2': ['a', np.nan]})
    assert (find_fruits_veg(iris, type_of_out = 'num') == [0, 1, 2, 3])
    assert (find_fruits_veg(iris, type_of_out = 'categ') == [4])
    assert (find_fruits_veg(df_few_nas, type_of_out = 'categ') == [1])
    assert (find_fruits_veg(df_lot_nas, type_of_out = 'categ') == "It is a empty data frame or too many missing data")
