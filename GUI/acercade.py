# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercade.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AcercaDe(object):
    def setupUi(self, AcercaDe):
        AcercaDe.setObjectName("AcercaDe")
        AcercaDe.resize(276, 142)
        AcercaDe.setMaximumSize(QtCore.QSize(276, 142))
        self.verticalLayout = QtWidgets.QVBoxLayout(AcercaDe)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(AcercaDe)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(AcercaDe)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(AcercaDe)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(AcercaDe)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(AcercaDe)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(AcercaDe)
        QtCore.QMetaObject.connectSlotsByName(AcercaDe)

    def retranslateUi(self, AcercaDe):
        _translate = QtCore.QCoreApplication.translate
        AcercaDe.setWindowTitle(_translate("AcercaDe", "Acerca de..."))
        self.label_2.setText(_translate("AcercaDe", "Programa de administracion de Stock"))
        self.label_3.setText(_translate("AcercaDe", "Version: 0.1"))
        self.label_5.setText(_translate("AcercaDe", "Marzo 2016"))
        self.label_4.setText(_translate("AcercaDe", "Python 3.5.1 + PyQt4 + SQLite"))
        self.label.setText(_translate("AcercaDe", "Autor: Matias Daniel Vico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AcercaDe = QtWidgets.QWidget()
    ui = Ui_AcercaDe()
    ui.setupUi(AcercaDe)
    AcercaDe.show()
    sys.exit(app.exec_())

