"""
This module contains the Generator base class.
Any generator should inherit from the Generator class and must implement 
a generate method.
"""

import pandas as pd

class Generator(object):
    
    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError('data argument must be a pandas dataframe')
        self._data = data
        self._figure = None

    def generate(self):
        raise NotImplementedError

    @property
    def figure(self):
        return self._figure
