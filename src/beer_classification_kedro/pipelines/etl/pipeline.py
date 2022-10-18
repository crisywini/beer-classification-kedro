"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.18.3
"""

from beer_classification_kedro.pipelines.etl.nodes import get_data_from_url
from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=get_data_from_url,
             inputs="parameters",
             outputs="data_raw",
             name="process_data")
    ])
