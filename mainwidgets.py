# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from tkinter import Label
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, qApp, QMessageBox
from sorry_window import Sorrymywindow 
from PyQt5.QtGui import QIcon

class Ui_MainWindow(Sorrymywindow, object):     

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1000, 600)
        MainWindow.showMaximized()
        MainWindow.setMinimumSize(1000, 600)
        MainWindow.setWindowIcon(QIcon('img\icons8-анализ-навыков-48.png'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.scrollArea_Name = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_Name.sizePolicy().hasHeightForWidth())
        self.scrollArea_Name.setSizePolicy(sizePolicy)
        self.scrollArea_Name.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollArea_Name.setAutoFillBackground(True)
        self.scrollArea_Name.setWidgetResizable(True)
        self.scrollArea_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_Name.setObjectName("scrollArea_Name")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 218, 440))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_Name.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea_Name)

        # Добавление надписи Испытуемые
        

        self.scrollArea_Research = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_Research.sizePolicy().hasHeightForWidth())
        self.scrollArea_Research.setSizePolicy(sizePolicy)
        self.scrollArea_Research.setWidgetResizable(True)
        self.scrollArea_Research.setObjectName("scrollArea_Research")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 548, 440))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(526, 382))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Sorrymywindow.showdialog)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.scrollArea_Research.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea_Research)
        MainWindow.setCentralWidget(self.centralwidget)
      
        # Создание кнопки добавить испытуемого
        newpersonAction = QAction(QIcon('img\icons8-создать-новый-48.png'), '&New person', MainWindow)
        newpersonAction.setShortcut('Ctrl+N')
        newpersonAction.setStatusTip('New Person')
        newpersonAction.triggered.connect(Sorrymywindow.showdialog)

        # Создание кнопки сохранить
        saveAction = QAction(QIcon('img\icons8-сохранить-48.png'), '&Save', MainWindow)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save File')
        saveAction.triggered.connect(Sorrymywindow.showdialog)

        # Создание кнопки сохранить как
        saveasAction = QAction(QIcon('img\icons8-сохранить-как-48.png'), '&Save as', MainWindow)
        saveasAction.setShortcut('Alt+1')
        saveasAction.setStatusTip('Save File as')
        saveasAction.triggered.connect(Sorrymywindow.showdialog)

        # Создание кнопки export to pdf
        exportPDFAction = QAction(QIcon('img\icons8-pdf-48.png'), '&Export to PDF', MainWindow)
        exportPDFAction.setStatusTip('Export file to PDF')
        exportPDFAction.triggered.connect(Sorrymywindow.showdialog)

        # Создание кнопки export to CSV
        exportCSVAction = QAction(QIcon('img\icons8-экспорт-в-csv-48.png'), '&Export to CSV', MainWindow)
        exportCSVAction.setStatusTip('Export file to CSV')
        exportCSVAction.triggered.connect(Sorrymywindow.showdialog)

        # Создание кнопки import
        importAction = QAction(QIcon('img\icons8-импортировать-48.png'), '&Import CSV', MainWindow)
        importAction.setStatusTip('Import file CSV')
        importAction.triggered.connect(Sorrymywindow.showdialog)
        
        # Создание кнопки выход
        exitAction = QAction(QIcon('img\icons8-выход-48.png'), '&Exit', MainWindow)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        # Создание MenuBar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
              
        # Отображение всех элементов в MenuBar
        #File
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(newpersonAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveasAction)
        exportFile = fileMenu.addMenu('&Export') # Export File Menu
        exportFile.setIcon(QIcon('img\icons8-экспорт-48.png'))
        exportFile.addAction(exportPDFAction)
        exportFile.addAction(exportCSVAction)
        fileMenu.addAction(importAction)
        fileMenu.addAction(exitAction)
        MainWindow.setMenuBar(self.menubar)

        # Создание кнопки settings
        SettingsAction = QAction(QIcon('img\icons8-настройки-48.png'), '&Settings', MainWindow)
        SettingsAction.setShortcut('Alt+P')
        SettingsAction.setStatusTip('Settings App')
        SettingsAction.triggered.connect(Sorrymywindow.showdialog)
        
        # Settings
        settingsMenu = self.menubar.addMenu('&Settings')
        settingsMenu.addAction(SettingsAction)
        MainWindow.setMenuBar(self.menubar)  

        # Вывод графиков
        statisticAction = QAction(QIcon('img\icons8-статистика-48.png'), 'Statistic', MainWindow)
        statisticAction.setStatusTip('Output of Statistic') 
        statisticAction.triggered.connect(Sorrymywindow.showdialog)       

        # Tools
        toolsMenu = self.menubar.addMenu('&Tools')
        toolsMenu.addAction(statisticAction)
        MainWindow.setMenuBar(self.menubar)

        # Application help
        application_helpAction = QAction(QIcon('img\icons8-обслуживание-48.png'), 'Application help', MainWindow)
        application_helpAction.setStatusTip('Application help')
        application_helpAction.triggered.connect(Sorrymywindow.showdialog)

        # Sample information
        sampleinfoAction = QAction(QIcon('img\icons8-задать-вопрос-48.png'), 'Sample information', MainWindow)
        sampleinfoAction.setStatusTip('Sample information')
        sampleinfoAction.triggered.connect(Sorrymywindow.showdialog)

        # Help
        helpMenu = self.menubar.addMenu('&Help')
        helpMenu.addAction(application_helpAction)
        helpMenu.addAction(sampleinfoAction)
        MainWindow.setMenuBar(self.menubar)      

        # Создание Статус бара
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Исследования"))
        self.pushButton.setText(_translate("MainWindow", "Добавить тест"))





