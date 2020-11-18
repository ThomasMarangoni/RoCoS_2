from PyQt5 import QtWidgets, QtGui, QtCore, QtSvg

from config import CONFIG as CONFIG
from ui import CodeGenerator as CodeGenerator
from uiHelper import CodeGeneratorHelper as CodeGeneratorHelper
from ui import SimulationControl as SimulationControl
from uiHelper import SimulationControlHelper as SimulationControlHelper
from uiHelper.classes import Channel as Channel
from uiHelper.classes import Receiver as Receiver
from uiHelper.classes import Transmitter as Transmitter

import os
import math
import numpy as np
import matplotlib.pyplot as plot

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

    # GUI Events
    def actionSimulationControl(self, checked):
        windowSimulationControl = SimulationControlHelper.SimulationControlHelper()
        windowSimulationControl.ui = SimulationControl.Ui_Dialog_SimulationControl()
        windowSimulationControl.ui.setupUi(windowSimulationControl)
        windowSimulationControl.show()
        windowSimulationControl.exec()

    def pushButtonGenerateSequence(self): #TODO: Gets triggered two times
        windowCodeGenerator = CodeGeneratorHelper.CodeGeneratorHelper()
        windowCodeGenerator.ui = CodeGenerator.Ui_Dialog_CodeGenerator()
        windowCodeGenerator.ui.setupUi(windowCodeGenerator)
        windowCodeGenerator.show()
        windowCodeGenerator.exec()

    def pushButtonPulseshapeShow(self):
        sequence = self.createSincSequence(20, 5)
        self.createPulseShapeImage(self, sequence, 20)

        renderer = QtSvg.QSvgRenderer()
        renderer.load("tmp/pulseshape_plot.svg")
        size = renderer.defaultSize()

        item = QtSvg.QGraphicsSvgItem()
        item.setSharedRenderer(renderer)

        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)

        graphicsView = QtWidgets.QGraphicsView()
        graphicsView.setScene(scene)
        graphicsView.fitInView(item)
        graphicsView.isInteractive = True

        layout = QtWidgets.QGridLayout()
        layout.addWidget(graphicsView)

        dialog = QtWidgets.QDialog(self)
        dialog.setLayout(layout)
        dialog.setWindowTitle("Pulseshape")
        dialog.exec_()

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
        if transmitter.pulseshapeDuration is not None:
            transmitter.signalResultsSampleRate = float(1/(transmitter.pulseshapeDuration/transmitter.pulseshapeSamplePulse))
            mainUi.lineEdit_transmitter_signalresults_samplerate.setText(str(transmitter.signalResultsSampleRate))

        if transmitter.signalParameterChipDuration is not None and transmitter.pulseshapeDuration is not None:
            transmitter.signalResultsOversampling = float(transmitter.signalParameterChipDuration/(transmitter.pulseshapeDuration/transmitter.pulseshapeSamplePulse))
            mainUi.lineEdit_transmitter_signalresults_oversampling.setText(str(transmitter.signalResultsOversampling))

    def lineEditTransmitterPulseshapeDuration(self):
        transmitter.pulseshapeDuration = float(self.sender().text())
        if transmitter.pulseshapeSamplePulse is not None:
            transmitter.signalResultsSampleRate = float(1/(transmitter.pulseshapeDuration/transmitter.pulseshapeSamplePulse))
            mainUi.lineEdit_transmitter_signalresults_samplerate.setText(str(transmitter.signalResultsSampleRate))
        
        if transmitter.signalParameterChipDuration is not None and transmitter.pulseshapeSamplePulse is not None:
            transmitter.signalResultsOversampling = float(transmitter.signalParameterChipDuration/(transmitter.pulseshapeDuration/transmitter.pulseshapeSamplePulse))
            mainUi.lineEdit_transmitter_signalresults_oversampling.setText(str(transmitter.signalResultsOversampling))

    def lineEditTransmitterPulseshapeNumberOfZeros(self):
        transmitter.pulseshapeNumberOfZeros = int(self.sender().text())

    def lineEditTransmitterPulseshapeRollOffFactor(self):
        transmitter.pulseshapeRollOffFactor = int(self.sender().text())

    def lineEditTransmitterPulseshapeStandardDeviation(self):
        transmitter.pulseshapeStandardDeviation = int(self.sender().text())

    def lineEditTransmitterSignalResultsChipRate(self):
        # lineEdit is read-only, event is only for debug purpose
        print("Debug only event")

    def lineEditTransmitterSignalResultsBitDuration(self):
        # lineEdit is read-only, event is only for debug purpose
        print("Debug only event")

    def lineEditTransmitterSignalResultsBitRate(self):
        # lineEdit is read-only, event is only for debug purpose
        print("Debug only event")

    def lineEditTransmitterSignalResultsSampleRate(self):
        # lineEdit is read-only, event is only for debug purpose
        print("Debug only event")

    def lineEditTransmitterSignalResultsOversampling(self):
        # lineEdit is read-only, event is only for debug purpose
        print("Debug only event")

    def lineEditTransmitterSignalParameterChipAmplitude(self):
        transmitter.signalParameterChipAmplitude = float(self.sender().text())

    def lineEditTransmitterSignalParameterChipDuration(self):
        transmitter.signalParameterChipDuration = float(self.sender().text())
        transmitter.signalResultsChipRate = float(1/transmitter.signalParameterChipDuration)
        mainUi.lineEdit_transmitter_signalresults_chiprate.setText(str(transmitter.signalResultsChipRate))

        if transmitter.pulseshapeDuration is not None and transmitter.pulseshapeSamplePulse is not None:
            transmitter.signalResultsOversampling = float(transmitter.signalParameterChipDuration/(transmitter.pulseshapeDuration/transmitter.pulseshapeSamplePulse))
            mainUi.lineEdit_transmitter_signalresults_oversampling.setText(str(transmitter.signalResultsOversampling))

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
        transmitter.pulseshapeShapeIndex = int(index)
        if (index == 1): # index 1 is sinc
            mainUi.lineEdit_transmitter_pulseshape_numberofzeros.setEnabled(True)
        else:
            mainUi.lineEdit_transmitter_pulseshape_numberofzeros.setEnabled(False)

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

   # Additional Functions
    def createPulseShapeImage(self, ui, sequence, length):
        fig, _ = plot.subplots(figsize=(15, 5), facecolor="white")
        x = range(0, length)
        y = sequence
        plot.plot(x, y)

        if not os.path.exists(CONFIG.TEMPORARY_DIRECTORY_NAME):
            os.makedirs(CONFIG.TEMPORARY_DIRECTORY_NAME)

        plot.savefig(CONFIG.TEMPORARY_DIRECTORY_NAME + 'pulseshape_plot.svg')
        plot.close(fig)

    def createRectSequence(self, length):
        length = int(length)

        sequence = []
        for i in range(0, length):
            sequence.insert(i,float(1.0))

        return sequence

    def createSincSequence(self, length, zeroes):
        length = int(length)

        arg = math.pi / length

        sequence = [] 
        for i in range(0, int(length/2)):
            sequence.insert(i, math.sin((length/2-i)*arg)/((length/2-i)*arg))
        
        for i in range(int(length/2), length):
            if ((math.sin((i-length/2)*arg) == 0) and ((i-length/2)*arg) == 0):
                sequence.insert(i, 1)
            else:
                sequence.insert(i, math.sin((i-length/2)*arg)/((i-length/2)*arg))

        return sequence