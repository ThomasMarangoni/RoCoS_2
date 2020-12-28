"""
In this file all validators for input fields get configured. With validators the input
only gets accepted, if the validator returns true. This means that the data change events
also only getting triggered, if the validator returns true.
"""

from PyQt5 import QtWidgets, QtGui, QtCore

# This Regex is checking for double format eg. -01.0285, +0.34, 2332.12321
doubleValidator = QtGui.QRegExpValidator(QtCore.QRegExp("[+-]?([0-9]*[.])?[0-9]+"))

# This Regex is checking for interger format eg. -21321132, +90890, 008689
integerValidator = QtGui.QRegExpValidator(QtCore.QRegExp("[+-]?[0-9]+"))

# This Regex is checking for binary format eg. 01010
binaryValidator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-1]+"))

def setupMainValidators(mainUi):
    mainUi.lineEdit_transmitter_pulseshape_samples.setValidator(integerValidator)
    mainUi.lineEdit_transmitter_pulseshape_duration.setValidator(doubleValidator)
    mainUi.lineEdit_transmitter_signalresults_chiprate.setValidator(integerValidator)
    mainUi.lineEdit_transmitter_signalresults_bitduration.setValidator(doubleValidator)
    mainUi.lineEdit_transmitter_signalresults_bitrate.setValidator(integerValidator)
    mainUi.lineEdit_transmitter_signalresults_samplerate.setValidator(integerValidator)
    mainUi.lineEdit_transmitter_signalresults_oversampling.setValidator(integerValidator)
    mainUi.lineEdit_transmitter_signalparameter_chipamplitude.setValidator(doubleValidator)
    mainUi.lineEdit_transmitter_signalparameter_chipduration.setValidator(doubleValidator)

    mainUi.lineEdit_channel_awgn_snr.setValidator(doubleValidator)
    mainUi.lineEdit_channel_awgn_stddev.setValidator(doubleValidator)
    mainUi.lineEdit_channel_cw_frequency.setValidator(doubleValidator)
    mainUi.lineEdit_channel_cw_procent.setValidator(integerValidator)
    mainUi.lineEdit_channel_mw_seconds.setValidator(doubleValidator)
    mainUi.lineEdit_channel_mw_procent.setValidator(integerValidator)
    mainUi.lineEdit_channel_mu_procent.setValidator(integerValidator)
    mainUi.lineEdit_channel_cw.setValidator(integerValidator)
    mainUi.lineEdit_channel_mw.setValidator(integerValidator)
    mainUi.lineEdit_channel_mu_procent.setValidator(integerValidator)

    mainUi.lineEdit_receiver_filter_integrate_and_dump_delay.setValidator(doubleValidator)
    mainUi.lineEdit_receiver_filter_low_pass_filter_delay.setValidator(doubleValidator)
    mainUi.lineEdit_receiver_filter_matched_filter_delay.setValidator(doubleValidator)
    mainUi.lineEdit_receiver_filter_rake_receiver_delay.setValidator(doubleValidator)
    mainUi.lineEdit_receiver_filter_rake_receiver_procent.setValidator(integerValidator)
