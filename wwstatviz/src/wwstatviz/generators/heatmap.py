import numpy as np
import pandas as pd
from scipy.stats.stats import pearsonr, kendalltau, spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
from .generator import Generator

class HeatmapGenerator(Generator):

    def __init__(self, data, countries = 'all', features = 'all', 
                 method = 'pearson', mask = True):
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
        # method
        if method not in ['pearson', 'spearman', 'kendall']:
            raise ValueError('unknown correlation method')
        # mask
        if not isinstance(mask, bool):
            raise ValueError('invalid mask argument')
        self._countries = countries
        self._features = features
        self._method = method
        self._mask = mask

    def _compute_corr_matrix(self, indexes, columns):
        methods = {
            'pearson': pearsonr, 
            'spearman': spearmanr, 
            'kendall': kendalltau
        }
        corrf = methods[self._method]
        df = self._data.loc[indexes, columns]
        l = len(indexes)
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
        if self._mask:
            mask = np.zeros_like(corr_matrix.values)
            mask[np.triu_indices_from(mask)] = True
        else:
            mask = None
        xticklabels = corr_matrix.index.tolist()
        yticklabels = corr_matrix.columns.tolist()
        fig, ax = plt.subplots()
        ax = sns.heatmap(corr_matrix, mask = mask, square = True,
                         vmin = -1., vmax = 1., center = 0., 
                         xticklabels = xticklabels, yticklabels = yticklabels,
                         linewidths = 0.5)
        return fig

    def generate(self):
        ### computing correlation
        if self._countries == 'all':
            idx = self._data.index.tolist()
        else:
            idx = self._countries
        if self._features == 'all':
            cols = self._data.columns.tolist()
        else:
            cols = self._features
        df_corr = self._compute_corr_matrix(idx, cols)
        ### generating heatmap
        self._figure = self._heatmap(df_corr)
        return self._figure
