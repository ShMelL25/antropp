# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sorry.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from fileinput import close
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp, QAction, QMessageBox, QInputDialog, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon


class Sorrymywindow():
    
   def showdialog():
        msg = QMessageBox()
        msg.setWindowIcon(QIcon('img\icons8-грустно-48.png'))
        msg.setIcon(QMessageBox.Information)

        msg.setText("Information")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        msg.setFont(font)
        msg.setInformativeText("We're sorry, but this feature is not yet available.")
        msg.setWindowTitle("Sorry")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(close)
        
        retval = msg.exec_()


# Создание кнопок испытуемых
class Button_isp():
   
   def __init__(self) -> None:
      pass

   def isp_buttom(self):
      self.btn_isp_1 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_1.setText(f'1) Егор')
      self.btn_isp_1.setObjectName("btn_isp_1") 
      self.verticalLayout.addWidget(self.btn_isp_1)

      self.btn_isp_2 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_2.setText(f'2) Егор')
      self.btn_isp_2.setObjectName("btn_isp_2") 
      self.verticalLayout.addWidget(self.btn_isp_2)

      self.btn_isp_3 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_3.setText(f'3) Егор')
      self.btn_isp_3.setObjectName("btn_isp_3") 
      self.verticalLayout.addWidget(self.btn_isp_3)

      self.btn_isp_4 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_4.setText(f'4) Егор')
      self.btn_isp_4.setObjectName("btn_isp_4") 
      self.verticalLayout.addWidget(self.btn_isp_4)

      self.btn_isp_5 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_5.setText(f'5) Егор')
      self.btn_isp_5.setObjectName("btn_isp_5") 
      self.verticalLayout.addWidget(self.btn_isp_5)

      self.btn_isp_6 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_6.setText(f'6) Егор')
      self.btn_isp_6.setObjectName("btn_isp_6") 
      self.verticalLayout.addWidget(self.btn_isp_6)

      self.btn_isp_7 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_7.setText(f'7) Егор')
      self.btn_isp_7.setObjectName("btn_isp_7") 
      self.verticalLayout.addWidget(self.btn_isp_7)

      self.btn_isp_8 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_8.setText(f'8) Егор')
      self.btn_isp_8.setObjectName("btn_isp_8") 
      self.verticalLayout.addWidget(self.btn_isp_8)

      self.btn_isp_9 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_9.setText(f'9) Егор')
      self.btn_isp_9.setObjectName("btn_isp_9") 
      self.verticalLayout.addWidget(self.btn_isp_9)

      self.btn_isp_10 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_10.setText(f'10) Егор')
      self.btn_isp_10.setObjectName("btn_isp_10") 
      self.verticalLayout.addWidget(self.btn_isp_10)

      self.btn_isp_11 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_11.setText(f'11) Егор')
      self.btn_isp_11.setObjectName("btn_isp_11") 
      self.verticalLayout.addWidget(self.btn_isp_11)

      self.btn_isp_12 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_12.setText(f'12) Егор')
      self.btn_isp_12.setObjectName("btn_isp_12") 
      self.verticalLayout.addWidget(self.btn_isp_12)

      self.btn_isp_13 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_13.setText(f'13) Егор')
      self.btn_isp_13.setObjectName("btn_isp_13") 
      self.verticalLayout.addWidget(self.btn_isp_13)

      self.btn_isp_14 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_14.setText(f'14) Егор')
      self.btn_isp_14.setObjectName("btn_isp_14") 
      self.verticalLayout.addWidget(self.btn_isp_14)

      self.btn_isp_15 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_15.setText(f'15) Егор')
      self.btn_isp_15.setObjectName("btn_isp_15") 
      self.verticalLayout.addWidget(self.btn_isp_15)

      self.btn_isp_16 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_16.setText(f'16) Егор')
      self.btn_isp_16.setObjectName("btn_isp_16") 
      self.verticalLayout.addWidget(self.btn_isp_16)

      self.btn_isp_17 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_17.setText(f'17) Егор')
      self.btn_isp_17.setObjectName("btn_isp_17") 
      self.verticalLayout.addWidget(self.btn_isp_17)

      self.btn_isp_18 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_18.setText(f'18) Егор')
      self.btn_isp_18.setObjectName("btn_isp_18") 
      self.verticalLayout.addWidget(self.btn_isp_18)

      self.btn_isp_19 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_19.setText(f'19) Егор')
      self.btn_isp_19.setObjectName("btn_isp_19") 
      self.verticalLayout.addWidget(self.btn_isp_19)

      self.btn_isp_20 = QtWidgets.QPushButton(self.scrollArea_Name)
      self.btn_isp_20.setText(f'20) Егор')
      self.btn_isp_20.setObjectName("btn_isp_20") 
      self.verticalLayout.addWidget(self.btn_isp_20)