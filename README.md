# Mealprep 

![](https://github.com/mglu123/mealprep/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/mglu123/foocat/branch/master/graph/badge.svg)](https://codecov.io/gh/mglu123/mealprep) ![Release](https://github.com/mglu123/mealprep/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/mealprep/badge/?version=latest)](https://mealprep.readthedocs.io/en/latest/?badge=latest)

Mealprep offers a toolkit, made with care, to help users save time in the data preprocessing kitchen.

## Overview

Recognizing that the preparation step of a data science project often requires the most time and effort, `mealprep` aims to help data science chefs of all specialties master their recipes of analysis. This package tackles pesky tasks such as classifying columns as categorical or numeric ingredients, straining NA values and outliers, and automating a preprocessing recipe pipeline.

### Functions
Function 1)`peel_columns()`: determine numeric and categorical variable names from an input dataset
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

```

Function 2)`strain_nas()`: identify columns with missing values, their frequency and proportion
```
ENTER DOC STRING
```

Function 3)`strain_outliers()`: identify columns with outliers, their frequency and proportion
```
ENTER DOC STRING
```

Function 4)`preprocess_recipe()`: quickly apply your favourite data preprocessing recipes in one line of code.
```
ENTER DOC STRING
```

### Mealprep and Python's Ecosystem

There are many great tools in the data science ecosystem for pre-processing data:

- [scikit-learn preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html) (python)


### Python Dependencies

- TODO


### Installation:

```
pip install -i https://test.pypi.org/simple/ mealprep
```

### Usage

- TODO

### Documentation
The official documentation is hosted on Read the Docs: <https://mealprep.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
