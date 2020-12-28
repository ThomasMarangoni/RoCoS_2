import sys
import os

from PyQt5 import QtWidgets, QtGui, QtCore

from ui import Main as Main
from uiHelper import MainHelper as MainHelper
from uiHelper import Validators as Validators

from ui import Analyse as Analyse
from ui import CodeGenerator as CodeGenerator
from ui import SimulationControl as SimulationControl

from config import CONFIG as CONFIG

if not os.path.exists(CONFIG.TEMPORARY_DIRECTORY_NAME):
    os.makedirs(CONFIG.TEMPORARY_DIRECTORY_NAME)

app = QtWidgets.QApplication([])

print("Starting Main Window")
mainUi = Main.Ui_MainWindow()
windowMain = MainHelper.MainHelper(mainUi)
mainUi.setupUi(windowMain)
windowMain.show()
Validators.setupMainValidators(mainUi)

app.exec_()

print("Removing " + CONFIG.TEMPORARY_DIRECTORY_NAME + " directory.")
if os.path.exists(CONFIG.TEMPORARY_DIRECTORY_NAME):
    for root, dirs, files in os.walk(CONFIG.TEMPORARY_DIRECTORY_NAME, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(CONFIG.TEMPORARY_DIRECTORY_NAME)

sys.exit()