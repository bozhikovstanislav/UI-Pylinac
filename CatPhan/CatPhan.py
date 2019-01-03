# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CatPhan.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 332)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_OpenGFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OpenGFile.setGeometry(QtCore.QRect(70, 200, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_OpenGFile.setFont(font)
        self.pushButton_OpenGFile.setObjectName("pushButton_OpenGFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 251, 171))
        self.label.setMinimumSize(QtCore.QSize(61, 0))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_OpenGFile.clicked.connect(MainWindow.OpenDirectory)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form1"))
        self.pushButton_OpenGFile.setText(_translate("MainWindow", "OpenFile"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Icones/development-gtk.ico\"/><img src=\":/Icones/amule.png\"/></p></body></html>"))

import Resource
