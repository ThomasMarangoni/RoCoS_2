from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtSvg

from ui import CodeGenerator as CodeGenerator
from uiHelper import CodeGeneratorHelper as CodeGeneratorHelper
from ui import SimulationControl as SimulationControl
from uiHelper import SimulationControlHelper as SimulationControlHelper
from uiHelper import MainFunctions as MainFunctions

class MainHelper(QtWidgets.QMainWindow):
    def __init__(self, main):
        global mainUi
        mainUi = main
        global transmitter 
        transmitter = MainFunctions.Transmitter()
        super().__init__()

    def actionSimulationControl(checked):
        windowSimulationControl = SimulationControlHelper.SimulationControlHelper()
        windowSimulationControl.ui = SimulationControl.Ui_Dialog_SimulationControl()
        windowSimulationControl.ui.setupUi(windowSimulationControl)
        windowSimulationControl.show()
        windowSimulationControl.exec()

    def pushButtonGenerateSequence(self): #TODO: Gets triggered two times
        print("Test")
        windowCodeGenerator = CodeGeneratorHelper.CodeGeneratorHelper()
        windowCodeGenerator.ui = CodeGenerator.Ui_Dialog_CodeGenerator()
        windowCodeGenerator.ui.setupUi(windowCodeGenerator)
        windowCodeGenerator.show()
        windowCodeGenerator.exec()

    def pushButtonPulseshapeShow(self):
        transmitter.createPulseShapeImage(self)

        renderer = QtSvg.QSvgRenderer()
        renderer.load("tmp/pulseshape_plot.svg")
        size = renderer.defaultSize()

        item = QtSvg.QGraphicsSvgItem()
        item.setSharedRenderer(renderer)

        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)

        graphicsView = mainUi.graphicsView_transmitter_pulseshape
        graphicsView.setScene(scene)
        graphicsView.fitInView(item)
        graphicsView.isInteractive = True

    def pushButtonPulseshapeProperties(self):
        print("Not Implemented")

    def pushButtonTransmitterAntipodalAnalyseSequence(self):
        print("Not Implemented")

    def pushButtonTransmitterAntipodalAnalyseKKF(self):
        print("Not Implemented")

    def pushButtonTransmitterOthogonalAnalyseSequence(self):
        print("Not Implemented")

    def pushButtonTransmitterOthogonalAnalyseKKF(self):
        print("Not Implemented")

    def pushButtonCloneTransmitterSettings(self):
        print("Not Implemented")

    def pushButtonReceiverOthogonalAnalyseSequence(self):
        print("Not Implemented")

    def pushButtonReceiverOthogonalAnalyseKKF(self):
        print("Not Implemented")

    def pushButtonReceiverAntipodalAnalyseSequence(self):
        print("Not Implemented")

    def pushButtonReceiverAntipodalAnalyseKKF(self):
        print("Not Implemented")

    def pushButtonFilterLowPassShowImpulseresponse(self):
        print("Not Implemented")

    def pushButtonFilterRakeReceiverAddToList(self):
        print("Not Implemented")

    def pushButtonFilterRakeReceiverCloneChannelMWs(self):
        print("Not Implemented")

    def pushButtonChannelCWAddToList(self):
        print("Not Implemented")

    def pushButtonChannelMWAddToList(self):
        print("Not Implemented")

    def pushButtonChannelMUAnalyseSequence(self):
        print("Not Implemented")

    def pushButtonChannelMUAnalyseKKF(self):
        print("Not Implemented")

    def pushButtonChannelMUAddToList(self):
        print("Not Implemented")

    def lineEditTransmitterPulseshapeSamples(self):
        transmitter.pulseshapeSamplePulse = int(self.sender().text())

    def lineEditTransmitterPulseshapeDuration(self):
        transmitter.pulseshapeDuration = float(self.sender().text())

    def lineEditTransmitterSignalResultsChipRate(self):
        transmitter.signalResultsChipRate = int(self.sender().text())

    def lineEditTransmitterSignalResultsBitDuration(self):
        transmitter.signalResultsBitRate = float(self.sender().text())

    def lineEditTransmitterSignalResultsBitRate(self):
        transmitter.signalResultsBitRate = int(self.sender().text())

    def lineEditTransmitterSignalResultsSampleRate(self):
        transmitter.signalResultsSampleRate = int(self.sender().text())

    def lineEditTransmitterSignalResultsOversampling(self):
        transmitter.signalResultsOversampling = int(self.sender().text())

    def lineEditTransmitterSignalParameterChipAmplitude(self):
        transmitter.signalParameterChipAmplitude = float(self.sender().text())

    def lineEditTransmitterSignalParameterChipDuration(self):
        transmitter.signalParameterChipDuration = float(self.sender().text())

    def lineEditChannelAWGNPropertiesSNR(self):
        print("Not Implemented")

    def lineEditChannelAWGNPropertiesStdDev(self):
        print("Not Implemented")

    def lineEditChannelCWHz(self):
        print("Not Implemented")

    def lineEditChannelCWPercentage(self):
        print("Not Implemented")

    def lineEditChannelMWs(self):
        print("Not Implemented")

    def lineEditChannelMWPercentage(self):
        print("Not Implemented")

    def lineEditChannelMUPercentage(self):
        print("Not Implemented")

    def lineEditChannelNumberOfCW(self):
        print("Not Implemented")

    def lineEditChannelNumberOfMW(self):
        print("Not Implemented")

    def lineEditChannelNumberOfMU(self):
        print("Not Implemented")

    def lineEditReceiverFilterMatchedFilter(self):
        print("Not Implemented")

    def lineEditReceiverFilterLowPassFilterDelay(self):
        print("Not Implemented")

    def lineEditReceiverFilterRakeReceiverDelay(self):
        print("Not Implemented")

    def lineEditReceiverFilterRakeReceiverPercentage(self):
        print("Not Implemented")

    def lineEditReceiverFilterIntegrateAndDumpDelay(self):
        print("Not Implemented")

    def tabWidgetTransmitterSSSequence(self, index):
        print("Not Implemented")

    def tabWidgetChannel(self, index):
        print("Not Implemented")

    def tabWidgetReceiverSSSequence(self, index):
        print("Not Implemented")

    def tabWidgetReceiverFilter(self, index):
        print("Not Implemented")

    def comboBoxTransmitterPulseshape(self, index):
        transmitter.pulseShapeShapeIndex = int(index)

    def checkBoxChannelAWGN(self, toggle):
        print("Not Implemented" + " Status: " + str(toggle))

    def checkBoxChannelNumberOfCW(self, toggle):
        print("Not Implemented")

    def checkBoxChannelNumberOfMW(self, toggle):
        print("Not Implemented")

    def checkBoxChannelMUNumberOfUsers(self, toggle):
        print("Not Implemented")

    def radioButtonChannelMUSCDMA(self, toggle):
        print("Not Implemented")

    def radioButtonChannelMUACDMA(self, toggle):
        print("Not Implemented")

    def radioButtonReceiverFilterRakeReceiverFingerTypesMatchedFilter(self, toggle):
        print("Not Implemented")

    def radioButtonReceiverFilterRakeReceiverFingerTypesLowPassFilter(self, toggle):
        print("Not Implemented")

    def radioButtonReceiverFilterRakeReceiverFingerTypesIntegrateAndDump(self, toggle):
        print("Not Implemented")

    def listWidgetTransmitterSSSequenceAntipodal(self, current, previous):
        print("Not Implemented")

    def listWidgetTransmitterSSSequenceOrthogonal1(self, current, previous):
        print("Not Implemented")

    def listWidgetTransmitterSSSequenceOrthogonal2(self, current, previous):
        print("Not Implemented")

    def listWidgetReceiverSSSequenceOrthogonal1(self, current, previous):
        print("Not Implemented")

    def listWidgetReceiverSSSequenceOrthogonal2(self, current, previous):
        print("Not Implemented")

    def listWidgetReceiverSSSequenceAntipodal(self, current, previous):
        print("Not Implemented")

    def listWidgetReceiverFilterRakeReceiver(self, current, previous):
        print("Not Implemented")

    def listWidgetChannelCW(self, current, previous):
        print("Not Implemented")

    def listWidgetChannelMW(self, current, previous):
        print("Not Implemented")

    def listWidgetChannelMU(self, current, previous):
        print("Not Implemented")

    def listWidgetChannelMUNewUser(self, current, previous):
        print("Not Implemented")