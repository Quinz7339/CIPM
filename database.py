import os

from PyQt6.QtWidgets import QFileDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
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

        print("Entering folder and file creation phase.")
        db_name = self.lineEdit_dbName.text()
        db_master_passwd = self.lineEdit_MasterPasswd.text()

        user_path = os.path.expanduser('~')     #'C:\Users\<username>'
        default_dir = user_path+"\\Documents"   #'C:\Users\<username>\Documents'
        
        folderPath = ''
        while folderPath == '':
            try:
                folderPath = QFileDialog.getExistingDirectory(self, 
                caption="Select the location to create a new folder to store your password database files...", 
                directory=default_dir,
                options=QFileDialog.Option.DontUseNativeDialog
                )
                if folderPath == '':
                    raise Exception("No directories/folders were selected.")
                folderPath = folderPath + "/" + db_name
                os.mkdir(folderPath)
                print("Folder created.")

            except:
                error = QMessageBox(self)
                error.setIcon(QMessageBox.Icon.Critical)
                error.setText("No files were selected.")
                error.setInformativeText("Please select a folder to create a new folder to store your password database files.")
                error.setStandardButtons(QMessageBox.StandardButton.Ok)
                error.exec()
                print("Folder creation failed.")
       
        salt = str(Passwords.salter())
        hi =input ("Salt: " + salt)

        #w is used instead of wb because salt is a string, not bytes
        with open(os.path.join(folderPath, db_name + "_salt.txt"), 'w') as salt_file:
            salt_file.write(salt)
            print ("Salt file created. Salt: ",salt)
            
        encryptor = Passwords.encryptor(bytes(db_master_passwd,'utf-8'), bytes(salt,'utf-8'))
        
        db_filename = folderPath + "//" + db_name + ".CIPM"
        with open(db_filename,'w') as db:
            pass
        
        with open(db_filename,'rb') as db:
            unencrypted_db = db.read()

        encrypted_db = encryptor.encrypt(unencrypted_db)

        with open(db_filename,'wb') as db:
            db.write(encrypted_db)

        self.close()
        
        #with open(os.path.join(folderPath, "salt.txt"), 'rb') as salt_file:
            #salt = salt_file.read()

      
    