from wwstatviz import Visualizer
import plotly
from pathlib import Path


def test_choropleth():
    v = Visualizer('data/test_cc_3d.csv')
    fig = v.choropleth(feature='f1', countries='all',
                       title='This is a test choropleth')
    assert fig.figure is not None
    assert isinstance(fig.figure, plotly.graph_objs.Figure)
    fig.save('test_choropleth.pdf')
    assert Path('test_choropleth.pdf').is_file()
