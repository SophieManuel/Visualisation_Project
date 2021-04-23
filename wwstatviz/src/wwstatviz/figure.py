"""
This module contains the Figure class returned by the Visualizer methods
(heatmap, coropleth, etc.).
"""

import matplotlib
import plotly
import matplotlib.pyplot as plt


class Figure(object):

    def __init__(self):
        self.figure = None
        self._title = None
        self._xlabel = None
        self._ylabel = None

    def show(self):
        """
        Displays figure inline (to be used in web browsers for example).
        """
        if isinstance(self.figure, matplotlib.figure.Figure):
            self.figure.show()
        if isinstance(self.figure, plotly.graph_objs.Figure):
            self.figure.show()

    def save(self, output_path):
        """
        Save the figure to a file. The format is inferred from the file
        extension.

        Parameters
        ----------
        output_path : str
            Path where to save the figure.
        """
        if isinstance(self.figure, matplotlib.figure.Figure):
            self.figure.tight_layout()
            self.figure.savefig(output_path)
        if isinstance(self.figure, plotly.graph_objs.Figure):
            self.figure.write_image(file=output_path)

    def annotate(self, title='', xlabel='', ylabel=''):
        # check args
        for arg in [title, xlabel, ylabel]:
            if not isinstance(arg, str):
                raise ValueError(f'invalid argument {arg}')
        self._title = title
        self._xlabel = xlabel
        self._ylabel = ylabel
        if isinstance(self.figure, matplotlib.figure.Figure):
            self.figure.suptitle(title)
            self.figure.supxlabel(xlabel)
            self.figure.supylabel(ylabel)
