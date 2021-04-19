from .generator import Generator

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
        raise NotImplementedError
