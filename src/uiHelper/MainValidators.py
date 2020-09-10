from PyQt5 import QtWidgets, QtGui

def setup(mainUi):
    mainUi.lineEdit_transmitter_pulseshape_samples.setValidator(QtGui.QIntValidator())
    mainUi.lineEdit_transmitter_pulseshape_duration.setValidator(QtGui.QDoubleValidator())
    mainUi.lineEdit_transmitter_signalresults_chiprate.setValidator(QtGui.QIntValidator())
    mainUi.lineEdit_transmitter_signalresults_bitduration.setValidator(QtGui.QDoubleValidator())
    mainUi.lineEdit_transmitter_signalresults_bitrate.setValidator(QtGui.QIntValidator())
    mainUi.lineEdit_transmitter_signalresults_samplerate.setValidator(QtGui.QIntValidator())
    mainUi.lineEdit_transmitter_signalresults_oversampling.setValidator(QtGui.QIntValidator())
    mainUi.lineEdit_transmitter_signalparameter_chipamplitude.setValidator(QtGui.QDoubleValidator())
    mainUi.lineEdit_transmitter_signalparameter_chipduration.setValidator(QtGui.QDoubleValidator())