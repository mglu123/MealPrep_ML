from mealprep import mealprep
import numpy as np
import pandas as pd
import pytest

from pandas._testing import assert_frame_equal

def test_find_bad_apples():
    '''
    This function tests the following behaviour for the find_bad_apples() function:
    1. That find_bad_apples() raises an exception when a dataframe with non-numeric columns is passed as an argument.
    2. That find_bad_apples() raises an exception when a dataframe with fewer than 30 rows is passed as an argument.
    3. That find_bad_apples() produces the correct output when a dataframe with positive and negative values in the same column is passed as an argument.
    4. That find_bad_apples() returns 'Congratulations! You have no bad apples.' when there are no outliers present in the dataframe.
    5. That find_bad_apples() produces the correct output when a dataframe with only one column is passed as an argument.
    6. That find_bad_apples() produces the correct output when a dataframe with more than one column is passed as an argument.
    
    Parameter
    ---------
    None
    
    Returns
    -------
    None
    
    Example
    -------
    test_find_bad_apples()
    '''

    df_test1 = pd.DataFrame({'A' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, "test"]})
    df_test2 = pd.DataFrame({'A' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1]})
    df_test3 = pd.DataFrame({'A' : [100, -100, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})
    df_test4 = pd.DataFrame({'A' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})
    df_test5 = pd.DataFrame({'A' : [1, 1, 10, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})
    df_test6 = pd.DataFrame({'A' : [1, 1, 10, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             'B' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 10]})
    
    # Checks Item 1
    with pytest.raises(AssertionError):
        find_bad_apples(df_test1)
    
    # Checks Item 2
    with pytest.raises(AssertionError):
        find_bad_apples(df_test2)
    
    # Checks Item 3
    df_answer3 = pd.DataFrame({'Variable' : 'A', 'Indices' : [[0, 1]], 'Total Outliers' : 2})
    assert_frame_equal(find_bad_apples(df_test3), df_answer3, check_dtype = False)
    
    # Checks Item 4
    assert find_bad_apples(df_test4) == print('Congratulations! You have no bad apples.'), 'Test 4 for test_find_bad_apples() failed'
    
    # Checks Item 5
    df_answer5 = pd.DataFrame({'Variable' : ['A'], 'Indices' : [[2]], 'Total Outliers' : [1]})
    assert_frame_equal(find_bad_apples(df_test5), df_answer5, check_dtype = False)
    
    # Checks Item 6
    df_answer6 = pd.DataFrame({'Variable' : ['A', 'B'], 'Indices' : [[2], [29]], 'Total Outliers' : [1, 1]})
    assert_frame_equal(find_bad_apples(df_test6), df_answer6, check_dtype = False)
