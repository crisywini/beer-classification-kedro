"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.3
"""
import pandas as pd 
from sklearn.utils import resample

def resample_classes(data: pd.DataFrame) -> pd.DataFrame:
    '''
    This function allows to resample the classes with less than 100 elements on it
    '''
    count_df = data.groupby(['Style'])['Style'].count()

    styles_unbalanced = [k for k, v in count_df.items() if v <= 100]

    df_sampled = pd.DataFrame()
    for j in styles_unbalanced:

        df_minority_j = data[data.Style == j]
        df_minority_upsampled = resample(df_minority_j,
                                         replace=True,
                                         n_samples=400,
                                         stratify=df_minority_j,
                                         random_state=123)
        df_sampled = pd.concat([df_sampled, df_minority_upsampled])

    return df_sampled