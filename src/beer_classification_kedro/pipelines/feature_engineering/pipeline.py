"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.3
"""

from beer_classification_kedro.pipelines.feature_engineering.nodes import resample_classes
from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=resample_classes,
             inputs="data_clean",
             outputs="data_balanced",
             name="balance_classes")
    ])
