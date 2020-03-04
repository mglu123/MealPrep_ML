##Finding numeric and categorical variable names (HUAYUE LUKE)
import numpy as np
import pandas as pd

def find_fruits_veg(df, type_of_out = 'categ'):
    '''
    This function will find the index of columns with all
    numeric value or categorical value based on the specification

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
    list_of_index: list
        list of index value
    
    Example
    --------
    >>>df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    >>>find_fruits_veg(df, type_of_out = 'categ')
    [1]

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
    -------
    pandas.core.frame.DataFrame
        Data frame summarizing the indexes, count and proportion of missing values in each column

    """
    return None    


##Outlier checking (ANNY)
def find_bad_apples(df):
    '''
    This function uses a univariate approach to outlier detection.
    For each column with outliers (values that are 2 or more standard deviations from the mean),
    this function will create a reference list of row indices with outliers, and
    the total number of outliers in that column.

    Note: This function works best for small datasets with unimodal variable distributions.
    Note: If your dataframe has duplicate column names, only the last of the duplicated columns will be checked.

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

    Examples
    --------
    >>> df = pd.DataFrame({'A' : ['test', 1, 1, 1, 1])
    >>> find_bad_apples(df)
    AssertionError: Every column in your dataframe must be numeric.

    >>> df = pd.DataFrame({'A' : [1, 1, 1, 1, 1],
    ...                    'B' : [10000, 1, 1, 1, 1]})
    >>> find_bad_apples(df)
    AssertionError: Sorry, you don't have enough data. The dataframe needs to have at least 30 rows.

    >>> df = pd.DataFrame({'A' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ...                    'B' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-100,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100],
    ...                    'C' : [1,1,1,1,1,19,1,1,1,1,1,1,1,1,19,1,1,1,1,1,1,1,1,1,1,1,19,1,1,1,1,1,1,1,1]})
    >>> find_bad_apples(df)
    Variable      Indices     Total Outliers
        B         [17, 34]          2
        C      [5, 14, 26]          3
        
    >>> df = pd.DataFrame({'A' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ...                    'B' : [1.000001, 1.000001, 1.000001, 1.000001, 1.000001, 1.000001, 1.000001, 1.000001,
    ...                           1.000001, 1.000001, 1.000001, 1.000001, 1.000001, 1.000001, 1.000001,
    ...                           1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]})
    >>> find_bad_apples(df))
    Variable                Indices     Total Outliers
    No outliers detected        []              0
    '''

    # Checks that every column in the dataframe is numeric
    assert df.select_dtypes(include=['float', 'int']).shape[1] == df.shape[1], 'Every column in your dataframe must be numeric.'

    # Checks that there are at least 30 rows in the dataframe
    assert df.shape[0] >= 30, 'Sorry, you don\'t have enough data. The dataframe needs to have at least 30 rows.'

    columns = list(df)

    # Initializes empty dataframe
    output = pd.DataFrame(columns = ['Variable', 'Indices', 'Total Outliers'])

    # Initializes column counter
    c = 0

    for column in columns:

        # Finds the mean and standard deviation values for the column
        mean = df.mean(axis = 0)[c]
        sd = np.std(df.iloc[:, c])

        # Initializes the column value (col), list of indices (ind), and total outliers (tot) values that will be output
        col = column
        ind = []
        tot = 0

        # Initializes the row counter
        r = 0

        values = df.values[:,c]
        for value in values:
            # If the value is between 2 standard deviations of the column mean, move on to the next value
            if ((mean - 2*sd) <= value <= (mean + 2*sd)) == True:
                r += 1
            # If the value is not between 2 standard deviations of the column mean, add the value index to the indices list, and add 1 to the total
            elif ((mean - 2*sd) <= value <= (mean + 2*sd)) == False:
                ind.append(r)
                tot += 1
                r += 1
        c += 1
        
        # If the column has outlier values (values more than 2 standard deviations from the column mean), append it to the output; otherwise, move on to the next column
        if tot == 0:
            continue
        else:
            output = output.append({'Variable' : col, 'Indices' : ind, 'Total Outliers' : tot}, ignore_index = True)

    if len(output) == 0:
        output = output.append({'Variable' : 'No outliers detected', 'Indices' : 'x', 'Total Outliers' : tot}, ignore_index = True)
        return output
    else:
        return output


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
