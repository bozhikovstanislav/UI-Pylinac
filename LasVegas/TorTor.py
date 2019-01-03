# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TorTor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 331)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 441, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Icones/emblem-advertisement-dollar.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 91, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Icones/xfig.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 10, 71, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Icones/amor.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 100, 71, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/Icones/development-ruby.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 120, 91, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/Icones/kstars.png"))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.OpenDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form1"))
        self.pushButton.setText(_translate("MainWindow", "Open Dir"))
        self.label_2.setText(_translate("MainWindow", "LAS VEGAS"))

import Resource
