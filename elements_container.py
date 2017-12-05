'''
Elements container.
Contains information about GUI elements, like variables names, labels, and other elements.
Logic how to setup is in _populate_window method of every window class file.
'''

# Setting radiobuttons
radiobuttons_name_prefix = 'checkBox'
radiobuttons_name_postfix = [('ColorKeyImages', ''),
                             ('Animation', ''),
                             ('ViewGrowthTypes', ''),
                             ('ECHO', ''),
                             ('COEFFile', ''),
                             ('AVGFile', ''),
                             ('STDDEVFile', ''),
                             ('MEMORYMap', ''),
                             ('LOGGING', ''),
                             ('LogLandclassSummary', ''),
                             ('LogSlopeWeight', ''),
                             ('LogReads', ''),
                             ('LogWrites', ''),
                             ('LogColortables', ''),
                             ('LogTransitionMatrix', ''),
                             ('LogUrbanizationAttempts', ''),
                             ('LogInitialCoefficients', ''),
                             ('LogBaseStatistics', ''),
                             ('LogDebug', ''),
                             ('LogProcessingStatus', ''),
                             ('LogTimings', ''),
                             ('WorkingGrids', ''),
                             ('RandomSeed', ''),
                             ('MontecarloIterations', ''),
                             ('AuxDiffusionMult', ''),
                             ('AuxDiffusionCoeff', ''),
                             ('AuxBreedCoeff', ''),
                             ('WriteRatioFile', ''),
                             ('WriteSlopeFile', ''),
                             ('WriteXYPointsFile', ''),
                             ('ViewDeltatronAging', ''),
                             ('WriteColorKeyImages', ''),
                             ('Animation', '')]

# Setting buttons
buttons_name_prefix = 'button'
# Variable name, label on button, bound layout
buttons_name_postfix_and_text = [('UrbanDataImage', 'Wybierz z dysku'),
                                 ('RoadDataImage', 'Wybierz z dysku'),
                                 ('LanduseDataImage', 'Wybierz z dysku'),
                                 ('ExcludedDataImage', 'Wybierz z dysku'),
                                 ('SlopeDataImage', 'Wybierz z dysku'),
                                 ('BackgroundDataImage', 'Wybierz z dysku'),
                                 ('OutputFilesColorSettings',
                                  'Output File Color Settings',
                                  'labelColorsSettingsButtons',
                                  ''),
                                 ('ProbabilityColorSettings',
                                  'Probability Colortable Color Settings',
                                  'labelColorsSettingsButtons',
                                  ''),
                                 ('DeltatronAgingColortable',
                                  'Color settings for deltatron aging',
                                  'labelColorsSettingsButtons',
                                  ''),
                                 ('Save', 'Save'),
                                 ('Exit', 'Exit')]

