from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtSvg

from ui import CodeGenerator as CodeGenerator
from uiHelper import CodeGeneratorHelper as CodeGeneratorHelper
from ui import SimulationControl as SimulationControl
from uiHelper import SimulationControlHelper as SimulationControlHelper
from uiHelper.classes import Channel as Channel
from uiHelper.classes import Receiver as Receiver
from uiHelper.classes import Transmitter as Transmitter

class MainHelper(QtWidgets.QMainWindow):
    def __init__(self, main):
        global mainUi
        mainUi = main

        global transmitter 
        transmitter = Transmitter.Transmitter()
        global channel 
        channel = Channel.Channel()
        global receiver 
        receiver = Receiver.Receiver()

        super().__init__()

    def actionSimulationControl(self, checked):
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
        channel.awgnSNR = float(self.sender().text())

    def lineEditChannelAWGNPropertiesStdDev(self):
        channel.awgnStdDev = float(self.sender().text())

    def lineEditChannelCWHz(self):
        channel.cwHz = float(self.sender().text())

    def lineEditChannelCWPercentage(self):
        channel.cwReferenceAmplitude = int(self.sender().text())

    def lineEditChannelMWs(self):
        channel.mwS = float(self.sender().text())

    def lineEditChannelMWPercentage(self):
        channel.mwReferenceAmplitude = int(self.sender().text())

    def lineEditChannelMUPercentage(self):
        channel.muReferenceAmplitude = int(self.sender().text())

    def lineEditChannelNumberOfCW(self):
        channel.numberOfCWLineEdit = int(self.sender().text())

    def lineEditChannelNumberOfMW(self):
        channel.numberOfMWLineEdit = int(self.sender().text())

    def lineEditChannelNumberOfMU(self):
        channel.muNumberOfUserLineEdit = int(self.sender().text())

    def lineEditReceiverFilterMatchedFilter(self):
        receiver.filterMatchedFilterDelay = float(self.sender().text())

    def lineEditReceiverFilterLowPassFilterDelay(self):
        receiver.filterLowPassFilterDelay = float(self.sender().text())

    def lineEditReceiverFilterRakeReceiverDelay(self):
        receiver.filterRakeReceiverDelay = float(self.sender().text())

    def lineEditReceiverFilterRakeReceiverPercentage(self):
        receiver.filterRakeReceiverReferenceAmplitude = int(self.sender().text())

    def lineEditReceiverFilterIntegrateAndDumpDelay(self):
        receiver.filterIntegrateAndDumpDelay = float(self.sender().text())

    def tabWidgetTransmitterSSSequence(self, index):
        transmitter.sequenceIndex = int(index)

    def tabWidgetChannel(self, index):
        channel.tabIndex = int(index)

    def tabWidgetReceiverSSSequence(self, index):
        receiver.sequenceIndex = int(index)

    def tabWidgetReceiverFilter(self, index):
        receiver.filterIndex = int(index)

    def comboBoxTransmitterPulseshape(self, index):
        transmitter.pulseShapeShapeIndex = int(index)

    def checkBoxChannelAWGN(self, toggle):
        channel.awgnCheckBox = bool(toggle)

    def checkBoxChannelNumberOfCW(self, toggle):
        channel.numberOfCWCheckBox = bool(toggle)

    def checkBoxChannelNumberOfMW(self, toggle):
        channel.numberOfMWCheckBox = bool(toggle)

    def checkBoxChannelMUNumberOfUsers(self, toggle):
        channel.muNumberOfUserCheckBox = bool(toggle)

    def radioButtonChannelMUSCDMA(self, toggle):
        channel.muSCDMA = bool(toggle)

    def radioButtonChannelMUACDMA(self, toggle):
        channel.muACDMA = bool(toggle)

    def radioButtonReceiverFilterRakeReceiverFingerTypesMatchedFilter(self, toggle):
        channel.filterRakeReceiverTypeIntegrateAndDump = bool(toggle)

    def radioButtonReceiverFilterRakeReceiverFingerTypesLowPassFilter(self, toggle):
        channel.filterRakeReceiverTypeLowPassFilter = bool(toggle)

    def radioButtonReceiverFilterRakeReceiverFingerTypesIntegrateAndDump(self, toggle):
        channel.filterRakeReceiverTypeIntegrateAndDump = bool(toggle)

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