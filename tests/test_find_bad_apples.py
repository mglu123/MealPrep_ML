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


# Checks Item 2
def test_except_min():
    '''
    This function tests that find_bad_apples()
    raises an exception
    when a dataframe with fewer than 30 rows
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

    df_test2 = pd.DataFrame({'A': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1]})

    with pytest.raises(AssertionError):
        find_bad_apples(df_test2)


# Checks Item 3
def test_pos_neg():
    '''
    This function tests that find_bad_apples()
    produces the correct output
    when a dataframe with positive and negative values
    in the same column is passed as an argument.

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

    df_test3 = pd.DataFrame({'A': [100, -100, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})

    output3 = find_bad_apples(df_test3)
    assert(output3.query('index == 0')['Variable'].values[0] == 'A')
    assert(output3.query('index == 0')['Indices'].values[0] == [0, 1])
    assert(output3.query('index == 0')['Total Outliers'].values[0] == 2)


# Checks Item 4
def test_no_bad_apples():
    '''
    This function tests that find_bad_apples() returns
    a dataframe with 'No outliers detected'
    when there are no outliers present in the dataframe.

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

    df_test4 = pd.DataFrame({'A': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})

    output4 = find_bad_apples(df_test4)
    assert(output4.query('index == 0')['Variable'].values[0] ==
           'No outliers detected')
    assert(output4.query('index == 0')['Indices'].values[0] == 'x')
    assert(output4.query('index == 0')['Total Outliers'].values[0] == 0)


# Checks Item 5
def test_one_col():
    '''
    This function tests that find_bad_apples()
    produces the correct output
    when a dataframe with only one column
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
    df_test5 = pd.DataFrame({'A': [1, 1, 10, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})

    output5 = find_bad_apples(df_test5)
    assert(output5.query('index == 0')['Variable'].values[0] == 'A')
    assert(output5.query('index == 0')['Indices'].values[0] == [2])
    assert(output5.query('index == 0')['Total Outliers'].values[0] == 1)


# Checks Item 6
def test_two_col():
    '''
    This function tests that find_bad_apples()
    produces the correct output
    when a dataframe with more than one column
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

    df_test6 = pd.DataFrame({'A': [1, 1, 10, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'B': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                  1, 1, 1, 1, 1, 1, 1, 1, 1, 10]})

    output6 = find_bad_apples(df_test6)
    assert(output6.query('index == 0')['Variable'].values[0] == 'A')
    assert(output6.query('index == 0')['Indices'].values[0] == [2])
    assert(output6.query('index == 0')['Total Outliers'].values[0] == 1)
    assert(output6.query('index == 1')['Variable'].values[0] == 'B')
    assert(output6.query('index == 1')['Indices'].values[0] == [29])
    assert(output6.query('index == 1')['Total Outliers'].values[0] == 1)
