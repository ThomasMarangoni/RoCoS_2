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