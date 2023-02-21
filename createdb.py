from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6 import uic

import sys

class CreateDb(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('createdb.ui',self)
        self.setWindowTitle("Create Database")
        self.resize (568, 320)
        self.setStyleSheet('''
            QLabel{
                font-size: 18px;
            }
            QLineEdit{
                color: #FFFFFF;
            }
            QPushButton{
                font-size: 15px;
                color: #FFFFFF;
                background-color: #BFBFBF;
            }
        ''')
        print("CreateDb UI loaded")
        #makes the password fields show dots instead of characters
        self.lineEdit_MasterPasswd.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_MasterPasswd2.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.btn_dbCreate.setEnabled(False) #disables the Create button until all fields are filled
        self.btn_dbCreate.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB;}')
        self.show()

        self.lineEdit_dbName.textChanged.connect(self.CreateDb_dbName_checker)
        self.lineEdit_MasterPasswd.textChanged.connect(self.CreateDb_fieldChecker)
        self.lineEdit_MasterPasswd2.textChanged.connect(self.CreateDb_fieldChecker)

        self.btn_dbCreate.clicked.connect(self.CreateDb_checkout)
        self.btn_dbBack.clicked.connect(self.close)

    """

     supporting functions for UI logic

    """
    #disables the Create button, shows a message, until a name is entered
    def CreateDb_dbName_checker(self): 
        if (len(self.lineEdit_dbName.text()) <=0):
            self.btn_dbCreate.setEnabled(False)
            self.btn_dbCreate.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB;}')
            self.lbl_dbName_msg.setText("Please enter a database name.")
            self.lbl_dbName_msg.setStyleSheet('QLabel {color: #FF0000;}')
        else:
            self.CreateDb_fieldChecker()
            self.lbl_dbName_msg.setText("")

    # #disables the Create button, shows a message, until a master password is entered
    # def CreateDb_MasterPasswd_checker(self):
    #     #display
    #     if (len(self.lineEdit_MasterPasswd.text()) <=0):
    #         self.btn_dbCreate.setEnabled(False)
    #         self.lbl_MasterPasswd_msg.setText("Please enter a master password.")
    #         self.lbl_MasterPasswd_msg.setStyleSheet('QLabel {color: #FF0000;}')
    #     elif (len(self.lineEdit_MasterPasswd.text()) >0 & (len(self.lineEdit_MasterPasswd.text()) <8)):
    #         self.btn_dbCreate.setEnabled(False)
    #         self.lbl_MasterPasswd_msg.setText("Please enter a password with at least 8 characters.")
    #     else:
    #         self.btn_dbCreate.setEnabled(False)
    #         self.lbl_MasterPasswd_msg.setText("")
    
    #disables the Create button, shows a message, until all fields are entered and correct
    def CreateDb_fieldChecker(self):
        #ensures all fields are entered as intended
        if (len(self.lineEdit_MasterPasswd.text()) <=0):
            self.btn_dbCreate.setEnabled(False)
            self.lbl_MasterPasswd_msg.setText("Please enter a master password.")
            self.lbl_MasterPasswd_msg.setStyleSheet('QLabel {color: #FF0000;}')
        elif((len(self.lineEdit_MasterPasswd.text()) >=0) & ((len(self.lineEdit_MasterPasswd.text()) <=7))):
            self.btn_dbCreate.setEnabled(False)
            self.lbl_MasterPasswd_msg.setStyleSheet('QLabel {color: #FF0000;}')
            self.lbl_MasterPasswd_msg.setText("Please enter a password with at least 8 characters.")
        #(len(self.lineEdit_MasterPasswd.text()) >=8)
        else:
            if (self.lineEdit_MasterPasswd.text() == self.lineEdit_MasterPasswd2.text()) & (len(self.lineEdit_dbName.text()) >=0):
                self.btn_dbCreate.setEnabled(True)
                self.btn_dbCreate.setStyleSheet('QPushButton {background-color: #2B96CB; color: #FFFFFF;}')
                self.lbl_MasterPasswd_msg.setText("")
                print("Passwords match")
            else:
                self.btn_dbCreate.setEnabled(False)
                self.btn_dbCreate.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB;}')
                self.lbl_MasterPasswd_msg.setStyleSheet('QLabel {color: #FF0000;}')
                self.lbl_MasterPasswd_msg.setText("Entered password does not match.")
                print("Passwords do not match")           
            

    def CreateDb_checkout(self):
        print("CreateDb_checkout")
        db_name = self.lineEdit_dbName.text()
        db_master_passwd = self.lineEdit_MasterPasswd.text()

        self.close()


    