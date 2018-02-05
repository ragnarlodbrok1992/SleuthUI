import sys
from PyQt4 import QtGui, QtCore
import window_output_files_color_settings
import window_deltatron_aging_colortable
import window_probability_colortable_for_urban_growth
import elements_container
from configuration.scenario_file_creator import ScenarioCreator
import os
import subprocess
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

        self.scenario_creator = ScenarioCreator()

        w = QtGui.QWidget()
        w.resize(1024, 798)
        w.move(0, 0)
        w.setWindowTitle('SleuthUI')

        # Window class input and output dir
        self.input_dir = str()
        self.output_dir = str()

        # Initialization methods
        self._populate_window()
        self._set_layouts()
        self._set_button_functions()
        self._populate_default_values()

        w.setLayout(self.mainLayout)
        w.show()

        # DEBUG CODE

        self.fileDialog = QtGui.QFileDialog

        sys.exit(self.app.exec_())

    def _populate_default_values(self):
        default_sleuth_location = "Sleuth3\\Scenarios\\"

        # Input and output paths
        # print(self.scenario_creator.input_dir)
        # print(self.scenario_creator.output_dir)
        # print(os.path.abspath(default_sleuth_location + self.scenario_creator.input_dir))
        # print(os.path.abspath(default_sleuth_location + self.scenario_creator.output_dir))

        self.input_dir = os.path.abspath(default_sleuth_location + self.scenario_creator.input_dir)
        self.output_dir = os.path.abspath(default_sleuth_location + self.scenario_creator.output_dir)

        self.line_edits['lineEditDataDirectory'].setText(str(self.input_dir))
        self.line_edits['lineEditOutputDirectory'].setText(str(self.output_dir))

        # Line Edits - files
        self.line_edits['lineEditUrbanImage'].setText(str(self.scenario_creator.urban_data))
        self.line_edits['lineEditRoadDataImage'].setText(str(self.scenario_creator.road_data))
        self.line_edits['lineEditLanduseDataImage'].setText(str(self.scenario_creator.landuse_data))
        self.line_edits['lineEditExcludedDataImage'].setText(str(self.scenario_creator.excluded_data))
        self.line_edits['lineEditSlopeDataImage'].setText(str(self.scenario_creator.slope_data))
        self.line_edits['lineEditBackgroundDataImage'].setText(str(self.scenario_creator.background_data))

        # Line Edits
        self.line_edits['lineEditStartDate'].setText(str(self.scenario_creator.prediction_start_date))
        self.line_edits['lineEditStopDate'].setText(str(self.scenario_creator.prediction_stop_date))

        # Line Edits - coefficients
        self.line_edits['lineEditCalibDiffStart'].setText(str(self.scenario_creator.calibration_diffusion_start))
        self.line_edits['lineEditCalibDiffStep'].setText(str(self.scenario_creator.calibration_diffusion_step))
        self.line_edits['lineEditCalibDiffStop'].setText(str(self.scenario_creator.calibration_diffusion_stop))
        self.line_edits['lineEditCalibBreedStart'].setText(str(self.scenario_creator.calibration_breed_start))
        self.line_edits['lineEditCalibBreedStep'].setText(str(self.scenario_creator.calibration_breed_step))
        self.line_edits['lineEditCalibBreedStop'].setText(str(self.scenario_creator.calibration_breed_stop))
        self.line_edits['lineEditCalibSpreadStart'].setText(str(self.scenario_creator.calibration_spread_start))
        self.line_edits['lineEditCalibSpreadStep'].setText(str(self.scenario_creator.calibration_spread_step))
        self.line_edits['lineEditCalibSpreadStop'].setText(str(self.scenario_creator.calibration_spread_stop))
        self.line_edits['lineEditCalibSlopeStart'].setText(str(self.scenario_creator.calibration_slope_start))
        self.line_edits['lineEditCalibSlopeStep'].setText(str(self.scenario_creator.calibration_slope_step))
        self.line_edits['lineEditCalibSlopeStop'].setText(str(self.scenario_creator.calibration_slope_stop))
        self.line_edits['lineEditCalibRoadStart'].setText(str(self.scenario_creator.calibration_road_start))
        self.line_edits['lineEditCalibRoadStep'].setText(str(self.scenario_creator.calibration_road_step))
        self.line_edits['lineEditCalibRoadStop'].setText(str(self.scenario_creator.calibration_road_stop))
        self.line_edits['lineEditPredDiffBestFit'].setText(str(self.scenario_creator.prediction_diffustion_best_fit))
        self.line_edits['lineEditPredBreedBestFit'].setText(str(self.scenario_creator.prediction_breed_best_fit))
        self.line_edits['lineEditPredSpreadBestFit'].setText(str(self.scenario_creator.prediction_spread_best_fit))
        self.line_edits['lineEditPredSlopeBestFit'].setText(str(self.scenario_creator.prediction_slope_best_fit))
        self.line_edits['lineEditPredRoadBestFit'].setText(str(self.scenario_creator.prediction_road_best_fit))

        # Line Edits - self modification parameters
        self.line_edits['lineEditRoadGravSensitivity'].setText(str(self.scenario_creator.road_grav_sensitivity))
        self.line_edits['lineEditSlopeSensitivity'].setText(str(self.scenario_creator.slope_sensitivity))
        self.line_edits['lineEditCriticalLow'].setText(str(self.scenario_creator.critical_low))
        self.line_edits['lineEditCriticalHigh'].setText(str(self.scenario_creator.critical_high))
        self.line_edits['lineEditCriticalSlope'].setText(str(self.scenario_creator.critical_slope))
        self.line_edits['lineEditBoom'].setText(str(self.scenario_creator.boom))
        self.line_edits['lineEditBust'].setText(str(self.scenario_creator.bust))

        # Radio Buttons
        if self.scenario_creator.write_color_key_images is "yes" or "YES":
            self.radiobuttons['checkBoxColorKeyImages'].setChecked(True)
        if self.scenario_creator.animation is "yes" or "YES":
            self.radiobuttons['checkBoxAnimation'].setChecked(True)
        if self.scenario_creator.view_growth_types is "yes" or "YES":
            self.radiobuttons['checkBoxViewGrowthTypes'].setChecked(True)
        if self.scenario_creator.echo is "yes" or "YES":
            self.radiobuttons['checkBoxECHO'].setChecked(True)
        if self.scenario_creator.write_coeff_file is "yes" or "YES":
            self.radiobuttons['checkBoxCOEFFile'].setChecked(True)
        if self.scenario_creator.write_avg_file is "yes" or "YES":
            self.radiobuttons['checkBoxAVGFile'].setChecked(True)
        if self.scenario_creator.write_std_dev_file is "yes" or "YES":
            self.radiobuttons['checkBoxSTDDEVFile'].setChecked(True)
        if self.scenario_creator.write_memory_map is "yes" or "YES":
            self.radiobuttons['checkBoxMEMORYMap'].setChecked(True)
        if self.scenario_creator.logging is "yes" or "YES":
            self.radiobuttons['checkBoxLOGGING'].setChecked(True)
        if self.scenario_creator.log_landclass_summary is "yes" or "YES":
            self.radiobuttons['checkBoxLogLandclassSummary'].setChecked(True)
        if self.scenario_creator.log_slope_weights is "yes" or "YES":
            self.radiobuttons['checkBoxLogSlopeWeight'].setChecked(True)
        if self.scenario_creator.log_reads is "yes" or "YES":
            self.radiobuttons['checkBoxLogReads'].setChecked(True)
        if self.scenario_creator.log_writes is "yes" or "YES":
            self.radiobuttons['checkBoxLogWrites'].setChecked(True)
        if self.scenario_creator.log_colortables is "yes" or "YES":
            self.radiobuttons['checkBoxLogColortables'].setChecked(True)
        if self.scenario_creator.log_transition_matrix is "yes" or "YES":
            self.radiobuttons['checkBoxLogTransitionMatrix'].setChecked(True)
        if self.scenario_creator.log_urbanization_attempts is "yes" or "YES":
            self.radiobuttons['checkBoxLogUrbanizationAttempts'].setChecked(True)
        if self.scenario_creator.log_initial_coefficients is "yes" or "YES":
            self.radiobuttons['checkBoxLogInitialCoefficients'].setChecked(True)
        if self.scenario_creator.log_base_statistics is "yes" or "YES":
            self.radiobuttons['checkBoxLogBaseStatistics'].setChecked(True)
        if self.scenario_creator.log_debug is "yes" or "YES":
            self.radiobuttons['checkBoxLogDebug'].setChecked(True)
        if self.scenario_creator.log_processing_status is "yes" or "YES":
            self.radiobuttons['checkBoxLogProcessingStatus'].setChecked(True)
        if self.scenario_creator.log_timings is "yes" or "YES":
            self.radiobuttons['checkBoxLogTimings'].setChecked(True)
        if self.scenario_creator.num_working_grids is "yes" or "YES":
            self.radiobuttons['checkBoxWorkingGrids'].setChecked(True)
        if self.scenario_creator.random_seed is "yes" or "YES":
            self.radiobuttons['checkBoxRandomSeed'].setChecked(True)
        if self.scenario_creator.monte_carlo_iterations is "yes" or "YES":
            self.radiobuttons['checkBoxMontecarloIterations'].setChecked(True)
        # if self.scenario_creator.is "yes" or "YES":
        #     self.radiobuttons['checkBoxAuxDiffusionMult'].setChecked(True)
        # if is "yes" or "YES":
        #     self.radiobuttons['checkBoxAuxDiffusionCoeff'].setChecked(True)
        # if is "yes" or "YES":
        #     self.radiobuttons['checkBoxAuxBreedCoeff'].setChecked(True)
        # if is "yes" or "YES":
        #     self.radiobuttons['checkBoxWriteRatioFile'].setChecked(True)
        # if is "yes" or "YES":
        #     self.radiobuttons['checkBoxWriteSlopeFile'].setChecked(True)
        # if is "yes" or "YES":
        #     self.radiobuttons['checkBoxWriteXYPointsFile'].setChecked(True)
        if self.scenario_creator.view_deltatron_aging is "yes" or "YES":
            self.radiobuttons['checkBoxViewDeltatronAging'].setChecked(True)
        if self.scenario_creator.write_color_key_images is "yes" or "YES":
            self.radiobuttons['checkBoxWriteColorKeyImages'].setChecked(True)
        if self.scenario_creator.animation is "yes" or "YES":
            self.radiobuttons['checkBoxAnimation'].setChecked(True)

    def _run_cygwin(self, path_to_scenario_dir):
        print(path_to_scenario_dir)
        if self.radiobuttons['checkBoxCalibrate'].checkState():

            print("DEBUG: Calibration!")
            print("Scenario file: " + os.path.basename(path_to_scenario_dir))
            print(os.getcwd())

            os.chdir(os.path.dirname(path_to_scenario_dir))
            p = subprocess.Popen("../grow.exe calibrate " + os.path.basename(path_to_scenario_dir))
            p.wait()
            out, err = p.communicate()

        if self.radiobuttons['checkBoxPredict'].checkState():

            print("DEBUG: Prediction!")
            print("Scenario file: " + os.path.basename(path_to_scenario_dir))
            print(os.getcwd())

            os.chdir(os.path.dirname(path_to_scenario_dir))
            p = subprocess.Popen("../grow.exe predict " + os.path.basename(path_to_scenario_dir))
            p.wait()
            out, err = p.communicate()

    def _run_simulation(self, path_to_scenario_dir):

        # Saving changed values
        # TODO: Saving function

        self.scenario_creator.save_to_file(path_to_scenario_dir)
        return self._run_cygwin(path_to_scenario_dir)

        # Debug:
        # print "DEBUG!: " + str(path_to_scenario_dir)

    def _set_button_functions(self):
        # Buttons bottom for control

        # Buttons for files
        self.buttons['buttonUrbanDataImage'].clicked.connect(lambda: self.select_files('lineEditUrbanImage'))
        self.buttons['buttonRoadDataImage'].clicked.connect(lambda: self.select_files('lineEditRoadDataImage'))
        self.buttons['buttonLanduseDataImage'].clicked.connect(lambda: self.select_files('lineEditLanduseDataImage'))
        self.buttons['buttonExcludedDataImage'].clicked.connect(lambda: self.select_files('lineEditExcludedDataImage'))
        self.buttons['buttonSlopeDataImage'].clicked.connect(lambda: self.select_files('lineEditSlopeDataImage'))
        self.buttons['buttonBackgroundDataImage'].clicked.connect(lambda: self.select_files('lineEditBackgroundDataImage'))

        # Run simulation button
        self.buttons['buttonRun'].clicked.connect(lambda: self._run_simulation(str(os.path.dirname(__file__) + "\\Sleuth3\\Scenarios\\scenario.debug_calibrate")))

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


if __name__ == "__main__":
    pass
