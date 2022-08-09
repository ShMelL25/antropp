from email.mime import application
import sys
from PyQt5 import QtWidgets
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
