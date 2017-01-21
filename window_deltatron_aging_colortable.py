import PyQt4, sys
from PyQt4 import QtGui, QtCore

__author__ = 'Maciej Oliwa'


class WindowDeltatronAgingColortable:
    def __init__(self, app):
        self.w = QtGui.QWidget()
        self.w.resize(200, 200)
        self.w.move(150, 150)
        self.w.setWindowTitle('Deltatron aging colortable')
