#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from pylinac import LeedsTOR
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
            leeds = LeedsTOR(fileName)
            leeds.analyze(low_contrast_threshold=0.01, hi_contrast_threshold=0.5)
            leeds.plot_analyzed_image(low_contrast=True)
            leeds.publish_pdf(fileName.title()+'.pdf')

    def HightContrast(self):
        leeds = LeedsTOR(d.pathDir)
        leeds.plot_analyzed_image(low_contrast=False)
        leeds.publish_pdf(d.pathDir + '\\resultHightContrast.pdf')

    def __del__(self):
        self.ui = None


#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('TorTor')
    d = DirectoryPath(pathDir="", getCountImages=0)
    # create widget
    w = MainWindow()
    w.setWindowTitle('TorTor')
    w.show()

    # connection
    # QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit(app.exec_())