"""
This module contains the base writer class from which any data file writer
subclass should inherit.
"""


class Writer(object):

    def __init__(self, output_file):
        self._output_file = output_file

    def write(self):
        raise NotImplementedError
