import pandas as pd

class Generator(object):
    
    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError('data argument must be a pandas dataframe')
        self._data = data
        self._plot = None

    def generate(self):
        raise NotImplementedError
