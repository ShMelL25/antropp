from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon

class view_menuBar(QMainWindow, QWidget):
    def exitaction(self):
        exitAction = QAction(QIcon('img\icons8-выход-48.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)