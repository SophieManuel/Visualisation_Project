from wwstatviz import Visualizer
import matplotlib
from pathlib import Path


def test_heatmap():
    v = Visualizer('data/test_cc_3d.csv')
    fig = v.heatmap(title='This is a test heatmap',
                    xlabel='Countries', ylabel='Countries')
    assert fig.figure is not None
    assert isinstance(fig.figure, matplotlib.figure.Figure)
    fig.save('test_heatmap.png')
    assert Path('test_heatmap.png').is_file()
