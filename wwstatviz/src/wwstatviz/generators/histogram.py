"""
Histogram plot generator.
"""

from .generator import Generator

class HistogramGenerator(Generator):

    def __init__(self, data, countries='all', features='all', legend=False):
        super().__init__(data)
        self._countries = countries
        self._features = features
        self._legend = legend
