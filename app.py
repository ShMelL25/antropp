import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon



class Example(QMainWindow, QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.exitaction()
        self.status_Bar()
    
    def initUI(self):
        self.setGeometry(300, 300, 1000, 500)
        self.showMaximized()
        self.setWindowTitle('Исследования')
        self.setWindowIcon(QIcon('img\icons8-научное-приложение-50.png')) # <a target="_blank" href="https://icons8.com/icon/40391/научное-приложение">Научное приложение</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>   
        self.show()

    def exitaction(self):
        new_file = QAction(QIcon('img\icons8-создать-новый-48.png'), '&Новый документ', self)
        new_file.setShortcut('Ctrl+N')
        new_file.setStatusTip('Создание нового документа')
        new_file.trigger

        exitAction = QAction(QIcon('img\icons8-выход-48.png'), '&Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(new_file)
        fileMenu.addAction(exitAction)

    def status_Bar(self):
        self.statusBar().showMessage('Ready')

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
