import PyQt4, sys
from PyQt4 import QtGui, QtCore

__author__ = 'Maciej Oliwa'


class WindowOutputFilesColorSettings:
    def __init__(self, app):
        self.w = QtGui.QWidget()
        self.w.resize(200, 200)
        self.w.move(100, 100)
        self.w.setWindowTitle('Output files color settings')
        self.w.show()
