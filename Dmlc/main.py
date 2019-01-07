#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from pylinac import vmat
from dmlc import Ui_MainWindow
from pylinac.vmat import DMLC


class DirectoryPath(object):
    _pathDir: str

    def __init__(self, pathDir, getCountImages):
        assert isinstance(pathDir, object)
        self._pathDir=pathDir
        self._fieldOpenPathfile=""
        self._dmlcopenfilenamepath=""
        self._getCountImages=getCountImages

    @property
    def pathDir(self):
        return getattr(self, '_pathDir')

    @pathDir.setter
    def pathDir(self, pathDir):
        self._pathDir=pathDir

    @property
    def fieldOpenPathfile(self):
        return getattr(self, '_fieldOpenPathfile')

    @fieldOpenPathfile.setter
    def fieldOpenPathfile(self, fieldOpenPathfile):
        self._fieldOpenPathfile=fieldOpenPathfile

    @property
    def dmlcopenfilenamepath(self):
        return getattr(self, '_dmlcopenfilenamepath')

    @dmlcopenfilenamepath.setter
    def dmlcopenfilenamepath(self, dmlcopenfilenamepath):
        self._dmlcopenfilenamepath=dmlcopenfilenamepath


class MainWindow(QMainWindow, Ui_MainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent: object = None) -> object:
        super(MainWindow, self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    def openFileNameDialog(self):
        options=QFileDialog.Options()
        options|=QFileDialog.DontUseNativeDialog
        fileName, _=QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def OpenDialog(self):
        options=QFileDialog.Options()
        options|=QFileDialog.DontUseNativeDialog
        fileName, _=QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                "All Files (*);;DICOM Files (*.dcm)", options=options)
        if fileName:
            DirectoryPath.fieldOpenPathfile=fileName

    def OpenDmlcFiles(self):
        options=QFileDialog.Options()
        options|=QFileDialog.DontUseNativeDialog
        fileName, _=QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                "All Files (*);;DICOM Files (*.dcm)", options=options)
        if fileName:
            DirectoryPath.dmlcopenfilenamepath=fileName

    def DmlcCalculations(self, cal1, cal2, textparam):
        if cal1:
            open=DirectoryPath.fieldOpenPathfile
            field=DirectoryPath.dmlcopenfilenamepath
            dmlscall=vmat.DRMLC(image_paths=(open,field))
            dmlscall.analyze(tolerance=1.3)
            dmlscall.plot_analyzed_image('profile')
            print(dmlscall.results())
            dmlscall.plot_analyzed_image()
            dmlscall.publish_pdf(DirectoryPath.dmlcopenfilenamepath + '.pdf',metadata={"name":textparam,"unit":"TrueBeam STX"})
        if cal2:
            drgs=vmat.DRGS([str(DirectoryPath.fieldOpenPathfile), str(DirectoryPath.dmlcopenfilenamepath)])
            drgs.analyze(tolerance=1.3)
            print(drgs.results())
            drgs.plot_analyzed_image()
            drgs.publish_pdf(DirectoryPath.dmlcopenfilenamepath + 'drgs' + '.pdf', metadata={"name":textparam,"unit":"TrueBeam STX"})

    def __del__(self):
        self.ui=None


# -----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app=QApplication(sys.argv)
    app.setApplicationName('Dmlc')
    d=DirectoryPath(pathDir="", getCountImages=0)
    # create widget
    w=MainWindow()
    w.setWindowTitle('Dmlc')
    w.show()

    # connection
    # QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit(app.exec_())
