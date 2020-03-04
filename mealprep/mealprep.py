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


##Identifying which columns have missing values, how many they have, and the proportion (JAROME)
def find_missing_ingredients(data):
    """For each column with missing values, this function will create a reference list of row indices, 
    sum the number and calculate proportion of missing values 

    Parameters
    -----------
    data: pandas.core.frame.DataFrame
        A dataframe that need to be processed

    Returns
    -----------
    pandas.core.frame.DataFrame
        Data frame summarizing the indexes, count and proportion of missing values in each column

    """
    assert type(data) == pd.core.frame.DataFrame, "Input path should be a pandas data frame"

    assert data.shape[0] >= 1, "The input data frame has no rows"
    
    if np.sum(np.sum(data.isna(), axis=0)) == 0:
        print("There are no missing values")
        
    
    else:
        report = pd.DataFrame({'NaN count': np.sum(data.isna(),axis=0), 
                               'NaN proportion': np.sum(data.isna(),axis=0)/data.shape[0]}).reset_index()

        report['NaN proportion'] = pd.Series(["{0:.1f}%".format(val*100) for val in report['NaN proportion']])
        report = report.rename(columns={"index": 'Column name'})

        return report    

    


    


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


# Apply preprocessing (SAM)
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
