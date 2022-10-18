"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.18.3
"""
import pandas as pd


def get_data_from_url(parameters) -> pd.DataFrame:
    '''
    This function allows to get the dataset from the github url
    '''
    return pd.read_csv(parameters['url'])
