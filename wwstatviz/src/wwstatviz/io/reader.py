"""
This module contains the base reader class from which any data file reader
subclass should inherit.
"""


class Reader(object):

    def __init__(self, input_file):
        self._input_file = input_file

    def read(self):
        raise NotImplementedError
