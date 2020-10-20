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
