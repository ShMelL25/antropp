import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon
from view_prog import view_menuBar

class Example(view_menuBar, QMainWindow, QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.exitaction()
    
    def exitaction(self):
        exitAction = QAction(QIcon('img\icons8-выход-48.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        

    def initUI(self):    
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Исследования')
        self.setWindowIcon(QIcon('img\icons8-научное-приложение-50.png')) # <a target="_blank" href="https://icons8.com/icon/40391/научное-приложение">Научное приложение</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
                
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
