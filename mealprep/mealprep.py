##Finding numeric and categorical variable names (HUAYUE LUKE)
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import normalize, scale, Normalizer, StandardScaler, OneHotEncoder

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


def make_recipe(X, y, recipe, splits_to_return="train_test"):
    """The `make_recipe()` function is used to quickly apply common data preprocessing techniques
    
    Parameters
    ----------
    X : pandas.DataFrame
        A dataframe containing training, validation, and testing features
    y : pandas.DataFrame
        A dataframe containing training, validation, and testing response
    recipe : str
        A string specifying which recipe to apply to the data
    splits_to_return : str
        "train_test" to return train and test splits, "train_test_valid" to return train, test, and validation data, "train" to return all data without splits
    
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

    # validate inputs
    assert X.shape[0] == y.shape[0], "X and y should have the same number of observations."
    assert recipe in ["ohe_and_standard_scaler"], "Please select a valid string option for recipe."

    # clean input data
    y = y.to_numpy().ravel()
    
    # TODO: add parmeter for setting train, test, valid split size

    # split data
    if splits_to_return == "train_test":
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.8)
        X_valid = None
        y_valid = None
    elif splits_to_return == "train_test_valid":
        X_train_valid, X_test, y_train_valid, y_test = train_test_split(
            X, y, test_size=0.8)
        X_train, X_valid, y_train, y_valid = train_test_split(
            X_train_valid, y_train_valid, test_size=0.8)
    else:
        raise Exception("splits_to_return should be either 'train_test' or 'train_test_valid'.")        
    
    # determine column type
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    categorics = ['object']
    numeric_features = list(X_train.select_dtypes(include=numerics).columns)
    categorical_features = list(X_train.select_dtypes(include=categorics).columns)

    # preprocess data
    if recipe == "ohe_and_standard_scaler":
        numeric_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder()
    else:
        raise Exception("Please select a valid string option for recipe.")
        
    preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features)
            ]
        )
    
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)
    if splits_to_return == "train_test_valid":
        X_valid = preprocessor.transform(X_valid)
        
    # get column names back and convert back to a DataFrame
    categorical_features_transformed = preprocessor.transformers_[1][1].get_feature_names()
    features_transformed = list(numeric_features) + list(categorical_features_transformed)
    X_train = pd.DataFrame(data=X_train, columns=features_transformed)
    X_test = pd.DataFrame(data=X_test, columns=features_transformed)
    if splits_to_return == "train_test_valid":
        X_valid = pd.DataFrame(data=X_valid, columns=features_transformed)
    
    return (X_train, X_valid, X_test, y_train, y_valid, y_test)
