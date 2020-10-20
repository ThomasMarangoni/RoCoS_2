import os
import numpy as np
import matplotlib.pyplot as plot

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
        fig, _ = plot.subplots(figsize=(15, 5), facecolor="white")
        x = np.arange(0, 2, 0.1)
        y = np.random.randn(len(x))
        plot.plot(x, y)

        if not os.path.exists(CONFIG.TEMPORARY_DIRECTORY_NAME):
            os.makedirs(CONFIG.TEMPORARY_DIRECTORY_NAME)

        plot.savefig(CONFIG.TEMPORARY_DIRECTORY_NAME + 'pulseshape_plot.svg')
        plot.close(fig)