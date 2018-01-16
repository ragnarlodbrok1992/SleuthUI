import sys
from PyQt4 import QtGui, QtCore
import window_output_files_color_settings
import window_deltatron_aging_colortable
import window_probability_colortable_for_urban_growth
import elements_container
from pprint import pprint

__author__ = 'Maciej Oliwa'


class Window(object):
    app = QtGui.QApplication(sys.argv)
    WindowOutputFilesColorSettings = window_output_files_color_settings. \
        WindowOutputFilesColorSettings(app)
    WindowDeltatronAgingColortable = window_deltatron_aging_colortable. \
        WindowDeltatronAgingColortable(app)
    WindowProbabilityColortableForUrbanGrowth = window_probability_colortable_for_urban_growth. \
        WindowProbabilityColortableForUrbanGrowth(app)

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

    def _set_button_functions(self):
        # Buttons bottom for control

        # Buttons for files
        self.buttons['buttonUrbanDataImage'].clicked.connect(lambda: self.select_files('lineEditUrbanImage'))
        self.buttons['buttonRoadDataImage'].clicked.connect(lambda: self.select_files('lineEditRoadDataImage'))
        self.buttons['buttonLanduseDataImage'].clicked.connect(lambda: self.select_files('lineEditLanduseDataImage'))
        self.buttons['buttonExcludedDataImage'].clicked.connect(lambda: self.select_files('lineEditExcludedDataImage'))
        self.buttons['buttonSlopeDataImage'].clicked.connect(lambda: self.select_files('lineEditSlopeDataImage'))
        self.buttons['buttonBackgroundDataImage'].clicked.connect(lambda: self.select_files('lineEditBackgroundDataImage'))

        # Buttons new window functions
        self.buttons['buttonOutputFilesColorSettings']\
            .clicked\
            .connect(lambda: self.button_new_window_clicked('OutputFilesColorSettings'))
        self.buttons['buttonDeltatronAgingColortable']\
            .clicked\
            .connect(lambda: self.button_new_window_clicked('ProbabilityColorSettings'))
        self.buttons['buttonProbabilityColorSettings']\
            .clicked\
            .connect(lambda: self.button_new_window_clicked('ProbabilityColorSettings'))

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
        BUTTON_NAME = 0
        buttons_names = [''.join([elements_container.buttons_name_prefix,
                                  elements_container.buttons_name_postfix_and_text[x][BUTTON_NAME]])
                         for x in range(0, len(elements_container.buttons_name_postfix_and_text))]
        x = 0

        BUTTON_LABEL = 1
        for name in buttons_names:
            self.buttons[name] = QtGui.QPushButton()
            self.buttons[name].setText(elements_container.buttons_name_postfix_and_text[x][BUTTON_LABEL])
            x += 1
        del x, BUTTON_NAME, BUTTON_LABEL

        # Setting labels
        self.labels = dict()
        LABEL_NAME = 0
        labels_names = [''.join([elements_container.labels_name_prefix,
                                 elements_container.labels_name_postfix_and_text[x][LABEL_NAME]])
                        for x in range(0, len(elements_container.labels_name_postfix_and_text))]
        x = 0
        LABEL_LABEL = 1
        for name in labels_names:
            self.labels[name] = QtGui.QLabel()
            self.labels[name].setText(elements_container.labels_name_postfix_and_text[x][LABEL_LABEL])
            x += 1
        del x, LABEL_NAME, LABEL_LABEL

        # Setting label alignments
        for name in elements_container.labels_qt_align_center:
            self.labels[name].setAlignment(QtCore.Qt.AlignCenter)

        # Setting lineEdits
        x = 0
        self.line_edits = dict()
        LINE_EDIT_NAME = 0
        line_edits_names = [''.join([elements_container.line_edits_name_prefix,
                                     elements_container.line_edits_name_postfix_and_text_width_maxlength[x][LINE_EDIT_NAME]])
                            for x in range(0, len(elements_container.line_edits_name_postfix_and_text_width_maxlength))]
        del x, LINE_EDIT_NAME

        x = 0
        LINE_EDIT_LABEL, LINE_EDIT_FIXED_WIDTH, LINE_EDIT_MAX_LENGTH = 1, 2, 3
        for name in line_edits_names:
            self.line_edits[name] = QtGui.QLineEdit()
            self.line_edits[name].setText(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][LINE_EDIT_LABEL])
            if elements_container.line_edits_name_postfix_and_text_width_maxlength[x][LINE_EDIT_FIXED_WIDTH] is not None:
                self.line_edits[name].\
                    setFixedWidth(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][LINE_EDIT_FIXED_WIDTH])
            if elements_container.line_edits_name_postfix_and_text_width_maxlength[x][LINE_EDIT_MAX_LENGTH] is not None:
                self.line_edits[name].\
                    setMaxLength(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][LINE_EDIT_MAX_LENGTH])
            x += 1
        del x, LINE_EDIT_LABEL, LINE_EDIT_FIXED_WIDTH, LINE_EDIT_MAX_LENGTH

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

        topRightColumnLayout = QtGui.QHBoxLayout()
        middleRightColumnLayout = QtGui.QHBoxLayout()
        bottomRightColumnLayout = QtGui.QHBoxLayout()

        bottomBottomRowLayout = QtGui.QHBoxLayout()

        # Add elements into columns
        space_dict = {'leftColumn': leftColumnLayout,
                      'rightColumn': rightColumnLayout,
                      'middleColumn': middleColumnLayout,
                      'topRow': topRowLayout,
                      'bottomRow': bottomRowLayout,
                      'topRightColumn': topRightColumnLayout,
                      'middleRightColumnLayout': middleRightColumnLayout,
                      'bottomRightColumnLayout': bottomRightColumnLayout,
                      'bottomBottomRow': bottomBottomRowLayout}

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

        for _ in [topRightColumnLayout, middleRightColumnLayout, bottomRightColumnLayout]:
            rightColumnLayout.addRow(_)

        for _ in [leftColumnLayout, middleColumnLayout, rightColumnLayout]:
            middleRowLayout.addLayout(_)

        for _ in [topRowLayout, middleRowLayout, bottomRowLayout, bottomBottomRowLayout]:
            self.mainLayout.addLayout(_)

    def select_files(self, line_edit_name):
        files_text = self.fileDialog.getOpenFileNames()
        self.line_edits[line_edit_name].setText(files_text.join(' '))

    def button_new_window_clicked(self, window_name):
        if window_name == 'OutputFilesColorSettings':
            Window.WindowOutputFilesColorSettings.w.show()
        elif window_name == 'DeltatronAgingColortable':
            Window.WindowDeltatronAgingColortable.w.show()
        elif window_name == 'ProbabilityColorSettings':
            Window.WindowProbabilityColortableForUrbanGrowth.w.show()
