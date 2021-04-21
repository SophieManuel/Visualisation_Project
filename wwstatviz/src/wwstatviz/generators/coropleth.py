"""
Coropleth map generator.
"""

from .generator import Generator
import plotly.graph_objects as go

class CoroplethGenerator(Generator):
    
    def __init__(self, data, feature, countries = 'all'):
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
        # feature
        if not isinstance(feature, str):
            raise ValueError('invalid feature argument')
        if feature not in data.columns.tolist():
            raise ValueError('invalid feature argument')
        self._feature = feature
        self._countries = countries

    def generate(self):
        ### get data
        if self._countries == 'all':
            idx = self._data.index.tolist()
        else:
            idx = self._countries
        df = self._data.loc[idx, self._feature]
        ### coropleth using plotly
        # https://plotly.com/python/choropleth-maps/
        fig = go.Figure(
            data = go.Choropleth(
                locations = df.index.tolist(),
                z = df.values,
                colorscale = 'Blues',
                autocolorscale = False,
                reversescale = True,
                marker_line_color = 'darkgray',
                marker_line_width = 0.5,
            )
        )
        self._figure = fig
        return self._figure
