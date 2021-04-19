from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Figure(object):
    
    def __init__(self):
        self.figure = None

    def show(self):
        if isinstance(self._figure, Figure):
            plt.show()

    def save(self, output_path):
        if isinstance(self._figure, Figure):
            plt.tight_layout()
            self.figure.savefig(output_path)
