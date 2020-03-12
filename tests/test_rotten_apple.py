from mealprep.mealprep import find_bad_apples
import pandas as pd
import pytest


# Checks Item 1
def test_except_nonnumeric():
    '''
    This function tests that find_bad_apples()
    raises an exception
    when a dataframe with non-numeric columns
    is passed as an argument.

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

    df_test1 = pd.DataFrame({'A': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, "test"]})

    with pytest.raises(AssertionError):
        find_bad_apples(df_test1)
