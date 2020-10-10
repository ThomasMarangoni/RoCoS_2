import matplotlib.pyplot as plot
import numpy as np
import os

from config import CONFIG as CONFIG

class Transmitter:
    sequenceIndex = 0               # Needs to be initialized with 0, because event is only triggered on change
    sequenceAntipodal = None
    sequenceOrthogonal = None

    pulseShapeShapeIndex = 0        # Needs to be initialized with 0, because event is only triggered on change
    pulseshapeSamplePulse = None    # spp
    pulseshapeDuration = None       # sec

    signalParameterChipAmplitude = None    # V
    signalParameterChipDuration = None     # sec

    signalResultsChipRate = None       # cps
    signalResultsBitDuration = None    # sec
    signalResultsBitRate = None        # bps
    signalResultsSampleRate = None     # sps
    signalResultsOversampling = None

    def createPulseShapeImage(self, ui):
        fig, axe = plot.subplots(figsize=(15, 5), facecolor="white")
        x = np.arange(0, 2, 0.1)
        y = np.random.randn(len(x))
        plot.plot(x, y)

        if not os.path.exists(CONFIG.TEMPORARY_DIRECTORY_NAME):
            os.makedirs(CONFIG.TEMPORARY_DIRECTORY_NAME)

        plot.savefig(CONFIG.TEMPORARY_DIRECTORY_NAME + 'pulseshape_plot.svg')
        plot.close(fig)

class Channel:
    tabIndex = 0                # Needs to be initialized with 0, because event is only triggered on change
    awgnCheckBox = False        # Needs to be initialized with False, because event is only triggered on change
    numberOfCWCheckBox = False  # Needs to be initialized with False, because event is only triggered on change
    numberOfMWCheckBox = False  # Needs to be initialized with False, because event is only triggered on change
    numberOfCWLineEdit = None
    numberOfMWLineEdit = None

    muNumberOfUserCheckBox = False  # Needs to be initialized with False, because event is only triggered on change
    muNumberOfUserLineEdit = None
    muSCDMA = False                 # Needs to be initialized with False, because event is only triggered on change
    muACDMA = False                 # Needs to be initialized with False, because event is only triggered on change

    awgnSNR = None      # dB
    awgnStdDev = None   # V

    cwHz = None                 # Hz
    cwReferenceAmplitude = None # %
    cwUserList = None

    mwS = None                  # sec
    mwReferenceAmplitude = None # %
    mwUserList = None

    muUser = None
    muReferenceAmplitude = None # %
    muUserList = None

class Receiver:
    sequenceIndex = 0               # Needs to be initialized with 0, because event is only triggered on change
    sequenceAntipodal = None
    sequenceOrthogonal = None

    filterIndex = 0                 # Needs to be initialized with 0, because event is only triggered on change

    filterIntegrateAndDumpDelay = None  # sec

    filterMatchedFilterDelay = None     # sec

    filterLowPassFilterDelay = None     # sec
    
    filterRakeReceiverDelay = None              # sec
    filterRakeReceiverReferenceAmplitude = None # %
    filterRakeReceiverList = None
    filterRakeReceiverTypeIntegrateAndDump = False  # Needs to be initialized with False, because event is only triggered on change
    filterRakeReceiverTypeMatchedFilter = False     # Needs to be initialized with False, because event is only triggered on change
    filterRakeReceiverTypeLowPassFilte = False      # Needs to be initialized with False, because event is only triggered on change
