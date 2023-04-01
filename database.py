#Author         : Chua Philip
#Name of program: CIPM - Cybersecurity Integrated Password Manager
#Program name   : database.py
#Description    : This holds the modules related to database creation, opening and encryption.
#First written on: 19/02/2023
#Last modified  : 13/03/2023

from PyQt6.QtWidgets import QFileDialog, QLineEdit, QWidget, QMessageBox
from PyQt6 import uic

import os
import Passwords

############################################################################################################
################             Class to create new password database     #####################################
############################################################################################################
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

    """----------------------------------------------------------------------
     supporting functions for CreateDb user interface logic - fields checker
    -------------------------------------------------------------------------"""
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
    

    '''-------------------------------------------------------------------------------------
    main function for file creation and encryption using entered database name and password
    ----------------------------------------------------------------------------------------''' 
    def CreateDb_checkout(self):
        db_name = self.lineEdit_dbName.text()
        db_master_passwd = self.lineEdit_MasterPasswd.text()
        folderPath = ''

        #try catch block to catch if no folder is selected for database file creation
        try:
            folderPath = QFileDialog.getExistingDirectory(
            self, 
            caption="Select the location to create a new folder to store your password database files...", 
            directory=self.default_dir,
            options=QFileDialog.Option.DontUseNativeDialog
            )
            if folderPath == '':
                print ("No folder selected. Closing file dialog.")
                raise Exception("No directories/folders were selected.")
            folderPath = folderPath + "/" + db_name
            os.mkdir(folderPath)
            print("Folder created.")
        except:
            error = QMessageBox(self)
            error.setIcon(QMessageBox.Icon.Critical)
            error.setText("No folder were selected or an identical named folder is found in the selected location..")
            error.setInformativeText("Please select a location (or another directory) to create a new folder to store your password database files.")
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.exec()
            return

        #if a folder is selected, the salt file is created and the database file is created and encrypted
        if folderPath != '':
            salt = str(Passwords.salter())

            #w is used instead of wb because salt is a string, not bytes
            with open(os.path.join(folderPath, db_name + "_salt.txt"), 'w') as salt_file:
                salt_file.write(salt)

            #establishing the parameters for the encryptor function    
            encryptor = Passwords.encryptor(bytes(db_master_passwd,'utf-8'), bytes(salt,'utf-8'))
            
            #creates a blank database file with the name entered by the user and the .cipm extension
            db_filename = folderPath + "//" + db_name + ".cipm"            
            with open(db_filename,'w') as db:
                pass
            
            #reads the empty database file and encrypts it
            with open(db_filename,'rb') as db:
                unencrypted_db = db.read()

            #encrypts the database file
            encrypted_db = encryptor.encrypt(unencrypted_db)

            #writes the encrypted database file
            with open(db_filename,'wb') as db:
                db.write(encrypted_db)

            output = QMessageBox(self)
            output.setIcon(QMessageBox.Icon.Information)
            output.setWindowTitle("Database created.")
            output.setText("Database created successfully.")
            output.setInformativeText("Please remember your master password. You can unlock the database by clicking the 'Unlock Database' button.")
            output.setStandardButtons(QMessageBox.StandardButton.Ok)
            output.exec()
            self.close()      

