import socket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import pymysql
from email_validator import validate_email

try:
    connection = pymysql.connect()
    cursor = connection.cursor()
except:
    error_msg = QMessageBox()
    error_msg.setIcon(QMessageBox.Information)
    error_msg.setText("Someting went wrong")
    error_msg.setWindowTitle("Error")
    error_msg.setStandardButtons(QMessageBox.Ok )
    error_msg.buttonClicked.connect(lambda: error_msg.close())
    error_msg.exec_()

from mainpage import Ui_MainWindow
from login import Ui_LonginWindow
from signup import Ui_SignupWindow
from acountSettings import Ui_AcountSettings

class AcountSettingsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_AcountSettings()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = AcountSettingsWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class SignupWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = SignupWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_LonginWindow()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = LoginWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.main = Ui_MainWindow()
        self.main.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #===========================My codes===================
        
        # windows
        self.login = LoginWindow()
        self.signup = SignupWindow()
        self.acountsettings = AcountSettingsWindow()

        # get ips from database | check if its new or not
        cursor.execute("SELECT ip FROM acounts;")
        self.ips = []
        for ip in cursor:
            self.ips.append(ip[0])

        self.userip = str(socket.gethostname())
        if self.userip in self.ips:
            print('already loged in')
        else:
            self.logingin()

    #===============================Designer codes=============
    def borders(self):
        self.mainwindow = RootMain()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    #===============================My funcitons================
    
    # open signin or login page
    def logingin(self):

        # sign in page
        def signing():
            self.login.close()
            self.signup.show()

            def putInfoToDB():

                # check infos
                correct_info = True

                # check blanks
                if ((self.signup.ui.username_en.text()).strip() == '') or ((self.signup.ui.email_en.text()).strip() == '') or ((self.signup.ui.password_en.text()).strip() == '') or ((self.signup.ui.repassword_en.text()).strip() == ''):
                    self.signup.ui.alarmlb.setText('Fill all the blanks') 
                    correct_info = False
                else:
                    # check password
                    numbers = '1234567890'
                    alphabets = 'mnbvcxzasdfghjklpoiuytrewqMNBVCXZASDFGHJKLPOIUYTREWQ'
                    signs = '!@#$%^&*()_-/+'
                    if self.signup.ui.password_en.text() != self.signup.ui.repassword_en.text():
                        self.signup.ui.alarmlb.setText('Passwords are not the same')
                        correct_info = False

                    else:
                        check_pass = [False , False , False]
                        for letter in self.signup.ui.password_en.text():
                            if (letter not in numbers) and (letter not in alphabets) and (letter not in signs):
                                self.signup.ui.alarmlb.setText('Password should contains numbers and alphabets and signs')
                                correct_info = False
                            else:
                                if letter in numbers:
                                    check_pass[0] = True
                                elif letter in alphabets:
                                    check_pass[1] = True
                                elif letter in signs:
                                    check_pass[2] = True
                        
                        if check_pass != [True , True , True]:
                            self.signup.ui.alarmlb.setText('Password should contains numbers and alphabets and signs')
                            correct_info = False
                        else:
                            self.signup.ui.alarmlb.setText('')

                    # check email     
                    try:
                        validate_email(self.signup.ui.email_en.text())

                        cursor.execute("SELECT email FROM acounts;")
                        db_emails = []
                        for email in cursor:
                            db_emails.append(email[0])
                        if self.signup.ui.email_en.text() in db_emails:
                            self.signup.ui.alarmlb.setText('Email already exists')
                            correct_info = False

                    except:
                        self.signup.ui.alarmlb.setText('Email address is not valid')
                        correct_info = False

                    # check username
                    for letter in self.signup.ui.username_en.text():
                        if (letter not in numbers) and (letter not in alphabets) and (letter not in signs):
                            self.signup.ui.alarmlb.setText('Username is not valid')
                            correct_info = False
                        else:
                            cursor.execute("SELECT username FROM acounts;")
                            db_usernames = []
                            for username in cursor:
                                db_usernames.append(username[0])
                            if self.signup.ui.username_en.text() in db_usernames:
                                self.signup.ui.alarmlb.setText('Username already exists')
                                correct_info = False
                            break
                
                # insert infos to database
                if correct_info == True:
                    try:
                        username = self.signup.ui.username_en.text()
                        email = self.signup.ui.email_en.text()
                        password = self.signup.ui.password_en.text()
                        ip = str(socket.gethostname())
                        quary = "INSERT INTO acounts VALUES( \'%s\' , \'%s\' , \'%s\' , \'%s\' );" % (username , email , password , ip)
                        cursor.execute(quary)
                        connection.commit()
                    except:
                        error_msg = QMessageBox()
                        error_msg.setIcon(QMessageBox.Information)
                        error_msg.setText("Someting went wrong")
                        error_msg.setWindowTitle("Error")
                        error_msg.setStandardButtons(QMessageBox.Ok )
                        error_msg.buttonClicked.connect(lambda: error_msg.close())
                        error_msg.exec_()
                    
                    

            self.signup.ui.btn_login.clicked.connect(self.logingin)
            self.signup.ui.btn_signup.clicked.connect(putInfoToDB)

            

        # login page
        self.login.show()
        self.signup.close()
        self.login.ui.btn_signup.clicked.connect(signing)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())