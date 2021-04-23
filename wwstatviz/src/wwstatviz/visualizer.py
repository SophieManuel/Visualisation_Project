"""
This module contains the Visualizer class, which is the main class for
generating plots.
"""

from pathlib import Path
from .figure import Figure
from .generators import HeatmapGenerator, CoroplethGenerator, LineGenerator, HistogramGenerator
from .io import CSVReader


class Visualizer(object):

    def __init__(self, data_path):
        """
        This the class contructor.

        Parameters
        ----------
        data_path : str
            The path to the CSV file containing data.
            The CSV file must have as an index column the 2-digit or 3-digit
            ISO country codes.

        Returns
        -------
        An instance (object) of the class Visualizer
        """
        self._data_path = data_path
        path = Path(data_path).absolute()
        if path.suffix == '.csv':
            reader = CSVReader(input_file=data_path)
        else:
            raise ValueError('unknown data format')
        self._data = reader.read()

    def heatmap(self, countries='all', features='all',
                method='pearson', mask=True, 
                title='', xlabel='', ylabel=''):
        """
        Construct a heatmap. Rows and columns of the heatmap represent the
        countries, and the coordinate (i, j) is represent the correlation
        between features of countries i and j.

        Parameters
        ----------
        countries : str or array_like
            List of country codes.
            If passed value is 'all', then include all countries.
        features : str or array_like
            List of features to consider.
            If passed value is 'all', then include all countries.
        method : str
            Correlation method to use. Supported correlation methods are:
            'pearson', 'spearman' and 'kendall'.
        mask : bool
            Hide the the upper triangular part of the correlation matrix.
            To be used in the case of symmetric correlation matrix.
            Default: False
        title : str
            Heatmap title
        xlabel : str
            Heatmap x-coordinate label
        ylabel : str
            Heatmap y-coordinate label

        Returns
        -------
        figure : Figure
            A figure object containing the generated heatmap.
        """
        fig = Figure()
        generator = HeatmapGenerator(self._data, countries, features,
                                     method, mask)
        fig.figure = generator.generate()
        fig.annotate(title=title, xlabel=xlabel, ylabel=ylabel)
        return fig

    def coropleth(self, feature, countries='all', title=''):
        """
        Generate a coropleth map.

        Parameters
        ----------
        countries : str or array_like
            List of country codes.
            If passed value is 'all', then include all countries.
        feature : str
            The name of the feature to show in the map.
        title : str
            Coropleth title.

        Returns
        -------
        figure : Figure
            A figure object containing the generated coropleth.
        """
        fig = Figure()
        generator = CoroplethGenerator(self._data, feature, countries)
        fig.figure = generator.generate()
        fig.annotate(title = title)
        return fig

    def line(self, countries='all', features='all',
             title='', xlabel='', ylabel='', legend=False):
        """
        Generate a line plot (e.g. for time series visualization).

        Parameters
        ----------
        countries : str or array_like
            List of country codes.
            If passed value is 'all', then include all countries.
        features : str or array_like
            List of features to consider.
            If passed value is 'all', then include all countries.
        title : str
            Line plot title
        xlabel : str
            Line plot x-coordinate label
        ylabel : str
            Line plot y-coordinate label
        legend : bool
            Whether or not to generate a legend for each line.
            Default value: False

        Returns
        -------
        figure : Figure
            A figure object containing the generated line plot.
        """
        fig = Figure()
        generator = LineGenerator(self._data, countries, features, legend)
        fig.figure = generator.generate()
        fig.annotate(title=title, xlabel=xlabel, ylabel=ylabel)
        return fig

    def histogram(self, countries='all', features='all',
                  title='', xlabel='', ylabel='', legend=False):
        """
        Generate a histogram plot.

        Parameters
        ----------
        countries : str or array_like
            List of country codes.
            If passed value is 'all', then include all countries.
        features : str or array_like
            List of features to consider.
            If passed value is 'all', then include all countries.
        title : str
            Histogram plot title
        xlabel : str
            Histogram plot x-coordinate label
        ylabel : str
            Histogram plot y-coordinate label
        legend : bool
            Whether or not to generate a legend for each histogram.
            Default value: False

        Returns
        -------
        figure : Figure
            A figure object containing the generated histogram plot.
        """
        fig = Figure()
        generator = HistogramGenerator(self._data, countries, features, legend)
        fig.figure = generator.generate()
        fig.annotate(title=title, xlabel=xlabel, ylabel=label)
        return fig
