#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from pylinac import PicketFence
from PicketFens import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """MainWindow inherits QMainWindow"""
    _pathDir: str

    def __init__(self, parent=None, pathDir=None):
        super(MainWindow, self).__init__(parent)
        assert isinstance(pathDir, object)
        self._pathDir=pathDir
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
    @property
    def pathDir(self):
        return getattr(self, '_pathDir')

    @pathDir.setter
    def pathDir(self, pathDir):
        self._pathDir=pathDir

    def OpenFile(self, textparam):
        options=QFileDialog.Options()
        options|=QFileDialog.DontUseNativeDialog
        fileName, _=QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                "All Files (*);;DICOM Files (*.dcm)", options=options)

        if fileName:
            MainWindow.pathDir=fileName;
            leeds=PicketFence(fileName)
            leeds.analyze(tolerance=0.15, action_tolerance=0.03,hdmlc=True)
            leeds.plot_analyzed_image()
            leeds.publish_pdf(MainWindow.pathDir + '.pdf', metadata={"name": textparam, "unit": "TrueBeam STX"})

    def __del__(self):
        self.ui=None


# -----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app=QApplication(sys.argv)
    app.setApplicationName('PicketFens')
    w=MainWindow()
    # create widget
    #w=MainWindow()
    w.setWindowTitle('PicketFens')
    w.show()

    # connection
    # QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit(app.exec_())
