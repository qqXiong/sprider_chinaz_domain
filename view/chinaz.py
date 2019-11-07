# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chinaz.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(515, 665)
        self.okButton = QtWidgets.QPushButton(Widget)
        self.okButton.setGeometry(QtCore.QRect(360, 130, 112, 32))
        self.okButton.setObjectName("okButton")
        self.result = QtWidgets.QTextEdit(Widget)
        self.result.setGeometry(QtCore.QRect(43, 180, 431, 451))
        self.result.setObjectName("result")
        self.host = QtWidgets.QLineEdit(Widget)
        self.host.setGeometry(QtCore.QRect(90, 20, 161, 21))
        self.host.setObjectName("host")
        self.port = QtWidgets.QLineEdit(Widget)
        self.port.setGeometry(QtCore.QRect(310, 20, 161, 21))
        self.port.setObjectName("port")
        self.user = QtWidgets.QLineEdit(Widget)
        self.user.setGeometry(QtCore.QRect(90, 50, 161, 21))
        self.user.setObjectName("user")
        self.passwd = QtWidgets.QLineEdit(Widget)
        self.passwd.setGeometry(QtCore.QRect(310, 50, 161, 21))
        self.passwd.setObjectName("passwd")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 58, 16))
        self.label_2.setObjectName("label_2")
        self.db = QtWidgets.QLineEdit(Widget)
        self.db.setGeometry(QtCore.QRect(90, 90, 161, 21))
        self.db.setObjectName("db")
        self.charset = QtWidgets.QLineEdit(Widget)
        self.charset.setGeometry(QtCore.QRect(310, 90, 161, 21))
        self.charset.setObjectName("charset")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(260, 50, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(260, 90, 58, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.okButton.setText(_translate("Widget", "开始"))
        self.label.setText(_translate("Widget", "host"))
        self.label_2.setText(_translate("Widget", "user"))
        self.label_3.setText(_translate("Widget", "port"))
        self.label_4.setText(_translate("Widget", "passwd"))
        self.label_5.setText(_translate("Widget", "db"))
        self.label_6.setText(_translate("Widget", "charset"))
