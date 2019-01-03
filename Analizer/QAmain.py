import os
from PyQt5 import QtCore
from pylinac import process

file=open("configQAwatchdir.txt","r")
a=file.readline()
file=open("configPathSRS.txt","r")
yamlanalise=file.readline()
win_directory = QtCore.QDir.toNativeSeparators(a)
yamlanalisePath = QtCore.QDir.toNativeSeparators(yamlanalise)
process(win_directory, yamlanalisePath)
