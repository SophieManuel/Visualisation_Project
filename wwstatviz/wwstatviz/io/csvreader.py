from . import Reader
from .iso import CC_2D, CC_3D
import pandas as pd

class CSVReader(Reader):

    def __init__(self, input_file, separator = ','):
        super().__init__(input_file)
        self._separator = separator

    def read(self):
        df = pd.read_csv(self._input_file, 
                         header = 0, 
                         index_col = 0, 
                         sep = self._separator)
        # checking if dataframe indexes are valid country codes
        index = df.index.tolist()
        ccs = CC_2D if len(index[0]) == 2 else CC_3D
        for e in index:
            if e not in ccs:
                raise ValueError(f'unknown country code {e}')
        return df
