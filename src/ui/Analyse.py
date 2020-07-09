# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tmarangoni/documents/RoCoS_2/src/ui/Analyse.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Analyse(object):
    def setupUi(self, Dialog_Analyse):
        Dialog_Analyse.setObjectName("Dialog_Analyse")
        Dialog_Analyse.resize(1156, 552)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_Analyse)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_Analyse)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView_sequence = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView_sequence.setObjectName("graphicsView_sequence")
        self.gridLayout_2.addWidget(self.graphicsView_sequence, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_Analyse)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        self.label_length = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_length.setFont(font)
        self.label_length.setObjectName("label_length")
        self.gridLayout_3.addWidget(self.label_length, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 2, 1, 1)
        self.graphicsView_periodicAFK = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_periodicAFK.setObjectName("graphicsView_periodicAFK")
        self.gridLayout_3.addWidget(self.graphicsView_periodicAFK, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(Dialog_Analyse)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(260, 0))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget, 0, 1, 2, 1)

        self.retranslateUi(Dialog_Analyse)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Analyse)

    def retranslateUi(self, Dialog_Analyse):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Analyse.setWindowTitle(_translate("Dialog_Analyse", "RoCoS 2 - Analyse"))
        self.groupBox.setTitle(_translate("Dialog_Analyse", "Sequence"))
        self.groupBox_2.setTitle(_translate("Dialog_Analyse", "Periodic AFK"))
        self.label.setText(_translate("Dialog_Analyse", "Length:"))
        self.label_length.setText(_translate("Dialog_Analyse", "NAN"))
