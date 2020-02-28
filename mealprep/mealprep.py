##Finding numeric and categorical variable names (HUAYUE LUKE)
import numpy as np
import pandas as pd

def find_num_categ(df, type_of_out = 'categ'):
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
    For each column with outliers (values that are 3 or more standard deviations from the mean), this function will create a reference list of row indices with outliers, and the total number of outliers in that column.

    Note: This function works best for small datasets with unimodal variable distributions.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        A dataframe containing numeric data
    
    Returns:
    --------
    bad_apples : pandas.DataFrame
        A dataframe showing 3 columns:
        Variable (column name),
        Indices (list of row indices with outliers), and
        Total Outliers (number of outliers in the column)
    
    Example:
    --------
    >>> data = pd.DataFrame({'A' : [1, 1, 1, 1, 1], 'B' : [10000, 1, 1, 1, 1, 1]}
    >>> df = pd.DataFrame(data)
    >>> find_bad_apples(df)
    Variable  Indices  Total Outliers
       B        0            1
    '''
    return bad_apples



##Shortcut for preprocessing code: StandardScaler / ohe, split data, then fit / fit_transform 
