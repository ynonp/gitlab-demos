from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from mainwindow import Ui_MainWindow

"""
1. Write a UI file for the editor
2. Connect signals to slots
3. Add shortcuts
4. Add style sheet
"""

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filename = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnOpen.clicked.connect(self.open_file)
        self.ui.btnSave.clicked.connect(self.save_file)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionOpen.setShortcut(QKeySequence.Open)

        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave.setShortcut(QKeySequence.Save)

        self.ui.actionQuit.triggered.connect(qApp.quit)
        self.ui.actionQuit.setShortcut(QKeySequence.Quit)

    def save_file(self):
        if self.filename is None:
            fname, _ = QFileDialog.getSaveFileName(self, "Please select a file name to save")
            if fname != '':
                self.filename = fname

        if self.filename is None:
            return

        with open(self.filename, 'w') as f:
            f.write(self.ui.text.toPlainText())


    def open_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Please select a file name")
        self.setWindowTitle(fname)
        if fname != '':
            self.filename = fname
            self.reload()

    def reload(self):
        with open(self.filename) as f:
            self.ui.text.setPlainText(f.read())

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
