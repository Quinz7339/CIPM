from PyQt6.QtWidgets import QApplication, QWidget,QMainWindow, QButtonGroup, QTableWidgetItem
from PyQt6 import uic
import ast
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

        #index 0 = main page
        #index 1 = add entry page
        #index 2 = edit entry page
        self.stackedWidget.setCurrentIndex(0)

        #estalishing connections for the toolbar buttons
        self.actionLock.triggered.connect(self.lockDatabase)
        self.actionAdd_Entry.triggered.connect(self.addEntry)
        self.actionEdit_Entry.triggered.connect(self.editEntry)
        self.actionDelete_Entry.triggered.connect(self.deleteEntry)
        self.actionExit.triggered.connect(self.exitManager)

        self.actionAdd_Entry.triggered.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.actionEdit_Entry.triggered.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        
        self.show()
        

    def showCredentialInfo(self):
        with open ('D:\Studies\Degree Year 3\FYP\CIPM\dict.txt','r') as f:
            self.database1 = f.readlines()
        credList=[]
        try:
            for lines in self.database1:
                cred= ast.literal_eval(lines) #evaluates the string as a dictionary
                credList.append(cred)
        except:
            pass
        self.table_credentialList.setRowCount(len(credList))
        self.table_credentialList.setColumnCount(6)
        for creds in credList:
            self.table_credentialList.setItem(credList.index(creds),0,QTableWidgetItem(creds['icon']))
            self.table_credentialList.setItem(credList.index(creds),1,QTableWidgetItem(creds['title']))
            self.table_credentialList.setItem(credList.index(creds),2,QTableWidgetItem(creds['username']))
            self.table_credentialList.setItem(credList.index(creds),3,QTableWidgetItem(creds['url']))
            self.table_credentialList.setItem(credList.index(creds),4,QTableWidgetItem(creds['remarks']))
            self.table_credentialList.setItem(credList.index(creds),5,QTableWidgetItem(creds['dateMod']))
        return
    
    def exitManager(self):
        print("Exit Manager")
        self.lockDatabase()
        self.close()
        return
    def lockDatabase(self):
        print("Lock Database")
        return
    
    def entry_UI(self):
        self.btn_Confirm.setStyleSheet('QPushButton {background-color: #5B9BD5; color: #FFFFFF; font-size: 18px}')
        self.btn_Cancel.setStyleSheet('QPushButton {background-color: #40444B; color: #A6A6A6; font-size: 18px}')
        self.stackedWidget.btn_Confirm.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.stackedWidget.btn_Cancel.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))

    def addEntry(self):
        self.entry_UI()
        
        print("Add Entry")
        return
    def confirmAddEntry(self):
        print("Confirm add Entry")
        return
    def editEntry(self):
        # self.stackedWidget.setCurrentIndex(1)
        self.entry_UI()
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