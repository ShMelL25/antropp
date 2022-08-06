from email.mime import application
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from mainwidgets import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    

def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
