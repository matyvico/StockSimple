# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ControlStock(object):
    def setupUi(self, ControlStock):
        ControlStock.setObjectName("ControlStock")
        ControlStock.resize(230, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(ControlStock)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ControlStock)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(ControlStock)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(ControlStock)
        QtCore.QMetaObject.connectSlotsByName(ControlStock)

    def retranslateUi(self, ControlStock):
        _translate = QtCore.QCoreApplication.translate
        ControlStock.setWindowTitle(_translate("ControlStock", "Control de Stock"))
        self.label.setText(_translate("ControlStock", "Fechas de vencimiento próximas:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ControlStock = QtWidgets.QWidget()
    ui = Ui_ControlStock()
    ui.setupUi(ControlStock)
    ControlStock.show()
    sys.exit(app.exec_())

