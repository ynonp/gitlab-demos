from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow

import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnClicker.clicked.connect(self.inc)

    def text(self):
        return f"You clicked {self.value} times"

    def inc(self):
        self.value += 1
        self.ui.label.setText(self.text())



"""
1. Install Designer
2. Write GUI Code using designer
3. Integrate Python program with designer code
"""

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
