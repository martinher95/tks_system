from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Charge(object):
    def setupUi(self, Form):
        Form.resize(203, 192)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 75, 23))
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 50, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.payline = QtWidgets.QLineEdit(Form)
        self.payline.setGeometry(QtCore.QRect(60, 90, 111, 31))
        self.label_value = QtWidgets.QLabel(Form)
        self.label_value.setGeometry(QtCore.QRect(70, 50, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_value.setFont(font)
        self.label_change = QtWidgets.QLabel(Form)
        self.label_change.setGeometry(QtCore.QRect(50, 131, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_change.setFont(font)
        self.label_hours = QtWidgets.QLabel(Form)
        self.label_hours.setGeometry(QtCore.QRect(70, 15, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_hours.setFont(font)
        self.label_hours.setStyleSheet("color: rgb(255, 0, 0);")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cobrança"))
        self.pushButton.setText(_translate("Form", "Ok"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))
        self.label.setText(_translate("Form", "Valor:"))
        self.label_2.setText(_translate("Form", "Pago: "))
        self.label_3.setText(_translate("Form", "Troco:"))
        self.label_4.setText(_translate("Form", "Horas:"))
        self.label_value.setText(_translate("Form", "R$0"))
        self.label_change.setText(_translate("Form", "R$0"))
        self.label_hours.setText(_translate("Form", "0"))