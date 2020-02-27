# Mealprep 

![](https://github.com/mglu123/mealprep/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/mglu123/foocat/branch/master/graph/badge.svg)](https://codecov.io/gh/mglu123/mealprep) ![Release](https://github.com/mglu123/mealprep/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/mealprep/badge/?version=latest)](https://mealprep.readthedocs.io/en/latest/?badge=latest)

Mealprep offers a toolkit, made with care, to help users save time in the data preprocessing kitchen.

## Overview

Recognizing that the preparation step of a data science project often requires the most time and effort, `mealprep` aims to help data science chefs of all specialties master their recipes of analysis. This package tackles pesky tasks such as classifying columns as categorical or numeric ingredients, straining NA values and outliers, and automating a preprocessing recipe pipeline.

## Functions
Function 1)`fruit_and_veg()`: determine numeric and categorical variable names from an input dataset
```
ENTER DOC STRING
```

Function 2)`missing_ingredients()`: identify columns with missing values, their frequency and proportion
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

Function 3)`bad_apples()`: identify columns with outliers, their frequency and proportion
```
ENTER DOC STRING
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
