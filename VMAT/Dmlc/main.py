#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from pylinac import VMAT
from dmlc import Ui_MainWindow


class DirectoryPath(object):
    def __init__(self, pathDir, getCountImages):
        self._pathDir = pathDir
        self._fieldOpenPathfile = ""
        self._dmlcopenfilenamepath = ""
        self._getCountImages = getCountImages

    @property
    def pathDir(self):
        return getattr(self, '_pathDir')

    @pathDir.setter
    def pathDir(self, pathDir):
        self._pathDir = pathDir

    @property
    def fieldOpenPathfile(self):
        return getattr(self, '_fieldOpenPathfile')

    @fieldOpenPathfile.setter
    def fieldOpenPathfile(self, fieldOpenPathfile):
        self._fieldOpenPathfile = fieldOpenPathfile

    @property
    def dmlcopenfilenamepath(self):
        return getattr(self, '_dmlcopenfilenamepath')

    @dmlcopenfilenamepath.setter
    def dmlcopenfilenamepath(self, dmlcopenfilenamepath):
        self._dmlcopenfilenamepath = dmlcopenfilenamepath


class MainWindow(QMainWindow, Ui_MainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent: object = None) -> object:
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
            DirectoryPath.fieldOpenPathfile = fileName

    def OpenDmlcFiles(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;DICOM Files (*.dcm)", options=options)
        if fileName:
            DirectoryPath.dmlcopenfilenamepath = fileName

    def DmlcCalculations(self, cal1, cal2, textparam):
        if cal1:
            leeds = VMAT(images=[DirectoryPath.fieldOpenPathfile, DirectoryPath.dmlcopenfilenamepath],
                         delivery_types=['open', 'dmlc'])
            leeds.analyze(test='drmlc', tolerance=1.3, x_offset=0)
            leeds.plot_analyzed_subimage('profile')
            leeds.save_analyzed_subimage('myprofile.png', subimage='profile')
            print(leeds.return_results())
            leeds.plot_analyzed_image()
            leeds.publish_pdf(DirectoryPath.dmlcopenfilenamepath + '.pdf')
        if cal2:
            drgs = VMAT(images=[DirectoryPath.fieldOpenPathfile, DirectoryPath.dmlcopenfilenamepath],
                        delivery_types=['open', 'drgs'])
            drgs.analyze(test='drgs', tolerance=1.3, x_offset=10)
            drgs.save_analyzed_subimage('myprofiledrgs.png', subimage='profile')
            print(drgs.return_results())
            drgs.plot_analyzed_image()
            drgs.publish_pdf(DirectoryPath.dmlcopenfilenamepath + 'drgs' + '.pdf', author=textparam, unit="TrueBeamSTX")

    def __del__(self):
        self.ui = None


# -----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('Dmlc')
    d = DirectoryPath(pathDir="", getCountImages=0)
    # create widget
    w = MainWindow()
    w.setWindowTitle('Dmlc')
    w.show()

    # connection
    # QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit(app.exec_())
