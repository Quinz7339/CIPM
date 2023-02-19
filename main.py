import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6 import uic

import resource_rc

class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui',self)

        #Initializing landing page UI
        self.setWindowTitle("CIPM - Cybersecrurity Integrated Password Manager")
        self.resize (640, 480)
        
        
        id = QFontDatabase.addApplicationFont("zh-cn.ttf")
        if id < 0: print("Error")


        #Creating layout to store widgets
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        
        #Creating widgets
        #self.input_masterpassword = QLineEdit()
        #btn_Unlock = QPushButton("Unlock")
        self.btn_CreateDb.clicked.connect(self.CreateDatabase)

        #self.output = QTextEdit()

        # layout.addWidget(self.input_masterpassword)
        # layout.addWidget(btn_Unlock)
        # layout.addWidget(self.output)


        '''code block for hiding passwords'''
        # self.input_masterpassword.setPlaceholderText("Enter Master Password")
        # self.input_masterpassword.setEchoMode(QLineEdit.EchoMode.Password)


    def CreateDatabase(self):
        #1. Let user create database name
        #2. Let user add a descriptionS
        #3. Ask for user master password (include password generator and visisibility toggle)
        #4. Confirm master password
        #5. Done -> Let them store at arbitary file location

        
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
