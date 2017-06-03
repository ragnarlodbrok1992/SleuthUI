import sys
from PyQt4 import QtGui, QtCore
import window_output_files_color_settings
import window_deltatron_aging_colortable
import window_probability_colortable_for_urban_growth
import elements_container

__author__ = 'Maciej Oliwa'


class Window:
    app = QtGui.QApplication(sys.argv)
    WindowOutputFilesColorSettings = window_output_files_color_settings. \
        WindowOutputFilesColorSettings(app)
    WindowDeltatronAgingColortable = window_deltatron_aging_colortable. \
        WindowDeltatronAgingColortable(app)
    WindowProbabilityColortableForUrbanGrowth = window_probability_colortable_for_urban_growth. \
        WindowProbabilityColortableForUrbanGrowth(app)

    def _set_button_functions(self):
        # Buttons for files
        self.buttons['buttonUrbanDataImage'].clicked.connect(lambda: self.selectfileurban())
        self.buttons['buttonRoadDataImage'].clicked.connect(lambda: self.selectfileroaddata())
        self.buttons['buttonLanduseDataImage'].clicked.connect(lambda: self.selectfilelandusedata())
        self.buttons['buttonExcludedDataImage'].clicked.connect(lambda: self.selectfileexcludeddata())
        self.buttons['buttonSlopeDataImage'].clicked.connect(lambda: self.selectfileslopedata())
        self.buttons['buttonBackgroundDataImage'].clicked.connect(lambda: self.selectfilebackgrounddata())

        # Buttons new window functions
        self.buttons['buttonOutputFilesColorSettings'].clicked.connect(lambda:
                                                                       self.buttonOutputFilesColorSettingsClicked())
        self.buttons['buttonDeltatronAgingColortable'].clicked.connect(lambda:
                                                                       self.buttonDeltatronAgingColortableClicked())
        self.buttons['buttonProbabilityColorSettings'].clicked.connect(lambda:
                                                                       self.buttonProbabilityColorSettingsClicked())

    def _populate_window(self):

        # Setting radiobuttons
        self.radiobuttons = dict()
        radiobuttons_names = [''.join([elements_container.radiobuttons_name_prefix,
                                       elements_container.radiobuttons_name_postfix[x][0]])
                              for x in range(0, len(elements_container.radiobuttons_name_postfix))]
        for name in radiobuttons_names:
            self.radiobuttons[name] = QtGui.QCheckBox()

        # Setting buttons
        self.buttons = dict()
        buttons_names = [''.join([elements_container.buttons_name_prefix,
                                  elements_container.buttons_name_postfix_and_text[x][0]])
                         for x in range(0, len(elements_container.buttons_name_postfix_and_text))]
        x = 0
        for name in buttons_names:
            self.buttons[name] = QtGui.QPushButton()
            self.buttons[name].setText(elements_container.buttons_name_postfix_and_text[x][1])
            x += 1
        del x

        # Setting labels
        self.labels = dict()
        labels_names = [''.join([elements_container.labels_name_prefix,
                                 elements_container.labels_name_postfix_and_text[x][0]])
                        for x in range(0, len(elements_container.labels_name_postfix_and_text))]
        x = 0
        for name in labels_names:
            self.labels[name] = QtGui.QLabel()
            self.labels[name].setText(elements_container.labels_name_postfix_and_text[x][1])
            x += 1
        del x

        # Setting label alignments
        for name in elements_container.labels_qt_align_center:
            self.labels[name].setAlignment(QtCore.Qt.AlignCenter)

        # Setting lineEdits
        self.line_edits = dict()
        line_edits_names = [''.join([elements_container.line_edits_name_prefix,
                                     elements_container.line_edits_name_postfix_and_text_width_maxlength[x][0]])
                            for x in range(0, len(elements_container.line_edits_name_postfix_and_text_width_maxlength))]
        x = 0
        for name in line_edits_names:
            self.line_edits[name] = QtGui.QLineEdit()
            self.line_edits[name].setText(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][1])
            if elements_container.line_edits_name_postfix_and_text_width_maxlength[x][2] is not None:
                self.line_edits[name].\
                    setFixedWidth(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][2])
            if elements_container.line_edits_name_postfix_and_text_width_maxlength[x][3] is not None:
                self.line_edits[name].\
                    setMaxLength(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][3])
            x += 1
        del x

    def _set_layouts(self):
        # Layout design
        # TopRow
        # (LeftColumn - CentreColumn - RightColumn) - within MiddleRowLayout
        # BottomRow

        self.mainLayout = QtGui.QVBoxLayout()
        topRowLayout = QtGui.QHBoxLayout()
        middleRowLayout = QtGui.QHBoxLayout()
        bottomRowLayout = QtGui.QHBoxLayout()

        leftColumnLayout = QtGui.QFormLayout()
        middleColumnLayout = QtGui.QFormLayout()
        rightColumnLayout = QtGui.QFormLayout()

        # Add elements into columns
        space_dict = {'leftColumn': leftColumnLayout,
                      'rightColumn': rightColumnLayout,
                      'middleColumn': middleColumnLayout,
                      'topRow': topRowLayout,
                      'bottomRow': bottomRowLayout}
        for label in elements_container.labels_name_postfix_and_text:
            for space in space_dict:
                if label[2] == space:
                    row_right = list()
                    rowLayout = QtGui.QHBoxLayout()
                    if label.__len__() > 3:
                        for _ in [self.line_edits, self.buttons, self.radiobuttons]:
                            for key in _.viewkeys():
                                if key in label[3:]:
                                    row_right.append(_[str(key)])
                    if row_right:
                        for row in row_right:
                            rowLayout.addWidget(row)
                    if type(space_dict[space]) is QtGui.QHBoxLayout:
                        space_dict[space].addWidget(self.labels[str('label') + label[0]])
                        space_dict[space].addLayout(rowLayout)
                    elif type(space_dict[space]) is QtGui.QFormLayout:
                        space_dict[space].addRow(self.labels[str('label') + label[0]], rowLayout)

        for _ in [leftColumnLayout, middleColumnLayout, rightColumnLayout]:
            middleRowLayout.addLayout(_)

        for _ in [topRowLayout, middleRowLayout, bottomRowLayout]:
            self.mainLayout.addLayout(_)

    def selectfileurban(self):
        self.line_edits['lineEditUrbanImage'].setText(self.fileDialog.getOpenFileName())

    def selectfileroaddata(self):
        self.line_edits['lineEditRoadDataImage'].setText(self.fileDialog.getOpenFileName())

    def selectfilelandusedata(self):
        self.line_edits['lineEditLanduseDataImage'].setText(self.fileDialog.getOpenFileName())

    def selectfileexcludeddata(self):
        self.line_edits['lineEditExcludedDataImage'].setText(self.fileDialog.getOpenFileName())

    def selectfileslopedata(self):
        self.line_edits['lineEditSlopeDataImage'].setText(self.fileDialog.getOpenFileName())

    def selectfilebackgrounddata(self):
        self.line_edits['lineEditBackgroundDataImage'].setText(self.fileDialog.getOpenFileName())

    def buttonOutputFilesColorSettingsClicked(self):
        Window.WindowOutputFilesColorSettings.w.show()

    def buttonDeltatronAgingColortableClicked(self):
        Window.WindowDeltatronAgingColortable.w.show()

    def buttonProbabilityColorSettingsClicked(self):
        Window.WindowProbabilityColortableForUrbanGrowth.w.show()

    def __init__(self):
        # Interface initialisation

        w = QtGui.QWidget()
        w.resize(1024, 798)
        w.move(0, 0)
        w.setWindowTitle('SleuthUI')

        # Initialization methods
        self._populate_window()
        self._set_layouts()
        self._set_button_functions()

        w.setLayout(self.mainLayout)
        w.show()

        # DEBUG CODE

        self.fileDialog = QtGui.QFileDialog
        sys.exit(self.app.exec_())
