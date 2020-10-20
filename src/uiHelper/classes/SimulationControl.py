class SimulationControl:
    tabIndex = 0
    showSimulationProgress = False
    comboBoxSimulationIndex = 0

    signalsOutputData = False
    signalsOutputTransmitter = False
    signalsOutputModulator = False
    signalsOutputChannel = False
    signalsDataGenerated = False
    signalsDataEstimated = False
    signalsShowHistogramms = False
    signalsShowRunningWindow = False
    signalsSimulationBitsPerFrame = None
    signalsSimulationSamplerate = None
    signalsSimulationNumberOfShownSamples = None

    histogrammsPropertiesDataOutput = False
    histogrammsPropertiesSignalBeforeDecision = False
    histogrammsPropertiesSampledSignal = False
    histogrammsPropertiesErrorDistribution = False
    histogrammsSimulationAutomaticRangeEstimation = False
    histogrammsSimulationGranularity = None

    bepSimulationBEPSNRActivate = False
    bepSimulationBEPSNRRangeFrom = None
    bepSimulationBEPSNRRangeTo = None
    bepSimulationBEPSNRRangeGranularity = None
    bepSimulationBEPMUActivate = False
    bepSimulationBEPMUNrOfUsers = None
    bepSimulationSimulationNrOfBitsToSimulate = None
    bepSimulationSimulationShowTimeSamples = False
    bepSimulationSimulationTimeSamples = None
    bepSimulationSimulationShowHistogramms = False