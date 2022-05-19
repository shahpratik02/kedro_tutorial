"""
This is a boilerplate pipeline 'plots'
generated using Kedro 0.18.1
"""
import plotly.express as px
import pandas as pd
from kedro.extras.datasets.plotly import JSONDataSet

def compare_pred_test_plot(y_pred:pd.DataFrame):
    fig = px.line(y=[y_pred.y_pred,y_pred.y_test])
    
    return fig