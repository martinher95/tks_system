import time
from PyQt5 import QtCore, QtGui, QtWidgets

import db.database
import main
import gui.listview


class Ui_NewWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(285, 315)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameline = QtWidgets.QLineEdit(self.centralwidget)
        self.nameline.setGeometry(QtCore.QRect(20, 70, 241, 20))
        self.nameline.setObjectName("lineEdit")
        self.carline = QtWidgets.QLineEdit(self.centralwidget)
        self.carline.setGeometry(QtCore.QRect(20, 120, 141, 20))
        self.carline.setObjectName("lineEdit_2")
        self.brandline = QtWidgets.QLineEdit(self.centralwidget)
        self.brandline.setGeometry(QtCore.QRect(20, 170, 141, 20))
        self.brandline.setObjectName("lineEdit_3")
        self.plateline = QtWidgets.QLineEdit(self.centralwidget)
        self.plateline.setGeometry(QtCore.QRect(20, 220, 141, 20))
        self.plateline.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Novo veículo"))
        self.label.setText(_translate("MainWindow", "Nome do motorista"))
        self.label_2.setText(_translate("MainWindow", "Veículo"))
        self.label_3.setText(_translate("MainWindow", "Marca"))
        self.label_4.setText(_translate("MainWindow", "Placa"))
        self.pushButton.setText(_translate("MainWindow", "Cadastrar"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancelar"))
        self.label_5.setText(_translate("MainWindow", "Novo veículo"))



