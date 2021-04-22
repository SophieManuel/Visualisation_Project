from wwstatviz import Visualizer
import matplotlib
from pathlib import Path

def test_line_plot():
    v = Visualizer('/workspace/data/test_cc_3d.csv')
    fig = v.line(title = 'This is a test of line plot',
                 xlabel = 'Label of x axis', 
                 ylabel = 'Label of y axis', 
                 legend = True)
    assert fig.figure is not None
    assert isinstance(fig.figure, matplotlib.figure.Figure)
    fig.save('test_line_plot.png')
    assert Path('test_line_plot.png').is_file()
