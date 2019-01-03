#!-*- coding:utf-8 -*-
import sys
import os
# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from pylinac import WinstonLutz
from PyQt5 import QtCore
import matplotlib.pyplot as plt
from statsmodels.tsa.tests.results.results_arma import current_path

from Window import Ui_MainWindow

(Ui_MainWindow, QWindow) = uic.loadUiType('Window.ui')

GANTRY = 'Gantry'
COLLIMATOR = 'Collimator'
COUCH = 'Couch'

class DirectoryPath(object):
    def __init__(self, pathDir,getCountImages):
        self._pathDir = pathDir
        self._getCountImages=getCountImages

    @property
    def pathDir(self):
        return getattr(self, '_pathDir')

    @pathDir.setter
    def pathDir(self, pathDir):
        self._pathDir = pathDir

    @property
    def getCountImages(self):
        return getattr(self,'_getCountImages')

    @getCountImages.setter
    def getCountImages(self,getCountImages):
        self._getCountImages=getCountImages

class MainWindow(QWindow):
    """MainWindow inherits QMainWindow"""

    # d = DirectoryPath(pathDir=None)
    def __init__(self, parent=None):
        super(QWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def __del__(self):
        self.ui = None

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("End of the Images")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.exec_()

    def changeImages(self):

        num = int(self.ui.spinBox.text())
        direct_tory = d.pathDir
        wl = WinstonLutz(direct_tory)
        if num < d.getCountImages:
            wl.images[num].plot()
        else:
            self.showdialog()
    def summeryCone(self):
        wl = WinstonLutz(d.pathDir)
        wl.plot_coneSummery()
        wl.publishCone_pdf(d.pathDir+'//resultCone.pdf')


    def getIzoSize(self):
        wl = WinstonLutz(d.pathDir)
        self.ui.label_CouchZize.setText(str('{0:.2f}'.format(wl.couch_iso_size)))
        self.ui.label_GentrySize.setText(str(wl.collimator_iso_size))
        self.ui.label_GentryIZOSIZE.setText(str('{0:.2f}'.format(wl.gantry_iso_size)))

    def GetConeIzoSize(self):
        wl = WinstonLutz(d.pathDir)
        self.ui.label_CouchZize.setText(str('{0:.2f}'.format(wl.couch_iso_size)))
        self.ui.label_GentryIZOSIZE.setText(str('{0:.2f}'.format(wl.gantry_iso_size)))

    def getEpidSag(self):
        wl = WinstonLutz(d.pathDir)
        wl.plot_epid_sag()

    def GentrySag(self):
        wl = WinstonLutz(d.pathDir)
        wl.plot_gantry_sag()


    def slot1(self):
        file = open("file.txt", "w")
        directory = QFileDialog.getExistingDirectory(self, 'Select backup directory')
        win_directory = QtCore.QDir.toNativeSeparators(directory)
        wl = WinstonLutz(win_directory)
        d.getCountImages=len(wl.images)
        d.pathDir = win_directory
        wl.images[0].plot()
        self.ui.pushButton__ConeOpen.setEnabled(False)
        self.ui.pushButton__SummaryCone.setEnabled(False)
        self.ui.pushButton__ConeIzoSize.setEnabled(False)

        a=wl.results()
        file.write(str(a))
        file.close()

    def OpenCOne(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select backup directory')
        win_directory = QtCore.QDir.toNativeSeparators(directory)
        wl = WinstonLutz(win_directory)
        d.getCountImages = len(wl.images)
        d.pathDir = win_directory
        wl.images[0].plot()
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton__Summary.setEnabled(False)
        self.ui.pushButton__IzoSize.setEnabled(False)
        file = open("file.txt", "w")
        file.write(str(wl.result_cone()))
        file.close()

    def sumary_Info(self):
        wl = WinstonLutz(d.pathDir)
        wl.plot_summary()
        wl.publish_pdf(d.pathDir+'//result.pdf')


# -----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('untitled2')

    d = DirectoryPath(pathDir="",getCountImages=0)

    # create widget
    w = MainWindow()
    w.setWindowTitle('untitled2')
    w.show()

    # connection
    # QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit(app.exec_())
