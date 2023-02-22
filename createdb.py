import os

from PyQt6.QtWidgets import QFileDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6 import uic

from cryptography.fernet import Fernet

import Passwords


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
        self.btn_dbCreate.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB;}') #sets the Create Database button to grey
        self.show()

        self.lineEdit_dbName.textChanged.connect(self.CreateDb_dbName_checker)
        self.lineEdit_MasterPasswd.textChanged.connect(self.CreateDb_fieldChecker)
        self.lineEdit_MasterPasswd2.textChanged.connect(self.CreateDb_fieldChecker)
        
        self.btn_dbCreate.clicked.connect(self.CreateDb_checkout)
        self.btn_dbBack.clicked.connect(self.close)

    """

     supporting functions for UI logic

    """
    #function - disables the Create button, shows a message, until a name is entered
    def CreateDb_dbName_checker(self): 
        if (len(self.lineEdit_dbName.text()) <=0):
            self.btn_dbCreate.setEnabled(False)
            self.btn_dbCreate.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB;}')
            self.lbl_dbName_msg.setText("Please enter a database name.")
            self.lbl_dbName_msg.setStyleSheet('QLabel {color: #FF0000;}')
        else:
            self.CreateDb_fieldChecker()
            self.lbl_dbName_msg.setText("")
    
    #function - disables the Create button, shows a message, until all fields are entered and correct
    def CreateDb_fieldChecker(self):
        #checks if master password is empty
        if (len(self.lineEdit_MasterPasswd.text()) <=0): 
            self.btn_dbCreate.setEnabled(False)
            self.lbl_MasterPasswd_msg.setText("Please enter a master password.")
            self.lbl_MasterPasswd_msg.setStyleSheet('QLabel {color: #FF0000;}')

        #checks if master password is less than 8 characters
        elif((len(self.lineEdit_MasterPasswd.text()) >=0) & ((len(self.lineEdit_MasterPasswd.text()) <=7))): 
            self.btn_dbCreate.setEnabled(False)
            self.lbl_MasterPasswd_msg.setStyleSheet('QLabel {color: #FF0000;}')
            self.lbl_MasterPasswd_msg.setText("Please enter a password with at least 8 characters.")

        #checks if all fields are filled as intended
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
            
    #function - creates the encrypted database file using the entered database name and password
    def CreateDb_checkout(self):
        print("CreateDb_checkout")
        db_name = self.lineEdit_dbName.text()
        db_master_passwd = self.lineEdit_MasterPasswd.text()

        hash = Passwords.encryptor(db_master_passwd)
        hash = Fernet(hash)
        
        default_dir ="/home/qt_user/Documents"
        default_filename = os.path.join(default_dir, db_name)
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save password database file", default_filename, "CIPM Database file (*.cipm)"
        )
        with open(filename,'rb') as db:
            unencrypted_db = db.read()

        encrypted_db = hash.encrypt(unencrypted_db)
        with open(filename,'wb') as db:
            db.write(encrypted_db)
        self.close()


    