from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(682, 560)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 471, 491))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 50, 141, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 100, 141, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 460, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 150, 141, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(500, 29, 171, 501))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.tableView.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
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
        self.pushButton.setText(_translate("MainWindow", "Adicionar"))
        self.pushButton_2.setText(_translate("MainWindow", "Remover"))
        self.pushButton_3.setText(_translate("MainWindow", "Cobrar"))
        self.pushButton_4.setText(_translate("MainWindow", "Atualizar dados"))
        self.groupBox.setTitle(_translate("MainWindow", "Ações"))


# construcao de classe contendo o codigo base para as açoes da listview
class ListView(QtWidgets.QMainWindow, Ui_ListView):
    """Main window creation"""
    def __init__(self, parent=None):

        """list view construction"""
        super(ListView, self).__init__(parent)  # call init of QMainWindow, or QWidget or whatever)
        self.setupUi(self)  # call the function that actually does all the stuff you set up in QtDesigner