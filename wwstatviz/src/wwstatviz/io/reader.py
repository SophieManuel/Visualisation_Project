class Reader(object):
    
    def __init__(self, input_file):
        self._input_file = input_file

    def read(self):
        raise NotImplementedError
