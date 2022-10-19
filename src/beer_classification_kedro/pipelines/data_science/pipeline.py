"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.3
"""

from beer_classification_kedro.pipelines.data_science.nodes import train_model
from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=train_model,
             inputs="data_balanced",
             outputs="model_trained",
             name="train_model")
    ])
