"""
1. PyQt / PySide2 program structure
2. Layout Management
3. Handling events
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0
        self.setCentralWidget(QWidget())
        self.layout = QVBoxLayout(self.centralWidget())

        self.btn = QPushButton("Click Me")
        self.label = QLabel(self.text())
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn)

        self.btn.clicked.connect(self.inc)

    def text(self):
        return f"You clicked {self.value} times"

    def inc(self):
        self.value += 1
        self.label.setText(self.text())

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
