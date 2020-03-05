from mealprep.mealprep import  find_missing_ingredients
import pandas as pd
import numpy as np
import pytest


def test_find_missing_ingredients():
    '''
    This is a test function for find_missing_ingredients, which checks the following behaviour:
    1. If the function counts the number of missing values correctly
    2. If the function returns the desired string if there are no missing values
    3. If the find_missing_ingredients can handle dataframe with NAs.
    4. If the find_missing_ingredients can handle empty dataframe.
    5. If the find_missing_ingredients function confirms the right input type
    
   
    Example
    --------
    >>> test_find_missing_ingredients()
    '''
    test1 = {'column1': ['a','b','c', 'd'],'column2': [1,2,np.NaN,3], 'column3': [np.NaN]*4}
    df1 = pd.DataFrame(test1)

    output = find_missing_ingredients(df1)
    assert(output.query('index == 0')['NaN count'].values[0] == 0)
    assert(output.query('index == 1')['NaN count'].values[0] == 1)
    assert(output.query('index == 2')['NaN count'].values[0] == 4)

    test2 = {'column1': [1,2,3], 'column2': [4,5,6]}
    df2 = pd.DataFrame(test2)
    assert(find_missing_ingredients(df2) == "There are no missing values")

    test3 = {'column1': []}
    df3 = pd.DataFrame(test3)
    with pytest.raises(AssertionError):
        find_missing_ingredients(df3)

    with pytest.raises(AssertionError):
        find_missing_ingredients("test")
