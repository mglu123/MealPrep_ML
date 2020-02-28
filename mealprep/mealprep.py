##Finding numeric and categorical variable names (HUAYUE LUKE)
import numpy as np
import pandas as pd

def find_fruits_veg(df, type_of_out = 'categ'):
    '''
    This function will find the index of columns with all
    numeric value or categorical value based on the specification

    Parameters:
        -----------
        df: pandas.core.frame.DataFrame
            Data frame that need to be proceed
        type_of_out: string
            Type of columns that we want to know index of
        list_of_index: list
            list of index value
    Output:
        -----------
        list_of_index: list
            list of index value
    Example
    --------
    >>>df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    >>>find_num_categ(df, type_of_out = 'categ')
    >>>[1]

    '''
    
    return list_of_index


##Identifying which columns have missing values and how many they have




##Outlier checking (ANNY)
def find_bad_apples(df):
    '''
    This function uses a univariate approach to outlier detection.
    It returns the indices of rows within a dataframe that contain variable values
    which are at least 3 standard deviations from the norm of the variable (outliers),
    as well as how many outliers exist within those rows.
    
    Note: This function works best for small datasets with unimodal variable distributions.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        A dataframe containing numeric data
    
    Returns:
    --------
    bad_apples : list
        A list of tuples (index, number of outliers)
    
    Example:
    --------
    d = {'col1': [1, 1, 1, 9000, 1, 1], 'col2': [1, 1, 1000, 1, 1, 1]}
    df = pd.DataFrame(data=d)
    find_bad_apples(df)
    >>>> [(2, 1), (3, 1)]
    '''
    return bad_apples



def make_recipe(data, recipe, create_train_test = False, create_train_valid_test = True):
    """The `make_recipe()` function is used to quickly apply common data preprocessing techniques
    
    Parameters
    ----------
    data : pandas.DataFrame
        A dataframe containing training data, validation data, X, and y
    recipe : str
        A string specifying which recipe to apply to the data
    create_train_test : bool, optional
        If True will partition data into train and test, by default False
    create_train_valid_test : bool, optional
        If TRUE will partition data into train, valid, and test, by default True
    
    Returns
    -------
    Tuple of pandas.DataFrame
        A tuple of dataframes e.g. (train, valid, test)
    """
    return None
