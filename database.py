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
        self.user_path = os.path.expanduser('~')     #'C:\Users\<username>'
        self.default_dir = self.user_path+"\\Documents"   #'C:\Users\<username>\Documents'

        #makes the password fields show dots instead of characters
        self.lineEdit_MasterPasswd.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_MasterPasswd2.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.btn_dbCreate.setEnabled(False) #disables the Create button until all fields are filled
        self.btn_dbCreate.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB;}') #sets the Create Database button to grey
        self.show()
        
        #connecting textFields to field checking functions
        self.lineEdit_dbName.textChanged.connect(self.CreateDb_dbName_checker)
        self.lineEdit_MasterPasswd.textChanged.connect(self.CreateDb_fieldChecker)
        self.lineEdit_MasterPasswd2.textChanged.connect(self.CreateDb_fieldChecker)
        
        #concludes the file creation and encryption process and closes database creation window
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
    

    '''
        main function for file creation and encryption using entered database name and password
    '''

    def CreateDb_checkout(self):
        print("Entering folder and file creation phase.")
        db_name = self.lineEdit_dbName.text()
        db_master_passwd = self.lineEdit_MasterPasswd.text()
        
        folderPath = ''
        try:
            folderPath = QFileDialog.getExistingDirectory(
            self, 
            caption="Select the location to create a new folder to store your password database files...", 
            directory=self.default_dir,
            options=QFileDialog.Option.DontUseNativeDialog
            )
            if folderPath == '':
                print ("No file selected. Closing file dialog.")
                raise Exception("No directories/folders were selected.")
            folderPath = folderPath + "/" + db_name
            os.mkdir(folderPath)
            print("Folder created.")
        except:
            print("Exception caught.")
            error = QMessageBox(self)
            error.setIcon(QMessageBox.Icon.Critical)
            error.setText("No files were selected.")
            error.setInformativeText("Please select a folder to create a new folder to store your password database files.")
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.exec()
            print("Exception message closed.")

        if folderPath != '':
            salt = str(Passwords.salter())
            print("Salt: " + salt)

            #w is used instead of wb because salt is a string, not bytes
            with open(os.path.join(folderPath, db_name + "_salt.txt"), 'w') as salt_file:
                salt_file.write(salt)
                print ("Salt file created. Salt: ",salt)
                
            encryptor = Passwords.encryptor(bytes(db_master_passwd,'utf-8'), bytes(salt,'utf-8'))
            
            db_filename = folderPath + "//" + db_name + ".cipm"

            #creates a blank database file
            with open(db_filename,'w') as db:
                pass
            
            #reads the empty database file and encrypts it
            with open(db_filename,'rb') as db:
                unencrypted_db = db.read()
            
            print(unencrypted_db)
            encrypted_db = encryptor.encrypt(unencrypted_db)

            #writes the encrypted database file
            with open(db_filename,'wb') as db:
                db.write(encrypted_db)
            
            self.close()        
        
class OpenDb(QWidget):
    def __init__(self):
        super().__init__()
        #snippet adapted from https://www.youtube.com/watch?v=V_TU0eCOVP8&list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB&index=37
        self.user_path = os.path.expanduser('~')     #'C:\Users\<username>'
        self.default_dir = self.user_path+"\\Documents"   #'C:\Users\<username>\Documents'
        
        #response returns a tuple with 2 values
        #1. full file path of the selected file
        #2. file type of the selected file

        file = ''
        try:
            response = QFileDialog.getOpenFileName(
                self,
                caption='Select a file',
                directory=os.getcwd(),
                filter=self.default_dir,
                initialFilter = 'CIPM database file (*.cipm)',
                options=QFileDialog.Option.DontUseNativeDialog
                )
            file = response[0]
            if file == '':
                print ("No file selected. Closing file dialog.")
                raise Exception("No directories/folders were selected.")
        except:
            print ("Exception caught.")
            error = QMessageBox(self)
            error.setIcon(QMessageBox.Icon.Critical)
            error.setWindowTitle("No file selected.")
            error.setText("No database file were selected.")
            error.setInformativeText("Please select a .cipm file to unlock.")
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.exec()
            print ("Exception message closed.")
        
        if file != '':
            with open(file, 'rb') as f:
                print (f.read())
            hi = input (file)
        #open file dialog
        #get file path
        #get salt

        #create ppt slide2 ui

class EncryptDb(QWidget):
    def __init__(self):
        super().__init__()
        #create ppt slide3 ui