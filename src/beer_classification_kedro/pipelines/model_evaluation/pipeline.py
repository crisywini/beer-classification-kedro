"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.3
"""

from beer_classification_kedro.pipelines.model_evaluation.nodes import evaluate_model
from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                func=evaluate_model,
                inputs=["model_trained",
                        "data_balanced"],
                outputs="cross_validation_score",
                name="model_evaluation"
            )
    ])
