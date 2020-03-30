import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time

import gui.listview
import db.database
from gui.newview import Ui_NewWindow
import gui.listview


class NewView(QtWidgets.QMainWindow, Ui_NewWindow):
    """Main window creation"""
    def __init__(self, parent=None):

        """list view construction"""
        super(NewView, self).__init__(parent)  # call init of QMainWindow, or QWidget or whatever)
        self.setupUi(self)  # call the function that actually does all the stuff you set up in QtDesigner

        brands = ["Ford", "VW", "Scania", "Mercedes Benz", "Iveco", "Volvo", "MAN",
                   "Hiunday", "JAC", "DAF", "Sinotruk", "Renault", "GM"]
        completer = QtWidgets.QCompleter(brands, self.brandline)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.brandline.setCompleter(completer)

        # codes and connections
        self.pushButton.clicked.connect(self.check_values)
        self.pushButton_2.clicked.connect(self.close)

    def check_values(self):
        # check and fix plate entry
        plate = self.plateline.text()

        if not (plate[:3].isalpha() and plate[3:].isdigit() and (len(plate[3:]) is 4)):
            print(plate[:3])
            print(plate[3:])
            print("Please, enter a correct plate entry")
            self.erase_plate()
        else:
            self.commit_values()

    def erase_plate(self):
        self.plateline.clear()

    def commit_values(self):
        # uppercase entries
        name = self.nameline.text().upper()
        car = self.carline.text().upper()
        brand = self.brandline.text().upper()
        now = time.localtime()  # get struct_time
        date = time.strftime("%d/%m/%Y", now)
        hour = time.strftime("%H:%M", now)
        plate = str(self.plateline.text()[:3].upper()) + '-' + str(self.plateline.text()[3:])

        try:
            db.database.connect()
        except Exception as error:
            print("Erro de conexao de banco de dados: " + str(error))

        try:
            db.database.new_value(name, car, brand, plate, date, hour)
            main_window.update()
        except Exception as error:
            print("Erro de entrada de novo valor: " + str(error))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # configuracao inicial da janela
        MainWindow.setFixedSize(802, 580)
        MainWindow.setWindowOpacity(0.965)
        MainWindow.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

        # configuracao inicial da tela
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # labels superiores
        self.labelsys = QtWidgets.QLabel(self.centralwidget)
        self.labelsys.setGeometry(QtCore.QRect(10, 0, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.labelsys.setFont(font)

        self.labelsys2 = QtWidgets.QLabel(self.centralwidget)
        self.labelsys2.setGeometry(QtCore.QRect(10, 30, 250, 20))

        # imagem background
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/truck.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(260, 200, 600, 340))
        self.bg.setPixmap(QtGui.QPixmap(("img/truck.jpg")))

        # botao de listagem de veiculos
        self.listButton = QtWidgets.QPushButton(self.centralwidget)
        self.listButton.setGeometry(QtCore.QRect(10, 60, 181, 101))

        # botao para entrar novo veiculo
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setGeometry(QtCore.QRect(210, 60, 181, 101))

        # botao para abrir historico
        self.histButton = QtWidgets.QPushButton(self.centralwidget)
        self.histButton.setGeometry(QtCore.QRect(410, 60, 181, 101))

        # botao para abrir caixa
        self.moneyButton = QtWidgets.QPushButton(self.centralwidget)
        self.moneyButton.setGeometry(QtCore.QRect(610, 60, 181, 101))

        # groupbox para tabela de andamento
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 185, 235, 370))
        self.customerTable = QtWidgets.QTableWidget(self.groupBox)  # init da tabela de andamento
        self.customerTable.setGeometry(QtCore.QRect(10, 20, 215, 340))
        self.customerTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.customerTable.setColumnCount(3)
        self.customerTable.setHorizontalHeaderLabels(['Nome', 'Data', 'Hora'])
        self.customerTable.horizontalHeader()
        header1 = self.customerTable.horizontalHeader()
        header1.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # configuracoes automaticas por codigo gerado
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # chama funcao para adiçao de textos
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TKS v0.1"))
        self.labelsys.setText(_translate("MainWindow", "Truck Control System"))
        self.bg.setText(_translate("MainWindow", ""))
        self.listButton.setText(_translate("MainWindow", "Listar veículos"))
        self.newButton.setText(_translate("MainWindow", "Novo veículo"))
        self.histButton.setText(_translate("MainWindow", "Histórico"))
        self.moneyButton.setText(_translate("MainWindow", "Caixa"))
        self.groupBox.setTitle(_translate("MainWindow", "Em andamento"))
        self.labelsys2.setText(_translate("MainWindow", "Sistema de controle para pátio de caminhões"))


# construcao de classe contendo o codigo base para as açoes da mainwindow
class myMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window creation"""
    def __init__(self, parent=None):
        """Main Window construction"""

        # setups the ui
        super(myMainWindow, self).__init__(parent)  # call init of QMainWindow, or QWidget or whatever)
        self.setupUi(self)  # call the function that actually does all the stuff you set up in QtDesigner

        self.update()
        self.list_view = gui.listview.ListView()
        self.new_view = NewView()

        # connections codes
        self.listButton.clicked.connect(self.show_list)
        self.newButton.clicked.connect(self.show_newview)
        # self.histButton.clicked.connect()
        # self.moneyButton.clicked.connect()

    # methods for connections
    def show_list(self):
        self.list_view.show()

    def show_newview(self):
        self.new_view.show()

    def update(self):
        self.customerTable.setRowCount(0)
        self.list()

        QtCore.QTimer.singleShot(10000, self.update)

    def list(self):
        list = db.database.read_values()

        QtWidgets.QApplication.processEvents()
        for row in list:
            inx = list.index(row)
            self.customerTable.insertRow(inx)
            self.customerTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(str(row[0])))  # name
            # self.customerTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(str(row[3])))
            self.customerTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(str(row[4])))  # date
            self.customerTable.setItem(inx, 2, QtWidgets.QTableWidgetItem(str(row[5])))  # hour
        QtWidgets.QApplication.processEvents()


app = QtWidgets.QApplication(sys.argv)
main_window = myMainWindow()


def main():
    main_window = myMainWindow()
    main_window.show()
    sys.exit(app.exec_())