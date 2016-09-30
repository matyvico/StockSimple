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
        self.lineNombreMarca = QtWidgets.QLineEdit(MarcasStock)
        self.lineNombreMarca.setObjectName("lineNombreMarca")
        self.verticalLayout.addWidget(self.lineNombreMarca)
        self.label_2 = QtWidgets.QLabel(MarcasStock)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableMarca = QtWidgets.QTableView(MarcasStock)
        self.tableMarca.setObjectName("tableMarca")
        self.verticalLayout.addWidget(self.tableMarca)
        self.pushAgregarMarca = QtWidgets.QPushButton(MarcasStock)
        self.pushAgregarMarca.setObjectName("pushAgregarMarca")
        self.verticalLayout.addWidget(self.pushAgregarMarca)

        self.retranslateUi(MarcasStock)
        QtCore.QMetaObject.connectSlotsByName(MarcasStock)
        MarcasStock.setTabOrder(self.lineNombreMarca, self.pushAgregarMarca)
        MarcasStock.setTabOrder(self.pushAgregarMarca, self.tableMarca)

    def retranslateUi(self, MarcasStock):
        _translate = QtCore.QCoreApplication.translate
        MarcasStock.setWindowTitle(_translate("MarcasStock", "Marcas"))
        self.label.setText(_translate("MarcasStock", "Nombre de la marca:"))
        self.label_2.setText(_translate("MarcasStock", "Marcas existentes:"))
        self.pushAgregarMarca.setText(_translate("MarcasStock", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MarcasStock = QtWidgets.QWidget()
    ui = Ui_MarcasStock()
    ui.setupUi(MarcasStock)
    MarcasStock.show()
    sys.exit(app.exec_())

