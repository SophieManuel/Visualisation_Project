from pathlib import Path
from .figure import Figure
from .generators import HeatmapGenerator, CoroplethGenerator, LineGenerator
from .io import CSVReader

class Visualizer(object):

    def __init__(self, data_path):
        self._data_path = data_path
        path = Path(data_path).absolute()
        if path.suffix == '.csv':
            reader = CSVReader(input_file = data_path)
        else:
            raise ValueError('unknown data format')
        self._data = reader.read()

    def heatmap(self, countries = 'all', features = 'all', 
                method = 'pearson', mask = True, 
                title = '', xlabel = '', ylabel = ''):
        fig = Figure()
        generator = HeatmapGenerator(self._data, countries, features, method, mask)
        fig.figure = generator.generate()
        fig.annotate(title = title, xlabel = xlabel, ylabel = ylabel)
        return fig

    def coropleth(self, feature, countries = 'all', 
                  title = '', xlabel = '', ylabel = ''):
        fig = Figure()
        generator = CoroplethGenerator(self._data, feature, countries)
        fig.figure = generator.generate()
        fig.annotate(title = title, xlabel = xlabel, ylabel = ylabel)
        return fig

    def line(self, countries = 'all', features = 'all', 
             title = '', xlabel = '', ylabel = '', legend = False):
        fig = Figure()
        generator = LineGenerator(self._data, countries, features, legend)
        fig.figure = generator.generate()
        fig.annotate(title = title, xlabel = xlabel, ylabel = ylabel)
        return fig
