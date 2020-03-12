mealprep
================

![](https://github.com/mglu123/mealprep/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/mglu123/foocat/branch/master/graph/badge.svg)](https://codecov.io/gh/mglu123/mealprep)
![Release](https://github.com/mglu123/mealprep/workflows/Release/badge.svg)

[![Documentation
Status](https://readthedocs.org/projects/mealprep/badge/?version=latest)](https://mealprep.readthedocs.io/en/latest/?badge=latest)

Mealprep offers a toolkit, made with care, to help users save time in
the data preprocessing kitchen.

## Overview

Recognizing that the preparation step of a data science project often
requires the most time and effort, `mealprep` aims to help data science
chefs of all specialties master their recipes of analysis. This package
tackles pesky tasks such as classifying columns as categorical or
numeric ingredients, straining NA values and outliers, and automating a
preprocessing recipe pipeline.

## Functions

`find_fruits_veg()`: This function will drop rows with NAs and find the
index of columns with all numeric value or categorical value based on
the specification.

`find_missing_ingredients()`: For each column with missing values, this
function will create a reference list of row indices, sum the number,
and calculate the proportion of missing values.

`find_bad_apples()`: This function uses a univariate approach to outlier
detection. For each column with outliers (values that are 2 or more
standard deviations from the mean), this function will create a
reference list of row indices with outliers, and the total number of
outliers in that column.

`make_recipe()`: This function is used to quickly apply common data
preprocessing techniques.

## Mealprep and Python’s Ecosystem

**mealprep** complements many of the existing packages in the Python
ecosystem around the theme of data preprocessing. When preparing a
dataframe for a machine learning preprocessing pipeline, it is time
consuming to manually note which columns are categorical and numerical,
particularly for large datasets. The
[pandas](https://pypi.org/project/pandas/) function `df.select_dtypes()`
comes close by allowing users to select columns with data corresponding
to specific data types however the output of this function is a pandas
dataframe. `find_fruits_veg()` aims to fill this void by producing a
list of columns corresponding to the categorical and numerical groups.

In terms of missing values, [pandas](https://pypi.org/project/pandas/)
package’s `isna()` function converts all elements of a pandas.dataframe
or pandas.series to boolean values representing if they are missing
values. The package
[autoimpute](https://autoimpute.readthedocs.io/en/latest/) provides a
suite of tools to fill missing values in a dataset through multiple
univariate, multivariate and time series methods. The gap between these
packages is that neither provides you a summary of the missing values
including the list of indices where they occur.
`find_missing_ingredients()` augments these tools by providing a summary
dataframe detailing which columns have missing values, as well as their
count and proportion.

The [pandas](https://pypi.org/project/pandas/) package’s `describe()`
function is a staple in the data wrangling process because it returns
several summary statistics for each numeric column in a dataframe, such
as the mean, standard deviation, minimum, and maximum. Viewing these
statistics together is helpful for detecting outliers. However, the
output of this function does not tell you which rows of data these
outliers are found in, or how many outliers are present in the
dataframe. Packages like the
[PyOD](https://pyod.readthedocs.io/en/latest/) toolkit and other
functions that use clustering methods consider all variables at once to
detect outliers for multivariate data.
[PyOD](https://pyod.readthedocs.io/en/latest/) provides over 20
algorithms to select from in detecting these outliers, which is handy
for large multivariate datasets where you know you want to consider all
features in detecting outliers, but can be a bit extreme for initial
data exploration. The **mealprep** `find_bad_apples()` function lives
happily in the space between [pandas](https://pypi.org/project/pandas/)
and [PyOD](https://pyod.readthedocs.io/en/latest/)-type solutions for
outlier detection, where it provides more information than the
[pandas](https://pypi.org/project/pandas/) `describe()` function to
point out datapoints which need further investigation, but does not
consider all variables at once like the
[PyOD](https://pyod.readthedocs.io/en/latest/)-type functions do.

Lastly, there are many great tools in the data science ecosystem for
pre-processing data such as [scikit-learn
preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
in Python. However, you may find yourself frequently writing the same
lengthy code for common preprocessing tasks (e.g scale numeric features
and one hot encode categorical features). `preprocess_recipe()` provides
a *shortcut function* to apply your favourite recipes quickly to
preprocess data in one line of code.

## Installation:

    pip install -i https://test.pypi.org/simple/ mealprep

## Examples

### `find_bad_apples()`

First, load the required packages.

``` python
from mealprep import mealprep
import pandas as pd
```

If you don’t already have a dataframe to work with, run this code to set
up a toy dataframe (`df`) for testing.

``` python
df = pd.DataFrame({'A' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    'B' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-100,
                             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100],
                    'C' : [1,1,1,1,1,19,1,1,1,1,1,1,1,1,19,1,1,1,1,
                             1,1,1,1,1,1,1,19,1,1,1,1,1,1,1,1]})
df
```

    ##     A    B   C
    ## 0   1    1   1
    ## 1   1    1   1
    ## 2   1    1   1
    ## 3   1    1   1
    ## 4   1    1   1
    ## 5   1    1  19
    ## 6   1    1   1
    ## 7   1    1   1
    ## 8   1    1   1
    ## 9   1    1   1
    ## 10  1    1   1
    ## 11  1    1   1
    ## 12  1    1   1
    ## 13  1    1   1
    ## 14  1    1  19
    ## 15  1    1   1
    ## 16  1    1   1
    ## 17  1 -100   1
    ## 18  1    1   1
    ## 19  1    1   1
    ## 20  1    1   1
    ## 21  1    1   1
    ## 22  1    1   1
    ## 23  1    1   1
    ## 24  1    1   1
    ## 25  1    1   1
    ## 26  1    1  19
    ## 27  1    1   1
    ## 28  1    1   1
    ## 29  1    1   1
    ## 30  1    1   1
    ## 31  1    1   1
    ## 32  1    1   1
    ## 33  1    1   1
    ## 34  1  100   1

To find the outliers in the dataframe, run
`mealprep.find_bad_apples(df)` and you’ll get a dataframe that shows
which columns have outliers, which rows they can be found in, and how
many outliers are in those columns.

``` python
mealprep.find_bad_apples(df)
```

    ##   Variable      Indices Total Outliers
    ## 0        B     [17, 34]              2
    ## 1        C  [5, 14, 26]              3

### `find_fruits_veg()`

find\_fruits\_veg() will help you find the column indices for either
numerical or categorical variables in your data frame. The example below
shows how to use find\_fruits\_veg() to find the categorical columns’
index of a toy data frame.

First, load the required packages.

``` python
>>> from mealprep import mealprep
>>> import pandas as pd
```

Then, apply the find\_fruits\_veg() function to the data frame.

``` python
>>> df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
>>> find_fruits_veg(df, type_of_out = 'categ')
# [1]
```

### `find_missing_ingredients()`

### `make_recipe()`

Do you find yourself constantly applying the same data preprocessing
techniques time and time again? `make_recipe` can help by applying your
favourite preprocessing recipes in only a few lines of code.

Below `make_recipe` applies the following common recipe in only one line
of code:

1.  Split data into training, validation, and testing
2.  Standardise and scale numeric features
3.  One hot encode categorical features

First, load the required packages.

``` python
>>> from mealprep import mealprep
>>> import pandas as pd
>>> import numpy as np
>>> from vega_datasets import data
```

Then load the classic `mtcars` data set.

``` python
>>> df = pd.read_json(data.cars.url).drop(columns=["Year"])
>>> X = df.drop(columns=["Name"])
>>> y = df[["Name"]
    
>>> df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 406 entries, 0 to 405
# Data columns (total 8 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   Name              406 non-null    object 
#  1   Miles_per_Gallon  398 non-null    float64
#  2   Cylinders         406 non-null    int64  
#  3   Displacement      406 non-null    float64
#  4   Horsepower        400 non-null    float64
#  5   Weight_in_lbs     406 non-null    int64  
#  6   Acceleration      406 non-null    float64
#  7   Origin            406 non-null    object 
# dtypes: float64(4), int64(2), object(2)
# memory usage: 25.5+ KB
```

Use `make_recipe` to quickly apply split your data and apply your
favourite preprocessing techniques\!

``` python
>>> X_train, X_valid, X_test, y_train, y_valid, y_test = mealprep.make_recipe(
...    X=X, y=y, recipe="ohe_and_standard_scaler", 
...    splits_to_return="train_test"
... )

>>> X_train.head()
#    Miles_per_Gallon  Cylinders  Displacement  Horsepower  Weight_in_lbs  Acceleration  x0_Europe  x0_Japan  x0_USA
# 0         -1.524901   1.457871      1.722121    1.775523       2.315653     -1.285191        0.0       0.0     1.0
# 1         -0.287181   0.327847      0.395050   -0.307445       0.248186      0.643767        0.0       0.0     1.0
# 2         -0.699754  -1.367190     -1.028694   -0.145436      -0.586540     -0.652746        0.0       1.0     0.0
# 3          0.573330  -0.802178     -0.466227   -0.307445      -0.165307     -0.020301        0.0       1.0     0.0
# 4         -0.228241  -0.802178     -0.589266   -0.145436      -0.391955     -0.336523        0.0       1.0     0.0
```

### Documentation

The official documentation is hosted on Read the Docs:
<https://mealprep.readthedocs.io/en/latest/>

### Credits

This package was created with Cookiecutter and the
UBC-MDS/cookiecutter-ubc-mds project template, modified from the
[pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci)
project template and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
