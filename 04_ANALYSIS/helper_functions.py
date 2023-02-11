"""
Helper functions module

Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com

This script contains various helper functions that can be used to perform common tasks and operations in data analysis.
Functions include:

- dataframe_structure: Returns various attributes associated with the dataframe in the form of a dictionary
- dict_to_table: Generate a pretty looking structure of the output
- datatype_details: Prints the details of the datatype available in the dataframe
- describe_object_fields: Generates descriptive statistics results for the object datatype fields.
"""

import pandas as pd
from tabulate import tabulate


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
        
        
def describe_object_fields(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function generates descriptive statistics results for the object datatype fields.
    The column details that the function outputs are as follows:
        - count: count of non-null values
        - unique_values: count of unique values
        - longest_value: The long (length) value in the data
        - average_length_value: The average length value in the data
        - shortest_value: The short (length) value in the data
        - max_value_count: Number of values equal to maximum length value
        - min_value_count: Number of values equal to minimum length value
        
    Parameters:
    ----------
    df (pd.DataFrame): The input DataFrame for which details are to be extracted
    
    Returns:
    ----------
    pd.DataFrame: Pandas dataframe with details
    """
    object_field_stats = []

    for col in df.select_dtypes('object').columns:
        count = df[col].notnull().sum()
        unique_values = df[col].nunique()
        longest_value = df[col].str.len().max()
        average_length_value = df[col].str.len().mean()
        shortest_value = df[col].str.len().min()
        max_value_count = (df[col].str.len() == longest_value).sum()
        min_value_count = (df[col].str.len() == shortest_value).sum()

        summary_stats = {
            "column": col,
            "count": count,
            "unique_values": unique_values,
            "longest_values": longest_value,
            "average_length_value": average_length_value,
            "shortest_value": shortest_value,
            "max_value_count": max_value_count,
            "min_value_count": min_value_count
        }

        object_field_stats.append(summary_stats)
    
    return pd.DataFrame(object_field_stats).set_index('column')