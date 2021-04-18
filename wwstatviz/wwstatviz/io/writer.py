class Writer(object):

    def __init__(self, output_file):
        self._output_file = output_file

    def write(self):
        raise NotImplementedError
