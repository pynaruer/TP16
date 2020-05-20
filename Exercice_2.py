from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setFixedSize(300, 200)

        self.layout = QHBoxLayout()
        self.progressbar = QProgressBar()
        self.slider = QSlider(Qt.Vertical)

        self.layout.addWidget(self.progressbar)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.change_value_pb)

        self.setLayout(self.layout)

    def change_value_pb(self):
        self.progressbar.setValue(self.slider.value())

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
