from wwstatviz import Visualizer
import plotly
from pathlib import Path

def test_coropleth():
    v = Visualizer('/workspace/data/test_cc_3d.csv')
    fig = v.coropleth(feature = 'f1', countries = 'all', 
                      title = 'This is a test heatmap')
    assert fig.figure is not None
    assert isinstance(fig.figure, plotly.graph_objs._figure.Figure)
    fig.save('test_coropleth.pdf')
    assert Path('test_coropleth.pdf').is_file()
