"""
This is a boilerplate pipeline 'plots'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import compare_pred_test_plot


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=compare_pred_test_plot,
                inputs="y_pred",
                outputs="compare_pred_test_plot",
            ),
        ])
