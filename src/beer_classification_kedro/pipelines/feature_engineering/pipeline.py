"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.3
"""

from beer_classification_kedro.pipelines.feature_engineering.nodes import create_dummies_variables, encode_label, resample_classes
from kedro.pipeline import Pipeline, node, pipeline

     
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=create_dummies_variables,
             inputs="data_clean",
             outputs="data_dummies",
             name="dummies_categoric"),
        node(func=encode_label,
             inputs="data_dummies",
             outputs="data_labeled",
             name="encode_classes"),
        node(func=resample_classes,
             inputs="data_labeled",
             outputs="data_balanced",
             name="balance_classes")
    ])
