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