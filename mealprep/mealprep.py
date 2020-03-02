##Finding numeric and categorical variable names (HUAYUE LUKE)
import numpy as np
import pandas as pd

def find_fruits_veg(df, type_of_out = 'categ'):
    '''
    This function will drop row with NAs and find the index of columns with all
    numeric value or categorical value based on the specification.
    
    Parameters
    -----------
    df: pandas.core.frame.DataFrame
        Data frame that need to be proceed
    type_of_out: string
        Type of columns that we want to know index of
    list_of_index: list
        list of index value
   
    Returns
    -------
    list_of_categ: list
        list of index of categorical value
    list_of_num: list
        list of index of numerical value
    
    Example
    --------
    >>> df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    >>> find_fruits_veg(df, type_of_out = 'categ')
    [1]
    '''
    list_of_categ = []
    list_of_num = []
    df_clean = df.dropna()
    if df_clean.shape[0] == 0:
        return "It is a empty data frame or too many missing data"
    for i in np.arange(df_clean.shape[1]):
        if type(df_clean.iloc[0,i]) == str:
            list_of_categ += [i]
        elif type(df_clean.iloc[0,i]) != str:
            list_of_num += [i]
    if type_of_out== 'categ':
        return list_of_categ
    elif type_of_out== 'num':
        return list_of_num
    

##Identifying which columns have missing values, how many they have, and the proportion (JAROME)
def find_missing_ingredients(data):
    """For each column with missing values, this function will create a reference list of row indices, 
    sum the number and calculate proportion of missing values 

    Parameters
    -----------
    data: pandas.core.frame.DataFrame
        A dataframe that need to be processed

    Returns
    -------
    pandas.core.frame.DataFrame
        Data frame summarizing the indexes, count and proportion of missing values in each column

    """
    return None    


##Outlier checking (ANNY)
def find_bad_apples(df):
    '''
    This function uses a univariate approach to outlier detection.
    For each column with outliers (values that are 3 or more standard deviations from the mean), this function will create a reference list of row indices with outliers, and the total number of outliers in that column.

    Note: This function works best for small datasets with unimodal variable distributions.
    
    Parameters
    -----------
    df : pandas.DataFrame
        A dataframe containing numeric data
    
    Returns
    -------
    bad_apples : pandas.DataFrame
        A dataframe showing 3 columns:
        Variable (column name),
        Indices (list of row indices with outliers), and
        Total Outliers (number of outliers in the column)
    
    Example
    --------
    >>> data = pd.DataFrame({'A' : [1, 1, 1, 1, 1], 'B' : [10000, 1, 1, 1, 1, 1]}
    >>> df = pd.DataFrame(data)
    >>> find_bad_apples(df)
    Variable  Indices  Total Outliers
       B        0            1
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
    
    Example
    --------
    >>> from sklearn.datasets import load_iris
    >>> from mealprep.mealprep import make recipe
    >>> make_recipe(iris, "ohe_and_standard_scaler")       
    """
    return None
