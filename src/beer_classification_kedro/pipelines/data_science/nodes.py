"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.3
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

def train_model(data: pd.DataFrame):
    '''
    This function allows to train the model of the beer classification
    '''
    X, y = get_x_and_y(data)

    
    model = RandomForestClassifier(n_estimators=100)

    mlflow.set_experiment('beer classification')
    mlflow.set_tag("mlflow.runName", model.__class__.__name__)

    model.fit(X, y.values.ravel())
    return model


def get_x_and_y(data: pd.DataFrame):
    '''
    This function allows to get easier the x and y values of the data
    ''' 
    label = {'Style'}
    columns_set = set(data.columns.values)
    X = data[list(columns_set-label)]
    y = data[list(label)]
    return X, y