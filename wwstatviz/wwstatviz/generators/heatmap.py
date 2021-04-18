from .generator import Generator

class HeatmapGenerator(Generator):

    def generate(self, countries = 'all', features = 'all'):
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
        # features
        if not isinstance(features, str) and not isinstance(features, list):
            raise ValueError('invalid features argument')
        if isinstance(features, str) and features != 'all':
            raise ValueError('invalid features argument')
        if isinstance(features, list):
            for e in features:
                if e not in self._data.columns.tolist():
                    raise ValueError(f'encountred invalid feature name: {e}')
        # extracting data from self._data
        idx = self._data.index.tolist() if countries == 'all' else countries
        cols = self._data.columns.tolist() if features == 'all' else features
        df = self._data.loc[idx, cols]
        # computing correlations
        l = len(idx)
        df_corr = pd.DataFrame(data = np.zeros((l, l)), 
                               index = idx, columns = idx)
        # TODO: compute correlations
        raise NotImplementedError
