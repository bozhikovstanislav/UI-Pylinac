#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from pylinac import PicketFence
from pylinac import picketfence
from PicketFens import Ui_MainWindow
import matplotlib.pyplot as plt
from pylinac import geometry


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
            # leeds.analyze(tolerance=0.2, action_tolerance=0.03, hdmlc=True, invert=False)
            leeds.analyze(orientation='Up-Down', tolerance=0.2, action_tolerance=0.1, hdmlc=True)
            d = picketfence.Settings(orientation='Up-Down', tolerance=0.2, action_tolerance=0.1, hdmlc=True,
                                     image=leeds.image, log_fits=None)
            d1 = picketfence.Settings(orientation='Left-Right', tolerance=0.2, action_tolerance=0.1, hdmlc=True,
                                      image=leeds.image, log_fits=None)
            m = picketfence.PicketManager(image=leeds.image, settings=d1, num_pickets=leeds.num_pickets)
            plt.hist(m.error_hist()[2])
            #oo = picketfence.Picket(image=leeds.image, settings=d1, approximate_idx=m.num_pickets,
            #                        spacing=m.mean_spacing)
            oo = picketfence.Picket(image=leeds.image, settings=d1, approximate_idx=m.num_pickets,
                                   spacing=m.mean_spacing)

            print(len(m.error_hist()[2]))
            plt.plot(m.passed)

            print(len(oo.mlc_meas))
            plt.show()  # y = picketfence.MLCMeas(point1=geometry.Point(), point2=geometry.Point(), settings=d)
            rr = picketfence.MLCMeas(point1=oo.mlc_meas[1], point2=oo.mlc_meas[9], settings=d1)
            print(oo.mlc_meas[1])
            print(rr.passed)
            print(oo.abs_median_error)



            # r = picketfence.Picket(image=leeds.image)

            # print(r.max_error)  # print(leeds.results())  # print(d.action_tolerance)  # print(d.number_large_leaves)  # print(d.tolerance)  # leeds.publish_pdf(fileName + '.pdf')  # a = picketfence.PicketManager(image=leeds.image, settings=d, num_pickets=9)

            # plt.hist(a.error_hist()[1])  # plt.show()

            # b = geometry.Point(x=2, y=1, z=4)  # c = geometry.Point(x=3, y=1, z=4)  # g = picketfence.MLCMeas(point1=b, point2=c, settings=d)  # g.plot2axes(axes=plt.axes,  #            width=1)  # plt.plot(a.image_mlc_inplane_mean_profile)  # plt.show()  # print(len(a.error_hist()[1]))  # plt.hist(a.error_hist()[2])  # plt.show()  # leeds.plot_analyzed_image()  # leeds.save_analyzed_image("image.jpg")  # leeds.publish_pdf(fileName + '.pdf')

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
