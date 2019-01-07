#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import Resource
from CatPhan import Ui_MainWindow
from PyQt5 import QtCore
from CatPhan import Ui_MainWindow
from pylinac import CatPhan504


class DirectoryPath(object):
    def __init__(self, pathDir, getCountImages):
        self._pathDir=pathDir
        self._getCountImages=getCountImages

    @property
    def pathDir(self):
        return getattr(self, '_pathDir')

    @pathDir.setter
    def pathDir(self, pathDir):
        self._pathDir=pathDir


class MainWindow(QMainWindow, Ui_MainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    def OpenDirectory(self, textparam):
        directory=QFileDialog.getExistingDirectory(self, 'Select backup directory')
        win_directory=QtCore.QDir.toNativeSeparators(directory)
        d.pathDir=win_directory

        mycbct=CatPhan504(win_directory)
        mycbct.analyze()
        mycbct.plot_analyzed_subimage('linearity')
        mycbct.save_analyzed_subimage('linearity.png', subimage='linearity')
        mycbct.publish_pdf(d.pathDir + '\\result.pdf', metadata={"name": textparam, "unit": "TrueBeam STX"})

    def __del__(self):
        self.ui=None


# -----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app=QApplication(sys.argv)
    app.setApplicationName('CatPhan')

    d=DirectoryPath(pathDir="", getCountImages=0)
    # create widget
    w=MainWindow()
    w.setWindowTitle('CatPhan')
    w.show()

    # connection
    # QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit(app.exec_())
