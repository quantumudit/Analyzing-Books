"""
Helper functions module

Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com

This script contains various helper functions that can be used to perform common tasks and operations in data analysis.
Functions include:

- dataframe_structure: Returns various attributes associated with the dataframe in the form of a dictionary
- dict_to_table: Generate a pretty looking structure of the output
- datatype_details: Prints the details of the datatype available in the dataframe
"""

# imports
import pandas as pd
from tabulate import tabulate

### ========== Functions ========== ### 

def dataframe_structure(dataframe: pd.DataFrame) -> dict:
    """
    This function takes in a Pandas DataFrame as an input and returns a dictionary containing details about the structure of the dataframe.
    The returned dictionary includes information such as the number of dimensions, shape, row and column count, total and non-null datapoints,
    total memory usage, and average memory usage of the dataframe.

    Parameters:
    ----------
    dataframe (pd.DataFrame): The input DataFrame for which structure details are to be extracted

    Returns:
    ----------
    dict: A dictionary containing the structure details of the input DataFrame

    """
    structure_details = {
        "Dimensions": dataframe.ndim,
        "Shape": dataframe.shape,
        "Row Count": len(dataframe),
        "Column Count": len(dataframe.columns),
        "Total Datapoints": dataframe.size,
        "Null Datapoints": dataframe.isnull().sum().sum(),
        "Non-Null Datapoints": dataframe.notnull().sum().sum(),
        "Total Memory Usage": dataframe.memory_usage(deep=True).sum(),
        "Average Memory Usage": dataframe.memory_usage(deep=True).mean().round()
    }
    
    return structure_details


def dict_to_table(input_dict:dict, column_headers:list):
    """
    This function creates a tabular view of the dictionary results
    
    Parameters:
    ----------
    input_dict (dict): The input dictionary to be pretty printed
    column_headers (list): The list of column headers as a list 
    
    Returns:
    ----------
    tabulate object: unicode tabular structure of the dataframe
    """
    table_vw = tabulate(input_dict.items(),
                        headers=column_headers, 
                        tablefmt="pretty",
                        stralign='left')

    return table_vw


def datatype_details(df: pd.DataFrame) -> None:
    """
    This function prints the field count with distinct datatypes
    
    Parameters:
    ----------
    df (pd.DataFrame): The input DataFrame for which details are to be extracted
    """
    available_dtypes = list(set([str(dt) for dt in df.dtypes]))
    for dt in available_dtypes:
        field_count = df.select_dtypes(dt).dtypes.count()
        print(f"There are {field_count} fields with {dt} datatype")
        