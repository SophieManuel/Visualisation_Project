from .generator import Generator
import numpy as np
from scipy.stats.stats import pearsonr, kendalltau, spearmanr
import seaborn as sns

class HeatmapGenerator(Generator):

    def _compute_corr_matrix(self, indexes, columns, method):
        methods = {
            'pearson': pearsonr, 
            'spearman': spearmanr, 
            'kendall': kendalltau
        }
        corrf = methods[method]
        df = self._data.loc[indexes, columns]
        df_corr = pd.DataFrame(data = np.zeros((l, l)), 
                               index = indexes, columns = indexes)
        np.fill_diagonal(df_corr.values, 1.)
        for i in range(len(indexes)):
            for j in range(i + 1, len(indexes)):
                x = df.loc[indexes[i]].values
                y = df.loc[indexes[j]].values
                corr, _ = corrf(x, y)
                df_corr.loc[indexes[i], indexes[j]] = corr
                df_corr.loc[indexes[j], indexes[i]] = corr
        return df_corr

    def _heatmap(self, corr_matrix):
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
        with sns.axes_style("white"):
            fig, ax = plt.subplots()
            ax = sns.heatmap(corr, mask=mask, vmax=.3, square=True)
        return fig

    def generate(self, countries = 'all', features = 'all', method = 'pearson'):
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
        # method
        if method not in ['pearson', 'spearman', 'kendall']:
            raise ValueError('unknown correlation method')
        ### computing correlation
        idx = self._data.index.tolist() if countries == 'all' else countries
        cols = self._data.columns.tolist() if features == 'all' else features
        df_corr = self._compute_corr_matrix(idx, cols, method)
        ### generating heatmap
        # TODO: use seaborn or matplotlib
        self._figure = self._heatmap(df_corr)
        raise NotImplementedError
