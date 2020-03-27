import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.listview import *
from gui.newview import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # configuracao inicial da janela
        MainWindow.setObjectName("MainWindow")
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
        self.groupBox.setGeometry(QtCore.QRect(9, 185, 211, 371))
        self.tableView = QtWidgets.QTableView(self.groupBox)  # init da tabela de andamento
        self.tableView.setGeometry(QtCore.QRect(10, 20, 185, 340))

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

        self.list_view = ListView()
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



