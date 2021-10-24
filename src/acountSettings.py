# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acount-settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AcountSettings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setStyleSheet("background-color: #fff; border-radius: 5px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.acount_email_2 = QtWidgets.QLabel(self.centralwidget)
        self.acount_email_2.setGeometry(QtCore.QRect(125, 70, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.acount_email_2.setFont(font)
        self.acount_email_2.setStyleSheet("color: #010A1A;")
        self.acount_email_2.setObjectName("acount_email_2")
        self.username_en = QtWidgets.QLineEdit(self.centralwidget)
        self.username_en.setGeometry(QtCore.QRect(255, 70, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.username_en.setFont(font)
        self.username_en.setStyleSheet("background-color: #DEDEDE; color: #010A1A;")
        self.username_en.setObjectName("username_en")
        self.username_en_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.username_en_2.setGeometry(QtCore.QRect(255, 120, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.username_en_2.setFont(font)
        self.username_en_2.setStyleSheet("background-color: #DEDEDE; color: #010A1A;")
        self.username_en_2.setObjectName("username_en_2")
        self.acount_email_3 = QtWidgets.QLabel(self.centralwidget)
        self.acount_email_3.setGeometry(QtCore.QRect(125, 120, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.acount_email_3.setFont(font)
        self.acount_email_3.setStyleSheet("color: #010A1A;")
        self.acount_email_3.setObjectName("acount_email_3")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(125, 190, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("background-color: #0088CC; color: #fff;")
        self.btn_login.setObjectName("btn_login")
        self.btn_login_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login_2.setGeometry(QtCore.QRect(315, 190, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_login_2.setFont(font)
        self.btn_login_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login_2.setStyleSheet("background-color: #DEDEDE; color: #010A1A;")
        self.btn_login_2.setObjectName("btn_login_2")
        self.alarmlb = QtWidgets.QLabel(self.centralwidget)
        self.alarmlb.setGeometry(QtCore.QRect(125, 160, 360, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.alarmlb.setFont(font)
        self.alarmlb.setStyleSheet("color: #d1131f;")
        self.alarmlb.setText("")
        self.alarmlb.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmlb.setObjectName("alarmlb")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 10, 600, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color: #010A1A;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typing online"))
        self.acount_email_2.setText(_translate("MainWindow", "Change Username:"))
        self.acount_email_3.setText(_translate("MainWindow", "Change Emal:"))
        self.btn_login.setText(_translate("MainWindow", "Save Changes"))
        self.btn_login_2.setText(_translate("MainWindow", "Cancel"))
        self.title.setText(_translate("MainWindow", "Acount Settings"))
