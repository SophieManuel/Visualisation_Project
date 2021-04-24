from wwstatviz import Visualizer
import matplotlib
from pathlib import Path


def test_histogram_plot():
    v = Visualizer('data/test_cc_3d.csv')
    fig = v.histogram(title='This is a test of line plot',
                      xlabel='Label of x axis',
                      ylabel='Label of y axis',
                      legend=True)
    assert fig.figure is not None
    assert isinstance(fig.figure, matplotlib.figure.Figure)
    fig.save('test_histogram.png')
    assert Path('test_histogram.png').is_file()
