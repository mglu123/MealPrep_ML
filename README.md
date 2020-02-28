# Mealprep 

![](https://github.com/mglu123/mealprep/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/mglu123/foocat/branch/master/graph/badge.svg)](https://codecov.io/gh/mglu123/mealprep) ![Release](https://github.com/mglu123/mealprep/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/mealprep/badge/?version=latest)](https://mealprep.readthedocs.io/en/latest/?badge=latest)

Mealprep offers a toolkit, made with care, to help users save time in the data preprocessing kitchen.

## Overview

Recognizing that the preparation step of a data science project often requires the most time and effort, `mealprep` aims to help data science chefs of all specialties master their recipes of analysis. This package tackles pesky tasks such as classifying columns as categorical or numeric ingredients, straining NA values and outliers, and automating a preprocessing recipe pipeline.

## Functions
Function 1)`find_fruits_veg()`: determine numeric and categorical variable names from an input dataset
```

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


```

Function 2)`find_missing_ingredients()`: identify columns with missing values, their frequency and proportion
```
For each column with missing values, this function will create a reference list of row indices, 
sum the number and calculate proportion of missing values 

Parameters
-----------
data: pandas.core.frame.DataFrame
    A dataframe that need to be processed

Returns
-----------
pandas.core.frame.DataFrame
    Data frame summarizing the indexes, count and proportion of missing values in each column

    
```

Function 3)`find_bad_apples()`: identify columns with outliers, their frequency and proportion
```
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

    
```

Function 4)`make_recipe()`: quickly apply your favourite data preprocessing recipes in one line of code.
```

The `make_recipe()` function is used to quickly apply common data preprocessing techniques
    
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

```

## Mealprep and Python's Ecosystem

There are many great tools in the data science ecosystem for pre-processing data:

- [scikit-learn preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html) (python)



## Installation:

```
pip install -i https://test.pypi.org/simple/ mealprep
```



### Documentation
The official documentation is hosted on Read the Docs: <https://mealprep.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
