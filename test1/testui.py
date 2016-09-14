# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\i067382\PycharmProjects\test1\testui.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Ui_Form()
    myapp.show()
    sys.exit(app.exec_())

