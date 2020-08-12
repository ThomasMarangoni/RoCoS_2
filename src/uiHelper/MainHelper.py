from PyQt5 import QtWidgets
from ui import CodeGenerator as CodeGenerator
from uiHelper import CodeGeneratorHelper as CodeGeneratorHelper
from ui import SimulationControl as SimulationControl
from uiHelper import SimulationControlHelper as SimulationControlHelper

class MainHelper(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def actionSimulationControl(checked):
        windowSimulationControl = SimulationControlHelper.SimulationControlHelper()
        windowSimulationControl.ui = SimulationControl.Ui_Dialog_SimulationControl()
        windowSimulationControl.ui.setupUi(windowSimulationControl)
        windowSimulationControl.exec_()
        windowSimulationControl.show()

    def pushButtonGenerateSequence(self):
        windowCodeGenerator = CodeGeneratorHelper.CodeGeneratorHelper()
        windowCodeGenerator.ui = CodeGenerator.Ui_Dialog_CodeGenerator()
        windowCodeGenerator.ui.setupUi(windowCodeGenerator)
        windowCodeGenerator.exec_()
        windowCodeGenerator.show()

    def pushButtonPulseshapeShow(self):
        print("Not Implemented")

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
        print("Not Implemented" + " " + self.sender().text())

    def lineEditTransmitterPulseshapeDuration(self):
        print("Not Implemented")

    def lineEditTransmitterSignalResultsChipRate(self):
        print("Not Implemented")

    def lineEditTransmitterSignalResultsBitDuration(self):
        print("Not Implemented")

    def lineEditTransmitterSignalResultsBitRate(self):
        print("Not Implemented")

    def lineEditTransmitterSignalResultsSampleRate(self):
        print("Not Implemented")

    def lineEditTransmitterSignalResultsOversampling(self):
        print("Not Implemented")

    def lineEditTransmitterSignalParameterChipAmplitude(self):
        print("Not Implemented")

    def lineEditTransmitterSignalParameterChipDuration(self):
        print("Not Implemented")

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
        print("Not Implemented")

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