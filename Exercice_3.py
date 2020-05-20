from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500, 300)
        self.counter = 0

        self.layout = QVBoxLayout()
        self.button = QPushButton("Changer mon texte")

        self.text_edit = QTextEdit("Le nombre de clics va être affiché ici")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text_edit)

        self.button.clicked.connect(self.button_clicked)

        self.setLayout(self.layout)

    def button_clicked(self):
        self.counter += 1
        print(f"Clic {self.counter}")
        self.button.setText(f"Clic {self.counter}")
        self.text_edit.setText(f"Click {self.counter}")

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
