from PyQt5 import QtWidgets

from uiHelper.classes import SimulationControl as SimulationControl

from functions import convertFloat, convertInt

class SimulationControlHelper(QtWidgets.QDialog):

    def __init__(self):
        global simulationControl 
        simulationControl = SimulationControl.SimulationControl()

        super().__init__()

    def pushButtonSaveResults(self):
	    print("Not Implemented")

    def pushButtonSaveSettings(self):
        print("Not Implemented")

    def pushButtonStartSimulation(self):
        print("Not Implemented")

    def pushButtonAbortSimulation(self):
        print("Not Implemented")

    def comboBoxSimulation(self, index):
        simulationControl.comboBoxSimulationIndex = convertInt(index)

    def checkBoxShowSimulationProgress(self, toggled):
        simulationControl.showSimulationProgress = bool(toggled)

    def tabWidget(self, index):
        simulationControl.tabIndex = convertInt(index)

    def checkBoxSignalsOutputData(self, toggled):
        simulationControl.signalsOutputData = bool(toggled)

    def checkBoxSignalsOutputTransmitter(self, toggled):
        simulationControl.signalsOutputTransmitter = bool(toggled)

    def checkBoxSignalsOutputModulator(self, toggled):
        simulationControl.signalsOutputModulator = bool(toggled)

    def checkBoxSignalsOutputChannel(self, toggled):
        simulationControl.signalsOutputChannel = bool(toggled)

    def checkBoxSignalsDataGenerated(self, toggled):
        simulationControl.signalsDataGenerated = bool(toggled)

    def checkBoxSignalsDataEstimated(self, toggled):
        simulationControl.signalsDataEstimated = bool(toggled)

    def checkBoxSignalsShowHistogramms(self, toggled):
        simulationControl.signalsShowHistogramms = bool(toggled)

    def checkBoxSignalsShowRunningWindow(self, toggled):
        simulationControl.signalsShowRunningWindow = bool(toggled)

    def lineEditSignalsSimulationBitsFrame(self):
        simulationControl.signalsSimulationBitsPerFrame = convertInt(self.sender().text())

    def lineEditSignalsSimulationSamplerate(self):
        simulationControl.signalsSimulationSamplerate = convertInt(self.sender().text())

    def lineEditSignalsSimulationNumberOfShownSamples(self):
        simulationControl.signalsSimulationNumberOfShownSamples = convertInt(self.sender().text())

    def checkBoxHistogrammsPropertiesDataOutput(self, toggled):
        simulationControl.histogrammsPropertiesDataOutput = bool(toggled)

    def checkBoxHistogrammsPropertiesSignalBeforeDecision(self, toggled):
        simulationControl.histogrammsPropertiesSignalBeforeDecision = bool(toggled)

    def checkBoxHistogrammsPropertiesSampledSignal(self, toggled):
        simulationControl.histogrammsPropertiesSampledSignal = bool(toggled)

    def checkBoxHistogrammsPropertiesErrorDistribution(self, toggled):
        simulationControl.histogrammsPropertiesErrorDistribution = bool(toggled)

    def checkBoxHistogrammsSimulationAutomaticRangeEstimation(self, toggled):
        simulationControl.histogrammsSimulationAutomaticRangeEstimation = bool(toggled)

    def lineEditHistogrammsSimulationGranularity(self):
        simulationControl.histogrammsSimulationGranularity = convertInt(self.sender().text())

    def checkBoxBEPSimulationBEPSNRActivate(self, toggled):
        simulationControl.bepSimulationBEPMUActivate = bool(toggled)

    def checkBoxBEPSimulationBEPMUsActivate(self, toggled):
        simulationControl.bepSimulationBEPMUActivate = bool(toggled)

    def checkBoxBEPSimulationSimulationShowFirst(self, toggled):
        simulationControl.checkBoxBEPSimulationSimulationShowFirst = bool(toggled)

    def checkBoxBEPSimulationSimulationShowHistogramms(self, toggled):
        simulationControl.bepSimulationSimulationShowHistogramms = bool(toggled)

    def lineEditBEPSimulationBEPSNRSNRRangeFrom(self):
        simulationControl.bepSimulationBEPSNRRangeFrom = convertFloat(self.sender().text())

    def lineEditBEPSimulationBEPSNRSNRRangeTo(self):
        simulationControl.bepSimulationBEPSNRRangeTo = convertFloat(self.sender().text())

    def lineEditBEPSimulationBEPSNRGranularity(self):
        simulationControl.bepSimulationBEPSNRGranularity = convertFloat(self.sender().text())

    def lineEditBEPSimulationBEPMUsNrOfUsers(self):
        simulationControl.bepSimulationBEPMUNrOfUsers = convertInt(self.sender().text())

    def lineEditBEPSimulationBEPSNRNrOfBitsToSimulate(self):
        simulationControl.bepSimulationSimulationNrOfBitsToSimulate = convertInt(self.sender().text())

    def lineEditBEPSimulationSimulationTimeSamples(self):
        simulationControl.bepSimulationSimulationTimeSamples = convertInt(self.sender().text())
