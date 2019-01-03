#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from pylinac import LasVegas
from TorTor import Ui_MainWindow

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

class MainWindow(QMainWindow,Ui_MainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def OpenDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;DICOM Files (*.dcm)", options=options)
        if fileName:
            leeds = LasVegas(fileName)
            leeds.analyze(low_contrast_threshold=0.35,invert=True)
            leeds.plot_analyzed_image(True,True)
            leeds.publish_pdf(fileName.title()+'.pdf')

    def HightContrast(self):
        leeds = LasVegas(d.pathDir)
        leeds.plot_analyzed_image(low_contrast=False)
        leeds.publish_pdf(d.pathDir + '\\resultHightContrast.pdf')

    def __del__(self):
        self.ui = None


#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('L A S   V E G A S')
    d = DirectoryPath(pathDir="", getCountImages=0)
    # create widget
    w = MainWindow()
    w.setWindowTitle('L A S   V E G A S')
    w.show()

    # connection
    # QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit(app.exec_())