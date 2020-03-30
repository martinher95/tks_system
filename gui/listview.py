from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import *
import time

import db.database
from gui import mainview

item = []


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

        self.customerTable.horizontalHeader()
        header1 = self.customerTable.horizontalHeader()
        self.customerTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        header1.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.customerTable.setFont(font)

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
        self.upButton.setText(_translate("MainWindow", "Atualizar lista"))
        self.groupBox.setTitle(_translate("MainWindow", "Ações"))


# construcao de classe contendo o codigo base para as açoes da listview

class ListView(QtWidgets.QMainWindow, Ui_ListView):
    """Main window creation"""
    def __init__(self, parent=None):
        """list view construction"""
        super(ListView, self).__init__(parent)  # call init of QMainWindow, or QWidget or whatever)
        self.index = ''
        self.setupUi(self)  # call the function that actually does all the stuff you set up in QtDesigner
        self.update()  # list all db entries for first
        global item_id
        global item
        self.item_date = ''
        self.item_name = ''
        self.item_hour = ''

        # objects and variables
        self.new_view = mainview.NewView()

        # codes and connections
        self.addButton.clicked.connect(self.new_show)
        self.delButton.clicked.connect(self.delete_value)
        self.upButton.clicked.connect(self.update)
        self.valButton.clicked.connect(self.charge)
        self.customerTable.itemClicked.connect(self.take_item)

    def new_show(self):
        self.new_view.show()

    def update(self):
        global item

        self.customerTable.setRowCount(0)
        self.list()

        QtCore.QTimer.singleShot(2500, self.update)

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

    def delete_value(self):
        global item_id

        # check if some row is selected
        """TODO"""
        # for i in range(self.customerTable.rowCount()):

        try:
            db.database.delete_value(str(item_id))
        except Exception as e:
            print(str(e))

        self.update()

    def charge(self):
        # date difference
        #old
        old_date = self.item_date
        old_hour = self.item_hour

        old_day = int(old_date[0:2])
        old_month = int(old_date[3:5])
        old_year = int(old_date[6:10])

        # current
        now = datetime.now()
        cur_date = now.strftime("%d/%m/%Y")
        cur_day = int(cur_date[0:2])
        cur_month = int(cur_date[3:5])
        cur_year = int(cur_date[6:10])

        # difference establishment
        diff_date = [abs(cur_day-old_day), abs(cur_month-old_month), abs(cur_year-old_year)]
        print(diff_date)

        # hour difference

        # old
        old_hours = int(old_hour[0:2])
        old_min = int(old_hour[3:])

        # current
        cur_hour = now.strftime("%H:%M")
        cur_hours = int(cur_hour[0:2])
        cur_min = int(cur_hour[3:])

        # difference
        diff_hours = [abs(cur_hours-old_hours), abs(cur_min-old_min)]
        print(diff_hours)



    def take_item(self):
        global item_id
        global item

        current_row = self.customerTable.currentRow()
        item = self.customerTable.item(current_row, 0)
        item_id = self.customerTable.item(current_row, 0).text()
        self.item_name = self.customerTable.item(current_row, 1).text()
        self.item_date = self.customerTable.item(current_row, 5).text()
        self.item_hour = self.customerTable.item(current_row, 6).text()


