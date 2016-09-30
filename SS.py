import sqlite3
import time
import datetime
import sys
import os

GUI = os.getcwd() + '/GUI'
DB = os.getcwd() + '/DB'

from GUI.stock import Ui_MainWindow
from GUI.agregar import Ui_AgregarStock
from GUI.marcas import Ui_MarcasStock
from GUI.control import Ui_ControlStock
from GUI.acercade import Ui_AcercaDe

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


global conn
global c


class MainWindow(QMainWindow):
    """Clase para la ventana principal de la aplicacion."""

    def __init__(self, parent=None):
        """Inicializacion ventana principal y conexiones de funciones."""
        super(MainWindow, self).__init__(parent)
        QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.menuArchivo.triggered.connect(self.cerrarAplicacion)
        self.ui.botonConsultar.clicked.connect(self.consultaBD)
        self.ui.botonBorrar.clicked.connect(self.eliminarBD)
        self.ui.actionModificar.triggered.connect(self.Agregar)
        self.ui.actionControl.triggered.connect(self.Control)
        self.ui.actionMarcass.triggered.connect(self.Marca)
        self.ui.actionAcercaDe.triggered.connect(self.AcercaDe)
        self.ui.tableStock.setColumnCount(4)
        header = ['Cantidad', 'Producto', 'Marca', 'Precio']
        self.ui.tableStock.setHorizontalHeaderLabels(header)
        self.ui.tableStock.verticalHeader().setVisible(False)

    def consultaBD(self):
        """Lectura de la base de datos."""
        codigo = int(self.ui.textoCodigo.text())
        if codigo == 0:
            c.execute("SELECT cantidad, producto, marca, precio FROM stock")
        else:
            c.execute("SELECT cantidad, producto, marca, precio FROM stock WHERE codigo = ?", (codigo,))
        data = c.fetchall()

        self.ui.tableStock.setRowCount(len(data))
        # self.ui.tableStock.setColumnCount(4)
        # header = ['Cantidad', 'Producto', 'Marca', 'Precio']
        # self.ui.tableStock.setHorizontalHeaderLabels(header)
        i = 0
        j = 0
        for i in range(len(data)):
            for j in range(4):
                self.ui.tableStock.setItem(i, j, QTableWidgetItem(data[i][j]))
                print(data[i][j])
                j += 1
            i += 1

        # tabla.setShowGrid(False)
        # tabla.setShowGrid(True)

        # hide vertical header
        # vh = self.ui.tableStock.verticalHeader()
        # vh.setVisible(False)
        # vh.setVisible(True)

        # set horizontal header properties
        # hh = tabla.horizontalHeader()
        # hh.setStretchLastSection(True)

        # set column width to fit contents
        # self.ui.tabla.resizeColumnsToContents()

        # set row height
        # self.ui.tabla.resizeRowsToContents()

        # enable sorting
        # tabla.setSortingEnabled(False)
        # tabla.setSortingEnabled(True)

        # return tabla

    def actualizarBD(precioAnterior, precioNuevo):
        """Funcion para actualizar elementos de la base de datos."""
        c.execute("UPDATE stock SET precio = ? WHERE precio = ?",
                  (precioNuevo, precioAnterior))
        conn.commit()

    def eliminarBD(self):
        """Funcion para eliminar elementos de la base de datos."""
        codigo = int(self.ui.textoCodigo.text())
        c.execute("DELETE FROM stock WHERE codigo = ?", (codigo,))
        conn.commit()

    def cerrarAplicacion(self):
        """Consulta de cierre limpio de la aplicacion."""
        choice = QMessageBox.question(self, "Cerrar la aplicacion", "Esta seguro que desea salir de la aplicacion?", QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def Agregar(self):
        """Llamada a la ventana de modificacion de stock."""
        self.w = AgregarStock()
        self.w.exec_()  # Solo se puede interactuar con esta ventana

    def Marca(self):
        """Llamada a la ventana de modificacion de marcas."""
        self.w = MarcasStock()
        self.w.exec_()

    def Control(self):
        """Llamada a la ventana de control de stock."""
        self.w = ControlStock()
        self.w.exec_()

    def AcercaDe(self):
        """Llamada a la ventana de informacion del programa."""
        self.w = AcercaDe()
        self.w.exec_()


class AgregarStock(QDialog):
    """Clase para la ventana de modificacion de stock."""

    def __init__(self, parent=None):
        """Inicializacion de la ventana de agregado en el stock."""
        super(AgregarStock, self).__init__(parent)
        QMainWindow.__init__(self, parent)
        self.ui = Ui_AgregarStock()
        self.ui.setupUi(self)

        self.ui.botonAgregar.clicked.connect(self.agregarBD)

    def agregarBD(self):
        """Agregado dinamico de la tabla de stock."""
        codigo = self.ui.spinCodigo.value()
        cantidad = self.ui.spinCantidad.value()
        producto = str(self.ui.lineProducto.text())
        marca = "La Serenisima"
        precio = self.ui.spinPrecio.value()
        creado = int(time.time())
        creado = str(datetime.datetime.fromtimestamp(creado).strftime
                     ("%Y-%m-%d %H:%M:%S"))
        vencimiento = self.ui.dateVencimiento.date().toPyDate()
        c.execute("INSERT INTO stock(codigo, cantidad, producto, marca, precio, creado, vencimiento) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (codigo, cantidad, producto, marca, precio, creado, vencimiento))
        conn.commit()


class MarcasStock(QDialog):
    """Creacion y modificacion de las marcas de la base de datos."""
    def __init__(self, parent=None):
        """Inicializacion de la ventana de agregado de marcas."""
        super(MarcasStock, self).__init__()
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MarcasStock()
        self.ui.setupUi(self)

        self.ui.botonAgregar.clicked.connect(self.agregarMarcaBD)

    def agregarMarcaBD(self):
        pass


class ControlStock(QDialog):
    """Control del Stock, ejemplo: vencimiento."""

    def __init__(self, parent=None):
        """Inicializacion de la ventana de control de stock."""
        super(ControlStock, self).__init__()
        self.ui = Ui_ControlStock()
        self.ui.setupUi(self)


class AcercaDe(QDialog):
    """Informacion del versionado del programa."""

    def __init__(self, parent=None):
        """Inicializacion de la ventana de informacion de versionado del programa."""
        super(AcercaDe, self).__init__()
        self.ui = Ui_AcercaDe()
        self.ui.setupUi(self)


def run():
    """Ejecucion de la parte grafica del programa."""
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())


def crearTabla():
    """Creacion de la tabla en caso que esta no exista en el directorio."""
    c.execute("CREATE TABLE IF NOT EXISTS stock(ID INTEGER PRIMARY KEY, codigo INT, cantidad INT, producto TEXT, marca TEXT, precio REAL, creado TEXT, vencimiento TEXT)")
    c.execute("CREATE UNIQUE INDEX IF NOT EXISTS ID ON stock (ID)")

try:
    conn = sqlite3.connect(os.path.join(DB, 'stock.db'))
    c = conn.cursor()
    crearTabla()
    run()
    c.close
    conn.close()

except Exception as e:
    print(str(e))
    error = int(time.time())
    error = str(datetime.datetime.fromtimestamp(error).strftime
                ('%Y-%m-%d %H:%M:%S')) + " - " + str(e)
    saveFile = open("errorDB.txt", "a")
    saveFile.write(error)
    saveFile.write('\n')
    saveFile.close()
