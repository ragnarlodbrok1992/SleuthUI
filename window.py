import PyQt4, sys
from PyQt4 import QtGui, QtCore

__author__ = 'Maciej Oliwa'


class Window:

    def __init__(self):
        # Interface initialisation
        app = QtGui.QApplication(sys.argv)

        w = QtGui.QWidget()
        w.resize(1024, 798)
        w.move(0, 0)
        w.setWindowTitle('SleuthUI')
        # Setting radiobuttons
        radioButtonWriteColorKeyImages = QtGui.QRadioButton()
        radioButtonAnimation = QtGui.QRadioButton()
        radioButtonViewGrowthTypes = QtGui.QRadioButton()

        radioButtonECHO = QtGui.QRadioButton()
        radioButtonCOEFFile = QtGui.QRadioButton()
        radioButtonAVGFile = QtGui.QRadioButton()
        radioButtonSTDDEVFile = QtGui.QRadioButton()
        radioButtonMEMORYMap = QtGui.QRadioButton()
        radioButtonLOGGING = QtGui.QRadioButton()

        # Setting buttons
        buttonUrbanDataImage = QtGui.QPushButton()
        buttonUrbanDataImage.setText("Wybierz z dysku")
        buttonRoadDataImage = QtGui.QPushButton()
        buttonRoadDataImage.setText("Wybierz z dysku")
        buttonLanduseDataImage = QtGui.QPushButton()
        buttonLanduseDataImage.setText("Wybierz z dysku")
        buttonExcludedDataImage = QtGui.QPushButton()
        buttonExcludedDataImage.setText("Wybierz z dysku")
        buttonSlopeDataImage = QtGui.QPushButton()
        buttonSlopeDataImage.setText("Wybierz z dysku")
        buttonBackgroundDataImage = QtGui.QPushButton()
        buttonBackgroundDataImage.setText("Wybierz z dysku")

        # Setting Labels
        labelSleuthModel = QtGui.QLabel()
        labelSimulation = QtGui.QLabel()
        labelModelDate = QtGui.QLabel()
        labelSimulationDate = QtGui.QLabel()
        labelInputOutputDirectoryMain = QtGui.QLabel()
        labelDataDirectory = QtGui.QLabel()
        labelOutputDirectory = QtGui.QLabel()
        labelPredictionRange = QtGui.QLabel()
        labelRunningStatusVariables = QtGui.QLabel()
        labelStartDate = QtGui.QLabel()
        labelStopDate = QtGui.QLabel()
        labelInputImages = QtGui.QLabel()
        labelOutputImages = QtGui.QLabel()
        labelCoefficients = QtGui.QLabel()
        labelSelfModificationParameters = QtGui.QLabel()
        labelLogFilePreferences = QtGui.QLabel()
        labelDeltatronAgingSection = QtGui.QLabel()
        labelWriteColorKeyImages = QtGui.QLabel()
        labelAnimation = QtGui.QLabel()
        labelViewGrowthTypes = QtGui.QLabel()
        labelGrowthTypePrintWindow = QtGui.QLabel()

        labelEcho = QtGui.QLabel()
        labelCOEFFile = QtGui.QLabel()
        labelAVGFile = QtGui.QLabel()
        labelSTDDEVFile = QtGui.QLabel()
        labelMEMORYmap = QtGui.QLabel()
        labelLOGGING = QtGui.QLabel()

        # Setting label input images
        labelUrbanImage = QtGui.QLabel()
        labelRoadDataImage = QtGui.QLabel()
        labelLanduseIDataImage = QtGui.QLabel()
        labelExcludedDataImage = QtGui.QLabel()
        labelSlopeDataImage = QtGui.QLabel()
        labelBackgroundDataImage = QtGui.QLabel()

        # Setting label coefficients
        labelCalibDiffStart = QtGui.QLabel()
        labelCalibDiffStep = QtGui.QLabel()
        labelCalibDiffStop = QtGui.QLabel()

        labelCalibBreedStart = QtGui.QLabel()
        labelCalibBreedStep = QtGui.QLabel()
        labelCalibBreedStop = QtGui.QLabel()

        labelCalibSpreadStart = QtGui.QLabel()
        labelCalibSpreadStep = QtGui.QLabel()
        labelCalibSpreadStop = QtGui.QLabel()

        labelCalibSlopeStart = QtGui.QLabel()
        labelCalibSlopeStep = QtGui.QLabel()
        labelCalibSlopeStop = QtGui.QLabel()

        labelCalibRoadStart = QtGui.QLabel()
        labelCalibRoadStep = QtGui.QLabel()
        labelCalibRoadStop = QtGui.QLabel()

        labelPredDiffBestFit = QtGui.QLabel()
        labelPredBreedBestFit = QtGui.QLabel()
        labelPredSpreadBestFit = QtGui.QLabel()
        labelPredSlopeBestFit = QtGui.QLabel()
        labelPredRoadBestFit = QtGui.QLabel()

        # Setting label self-modification parameters
        labelRoadGravSensitivity = QtGui.QLabel()
        labelSlopeSensitivity = QtGui.QLabel()
        labelCriticalLow = QtGui.QLabel()
        labelCriticalHigh = QtGui.QLabel()
        labelCriticalSlope = QtGui.QLabel()
        labelBoom = QtGui.QLabel()
        labelBust = QtGui.QLabel()

        # Setting label texts
        labelSleuthModel.setText("SLEUTH Model: ")
        labelSimulation.setText("SIMULATION: ")
        labelModelDate.setText("Model date: ")
        labelSimulationDate.setText("Simulation date: ")
        labelInputOutputDirectoryMain.setText("INput / OUTput DIRECTORY")
        labelDataDirectory.setText("DATA DIRECTORY: ")
        labelOutputDirectory.setText("OUTPUT DIRECTORY: ")
        labelPredictionRange.setText("PREDICTION RANGE")
        labelRunningStatusVariables.setText("RUNNING status & variables")
        labelStartDate.setText("START Date: ")
        labelStopDate.setText("STOP Date: ")
        labelInputImages.setText("INPUT IMAGES")
        labelOutputImages.setText("OUTPUT IMAGES")
        labelCoefficients.setText("COEFFICIENTS")
        labelSelfModificationParameters.setText("SELF-MODIFICATION PARAMETERS")
        labelLogFilePreferences.setText("LOG FILE preferences")
        labelDeltatronAgingSection.setText("DELTATRON AGING SECTION")
        labelWriteColorKeyImages.setText("WRITE COLOR KEY IMAGES")
        labelAnimation.setText("ANIMATION")
        labelViewGrowthTypes.setText("VIEW GROWTH TYPES(YES/NO)")
        labelGrowthTypePrintWindow.setText("GROWTH TYPE PRINT WINDOW")

        labelEcho.setText("ECHO")
        labelCOEFFile.setText("COEF file")
        labelAVGFile.setText("AVG file")
        labelSTDDEVFile.setText("STD DEV file")
        labelMEMORYmap.setText("MEMORY map")
        labelLOGGING.setText("LOGGING")

        # Setting label alignments
        labelInputOutputDirectoryMain.setAlignment(QtCore.Qt.AlignCenter)
        labelPredictionRange.setAlignment(QtCore.Qt.AlignCenter)
        labelRunningStatusVariables.setAlignment(QtCore.Qt.AlignCenter)
        labelInputImages.setAlignment(QtCore.Qt.AlignCenter)
        labelCoefficients.setAlignment(QtCore.Qt.AlignCenter)
        labelLogFilePreferences.setAlignment(QtCore.Qt.AlignCenter)
        labelOutputImages.setAlignment(QtCore.Qt.AlignCenter)
        labelSelfModificationParameters.setAlignment(QtCore.Qt.AlignCenter)
        labelDeltatronAgingSection.setAlignment(QtCore.Qt.AlignCenter)

        # Setting label texts for input images
        labelUrbanImage.setText("Urban image: ")
        labelRoadDataImage.setText("Road data image: ")
        labelLanduseIDataImage.setText("Land use data image: ")
        labelExcludedDataImage.setText("Excluded data image: ")
        labelSlopeDataImage.setText("Slope data image: ")
        labelBackgroundDataImage.setText("Background data image: ")

        # Setting label texts for coefficients label
        labelCalibDiffStart.setText("CALIBRATION_DIFFUSION_START")
        labelCalibDiffStep.setText("CALIBRATION_DIFFUSION_STEP")
        labelCalibDiffStop.setText("CALIBRATION_DIFFUSION_STOP")

        labelCalibBreedStart.setText("CALIBRATION_BREED_START")
        labelCalibBreedStep.setText("CALIBRATION_BREED_STEP")
        labelCalibBreedStop.setText("CALIBRATION_BREED_STOP")

        labelCalibSpreadStart.setText("CALIBRATION_SPREAD_START")
        labelCalibSpreadStep.setText("CALIBRATION_SPREAD_STEP")
        labelCalibSpreadStop.setText("CALIBRATION_SPREAD_STOP")

        labelCalibSlopeStart.setText("CALIBRATION_SLOPE_START")
        labelCalibSlopeStep.setText("CALIBRATION_SLOPE_STEP")
        labelCalibSlopeStop.setText("CALIBRATION_SLOPE_STOP")

        labelCalibRoadStart.setText("CALIBRATION_ROAD_START")
        labelCalibRoadStep.setText("CALIBRATION_ROAD_START")
        labelCalibRoadStop.setText("CALIBRATION_ROAD_STOP")

        labelPredDiffBestFit.setText("PREDICTION_DIFFUSION_BEST_FIT")
        labelPredBreedBestFit.setText("PREDICTION_BREED_BEST_FIT")
        labelPredSpreadBestFit.setText("PREDICTION_SPREAD_BEST_FIT")
        labelPredSlopeBestFit.setText("PREDICTION_SLOPE_BEST_FIT")
        labelPredRoadBestFit.setText("PREDICTION_ROAD_BEST_FIT")

        # Setting label text for self-modification parameters
        labelRoadGravSensitivity.setText("ROAD_GRAV_SENSITIVITY")
        labelSlopeSensitivity.setText("SLOPE_SENSITIVITY")
        labelCriticalLow.setText("CRITICAL_LOW")
        labelCriticalHigh.setText("CRITICAL_HIGH")
        labelCriticalSlope.setText("CRITICAL_SLOPE")
        labelBoom.setText("BOOM")
        labelBust.setText("BUST")

        # Setting lineEdits
        lineEditSleuthModelName = QtGui.QLineEdit()
        lineEditSimulation = QtGui.QLineEdit()

        lineEditModelDate = QtGui.QLineEdit()
        lineEditModelDate.setFixedWidth(70)
        lineEditModelDate.setMaxLength(10)
        lineEditSimulationDate = QtGui.QLineEdit()
        lineEditSimulationDate.setFixedWidth(70)
        lineEditSimulationDate.setMaxLength(10)

        lineEditDataDirectory = QtGui.QLineEdit()
        lineEditOutputDirectory = QtGui.QLineEdit()

        lineEditStartDate = QtGui.QLineEdit()
        lineEditStartDate.setFixedWidth(70)
        lineEditStartDate.setMaxLength(10)
        lineEditStopDate = QtGui.QLineEdit()
        lineEditStopDate.setFixedWidth(70)
        lineEditStopDate.setMaxLength(10)

        lineEditSleuthModelName.setText("Nazwa modelu")
        lineEditSimulation.setText("Nazwa scenariusza")
        lineEditModelDate.setText("1.1.1970")
        lineEditSimulationDate.setText("1.1.1970")

        # Input images edit lines
        lineEditUrbanImage = QtGui.QLineEdit()
        lineEditRoadDataImage = QtGui.QLineEdit()
        lineEditLanduseDataImage = QtGui.QLineEdit()
        lineEditExcludedDataImage = QtGui.QLineEdit()
        lineEditSlopeDataImage = QtGui.QLineEdit()
        lineEditBackgroundDataImage = QtGui.QLineEdit()

        # Coefficients edit lines
        lineEditCalibDiffStart = QtGui.QLineEdit()
        lineEditCalibDiffStep = QtGui.QLineEdit()
        lineEditCalibDiffStop = QtGui.QLineEdit()
        lineEditCalibDiffStart.setFixedWidth(30)
        lineEditCalibDiffStart.setMaxLength(3)
        lineEditCalibDiffStep.setFixedWidth(30)
        lineEditCalibDiffStep.setMaxLength(3)
        lineEditCalibDiffStop.setFixedWidth(30)
        lineEditCalibDiffStop.setMaxLength(3)

        lineEditCalibBreedStart = QtGui.QLineEdit()
        lineEditCalibBreedStep = QtGui.QLineEdit()
        lineEditCalibBreedStop = QtGui.QLineEdit()
        lineEditCalibBreedStart.setFixedWidth(30)
        lineEditCalibBreedStart.setMaxLength(3)
        lineEditCalibBreedStep.setFixedWidth(30)
        lineEditCalibBreedStep.setMaxLength(3)
        lineEditCalibBreedStop.setFixedWidth(30)
        lineEditCalibBreedStop.setMaxLength(3)

        lineEditCalibSpreadStart = QtGui.QLineEdit()
        lineEditCalibSpreadStep = QtGui.QLineEdit()
        lineEditCalibSpreadStop = QtGui.QLineEdit()
        lineEditCalibSpreadStart.setFixedWidth(30)
        lineEditCalibSpreadStart.setMaxLength(3)
        lineEditCalibSpreadStep.setFixedWidth(30)
        lineEditCalibSpreadStep.setMaxLength(3)
        lineEditCalibSpreadStop.setFixedWidth(30)
        lineEditCalibSpreadStop.setMaxLength(3)

        lineEditCalibSlopeStart = QtGui.QLineEdit()
        lineEditCalibSlopeStep = QtGui.QLineEdit()
        lineEditCalibSlopeStop = QtGui.QLineEdit()
        lineEditCalibSlopeStart.setFixedWidth(30)
        lineEditCalibSlopeStart.setMaxLength(3)
        lineEditCalibSlopeStep.setFixedWidth(30)
        lineEditCalibSlopeStep.setMaxLength(3)
        lineEditCalibSlopeStop.setFixedWidth(30)
        lineEditCalibSlopeStop.setMaxLength(3)

        lineEditCalibRoadStart = QtGui.QLineEdit()
        lineEditCalibRoadStep = QtGui.QLineEdit()
        lineEditCalibRoadStop = QtGui.QLineEdit()
        lineEditCalibRoadStart.setFixedWidth(30)
        lineEditCalibRoadStart.setMaxLength(3)
        lineEditCalibRoadStep.setFixedWidth(30)
        lineEditCalibRoadStep.setMaxLength(3)
        lineEditCalibRoadStop.setFixedWidth(30)
        lineEditCalibRoadStop.setMaxLength(3)

        lineEditPredDiffBestFit = QtGui.QLineEdit()
        lineEditPredDiffBestFit.setFixedWidth(30)
        lineEditPredDiffBestFit.setMaxLength(3)
        lineEditPredBreedBestFit = QtGui.QLineEdit()
        lineEditPredBreedBestFit.setFixedWidth(30)
        lineEditPredBreedBestFit.setMaxLength(3)
        lineEditPredSpreadBestFit = QtGui.QLineEdit()
        lineEditPredSpreadBestFit.setFixedWidth(30)
        lineEditPredSpreadBestFit.setMaxLength(3)
        lineEditPredSlopeBestFit = QtGui.QLineEdit()
        lineEditPredSlopeBestFit.setFixedWidth(30)
        lineEditPredSlopeBestFit.setMaxLength(3)
        lineEditPredRoadBestFit = QtGui.QLineEdit()
        lineEditPredRoadBestFit.setFixedWidth(30)
        lineEditPredRoadBestFit.setMaxLength(3)

        # Setting line edits for self-modification parameters
        lineEditRoadGravSensitivity = QtGui.QLineEdit()
        lineEditSlopeSensitivity = QtGui.QLineEdit()
        lineEditCriticalLow = QtGui.QLineEdit()
        lineEditCriticalHigh = QtGui.QLineEdit()
        lineEditCriticalSlope = QtGui.QLineEdit()
        lineEditBoom = QtGui.QLineEdit()
        lineEditBust = QtGui.QLineEdit()

        lineEditRoadGravSensitivity.setFixedWidth(30)
        lineEditRoadGravSensitivity.setMaxLength(3)
        lineEditSlopeSensitivity.setFixedWidth(30)
        lineEditSlopeSensitivity.setMaxLength(3)
        lineEditCriticalLow.setFixedWidth(30)
        lineEditCriticalLow.setMaxLength(3)
        lineEditCriticalHigh.setFixedWidth(30)
        lineEditCriticalHigh.setMaxLength(3)
        lineEditCriticalSlope.setFixedWidth(30)
        lineEditCriticalSlope.setMaxLength(3)
        lineEditBoom.setFixedWidth(30)
        lineEditBoom.setMaxLength(3)
        lineEditBust.setFixedWidth(30)
        lineEditBust.setMaxLength(3)

        # Setting Layouts
        boxH1Layout = QtGui.QHBoxLayout()
        boxH2Layout = QtGui.QHBoxLayout()
        boxV2Layout = QtGui.QVBoxLayout()
        boxV1Layout = QtGui.QVBoxLayout()
        boxV3Layout = QtGui.QVBoxLayout()
        boxV4Layout = QtGui.QVBoxLayout()

        # Setting Minimal Layouts - label + lineEdits
        boxHmin1Layout = QtGui.QHBoxLayout()
        boxHmin2Layout = QtGui.QHBoxLayout()
        boxHmin3Layout = QtGui.QHBoxLayout()
        boxHmin4Layout = QtGui.QHBoxLayout()

        # Setting input images layouts
        boxHUrbanLayout = QtGui.QHBoxLayout()
        boxHRoadDataLayout = QtGui.QHBoxLayout()
        boxHLanduseDataLayout = QtGui.QHBoxLayout()
        boxHExcludedDataLayout = QtGui.QHBoxLayout()
        boxHSlopeDataLayout = QtGui.QHBoxLayout()
        boxHBackGroundLayout = QtGui.QHBoxLayout()

        # Setting output images minimal horizontal layouts
        boxHWriteColorKeyImages = QtGui.QHBoxLayout()
        boxHAnimation = QtGui.QHBoxLayout()
        boxHViewGrowthTypes = QtGui.QHBoxLayout()
        boxHGrowthTypeWindow = QtGui.QHBoxLayout()

        # Setting running status & variables minimal horizontal layouts
        boxHECHO = QtGui.QHBoxLayout()
        boxHCOEFFile = QtGui.QHBoxLayout()
        boxHAVGFile = QtGui.QHBoxLayout()
        boxHSTDDEVFile = QtGui.QHBoxLayout()
        boxHMEMORYmap = QtGui.QHBoxLayout()
        boxHLOGGING = QtGui.QHBoxLayout()

        # Setting coefficients minimal horizontal layouts
        boxHCalibDiffStart = QtGui.QHBoxLayout()
        boxHCalibDiffStep = QtGui.QHBoxLayout()
        boxHCalibDiffStop = QtGui.QHBoxLayout()

        boxHCalibBreedStart = QtGui.QHBoxLayout()
        boxHCalibBreedStep = QtGui.QHBoxLayout()
        boxHCalibBreedStop = QtGui.QHBoxLayout()

        boxHCalibSpreadStart = QtGui.QHBoxLayout()
        boxHCalibSpreadStep = QtGui.QHBoxLayout()
        boxHCalibSpreadStop = QtGui.QHBoxLayout()

        boxHCalibSlopeStart = QtGui.QHBoxLayout()
        boxHCalibSlopeStep = QtGui.QHBoxLayout()
        boxHCalibSlopeStop = QtGui.QHBoxLayout()

        boxHCalibRoadStart = QtGui.QHBoxLayout()
        boxHCalibRoadStep = QtGui.QHBoxLayout()
        boxHCalibRoadStop = QtGui.QHBoxLayout()

        boxHPredDiffBestFit = QtGui.QHBoxLayout()
        boxHPredBreedBestFit = QtGui.QHBoxLayout()
        boxHPredSpreadBestFit = QtGui.QHBoxLayout()
        boxHPredSlopeBestFit = QtGui.QHBoxLayout()
        boxHPredRoadBestFit = QtGui.QHBoxLayout()

        # Setting self-modification parameters layouts
        boxHRoadGravSensitivity = QtGui.QHBoxLayout()
        boxHSlopeSensitivity = QtGui.QHBoxLayout()
        boxHCriticalLow = QtGui.QHBoxLayout()
        boxHCriticalHigh = QtGui.QHBoxLayout()
        boxHCriticalSlope = QtGui.QHBoxLayout()
        boxHBoom = QtGui.QHBoxLayout()
        boxHBust = QtGui.QHBoxLayout()

        # Adding widgets to running status & variables horizontal minimal layouts
        boxHECHO.addWidget(labelEcho)
        boxHECHO.addWidget(radioButtonECHO)

        boxHCOEFFile.addWidget(labelCOEFFile)
        boxHCOEFFile.addWidget(radioButtonCOEFFile)

        boxHAVGFile.addWidget(labelAVGFile)
        boxHAVGFile.addWidget(radioButtonAVGFile)

        boxHSTDDEVFile.addWidget(labelSTDDEVFile)
        boxHSTDDEVFile.addWidget(radioButtonSTDDEVFile)

        boxHMEMORYmap.addWidget(labelMEMORYmap)
        boxHMEMORYmap.addWidget(radioButtonMEMORYMap)

        boxHLOGGING.addWidget(labelLOGGING)
        boxHLOGGING.addWidget(radioButtonLOGGING)

        # Adding widgets to output images horizontal minimal layouts
        boxHWriteColorKeyImages.addWidget(labelWriteColorKeyImages)
        boxHWriteColorKeyImages.addWidget(radioButtonWriteColorKeyImages)

        boxHAnimation.addWidget(labelAnimation)
        boxHAnimation.addWidget(radioButtonAnimation)

        boxHViewGrowthTypes.addWidget(labelViewGrowthTypes)
        boxHViewGrowthTypes.addWidget(radioButtonViewGrowthTypes)

        boxHGrowthTypeWindow.addWidget(labelGrowthTypePrintWindow)

        # Adding widgets to input images horizontal mini layouts
        boxHUrbanLayout.addWidget(labelUrbanImage)
        boxHUrbanLayout.addWidget(lineEditUrbanImage)
        boxHUrbanLayout.addWidget(buttonUrbanDataImage)

        boxHRoadDataLayout.addWidget(labelRoadDataImage)
        boxHRoadDataLayout.addWidget(lineEditRoadDataImage)
        boxHRoadDataLayout.addWidget(buttonRoadDataImage)

        boxHLanduseDataLayout.addWidget(labelLanduseIDataImage)
        boxHLanduseDataLayout.addWidget(lineEditLanduseDataImage)
        boxHLanduseDataLayout.addWidget(buttonLanduseDataImage)

        boxHExcludedDataLayout.addWidget(labelExcludedDataImage)
        boxHExcludedDataLayout.addWidget(lineEditExcludedDataImage)
        boxHExcludedDataLayout.addWidget(buttonExcludedDataImage)

        boxHSlopeDataLayout.addWidget(labelSlopeDataImage)
        boxHSlopeDataLayout.addWidget(lineEditSlopeDataImage)
        boxHSlopeDataLayout.addWidget(buttonSlopeDataImage)

        boxHBackGroundLayout.addWidget(labelBackgroundDataImage)
        boxHBackGroundLayout.addWidget(lineEditBackgroundDataImage)
        boxHBackGroundLayout.addWidget(buttonBackgroundDataImage)

        # Adding widgets to coefficients horizontal mini layouts
        boxHCalibDiffStart.addWidget(labelCalibDiffStart)
        boxHCalibDiffStart.addWidget(lineEditCalibDiffStart)
        boxHCalibDiffStep.addWidget(labelCalibDiffStep)
        boxHCalibDiffStep.addWidget(lineEditCalibDiffStep)
        boxHCalibDiffStop.addWidget(labelCalibDiffStop)
        boxHCalibDiffStop.addWidget(lineEditCalibDiffStop)

        boxHCalibBreedStart.addWidget(labelCalibBreedStart)
        boxHCalibBreedStart.addWidget(lineEditCalibBreedStart)
        boxHCalibBreedStep.addWidget(labelCalibBreedStep)
        boxHCalibBreedStep.addWidget(lineEditCalibBreedStep)
        boxHCalibBreedStop.addWidget(labelCalibBreedStop)
        boxHCalibBreedStop.addWidget(lineEditCalibBreedStop)

        boxHCalibSpreadStart.addWidget(labelCalibSpreadStart)
        boxHCalibSpreadStart.addWidget(lineEditCalibSpreadStart)
        boxHCalibSpreadStep.addWidget(labelCalibSpreadStep)
        boxHCalibSpreadStep.addWidget(lineEditCalibSpreadStep)
        boxHCalibSpreadStop.addWidget(labelCalibSpreadStop)
        boxHCalibSpreadStop.addWidget(lineEditCalibSpreadStop)

        boxHCalibSlopeStart.addWidget(labelCalibSlopeStart)
        boxHCalibSlopeStart.addWidget(lineEditCalibSlopeStart)
        boxHCalibSlopeStep.addWidget(labelCalibSlopeStep)
        boxHCalibSlopeStep.addWidget(lineEditCalibSlopeStep)
        boxHCalibSlopeStop.addWidget(labelCalibSlopeStop)
        boxHCalibSlopeStop.addWidget(lineEditCalibSlopeStop)

        boxHCalibRoadStart.addWidget(labelCalibRoadStart)
        boxHCalibRoadStart.addWidget(lineEditCalibRoadStart)
        boxHCalibRoadStep.addWidget(labelCalibRoadStep)
        boxHCalibRoadStep.addWidget(lineEditCalibRoadStep)
        boxHCalibRoadStop.addWidget(labelCalibRoadStop)
        boxHCalibRoadStop.addWidget(lineEditCalibRoadStop)

        boxHPredDiffBestFit.addWidget(labelPredDiffBestFit)
        boxHPredDiffBestFit.addWidget(lineEditPredDiffBestFit)
        boxHPredBreedBestFit.addWidget(labelPredBreedBestFit)
        boxHPredBreedBestFit.addWidget(lineEditPredBreedBestFit)
        boxHPredSpreadBestFit.addWidget(labelPredSpreadBestFit)
        boxHPredSpreadBestFit.addWidget(lineEditPredSpreadBestFit)
        boxHPredSlopeBestFit.addWidget(labelPredSlopeBestFit)
        boxHPredSlopeBestFit.addWidget(lineEditPredSlopeBestFit)
        boxHPredRoadBestFit.addWidget(labelPredRoadBestFit)
        boxHPredRoadBestFit.addWidget(lineEditPredRoadBestFit)

        # Adding widgets to self-modification parameters horizontal mini
        # layouts
        boxHRoadGravSensitivity.addWidget(labelRoadGravSensitivity)
        boxHRoadGravSensitivity.addWidget(lineEditRoadGravSensitivity)

        boxHSlopeSensitivity.addWidget(labelSlopeSensitivity)
        boxHSlopeSensitivity.addWidget(lineEditSlopeSensitivity)

        boxHCriticalLow.addWidget(labelCriticalLow)
        boxHCriticalLow.addWidget(lineEditCriticalLow)

        boxHCriticalHigh.addWidget(labelCriticalHigh)
        boxHCriticalHigh.addWidget(lineEditCriticalHigh)

        boxHCriticalSlope.addWidget(labelCriticalSlope)
        boxHCriticalSlope.addWidget(lineEditCriticalSlope)

        boxHBoom.addWidget(labelBoom)
        boxHBoom.addWidget(lineEditBoom)

        boxHBust.addWidget(labelBust)
        boxHBust.addWidget(lineEditBust)

        # Horizontal 1 layout
        boxH1Layout.addWidget(labelSleuthModel)
        boxH1Layout.addWidget(lineEditSleuthModelName)
        boxH1Layout.addWidget(labelSimulation)
        boxH1Layout.addWidget(lineEditSimulation)
        boxH1Layout.addWidget(labelModelDate)
        boxH1Layout.addWidget(lineEditModelDate)
        boxH1Layout.addWidget(labelSimulationDate)
        boxH1Layout.addWidget(lineEditSimulationDate)

        # Horizontal min 1 layout
        boxHmin1Layout.addWidget(labelDataDirectory)
        boxHmin1Layout.addWidget(lineEditDataDirectory)

        # Horizontal min 2 layout
        boxHmin2Layout.addWidget(labelOutputDirectory)
        boxHmin2Layout.addWidget(lineEditOutputDirectory)

        # Horizontal min 3 layout
        boxHmin3Layout.addWidget(labelStartDate)
        boxHmin3Layout.addWidget(lineEditStartDate)

        # Horizontal min 4 layout
        boxHmin4Layout.addWidget(labelStopDate)
        boxHmin4Layout.addWidget(lineEditStopDate)

        # Vertical 1 layout
        boxV1Layout.addWidget(labelInputOutputDirectoryMain)
        boxV1Layout.addLayout(boxHmin1Layout)
        boxV1Layout.addLayout(boxHmin2Layout)
        boxV1Layout.addWidget(labelInputImages)
        boxV1Layout.addLayout(boxHUrbanLayout)
        boxV1Layout.addLayout(boxHRoadDataLayout)
        boxV1Layout.addLayout(boxHLanduseDataLayout)
        boxV1Layout.addLayout(boxHExcludedDataLayout)
        boxV1Layout.addLayout(boxHSlopeDataLayout)
        boxV1Layout.addLayout(boxHBackGroundLayout)
        boxV1Layout.addWidget(labelOutputImages)
        boxV1Layout.addLayout(boxHWriteColorKeyImages)
        boxV1Layout.addLayout(boxHAnimation)
        boxV1Layout.addLayout(boxHViewGrowthTypes)
        boxV1Layout.addLayout(boxHGrowthTypeWindow)

        # Vertical 3 layout
        boxV3Layout.addWidget(labelPredictionRange)
        boxV3Layout.addLayout(boxHmin3Layout)
        boxV3Layout.addLayout(boxHmin4Layout)
        boxV3Layout.addWidget(labelCoefficients)

        boxV3Layout.addLayout(boxHCalibDiffStart)
        boxV3Layout.addLayout(boxHCalibDiffStep)
        boxV3Layout.addLayout(boxHCalibDiffStop)

        boxV3Layout.addLayout(boxHCalibBreedStart)
        boxV3Layout.addLayout(boxHCalibBreedStep)
        boxV3Layout.addLayout(boxHCalibBreedStop)

        boxV3Layout.addLayout(boxHCalibSpreadStart)
        boxV3Layout.addLayout(boxHCalibSpreadStep)
        boxV3Layout.addLayout(boxHCalibSpreadStop)

        boxV3Layout.addLayout(boxHCalibSlopeStart)
        boxV3Layout.addLayout(boxHCalibSlopeStep)
        boxV3Layout.addLayout(boxHCalibSlopeStop)

        boxV3Layout.addLayout(boxHCalibRoadStart)
        boxV3Layout.addLayout(boxHCalibRoadStep)
        boxV3Layout.addLayout(boxHCalibRoadStop)

        boxV3Layout.addLayout(boxHPredDiffBestFit)
        boxV3Layout.addLayout(boxHPredBreedBestFit)
        boxV3Layout.addLayout(boxHPredSpreadBestFit)
        boxV3Layout.addLayout(boxHPredSlopeBestFit)
        boxV3Layout.addLayout(boxHPredRoadBestFit)

        boxV3Layout.addWidget(labelSelfModificationParameters)

        boxV3Layout.addLayout(boxHRoadGravSensitivity)
        boxV3Layout.addLayout(boxHSlopeSensitivity)
        boxV3Layout.addLayout(boxHCriticalLow)
        boxV3Layout.addLayout(boxHCriticalHigh)
        boxV3Layout.addLayout(boxHCriticalSlope)
        boxV3Layout.addLayout(boxHBoom)
        boxV3Layout.addLayout(boxHBust)

        # Vertical 4 layout
        boxV4Layout.addWidget(labelRunningStatusVariables)

        boxV4Layout.addLayout(boxHECHO)
        boxV4Layout.addLayout(boxHCOEFFile)
        boxV4Layout.addLayout(boxHAVGFile)
        boxV4Layout.addLayout(boxHSTDDEVFile)
        boxV4Layout.addLayout(boxHMEMORYmap)
        boxV4Layout.addLayout(boxHLOGGING)

        boxV4Layout.addWidget(labelLogFilePreferences)
        boxV4Layout.addWidget(labelDeltatronAgingSection)

        # Setting main front layout
        boxH2Layout.addLayout(boxV1Layout)
        boxH2Layout.addLayout(boxV3Layout)
        boxH2Layout.addLayout(boxV4Layout)

        boxV2Layout.addLayout(boxH1Layout)
        boxV2Layout.addLayout(boxH2Layout)

        w.setLayout(boxV2Layout)
        w.show()

        # Def of operations
        fileDialog = QtGui.QFileDialog

        def selectfileurban():
            lineEditUrbanImage.setText(fileDialog.getOpenFileName())

        def selectfileroaddata():
            lineEditRoadDataImage.setText(fileDialog.getOpenFileName())

        def selectfilelandusedata():
            lineEditLanduseDataImage.setText(fileDialog.getOpenFileName())

        def selectfileexcludeddata():
            lineEditExcludedDataImage.setText(fileDialog.getOpenFileName())

        def selectfileslopedata():
            lineEditSlopeDataImage.setText(fileDialog.getOpenFileName())

        def selectfilebackgrounddata():
            lineEditBackgroundDataImage.setText(fileDialog.getOpenFileName())

        # Button operations
        buttonUrbanDataImage.clicked.connect(lambda: selectfileurban())
        buttonRoadDataImage.clicked.connect(lambda: selectfileroaddata())
        buttonLanduseDataImage.clicked.connect(lambda: selectfilelandusedata())
        buttonExcludedDataImage.clicked.connect(lambda: selectfileexcludeddata())
        buttonSlopeDataImage.clicked.connect(lambda: selectfileslopedata())
        buttonBackgroundDataImage.clicked.connect(lambda: selectfilebackgrounddata())

        sys.exit(app.exec_())

        # Button operations
