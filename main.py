import sys
import os

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QTextEdit,QFileDialog
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6 import uic

from cryptography.fernet import Fernet
from argon2 import PasswordHasher

import resource_rc
from createdb import CreateDb

class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui',self)

        #Initializing landing page UI
        self.setWindowTitle("CIPM - Cybersecrurity Integrated Password Manager")
        self.resize (800, 540)
        
        
        id = QFontDatabase.addApplicationFont("zh-cn.ttf")
        if id < 0: print("Error")


        #Creating layout to store widgets
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        
        #Creating widgets
        #self.input_masterpassword = QLineEdit()
        #btn_Unlock = QPushButton("Unlock")
        self.btn_CreateDb.clicked.connect(self.CreateDatabase)
        self.btn_OpenDb.clicked.connect(self.OpenDatabase)  

        '''dummy code'''
        #self.output = QTextEdit()
        # layout.addWidget(self.input_masterpassword)
        # layout.addWidget(btn_Unlock)
        # layout.addWidget(self.output)


        '''code block for hiding passwords'''
        # self.input_masterpassword.setPlaceholderText("Enter Master Password")
        # self.input_masterpassword.setEchoMode(QLineEdit.EchoMode.Password)


    def CreateDatabase(self):
        print ("Hi")
        self.createdb = CreateDb()
        self.createdb.show()

        return


    def OpenDatabase(self):
        #snippet adapted from https://www.youtube.com/watch?v=V_TU0eCOVP8&list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB&index=37
        file_filter = 'CIPM file (*.cipm)'
        
        #response returns a tuple with 2 values
        #1. full file path of the selected file
        #2. file type of the selected file
        response = QFileDialog.getOpenFileName(
            self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter = 'CIPM file (*.cipm)'
            )
        file = response[0]
        if file == '':
            print ("No file selected")
            return
        else: 
            f = open(file, "r")
        print (file)
        #pass the f around
        return

    def unlock(self):
        inputText = self.input_masterpassword.text()
        self.output.setText("You entered {0}".format(inputText))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #setstylesheet methods applies to child widgets as well
    app.setStyleSheet('''
        QWidget {
            background-color: #40444B;
            font-size: 18px;  
        }
        QPushButton {
            font-size: 25px;
        }
        QLabel {
            color: #FFFFFF;
        }
        QToolButton{
            background-color: #BFBFBF;
            border-radius: 15px;
        }
        QTextEdit{
            background-color: #BFBFBF;
            border-radius: 15px;
        }    
    ''')

    window = Main()
    window.show()
    #wrap QApplication with sys.exit() to ensure the application is closed properly
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
