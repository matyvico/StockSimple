# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AgregarStock(object):
    def setupUi(self, AgregarStock):
        AgregarStock.setObjectName("AgregarStock")
        AgregarStock.resize(270, 272)
        self.formLayout = QtWidgets.QFormLayout(AgregarStock)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(AgregarStock)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinCodigo = QtWidgets.QSpinBox(AgregarStock)
        self.spinCodigo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinCodigo.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinCodigo.setMaximum(1000000000)
        self.spinCodigo.setObjectName("spinCodigo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinCodigo)
        self.label = QtWidgets.QLabel(AgregarStock)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinCantidad = QtWidgets.QSpinBox(AgregarStock)
        self.spinCantidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinCantidad.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinCantidad.setObjectName("spinCantidad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinCantidad)
        self.label_2 = QtWidgets.QLabel(AgregarStock)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboMarca = QtWidgets.QComboBox(AgregarStock)
        self.comboMarca.setObjectName("comboMarca")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboMarca)
        self.label_3 = QtWidgets.QLabel(AgregarStock)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineProducto = QtWidgets.QLineEdit(AgregarStock)
        self.lineProducto.setObjectName("lineProducto")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineProducto)
        self.label_4 = QtWidgets.QLabel(AgregarStock)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinPrecio = QtWidgets.QDoubleSpinBox(AgregarStock)
        self.spinPrecio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinPrecio.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinPrecio.setSpecialValueText("")
        self.spinPrecio.setMaximum(1000000.0)
        self.spinPrecio.setSingleStep(0.1)
        self.spinPrecio.setObjectName("spinPrecio")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinPrecio)
        self.botonAgregar = QtWidgets.QPushButton(AgregarStock)
        self.botonAgregar.setObjectName("botonAgregar")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.botonAgregar)
        self.dateVencimiento = QtWidgets.QDateEdit(AgregarStock)
        self.dateVencimiento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateVencimiento.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateVencimiento.setDate(QtCore.QDate(2016, 1, 1))
        self.dateVencimiento.setCalendarPopup(True)
        self.dateVencimiento.setObjectName("dateVencimiento")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dateVencimiento)
        self.label_6 = QtWidgets.QLabel(AgregarStock)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.retranslateUi(AgregarStock)
        QtCore.QMetaObject.connectSlotsByName(AgregarStock)
        AgregarStock.setTabOrder(self.spinCodigo, self.spinCantidad)
        AgregarStock.setTabOrder(self.spinCantidad, self.comboMarca)
        AgregarStock.setTabOrder(self.comboMarca, self.lineProducto)
        AgregarStock.setTabOrder(self.lineProducto, self.spinPrecio)
        AgregarStock.setTabOrder(self.spinPrecio, self.dateVencimiento)
        AgregarStock.setTabOrder(self.dateVencimiento, self.botonAgregar)

    def retranslateUi(self, AgregarStock):
        _translate = QtCore.QCoreApplication.translate
        AgregarStock.setWindowTitle(_translate("AgregarStock", "Agregar Stock"))
        self.label_5.setText(_translate("AgregarStock", "Código:"))
        self.label.setText(_translate("AgregarStock", "Cantidad:"))
        self.label_2.setText(_translate("AgregarStock", "Marca:"))
        self.label_3.setText(_translate("AgregarStock", "Producto:"))
        self.label_4.setText(_translate("AgregarStock", "Precio unitario:"))
        self.spinPrecio.setPrefix(_translate("AgregarStock", "$ "))
        self.botonAgregar.setText(_translate("AgregarStock", "Agregar"))
        self.dateVencimiento.setDisplayFormat(_translate("AgregarStock", "dd/MM/yyyy"))
        self.label_6.setText(_translate("AgregarStock", "Fecha de vencimiento:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarStock = QtWidgets.QWidget()
    ui = Ui_AgregarStock()
    ui.setupUi(AgregarStock)
    AgregarStock.show()
    sys.exit(app.exec_())

