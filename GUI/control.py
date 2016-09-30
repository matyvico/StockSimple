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
        ControlStock.resize(529, 530)
        self.verticalLayout = QtWidgets.QVBoxLayout(ControlStock)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(ControlStock)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tableResumen = QtWidgets.QTableWidget(ControlStock)
        self.tableResumen.setObjectName("tableResumen")
        self.tableResumen.setColumnCount(3)
        self.tableResumen.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableResumen.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResumen.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResumen.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableResumen)
        self.label_2 = QtWidgets.QLabel(ControlStock)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableRegistroVenta = QtWidgets.QTableWidget(ControlStock)
        self.tableRegistroVenta.setObjectName("tableRegistroVenta")
        self.tableRegistroVenta.setColumnCount(5)
        self.tableRegistroVenta.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegistroVenta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegistroVenta.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegistroVenta.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegistroVenta.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegistroVenta.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableRegistroVenta)
        self.label = QtWidgets.QLabel(ControlStock)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableVencimiento = QtWidgets.QTableView(ControlStock)
        self.tableVencimiento.setObjectName("tableVencimiento")
        self.verticalLayout.addWidget(self.tableVencimiento)

        self.retranslateUi(ControlStock)
        QtCore.QMetaObject.connectSlotsByName(ControlStock)

    def retranslateUi(self, ControlStock):
        _translate = QtCore.QCoreApplication.translate
        ControlStock.setWindowTitle(_translate("ControlStock", "Control de Stock"))
        self.label_3.setText(_translate("ControlStock", "Resumen"))
        item = self.tableResumen.horizontalHeaderItem(0)
        item.setText(_translate("ControlStock", "Vendedor"))
        item = self.tableResumen.horizontalHeaderItem(1)
        item.setText(_translate("ControlStock", "Total"))
        item = self.tableResumen.horizontalHeaderItem(2)
        item.setText(_translate("ControlStock", "Controlado"))
        self.label_2.setText(_translate("ControlStock", "Ventas"))
        item = self.tableRegistroVenta.horizontalHeaderItem(0)
        item.setText(_translate("ControlStock", "Vendedor"))
        item = self.tableRegistroVenta.horizontalHeaderItem(1)
        item.setText(_translate("ControlStock", "Producto"))
        item = self.tableRegistroVenta.horizontalHeaderItem(2)
        item.setText(_translate("ControlStock", "Cantidad"))
        item = self.tableRegistroVenta.horizontalHeaderItem(3)
        item.setText(_translate("ControlStock", "Precio unitario"))
        item = self.tableRegistroVenta.horizontalHeaderItem(4)
        item.setText(_translate("ControlStock", "Total"))
        self.label.setText(_translate("ControlStock", "Fechas de vencimiento próximas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ControlStock = QtWidgets.QWidget()
    ui = Ui_ControlStock()
    ui.setupUi(ControlStock)
    ControlStock.show()
    sys.exit(app.exec_())

