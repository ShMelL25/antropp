import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Исследования')
        self.setWindowIcon(QIcon('img\icons8-научное-приложение-50.png')) # <a target="_blank" href="https://icons8.com/icon/40391/научное-приложение">Научное приложение</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
