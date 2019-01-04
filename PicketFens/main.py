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

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def OpenFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;DICOM Files (*.dcm)", options=options)
        if fileName:
            leeds = PicketFence(fileName)
            # leeds = PicketFence(fileName, filter=1)
            #leeds.analyze(tolerance=0.2, action_tolerance=0.03, hdmlc=True, invert=False)
            leeds.analyze(tolerance=0.2, action_tolerance=0.1, hdmlc=True,)
            print(leeds.results())
            leeds.plot_analyzed_image()
            leeds.save_analyzed_image("image.jpg")
            leeds.publish_pdf(fileName + '.pdf')

    def __del__(self):
        self.ui = None


# -----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('PicketFens')

    # create widget
    w = MainWindow()
    w.setWindowTitle('PicketFens')
    w.show()

    # connection
    # QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit(app.exec_())
