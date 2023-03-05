from PyQt6.QtWidgets import QApplication, QWidget,QMainWindow
from PyQt6 import uic
import sys

import resource_rc


'''import re

from bs4 import BeautifulSoup

html_code = "<Some HTML code you get from somewhere>"

soup = BeautifulSoup(html_code, features="lxml")

for item in soup.find_all('link', attrs={'rel': re.compile("^(shortcut icon|icon)$", re.I)}):
    print(item.get('href'))'''

class Manager(QMainWindow): 
    def __init__(self):
        super().__init__()
        uic.loadUi('password_manager.ui',self)
        self.setWindowTitle("Passwords - CIPM")
        self.toolBar.setStyleSheet('QToolBar {spacing: 30px; background-color: #BFBFBF;}')
        self.toolBar.layout().setContentsMargins(5,5,5,5) #left, top, right, bottom

        self.database = None
        self.showCredentialInfo()

        #estalishing connections for the toolbar buttons
        self.actionLock.triggered.connect(self.lockDatabase)
        self.actionAdd_Entry.triggered.connect(self.addEntry)
        self.actionEdit_Entry.triggered.connect(self.editEntry)
        self.actionDelete_Entry.triggered.connect(self.deleteEntry)
        self.actionExit.triggered.connect(self.exitManager)

        
        #insert code to intialize UI styling
        self.show()
        

    def showCredentialInfo(self):
        credentialList = []
        credentialInfos = []
        #self.database = "icon here,title,username,password,url,remarks\nicon2 here,title2,username2,password2,url2,remarks2"
        try:
            for credential in self.database.split("\n"):
                credentialInfos = credential.split(",")
                credentialList.append(credentialInfos)
        except:
            pass
        #insert code of adding credentialList to the table
        
        print ("Credential list",credentialList)

        return
    
    def exitManager(self):
        print("Exit Manager")
        self.lockDatabase()
        self.close()
        return
    def lockDatabase(self):
        print("Lock Database")
        return
    def addEntry(self):
        
        print("Add Entry")
        return
    def editEntry(self):
        print("Edit Entry")
        return
    def deleteEntry(self):
        print("Delete Entry")
        return


'''comment the code block below after testing'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
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
    window = Manager()
    window.show()

    #wraps QApplication with sys.exit() to ensure the application is closed properly
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")