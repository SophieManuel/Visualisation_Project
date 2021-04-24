"""
Choropleth map generator.
"""

from .generator import Generator
import plotly.graph_objects as go


class ChoroplethGenerator(Generator):

    def __init__(self, data, feature, countries='all', scale_feature=False):
        super().__init__(data)
        # checking arguments
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
        # scale_feature
        if not isinstance(scale_feature, bool):
            raise ValueError('invalid scale_feature argument')
        self._feature = feature
        self._countries = countries
        self._scale_feature = scale_feature

    def generate(self):
        # get data
        if self._countries == 'all':
            idx = self._data.index.tolist()
        else:
            idx = self._countries
        df = self._data.loc[idx, self._feature]
        if self._scale_feature:
            mini, maxi = df.min(), df.max()
            df = (df - mini) / maxi
            zmax, zmin = 1., 0.
        else:
            zmax, zmin = None, None
        # choropleth using plotly
        # https://plotly.com/python/choropleth-maps/
        fig = go.Figure(
            data=go.Choropleth(
                locations=df.index.tolist(),
                z=df.values,
                zmax=zmax,
                zmin=zmin,
                colorscale='hot',
                autocolorscale=False,
                reversescale=True,
                marker_line_color='darkgray',
                marker_line_width=0.5,
            )
        )
        self._figure = fig
        return self._figure
