"""
Histogram plot generator.
"""

from .generator import Generator

class HistogramGenerator(Generator):

    def __init__(self, data, countries='all', features='all', legend=False):
        super().__init__(data)
        ### checking arguments
        # countries
        if not isinstance(countries, str) and not isinstance(countries, list):
            raise ValueError('invalid countries argument')
        if isinstance(countries, str) and countries != 'all':
            raise ValueError('invalid countries argument')
        if isinstance(countries, list):
            for e in countries:
                if e not in self._data.index.tolist():
                    raise ValueError(f'encountred invalid country code: {e}')
        # features
        if not isinstance(features, str) and not isinstance(features, list):
            raise ValueError('invalid features argument')
        if isinstance(features, str) and features != 'all':
            raise ValueError('invalid features argument')
        if isinstance(features, list):
            for e in features:
                if e not in self._data.columns.tolist():
                    raise ValueError(f'encountred invalid feature name: {e}')
        # legend
        if not isinstance(legend, bool):
            raise ValueError('invalid argument legend')
        self._countries = countries
        self._features = features
        self._legend = legend

    def generate(self):
        # get data
        if self._countries == 'all':
            idx = self._data.index.tolist()
        else:
            idx = self._countries
        if self._features == 'all':
            cols = self._data.columns.tolist()
        else:
            cols = self._features
        df = self._data.loc[idx, cols]
	self._figure = self._histogram(df)
        return self._figure
