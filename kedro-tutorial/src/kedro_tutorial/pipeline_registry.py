"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from sklearn.metrics import plot_confusion_matrix

from kedro_tutorial.pipelines import data_processing as dp
from kedro_tutorial.pipelines import data_science as ds
from kedro_tutorial.pipelines import plots as pl
def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.

    Returns:
    A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    plots_pipeline=pl.create_pipeline()

    return {
        "__default__": data_processing_pipeline + data_science_pipeline + plots_pipeline,
        "dp": data_processing_pipeline,
        "ds":data_science_pipeline,
        "pl":plots_pipeline,
    }