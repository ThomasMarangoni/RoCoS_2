class Transmitter:
    sequenceIndex = 0               # Needs to be initialized with 0, because event is only triggered on change
    sequenceAntipodal = None
    sequenceOrthogonal = None

    pulseshapeShapeIndex = 0        # Needs to be initialized with 0, because event is only triggered on change
    pulseshapeSamplePulse = None    # spp
    pulseshapeDuration = None       # sec
    pulseshapeNumberOfZeros = None
    pulseshapeRollOffFactor = None
    pulseshapeStandardDeviation = None

    signalParameterChipAmplitude = None    # V
    signalParameterChipDuration = None     # sec

    signalResultsChipRate = None       # cps
    signalResultsBitDuration = None    # sec
    signalResultsBitRate = None        # bps
    signalResultsSampleRate = None     # sps
    signalResultsOversampling = None