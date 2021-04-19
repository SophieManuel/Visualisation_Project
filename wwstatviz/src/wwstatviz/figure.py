import matplotlib
import matplotlib.pyplot as plt

class Figure(object):
    
    def __init__(self):
        self.figure = None
        self._title = None
        self._xlabel = None
        self._ylabel = None

    def show(self):
        if isinstance(self._figure, Figure):
            plt.show()

    def save(self, output_path):
        if isinstance(self.figure, matplotlib.figure.Figure):
            self.figure.tight_layout()
            self.figure.savefig(output_path)
    
    def annotate(self, title = '', xlabel = '', ylabel = ''):
        ### check args
        for arg in [title, xlabel, ylabel]:
            if not isinstance(arg, str):
                raise ValueError(f'invalid argument {arg}')
        self._title = title
        self._xlabel = xlabel
        self._ylabel = ylabel
        if isinstance(self.figure, matplotlib.figure.Figure):
            self.figure.suptitle(title)
            self.figure.supxlabel(xlabel)
            self.figure.supylabel(ylabel)
