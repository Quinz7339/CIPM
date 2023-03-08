from PyQt6.QtWidgets import QApplication, QWidget,QMainWindow, QTableWidgetItem, QPushButton, QLineEdit, QMessageBox
from PyQt6 import uic
from PyQt6.QtGui import QColor, QIcon, QAction

from datetime import date
from Passwords import gen_password
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
        with open ('D:\Studies\Degree Year 3\FYP\CIPM\dict.txt','r') as f:
            self.database = f.readlines()
        self.credList=[]
        try:
            for lines in self.database:
                cred = ast.literal_eval(lines) #literal_eval is used to convert the string to a dictionary
                self.credList.append(cred)
        except:
            pass
        self.populateCredentials()

        #index 0 = main page
        #index 1 = add entry page
        #index 2 = edit entry page
        self.stackedWidget.setCurrentIndex(0)

        #hiding the frame containing the specific entry details
        self.frame_credDetail.hide()

        #estalishing connections for the toolbar buttons
        self.actionLock.triggered.connect(self.lockDatabase)
        self.actionAdd_Entry.triggered.connect(self.addEntry)
        self.actionEdit_Entry.triggered.connect(self.editEntry)
        self.actionDelete_Entry.triggered.connect(self.deleteEntry)
        self.actionExit.triggered.connect(self.exitManager)

        self.actionAdd_Entry.triggered.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.actionEdit_Entry.triggered.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        
        #estalishing connections for showing/hiding the frame displaying the specific entry details
        self.table_credentialList.cellClicked.connect(self.showCredentialDetails)

        #initialization of session variab;es
        self.togglePwd_action = ''
        self.genPwd_action = ''
        self.pwdLength = 8
        self.show()
        
    '''----------------------------------------------------------------
    initial function to populate the QTableWidget with the credentials
    ------------------------------------------------------------------'''
    def populateCredentials(self):

        #sorting the list of dictionaries by the title key
        self.credList = sorted(self.credList, key=lambda k: k['title']) 

        #initializing the dimensions of the table
        self.table_credentialList.setRowCount(len(self.credList))
        self.table_credentialList.setColumnCount(6)

        #populating the table with the details of the credentials
        for creds in self.credList:
            #self.table_credentialList.setItem(self.credList.index(creds),0,QTableWidgetItem(<insert code to get favicon>)
            self.table_credentialList.setItem(self.credList.index(creds),1,QTableWidgetItem(creds['title']))
            self.table_credentialList.setItem(self.credList.index(creds),2,QTableWidgetItem(creds['username']))
            self.table_credentialList.setItem(self.credList.index(creds),3,QTableWidgetItem(creds['url']))
            self.table_credentialList.setItem(self.credList.index(creds),4,QTableWidgetItem(creds['remarks']))
            self.table_credentialList.setItem(self.credList.index(creds),5,QTableWidgetItem(creds['dateMod']))
        return
    
    '''----------------------------------------------------------------
    function called when the user clicks on the "Add Entry" button
    ------------------------------------------------------------------'''
    def showCredentialDetails(self):
        self.btn_closeCredInfo.clicked.connect(self.hideCrendentialDetails)
        self.frame_credDetail.show()

        #populating labels based on selected credential (QTableWidget Row)
        self.lbl_credTitle.setText(self.credList[self.table_credentialList.currentRow()]['title']) #QTableWidget.currentRow() = returns the row number of the selected row
        
        #self.lbl_credIcon.setPixmap(<insert part to fetch icon programitically>)
        self.lbl_Username.setText("Username: \t" + self.credList[self.table_credentialList.currentRow()]['username'])
        self.lbl_Password.setText("Password: \t" + self.credList[self.table_credentialList.currentRow()]['password'])
        self.lbl_Remarks.setText("Remarks: \t" + self.credList[self.table_credentialList.currentRow()]['remarks'])
        self.lbl_URL.setText("URL: \t\t" + self.credList[self.table_credentialList.currentRow()]['url'])
        self.lbl_dateExp.setText("Expiry Date: \t" + self.credList[self.table_credentialList.currentRow()]['dateExp'])
    

    '''----------------------------------------------------------------------
    function to hide the detailed credential information when "X" is clicked
    -------------------------------------------------------------------------'''
    def hideCrendentialDetails(self):
        self.frame_credDetail.hide()
        return

    '''----------------------------------------------------------------------
    function called when the user clicks on the "Exit" button
    -------------------------------------------------------------------------'''
    def exitManager(self):
        print("Exit Manager")
        self.lockDatabase()
        self.close()
        return
    def lockDatabase(self):
        print("Lock Database")
        return
    
    '''-------------------------------------------------------------------------
    function that initializes the UI for the "Add Entry" and "Edit Entry" pages
    ----------------------------------------------------------------------------'''
    def entry_UI(self):
        #clearing of fields
        self.lineEdit_Title.clear()
        self.lineEdit_Username.clear()
        self.lineEdit_Password.clear()
        self.lineEdit_URL.clear()
        self.textEdit_Remark.clear()
        self.lineEdit_dateExp.clear()


        #initializing the "Toggle Password Visibility" button 
        if self.togglePwd_action != '':
            self.lineEdit_Password.removeAction(self.togglePwd_action)
        self.togglePwd_action = QAction(QIcon(':/Icons/Show.svg'), 'Toggle Password visibility', self)
        self.lineEdit_Password.addAction(self.togglePwd_action, QLineEdit.ActionPosition.TrailingPosition)
        self.togglePwd_action.setCheckable(True)
        self.togglePwd_action.toggled.connect(self.togglePassword)

        #initializing the "Password Generator" button
        if self.genPwd_action != '':
            self.lineEdit_Password.removeAction(self.genPwd_action)
        self.genPwd_action = QAction(QIcon(':/Icons/Shuffle.svg'), 'Generate Password', self)
        self.lineEdit_Password.addAction(self.genPwd_action, QLineEdit.ActionPosition.TrailingPosition)
        self.genPwd_action.triggered.connect(self.generatePassword)
        

        self.btn_Confirm.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.btn_Cancel.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.btn_Confirm.setStyleSheet('QPushButton {background-color: #5B9BD5; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px}')
        self.btn_Cancel.setStyleSheet('QPushButton {background-color: #40444B; color: #A6A6A6; border-radius: 5px; font-size: 18px}')
    
    '''-------------------------------------------------------------------------
    helper function - logic of "Toggle Password Visibility" button
    ----------------------------------------------------------------------------'''
    def togglePassword(self):
        if self.togglePwd_action.isChecked():
            self.togglePwd_action.setIcon(QIcon(':/Icons/Hide.svg'))
            self.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.togglePwd_action.setIcon(QIcon(':/Icons/Show.svg'))
            self.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)

    '''-------------------------------------------------------------------------
    helper function - populate password field with a random password
    ----------------------------------------------------------------------------'''
    def generatePassword(self):
        self.lineEdit_Password.setText(gen_password(self.pwdLength))

    '''-------------------------------------------------------------------------
    function - called when user clicks on "Add Entry" button
    ----------------------------------------------------------------------------'''    
    def addEntry(self):
        self.newCred=''
        self.entry_UI() 
        self.btn_Confirm.clicked.connect(self.confirmAddEntry)
        print("Add Entry")
        return

    '''-------------------------------------------------------------------------
    function - called when user clicks "Confirm" upon adding a new entry
    ----------------------------------------------------------------------------''' 
    def confirmAddEntry(self):
        self.newCred = {
            "icon": "default",
            "title": self.lineEdit_Title.text(),
            "username": self.lineEdit_Username.text(),
            "password": self.lineEdit_Password.text(),
            "url": self.lineEdit_URL.text(),
            "remarks": self.textEdit_Remark.toPlainText(),
            "dateExp": self.lineEdit_dateExp.text(),
            "dateMod": date.today().strftime("%d/%m/%Y")
        }
        print (self.lineEdit_Password.text())
        print(self.lineEdit_Title.text())

        if (len(self.lineEdit_Password.text()) < 8):
            info = QMessageBox(self)
            info.setIcon(QMessageBox.Icon.Information)
            info.setWindowTitle("Weak Password.")
            info.setText("Maybe considering using a stronger password or use the password generator after this.")
            info.setInformativeText("Password longer than 8 characters is recommended.")
            info.setStandardButtons(QMessageBox.StandardButton.Ok)
            info.exec()
        print (self.newCred)
        self.credList.append(self.newCred)
        self.populateCredentials()
        print("Confirm add Entry")
        return
    
    def editEntry(self):
        self.entry_UI()

        #initialize the fields with the values of the selected credential/row
        self.lineEdit_Title.setText(self.credList[self.table_credentialList.currentRow()]['title'])
        self.lineEdit_Username.setText(self.credList[self.table_credentialList.currentRow()]['username'])
        self.lineEdit_Password.setText(self.credList[self.table_credentialList.currentRow()]['password'])
        self.lineEdit_URL.setText(self.credList[self.table_credentialList.currentRow()]['url'])
        self.lineEdit_dateExp.setText(self.credList[self.table_credentialList.currentRow()]['dateExp'])
        self.textEdit_Remark.setText(self.credList[self.table_credentialList.currentRow()]['remarks'])
        #add code here 6/march/2023


        print("Edit Entry")
        self.populateCredentials()
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