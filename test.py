from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import Qt
from PyQt5.Qt import QApplication
import sys

class loading(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200,300)
        self.label = QLabel(self)

        self.movie = QMovie('image/loading.gif')
        self.movie.start()
        self.show()

app = QApplication(sys.argv)

app.exit(app.exec())