# Setting labels
# Attach element to label
labels_name_prefix = 'label'
labels_name_postfix_and_text = [('SleuthModel', 'SLEUTH Model: ', 'topRow', 'lineEditSleuthModelName'),
                                ('Simulation', 'SIMULATION: ', 'topRow', 'lineEditSimulation'),
                                ('ModelDate', 'Model date: ', 'topRow', 'lineEditModelDate'),
                                ('SimulationDate', 'Simulation date: ', 'topRow', 'lineEditSimulationDate'),
                                ('InputOutputDirectoryMain', 'INput / OUTput DIRECTORY', 'leftColumn'),
                                ('DataDirectory', 'DATA DIRECTORY: ', 'leftColumn', 'lineEditDataDirectory'),
                                ('OutputDirectory', 'OUTPUT DIRECTORY: ', 'leftColumn', 'lineEditOutputDirectory'),
                                ('PredictionRange', 'PREDICTION RANGE', 'middleColumn'),
                                ('RunningStatusVariables', 'RUNNING status & variables', 'rightColumn'),
                                ('StartDate', 'START Date: ', 'middleColumn', 'lineEditStartDate'),
                                ('StopDate', 'STOP Date: ', 'middleColumn', 'lineEditStopDate'),
                                ('Coefficients', 'COEFFICIENTS', 'middleColumn'),
                                ('GrowthTypePrintWindow', 'GROWTH TYPE PRINT WINDOW', 'leftColumn',
                                 'lineEditStartRun', 'lineEditEndRun', 'lineEditStartMc', 'lineEditEndMc',
                                 'lineEditStartYear', 'lineEditEndYear'),
                                ('Echo', 'ECHO', 'rightColumn', 'checkBoxECHO'),
                                ('COEFFile', 'COEF File', 'rightColumn', 'checkBoxCOEFFile'),
                                ('AVGFile', 'AVG File', 'rightColumn', 'checkBoxAVGFile'),
                                ('STDDEVFile', 'STD DEV file', 'rightColumn', 'checkBoxSTDDEVFile'),
                                ('MEMORYmap', 'MEMORY map', 'rightColumn', 'checkBoxMEMORYMap'),
                                ('LOGGING', 'LOGGING', 'rightColumn', 'checkBoxLOGGING'),
                                ('LogFilePreferences', 'LOG FILE preferences', 'rightColumn'),
                                ('UrbanImage', 'Urban image: ', 'leftColumn',
                                 'lineEditUrbanImage', 'buttonUrbanDataImage'),
                                ('RoadDataImage', 'Road data image: ', 'leftColumn',
                                 'lineEditRoadDataImage', 'buttonRoadDataImage'),
                                ('LanduseDataImage', 'Land use data image: ', 'leftColumn',
                                 'lineEditLanduseDataImage', 'buttonLanduseDataImage'),
                                ('ExcludedDataImage', 'Excluded data image: ', 'leftColumn',
                                 'lineEditExcludedDataImage', 'buttonExcludedDataImage'),
                                ('SlopeDataImage', 'Slope data image: ', 'leftColumn',
                                 'lineEditSlopeDataImage', 'buttonSlopeDataImage'),
                                ('BackgroundDataImage', 'Background data image: ', 'leftColumn',
                                 'lineEditBackgroundDataImage', 'buttonBackgroundDataImage'),
                                ('CalibDiffStart', 'CALIBRATION_DIFFUSION_START', 'middleColumn',
                                 'lineEditCalibDiffStart'),
                                ('CalibDiffStep', 'CALIBRATION_DIFFUSTION_STEP', 'middleColumn',
                                 'lineEditCalibDiffStep'),
                                ('CalibDiffStop', 'CALIBRATION_DIFFUSTION_STOP', 'middleColumn',
                                 'lineEditCalibDiffStop'),
                                ('CalibBreedStart', 'CALIBRATION_BREED_START', 'middleColumn',
                                 'lineEditCalibBreedStart'),
                                ('CalibBreedStep', 'CALIBRATION_BREED_STEP', 'middleColumn',
                                 'lineEditCalibBreedStep'),
                                ('CalibBreedStop', 'CALIBRATION_BREED_STOP', 'middleColumn',
                                 'lineEditCalibBreedStop'),
                                ('CalibSpreadStart', 'CALIBRATION_SPREAD_START', 'middleColumn',
                                 'lineEditCalibSpreadStart'),
                                ('CalibSpreadStep', 'CALIBRATION_SPREAD_STEP', 'middleColumn',
                                 'lineEditCalibSpreadStep'),
                                ('CalibSpreadStop', 'CALIBRATION_SPREAD_STOP', 'middleColumn',
                                 'lineEditCalibSpreadStop'),
                                ('CalibSlopeStart', 'CALIBRATION_SLOPE_START', 'middleColumn',
                                 'lineEditCalibSlopeStart'),
                                ('CalibSlopeStep', 'CALIBRATION_SLOPE_STEP', 'middleColumn',
                                 'lineEditCalibSlopeStep'),
                                ('CalibSlopeStop', 'CALIBRATION_SLOPE_STOP', 'middleColumn',
                                 'lineEditCalibSlopeStop'),
                                ('CalibRoadStart', 'CALIBRATION_ROAD_START', 'middleColumn',
                                 'lineEditCalibRoadStart'),
                                ('CalibRoadStep', 'CALIBRATION_ROAD_STEP', 'middleColumn',
                                 'lineEditCalibRoadStep'),
                                ('CalibRoadStop', 'CALIBRATION_ROAD_STOP', 'middleColumn',
                                 'lineEditCalibRoadStop'),
                                ('PredDiffBestFit', 'PREDICTION_DIFFUSION_BEST_FIT', 'middleColumn',
                                 'lineEditPredDiffBestFit'),
                                ('PredBreedBestFit', 'PREDICTION_BREED_BEST_FIT', 'middleColumn',
                                 'lineEditPredBreedBestFit'),
                                ('PredSpreadBestFit', 'PREDICTION_SPREAD_BEST_FIT', 'middleColumn',
                                 'lineEditPredSpreadBestFit'),
                                ('PredSlopeBestFit', 'PREDICTION_SLOPE_BEST_FIT', 'middleColumn',
                                 'lineEditPredSlopeBestFit'),
                                ('PredRoadBestFit', 'PREDICTION_ROAD_BEST_FIT', 'middleColumn',
                                 'lineEditPredRoadBestFit'),
                                ('SelfModificationParameters', 'SELF-MODIFICATION PARAMETERS', 'middleColumn'),
                                ('RoadGravSensitivity', 'ROAD_GRAV_SENSITIVITY', 'middleColumn',
                                 'lineEditRoadGravSensitivity'),
                                ('SlopeSensitivity', 'SLOPE_SENSITIVITY', 'middleColumn', 'lineEditSlopeSensitivity'),
                                ('CriticalLow', 'CRITICAL_LOW', 'middleColumn', 'lineEditCriticalLow'),
                                ('CriticalHigh', 'CRITICAL_HIGH', 'middleColumn', 'lineEditCriticalHigh'),
                                ('CriticalSlope', 'CRITICAL_SLOPE', 'middleColumn', 'lineEditCriticalSlope'),
                                ('Boom', 'BOOM', 'middleColumn', 'lineEditBoom'),
                                ('Bust', 'BUST', 'middleColumn', 'lineEditBust'),
                                ('LogLandclassSummary', 'LOG_LANDCLASS_SUMMARY', 'rightColumn',
                                 'checkBoxLogLandclassSummary'),
                                ('LogSlopeWeight', 'LOG_SLOPE_WEIGHT', 'rightColumn', 'checkBoxLogSlopeWeight'),
                                ('LogReads', 'LOG_READS', 'rightColumn', 'checkBoxLogReads'),
                                ('LogWrites', 'LOG_WRITES', 'rightColumn', 'checkBoxLogWrites'),
                                ('LogColortables', 'LOG_COLORTABLES', 'rightColumn', 'checkBoxLogColortables'),
                                ('LogTransitionMatrix', 'LOG_TRANSITION_MATRIX', 'rightColumn',
                                 'checkBoxLogTransitionMatrix'),
                                ('LogUrbanizationAttempts', 'LOG_URBANIZATION_ATTEMPTS', 'rightColumn',
                                 'checkBoxLogUrbanizationAttempts'),
                                ('LogInitialCoefficients', 'LOG_INITIAL_COEFFICIENTS', 'rightColumn',
                                 'checkBoxLogInitialCoefficients'),
                                ('LogBaseStatistics', 'LOG_BASE_STATISTICS', 'rightColumn',
                                 'checkBoxLogBaseStatistics'),
                                ('LogDebug', 'LOG_DEBUG', 'rightColumn', 'checkBoxLogDebug'),
                                ('LogProcessingStatus', 'LOG_PROCESSING_STATUS', 'rightColumn',
                                 'checkBoxLogProcessingStatus'),
                                ('LogTimings', 'LOG_TIMINGS', 'rightColumn', 'checkBoxLogTimings'),
                                ('WorkingGrids', 'WORKING GRIDS', 'rightColumn', 'checkBoxWorkingGrids'),
                                ('RandomSeed', 'RANDOM SEED', 'rightColumn', 'checkBoxRandomSeed'),
                                ('MontecarloIterations', 'MONTECARLO ITERATIONS', 'rightColumn',
                                 'checkBoxMontecarloIterations'),
                                ('AuxDiffusionMult', 'AUX_DIFFUSION_MULT', 'rightColumn', 'checkBoxAuxDiffusionMult'),
                                ('AuxDiffusionCoeff', 'AUX_DIFFUSION_COEFF', 'rightColumn',
                                 'checkBoxAuxDiffusionCoeff'),
                                ('AuxBreedCoeff', 'AUX_BREED_COEFF', 'rightColumn', 'checkBoxAuxBreedCoeff'),
                                ('WriteRatioFile', 'WRITE_RATIO_FILE', 'rightColumn', 'checkBoxWriteRatioFile'),
                                ('WriteSlopeFile', 'WRITE_SLOPE_FILE', 'rightColumn', 'checkBoxWriteSlopeFile'),
                                ('WriteXYPointsFile', 'WRITE_XYPOINTS_FILE', 'rightColumn',
                                 'checkBoxWriteXYPointsFile'),
                                ('DeltatronAgingSection', 'DELTATRON_AGING_SECTION', 'rightColumn'),
                                ('ColorSettingsButtons', 'Color settings buttons: ', 'bottomRow',
                                 'buttonOutputFilesColorSettings', 'buttonProbabilityColorSettings',
                                 'buttonDeltatronAgingColortable'),
                                ('ViewDeltatronAging', 'VIEW_DELTATRON_AGING', 'rightColumn',
                                 'checkBoxViewDeltatronAging'),
                                ('OutputImages', 'OUTPUT IMAGES', 'leftColumn'),
                                ('WriteColorKeyImages', 'WRITE COLOR KEY IMAGES',
                                'leftColumn', 'checkBoxColorKeyImages'),
                                ('Animation', 'ANIMATION', 'leftColumn', 'checkBoxAnimation'),
                                ('ViewGrowthTypes', 'VIEW GROWTH TYPES (YES/NO)',
                                'leftColumn', 'checkBoxViewGrowthTypes'),
                                ('DeltatronPrintWindow', 'DELTATRON_PRINT_WINDOW', 'rightColumn'),
                                ('Save', 'Save: ', 'bottomBottomRow', 'buttonSave'),
                                ('Exit', 'Exit: ', 'bottomBottomRow', 'buttonExit'),
                                ]