############################################################################################################
################             Class to unlock selected database      ########################################
############################################################################################################
class OpenDb(QWidget):
    def __init__(self, parent=None):
        super(OpenDb,self).__init__(parent=parent)
        self.user_path = os.path.expanduser('~')            #'C:\Users\<username>'
        self.default_dir = self.user_path+"\\Documents"     #'C:\Users\<username>\Documents'
        
        self.decrypted_flag = False #flag to enable passing of decryption status
        uic.loadUi('unlockdb.ui', self)

        #styling of the unlockdb.ui window
        self.setWindowTitle("Unlocking database....")
        self.btn_unlockDb.setStyleSheet('QPushButton {background-color: #5B9BD5; color: #FFFFFF; font-size: 18px}')
        self.btn_cancelUnlock.setStyleSheet('QPushButton {background-color: #40444B; color: #A6A6A6; font-size: 18px}')
        self.lineEdit_MasterPasswd.setStyleSheet('QLineEdit {background-color: #FFFFFF; color: #000000; font-size: 18px}')
        self.SelectDb()
        self.database = ''

    '''-------------------------------------------------------------
    function to select the database file to be opened and decrypted
    -------------------------------------------------------------'''       
    def SelectDb(self):
        file_path = ''

        #try catch block to catch if no file is selected
        try:
            #QFileDialog (response variable) returns a tuple with 2 values
            #1. full file path of the selected file   <--- this is the value we want
            #2. file type of the selected file
            response = QFileDialog.getOpenFileName(
                self,
                caption='Select a file',
                directory=self.default_dir,
                filter='CIPM database file (*.cipm)',
                options=QFileDialog.Option.DontUseNativeDialog
                )
            file_path = response[0]
            if file_path == '':
                raise Exception("No directories/folders were selected.")
        except:
            error = QMessageBox(self)
            error.setIcon(QMessageBox.Icon.Critical)
            error.setWindowTitle("No file selected.")
            error.setText("No database file were selected.")
            error.setInformativeText("Please select a .cipm file to unlock.")
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.exec()
            self.close()
            return
        
        self.file_path = file_path
        self.dir_name = os.path.dirname(file_path)

        if ".cipm" not in self.file_path:
            return ""
        else:
            self.lbl_unlockFileName.setText("Unlocking [{}] CIPM database".format(os.path.basename(self.file_path)))
            self.lbl_unlockFileDir.setText("Location: {}".format(self.dir_name))
            self.show()
            self.lineEdit_MasterPasswd.setEchoMode(QLineEdit.EchoMode.Password)
            self.btn_unlockDb.clicked.connect(self.DecryptDb)
            self.btn_cancelUnlock.clicked.connect(self.close)
    
    '''-------------------------------------------------------------
    supporting function to decrypt the selected database file
    -------------------------------------------------------------''' 
    def has_decrypted(self):
        return True if self.decrypted_flag == True else False
    
    '''-------------------------------------------------------------
    function to decrypt the selected database file
    -------------------------------------------------------------'''
    def DecryptDb(self):
        self.file_name = os.path.basename(self.file_path).split(".")[0]
        try:
            with open (self.dir_name + "//" + self.file_name + "_salt.txt", 'r') as salt_file:
                self.salt = salt_file.read()
            with open (self.file_path, 'rb') as db:
                encrypted_db = db.read()  
        except:
            error = QMessageBox(self)
            error.setIcon(QMessageBox.Icon.Critical)
            error.setWindowTitle("File not found.")
            error.setText("The salt file was not found.")
            error.setInformativeText("Please ensure that the salt file is in the same directory as the database file.")
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.exec()
            return
        
        self.db_master_passwd = self.lineEdit_MasterPasswd.text()
        try:
            decryptor = Passwords.decryptor(bytes(self.db_master_passwd,'utf-8'), bytes(self.salt,'utf-8'))
            decrypted_db = decryptor.decrypt(encrypted_db)
            self.database = decrypted_db.decode()
            self.decrypted_flag = True
        except: 
            self.decrypted_flag = False
            error = QMessageBox(self)
            error.setIcon(QMessageBox.Icon.Critical)
            error.setWindowTitle("Incorrect password/Invalid files.")
            error.setText("The password you entered is incorrect or the database fiels are not generated by the program.")
            error.setInformativeText("Please try again.")
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.exec()
            return
        
        if self.decrypted_flag == True:
            self.btn_unlockDb.clicked.disconnect(self.DecryptDb)
            self.btn_unlockDb.animateClick()         
            self.close()
            return

############################################################################################################
########################             Class to emcrypt selected      ########################################
############################################################################################################

class EncryptDb(QWidget):
    def __init__(self):
        super().__init__()

    def encrypt(self):
        #encrypt the database file
        encryptor = Passwords.encryptor(bytes(self.db_master_password,'utf-8'), bytes(self.salt,'utf-8'))
        encrypted_db = encryptor.encrypt(bytes(self.database,'utf-8'))

        encrypted_db.decode()
        with open (self.dir_name + "//" + self.file_name +".cipm", 'wb+') as file:
            file.write(encrypted_db)
        return