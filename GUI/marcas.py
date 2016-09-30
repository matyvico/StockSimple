# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'marcas.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MarcasStock(object):
    def setupUi(self, MarcasStock):
        MarcasStock.setObjectName("MarcasStock")
        MarcasStock.resize(230, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(MarcasStock)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MarcasStock)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(MarcasStock)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(MarcasStock)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableView = QtWidgets.QTableView(MarcasStock)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.botonAgregar = QtWidgets.QPushButton(MarcasStock)
        self.botonAgregar.setObjectName("botonAgregar")
        self.verticalLayout.addWidget(self.botonAgregar)

        self.retranslateUi(MarcasStock)
        QtCore.QMetaObject.connectSlotsByName(MarcasStock)
        MarcasStock.setTabOrder(self.lineEdit, self.botonAgregar)
        MarcasStock.setTabOrder(self.botonAgregar, self.tableView)

    def retranslateUi(self, MarcasStock):
        _translate = QtCore.QCoreApplication.translate
        MarcasStock.setWindowTitle(_translate("MarcasStock", "Marcas"))
        self.label.setText(_translate("MarcasStock", "Nombre de la marca:"))
        self.label_2.setText(_translate("MarcasStock", "Marcas existentes:"))
        self.botonAgregar.setText(_translate("MarcasStock", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MarcasStock = QtWidgets.QWidget()
    ui = Ui_MarcasStock()
    ui.setupUi(MarcasStock)
    MarcasStock.show()
    sys.exit(app.exec_())

