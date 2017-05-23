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

    def _populate_window(self):

        # Setting radiobuttons
        self.radiobuttons = dict()
        radiobuttons_names = [''.join([elements_container.radiobuttons_name_prefix,
                                       elements_container.radiobuttons_name_postfix[x]])
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
        line_edits = dict()
        line_edits_names = [''.join([elements_container.line_edits_name_prefix,
                                     elements_container.line_edits_name_postfix_and_text_width_maxlength[x][0]])
                            for x in range(0, len(elements_container.line_edits_name_postfix_and_text_width_maxlength))]
        x = 0
        for name in line_edits_names:
            line_edits[name] = QtGui.QLineEdit()
            line_edits[name].setText(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][1])
            if elements_container.line_edits_name_postfix_and_text_width_maxlength[x][2] is not None:
                line_edits[name].setFixedWidth(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][2])
            if elements_container.line_edits_name_postfix_and_text_width_maxlength[x][3] is not None:
                line_edits[name].setMaxLength(elements_container.line_edits_name_postfix_and_text_width_maxlength[x][3])
            x += 1
        del x

    def _set_layouts(self):
        pass

    def __init__(self):
        # Interface initialisation

        w = QtGui.QWidget()
        w.resize(1024, 798)
        w.move(0, 0)
        w.setWindowTitle('SleuthUI')

        self._populate_window()

        self._set_layouts()

        w.show()

        sys.exit(self.app.exec_())

    def outputFilesColorSettingsButtonClicked(self):
        Window.WindowOutputFilesColorSettings.w.show()

    def deltatronAgingColortableButtonClicked(self):
        Window.WindowDeltatronAgingColortable.w.show()

    def probabilityColortableForUrbanGrowthClicked(self):
        Window.WindowProbabilityColortableForUrbanGrowth.w.show()
