from PyQt5 import QtCore, QtGui, QtWidgets

import db.database
from gui.newview import NewView


class Ui_ListView(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(682, 560)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.customerTable = QtWidgets.QTableWidget(self.centralwidget)
        self.customerTable.setGeometry(QtCore.QRect(10, 40, 471, 491))

        self.customerTable.setColumnCount(7)

        self.customerTable.setHorizontalHeaderLabels(['ID', 'Nome', 'Veículo', 'Marca', 'Placa', 'Data', 'Hora'])



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(510, 50, 141, 31))
        self.addButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(510, 100, 141, 31))
        self.delButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.valButton = QtWidgets.QPushButton(self.centralwidget)
        self.valButton.setGeometry(QtCore.QRect(510, 460, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.valButton.setFont(font)
        self.valButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(510, 150, 141, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.upButton.setFont(font)
        self.upButton.setStyleSheet("background-color: rgb(255, 255, 127);")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(500, 29, 171, 501))

        self.groupBox.raise_()
        self.customerTable.raise_()
        self.label.raise_()
        self.addButton.raise_()
        self.delButton.raise_()
        self.valButton.raise_()
        self.upButton.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lista de veículos"))
        self.label.setText(_translate("MainWindow", "Lista de veículos"))
        self.addButton.setText(_translate("MainWindow", "Adicionar"))
        self.delButton.setText(_translate("MainWindow", "Remover"))
        self.valButton.setText(_translate("MainWindow", "Cobrar"))
        self.upButton.setText(_translate("MainWindow", "Atualizar dados"))
        self.groupBox.setTitle(_translate("MainWindow", "Ações"))


# construcao de classe contendo o codigo base para as açoes da listview
def delete_value(index):
    try:
        delete_value(str(index))
    except Exception as e:
        print(str(e))


class ListView(QtWidgets.QMainWindow, Ui_ListView):
    """Main window creation"""
    def __init__(self, parent=None):
        """list view construction"""
        super(ListView, self).__init__(parent)  # call init of QMainWindow, or QWidget or whatever)
        self.setupUi(self)  # call the function that actually does all the stuff you set up in QtDesigner
        self.list()  # list all db entries for first

        # objects and variables
        self.new_view = NewView()

        # codes and connections
        self.addButton.clicked.connect(self.new_show)
        self.delButton.clicked.connect(delete_value)
        self.upButton.clicked.connect(self.update)

    def new_show(self):
        self.new_view.show()

    def update(self):
        self.customerTable.setRowCount(0)
        self.list()

    def list(self):
        list = db.database.read_values()

        for row in list:
            inx = list.index(row)
            self.customerTable.insertRow(inx)
            self.customerTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(str(row[6])))
            self.customerTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(str(row[0])))
            self.customerTable.setItem(inx, 2, QtWidgets.QTableWidgetItem(str(row[1])))
            self.customerTable.setItem(inx, 3, QtWidgets.QTableWidgetItem(str(row[2])))
            self.customerTable.setItem(inx, 4, QtWidgets.QTableWidgetItem(str(row[3])))
            self.customerTable.setItem(inx, 5, QtWidgets.QTableWidgetItem(str(row[4])))
            self.customerTable.setItem(inx, 6, QtWidgets.QTableWidgetItem(str(row[5])))