labels_qt_align_center = ['labelInputOutputDirectoryMain',
                          'labelPredictionRange',
                          'labelRunningStatusVariables',
                          'labelCoefficients',
                          'labelLogFilePreferences',
                          'labelSelfModificationParameters',
                          'labelDeltatronAgingSection']

# Setting lineEdits
line_edits_name_prefix = 'lineEdit'
# Variable name, label of lineEdit, width, length, bound layout
line_edits_name_postfix_and_text_width_maxlength = [('SleuthModelName', 'Nazwa modelu', None, None),
                                                    ('Simulation', 'Nazwa scenariusza', None, None),
                                                    ('ModelDate', '1.1.1970', 70, 10),
                                                    ('SimulationDate', '1.1.1970', 70, 10),
                                                    ('DataDirectory', '', None, None),
                                                    ('OutputDirectory', '', None, None),
                                                    ('StartDate', '', None, None),
                                                    ('StopDate', '', None, None),
                                                    ('StartRun', 'Start run', None, None),
                                                    ('EndRun', 'End run', None, None),
                                                    ('StartMc', 'Start mc', None, None),
                                                    ('EndMc', 'End mc', None, None),
                                                    ('StartYear', 'Start year', None, None),
                                                    ('EndYear', 'End year', None, None),
                                                    ('StartRunDeltatron', 'Start run', None, None),
                                                    ('EndRunDeltatron', 'End run', None, None),
                                                    ('StartMcDeltatron', 'Start mc', None, None),
                                                    ('EndMcDeltatron', 'End mc', None, None),
                                                    ('StartYearDeltatron', 'Start year', None, None),
                                                    ('EndYearDeltatron', 'End year', None, None),
                                                    ('UrbanImage', '', None, None),
                                                    ('RoadDataImage', '', None, None),
                                                    ('LanduseDataImage', '', None, None),
                                                    ('ExcludedDataImage', '', None, None),
                                                    ('SlopeDataImage', '', None, None),
                                                    ('BackgroundDataImage', '', None, None),
                                                    ('CalibDiffStart', '', 30, 3),
                                                    ('CalibDiffStep', '', 30, 3),
                                                    ('CalibDiffStop', '', 30, 3),
                                                    ('CalibBreedStart', '', 30, 3),
                                                    ('CalibBreedStep', '', 30, 3),
                                                    ('CalibBreedStop', '', 30, 3),
                                                    ('CalibSpreadStart', '', 30, 3),
                                                    ('CalibSpreadStep', '', 30, 3),
                                                    ('CalibSpreadStop', '', 30, 3),
                                                    ('CalibSlopeStart', '', 30, 3),
                                                    ('CalibSlopeStep', '', 30, 3),
                                                    ('CalibSlopeStop', '', 30, 3),
                                                    ('CalibRoadStart', '', 30, 3),
                                                    ('CalibRoadStep', '', 30, 3),
                                                    ('CalibRoadStop', '', 30, 3),
                                                    ('PredDiffBestFit', '', 30, 3),
                                                    ('PredBreedBestFit', '', 30, 3),
                                                    ('PredSpreadBestFit', '', 30, 3),
                                                    ('PredSlopeBestFit', '', 30, 3),
                                                    ('PredRoadBestFit', '', 30, 3),
                                                    ('RoadGravSensitivity', '', 30, 3),
                                                    ('SlopeSensitivity', '', 30, 3),
                                                    ('CriticalLow', '', 30, 3),
                                                    ('CriticalHigh', '', 30, 3),
                                                    ('CriticalSlope', '', 30, 3),
                                                    ('Boom', '', 30, 3),
                                                    ('Bust', '', 30, 3)]
