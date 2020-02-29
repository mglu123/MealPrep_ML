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

Returns
-------
    list_of_index: list
        list of index value

Example
--------
>>>df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
>>>find_fruits_veg(df, type_of_out = 'categ')
[1]

```

Function 2)`find_missing_ingredients()`: identify columns with missing values, their frequency and proportion
```
For each column with missing values, this function will create a reference list of row indices, 
sum the number and calculate proportion of missing values 

Parameters
-----------
data: pandas.core.frame.DataFrame
    A data frame that need to be processed

Returns
-------
pandas.core.frame.DataFrame
    Data frame summarizing the indexes, count and proportion of missing values in each column

    
```

Function 3)`find_bad_apples()`: identify columns with outliers, their frequency of outliers
```
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

**mealprep** complements many of the existing packages in the Python ecosystem around the theme of data preprocessing. When preparing a dataframe for a machine learning preprocessing pipeline, it is time consuming to manually note which columns are categorical and numerical, particularly for large datasets. The [pandas](https://pypi.org/project/pandas/) function `df.select_dtypes()` comes close by allowing users to select columns with data corresponding to specific data types however the output of this function is a pandas dataframe. `find_fruits_veg()` aims to fill this void by producing a list of columns corresponding to the categorical and numerical groups.  

In terms of missing values, [pandas](https://pypi.org/project/pandas/) package’s `isna()` function converts all elements of a pandas.dataframe or pandas.series to boolean values representing if they are missing values. The package [autoimpute](https://autoimpute.readthedocs.io/en/latest/) provides a suite of tools to fill missing values in a dataset through multiple univariate, multivariate and time series methods. The gap between these packages is that neither provides you a summary of the missing values including the list of indices where they occur. `find_missing_ingredients()` augments these tools by providing a summary dataframe detailing which columns have missing values, as well as their count and proportion.

The [pandas](https://pypi.org/project/pandas/) package’s `describe()` function is a staple in the data wrangling process because it returns several summary statistics for each numeric column in a dataframe, such as the mean, standard deviation, minimum, and maximum. Viewing these statistics together is helpful for detecting outliers. However, the output of this function does not tell you which rows of data these outliers are found in, or how many outliers are present in the dataframe. Packages like the [PyOD](https://pyod.readthedocs.io/en/latest/) toolkit and other functions that use clustering methods consider all variables at once to detect outliers for multivariate data. [PyOD](https://pyod.readthedocs.io/en/latest/) provides over 20 algorithms to select from in detecting these outliers, which is handy for large multivariate datasets where you know you want to consider all features in detecting outliers, but can be a bit extreme for initial data exploration. The **mealprep** `find_bad_apples()` function lives happily in the space between [pandas](https://pypi.org/project/pandas/) and [PyOD](https://pyod.readthedocs.io/en/latest/)-type solutions for outlier detection, where it provides more information than the [pandas](https://pypi.org/project/pandas/) `describe()` function to point out datapoints which need further investigation, but does not consider all variables at once like the [PyOD](https://pyod.readthedocs.io/en/latest/)-type functions do.

Lastly, there are many great tools in the data science ecosystem for pre-processing data such as [scikit-learn preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html) in Python. However, you may find yourself frequently writing the same lengthy code for common preprocessing tasks (e.g scale numeric features and one hot encode categorical features). `preprocess_recipe()` provides a _shortcut function_ to apply your favourite recipes quickly to preprocess data in one line of code.




## Installation:

```
pip install -i https://test.pypi.org/simple/ mealprep
```



### Documentation
The official documentation is hosted on Read the Docs: <https://mealprep.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
