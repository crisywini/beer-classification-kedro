"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.3
"""
import logging
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import mlflow

logger = logging.getLogger(__name__)


def evaluate_model(model: RandomForestClassifier,  data: pd.DataFrame) -> str:

    X, y = get_x_and_y(data)

    k_fold = model_selection.KFold(n_splits=10)
    scoring = 'accuracy'
    score = (model_selection.cross_val_score(
        model, X, y.values.ravel(),  scoring=scoring, cv=k_fold))

    print(f"({score.mean()}, {score.std()})")
    mlflow.set_experiment('beer classification')
    mlflow.log_metric("accuracy with cross validation", score.mean())
    mlflow.log_metric("standard deviation of cross validation", score.std())

    return f"---Accuracy in cross validation---\n Mean: {score.mean()} Standard deviation: {score.std()}"


def get_x_and_y(data: pd.DataFrame):
    '''
    This function allows to get easier the x and y values of the data
    ''' 
    label = {'Style'}
    columns_set = set(data.columns.values)
    X = data[list(columns_set-label)]
    y = data[list(label)]
    return X, y