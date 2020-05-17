from PyQt5 import QtWidgets

from ui import Main as Main
from ui import Analyse as Analyse
from ui import CodeGenerator as CodeGenerator
from ui import SimulationControl as SimulationControl


app = QtWidgets.QApplication([])

print("Starting Main Window")
window01 = QtWidgets.QMainWindow()
mainUi = Main.Ui_MainWindow()
mainUi.setupUi(window01)
window01.show()

print("Stating Code Generator Dialog")
window02 = QtWidgets.QDialog()
codeGen = CodeGenerator.Ui_Dialog_CodeGenerator()
codeGen.setupUi(window02)
window02.show()

print("Stating Analyse Dialog")
window03 = QtWidgets.QDialog()
analyse = Analyse.Ui_Dialog_Analyse()
analyse.setupUi(window03)
window03.show()

print("Stating Simulation Control Dialog")
window04 = QtWidgets.QDialog()
simCtrl = SimulationControl.Ui_Dialog_SimulationControl()
simCtrl.setupUi(window04)
window04.show()

app.exec_()