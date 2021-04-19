from pathlib import Path
from .figure import Figure
from .generators import HeatmapGenerator, CoroplethGenerator
from .io import CSVReader

class Visualizer(object):

    def __init__(self, data_path):
        self._data_path = data_path
        path = Path(data_path).absolute()
        if path.suffix == '.csv':
            reader = CSVReader()
        else:
            raise ValueError('unknown data format')
        self._data = reader.read()

    def heatmap(self, countries = 'all', features = 'all', 
                method = 'pearson', mask = True):
        fig = Figure()
        generator = HeatmapGenerator(self._data, countries, features, method, mask)
        fig.figure = generator.generate()
        return fig

    def map(self, feature, countries = 'all'):
        fig = Figure()
        generator = CoroplethGenerator(self._data, feature, countries)
        fig.figure = generator.generate()
        return fig
