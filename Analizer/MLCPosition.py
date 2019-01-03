import os
from PyQt5 import QtCore
from pylinac import TrajectoryLog
from pylinac import load_log
from pylinac import log_analyzer
from pylinac import MachineLogs
import csv
from pylinac import process

file = open("configQAwatchdir.txt", "r")
a = file.readline()
file = open("configPathSRS.txt", "r")
yamlanalise = file.readline()
win_directory = QtCore.QDir.toNativeSeparators(a)
yamlanalisePath = QtCore.QDir.toNativeSeparators(yamlanalise)

asr = load_log(win_directory)

log = TrajectoryLog("Arck_PFRAHDD1_T1.1_PF_RA_20181228080911.bin")

# a = log.axis_data.mlc.create_RMS_array(log.axis_data.mlc.get_leaves())
# print(a)
#b = log_analyzer.JawStruct(log.axis_data.jaws.x1, log.axis_data.jaws.y1, log.axis_data.jaws.x2, log.axis_data.jaws.y2)
# print(b.y1.plot_actual())

a1=log.subbeams
s=log.axis_data.mlc.leaf_axes[30]
print(s.difference[1])
with open('filename.txt', 'w') as f:
    for i in range(71):
        f.write('%.6f' % s.difference[i]+'\n')




#fs = open('myfile.txt','w')
#for i in range(120):
#    fs.write('%.5f' % s.actual[i])
#c=log_analyzer.MLC.from_tlog(log,a1,log.axis_data.jaws,log.axis_data.mlc.get_snapshot_values(),log.axis_data.mlc.snapshot_idx,s)
#print(a[0])
#d=log_analyzer.ActualFluence()
#log.axis_data.resolution = 0.1
#a = log.axis_data.mlc.create_RMS_array(log.axis_data.mlc.get_leaves())
#log.fluence.actual.calc_map()
##log.fluence.actual.save_map("save.jpg")

