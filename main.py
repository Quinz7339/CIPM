import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QTextEdit,QFileDialog
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6 import uic

import resource_rc
from database import CreateDb, OpenDb

#main class to initialize the landing page
#this class will hold abstracted functions to call the corresponding UIs
class Main(QWidget): 
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui',self)

        #Initializing landing page UI
        self.setWindowTitle("CIPM - Cybersecrurity Integrated Password Manager")
        self.resize (800, 540)
        
        id = QFontDatabase.addApplicationFont("zh-cn.ttf") #changes the application's font to the one specified
        if id < 0: 
            print("Error")   #prints error if font is not found

        self.btn_CreateDb.clicked.connect(self.CreateDatabase)
        self.btn_OpenDb.clicked.connect(self.OpenDatabase)  

    
        
    '''-------------------------------------------------------------
    function to call the createdb UI - for database creation
    -------------------------------------------------------------'''
    def CreateDatabase(self):
        print ("\nCreate Database function is called in main.py")
        self.createdb = CreateDb()
        self.createdb.show()
        return

    '''-------------------------------------------------------------
    function to call unlockdb UI - for database unlocking
    -------------------------------------------------------------'''
    def OpenDatabase(self):
        print ("\nOpen Database function is called in main.py")
        self.opendb = OpenDb()
        self.database = self.opendb.database
        #logic to return the database done dy

        if self.database != '':
            print ("Under if - Open DB function:",self.database)
            return
        else:
            return

    '''---------------------------------------------------------------
    function to call dashboard UI - for displaying the main dashboard
    ------------------------------------------------------------------'''
    def Dashboard(self):
        self.close()
        print ("Hi")
        #self.dashboard = 
        inputText = self.input_masterpassword.text()
        self.output.setText("You entered {0}".format(inputText))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #declaration of the application wide stylesheet
    #setStyleSheet method applies to all child widgets
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

    #wraps QApplication with sys.exit() to ensure the application is closed properly
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
