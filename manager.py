#Author         : Chua Philip
#Name of program: CIPM - Cybersecurity Integrated Password Manager
#Program name   : manager.py
#Description    : This holds the all the functionalities of the password manager. Credential creation, editing, deletion and password generation.
#First written on: 19/02/2023
#Last modified  : 19/03/2023

from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton, QLineEdit, QMessageBox, QSlider, QLabel
from PyQt6 import uic
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QDate

from datetime import date
from Passwords import gen_password, checkPwnedPasswords
import ast
import sys

import resource_rc

class Manager(QMainWindow): 
    def __init__(self):
        super().__init__()
        uic.loadUi('password_manager.ui',self)
        self.setWindowTitle("Passwords - CIPM")
        self.toolBar.setStyleSheet('QToolBar {spacing: 30px; background-color: #BFBFBF;}')
        self.lbl_Alert.setStyleSheet('font-size:17px')
        self.toolBar.layout().setContentsMargins(5,5,5,5) #left, top, right, bottom

        #initialization of session variables
        self.togglePwd_action_Entry = ''
        self.togglePwd_action_Frame = ''
        self.genPwd_action = ''
        self.pwdLength = 8
        self.database = ''
        

        return

    def secondaryInit(self):    
        self.credList=[]
        try:
            for lines in self.database.splitlines():
                cred = ast.literal_eval(lines) #literal_eval is used to convert the string to a dictionary
                self.credList.append(cred)
        except:
            pass
        self.populateCredentials()

        #index 0 = main page
        #index 1 = add entry and edit entry page
        #index 2 = settings page
        self.stackedWidget.setCurrentIndex(0)

        #hiding the frame containing the specific entry details
        self.frame_credDetail.hide()

        #estalishing connections for the toolbar buttons
        self.actionLock.triggered.connect(self.lockDatabase)
        self.actionAdd_Entry.triggered.connect(self.addEntry)
        self.actionEdit_Entry.triggered.connect(self.editEntry)
        self.actionDelete_Entry.triggered.connect(self.deleteEntry)
        self.actionSettings.triggered.connect(self.settings)
        self.actionExit.triggered.connect(self.lockDatabase)

        #estalishing connections for the stacked widget -- called to change the page
        self.actionAdd_Entry.triggered.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.actionEdit_Entry.triggered.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.actionSettings.triggered.connect(lambda:self.stackedWidget.setCurrentIndex(2))
        
        #estalishing connections for showing/hiding the frame displaying the specific entry details
        self.table_credentialList.cellClicked.connect(self.showCredentialDetails)

        #establishing connections for the buttons in the credential entry pages
        self.stackedWidget.widget(1).findChild(QPushButton,'btn_Cancel').clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.stackedWidget.widget(1).findChild(QPushButton,'btn_Confirm').clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))

        #establishing connections and styleSheets for the buttons in the settings page
        self.stackedWidget.widget(2).findChild(QPushButton,'btn_settingConfirm').clicked.connect(self.confirmSettings)
        self.stackedWidget.widget(2).findChild(QPushButton,'btn_settingCancel').clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.stackedWidget.widget(2).findChild(QPushButton,'btn_settingConfirm').setStyleSheet('QPushButton {background-color: #5B9BD5; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px}')
        self.stackedWidget.widget(2).findChild(QPushButton,'btn_settingCancel').setStyleSheet('QPushButton {background-color: #40444B; color: #A6A6A6; border-radius: 5px; font-size: 18px}')
        self.stackedWidget.widget(2).findChild(QLabel,'lbl_sliderPasswdLength').setText(str(self.pwdLength))
        self.stackedWidget.widget(2).findChild(QSlider,'slider_PasswordLength').valueChanged.connect(self.changePwdLength)  
        
        self.show()
        
    '''----------------------------------------------------------------
    initial function to populate the QTableWidget with the credentials
    ------------------------------------------------------------------'''
    def populateCredentials(self):
        self.table_credentialList.clearContents()
        self.showPwnedPassword()
        
        #sorting the list of dictionaries by the title key
        self.credList = sorted(self.credList, key=lambda k: k['title']) 

        #initializing the dimensions of the table
        self.table_credentialList.setRowCount(len(self.credList))
        self.table_credentialList.setColumnCount(5)

        creds =''
        #populating the table with the details of the credentials
        for index, creds in enumerate(self.credList):
            self.table_credentialList.setItem(index,0,QTableWidgetItem(creds['title']))
            self.table_credentialList.setItem(index,1,QTableWidgetItem(creds['username']))
            self.table_credentialList.setItem(index,2,QTableWidgetItem(creds['url']))
            self.table_credentialList.setItem(index,3,QTableWidgetItem(creds['remarks']))
            self.table_credentialList.setItem(index,4,QTableWidgetItem(creds['dateMod']))
        return
    
    '''----------------------------------------------------------------
    function to display breached passwords and its count
    ------------------------------------------------------------------'''
    def showPwnedPassword(self):
        #checking if the password is pwned
        creds=''
        pwnedPasswords = [] #list of dictionaries containing the hashed pwned passwords
        string =''
        print("Checking if password is pwned...")
        for creds in self.credList:
            pwned = checkPwnedPasswords(creds['password'])
            if pwned:
                pwnedPasswords.append(pwned)

        for pwned in pwnedPasswords:
            for key in pwned:
                string += "-> Password: " + key + " has been pwned for " + str(pwned[key]) + " times.\n"

        self.lbl_Alert.setText(string)
        return


    '''-----------------------------------------------------------------------------------------------------
    function called when the user clicks any row on the QTableWidget - shows detailed credential information
    --------------------------------------------------------------------------------------------------------'''
    def showCredentialDetails(self):
        self.btn_closeCredInfo.clicked.connect(self.hideCrendentialDetails)
        self.frame_credDetail.show()

        #setting the "Toggle Password Visibility" button
        if self.togglePwd_action_Frame !="":
            self.lineEdit_lblPassword.removeAction(self.togglePwd_action_Frame)
        self.togglePwd_action_Frame = QAction(QIcon(':/Icons/Show.svg'), 'Toggle Password visibility', self)
        self.lineEdit_lblPassword.addAction(self.togglePwd_action_Frame, QLineEdit.ActionPosition.TrailingPosition)
        self.togglePwd_action_Frame.setCheckable(True)
        self.togglePwd_action_Frame.toggled.connect(self.togglePassword_Frame)

        #populating labels based on selected credential (QTableWidget Row)
        self.lbl_credTitle.setText(self.credList[self.table_credentialList.currentRow()]['title']) #QTableWidget.currentRow() = returns the row number of the selected row
        self.lbl_Username.setText("Username: \t" + self.credList[self.table_credentialList.currentRow()]['username'])
        self.lineEdit_lblPassword.setEchoMode(QLineEdit.EchoMode.Password)         
        self.lineEdit_lblPassword.setText(self.credList[self.table_credentialList.currentRow()]['password'])
        self.lbl_Remarks.setText("Remarks: \t" + self.credList[self.table_credentialList.currentRow()]['remarks'])
        self.lbl_URL.setText("URL: \t\t" + self.credList[self.table_credentialList.currentRow()]['url'])
        self.lbl_dateExp.setText("Expiry Date: \t" + self.credList[self.table_credentialList.currentRow()]['dateExp'])
        return
    

    '''----------------------------------------------------------------------
    function to hide the detailed credential information when "X" is clicked
    -------------------------------------------------------------------------'''
    def hideCrendentialDetails(self):
        self.frame_credDetail.hide()
        return

    '''----------------------------------------------------------------------
    function called when the user clicks on the "Exit" button
    -------------------------------------------------------------------------'''
    ##gonna delete this prolly
    def exitManager(self):
        print("Exit Manager")
        self.lockDatabase()
        return
    
    '''----------------------------------------------------------------------
    function called when the user clicks on the "Lock" button
    -------------------------------------------------------------------------'''
    def lockDatabase(self):
        print("Lock Database")
        self.database =''
        for creds in self.credList:
            self.database += str(creds) + '\n'
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

        #set current date as default for the "Expiry Date" field
        self.dateEdit_dateExp.setDate(QDate().currentDate())

        #initializing the "Toggle Password Visibility" button 
        if self.togglePwd_action_Entry != '':
            self.lineEdit_Password.removeAction(self.togglePwd_action_Entry)
        self.togglePwd_action_Entry = QAction(QIcon(':/Icons/Show.svg'), 'Toggle Password visibility', self)
        self.lineEdit_Password.addAction(self.togglePwd_action_Entry, QLineEdit.ActionPosition.TrailingPosition)
        self.togglePwd_action_Entry.setCheckable(True)
        self.togglePwd_action_Entry.toggled.connect(self.togglePassword_Entry)

        #initializing the "Password Generator" button
        if self.genPwd_action != '':
            self.lineEdit_Password.removeAction(self.genPwd_action)
        self.genPwd_action = QAction(QIcon(':/Icons/Shuffle.svg'), 'Generate Password', self)
        self.lineEdit_Password.addAction(self.genPwd_action, QLineEdit.ActionPosition.TrailingPosition)
        self.genPwd_action.triggered.connect(self.generatePassword)
        
        #sets the stylehsheet of the button in the entry page
        self.btn_Confirm.setStyleSheet('QPushButton {background-color: #5B9BD5; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px}')
        self.btn_Cancel.setStyleSheet('QPushButton {background-color: #40444B; color: #A6A6A6; border-radius: 5px; font-size: 18px}')
        return
        
    '''-------------------------------------------------------------------------
    helper function - logic of the "Toggle Password Visibility" buttons
    ----------------------------------------------------------------------------'''
    #for the credential entry page
    def togglePassword_Entry(self):
        if self.togglePwd_action_Entry.isChecked():
            self.togglePwd_action_Entry.setIcon(QIcon(':/Icons/Hide.svg'))
            self.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Normal)
            return
        else:
            self.togglePwd_action_Entry.setIcon(QIcon(':/Icons/Show.svg'))
            self.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)
            return

    #for the credential detail frame
    def togglePassword_Frame(self):
        if self.togglePwd_action_Frame.isChecked():
            self.togglePwd_action_Frame.setIcon(QIcon(':/Icons/Hide.svg'))
            self.lineEdit_lblPassword.setEchoMode(QLineEdit.EchoMode.Normal)
            return
        else:
            self.togglePwd_action_Frame.setIcon(QIcon(':/Icons/Show.svg'))
            self.lineEdit_lblPassword.setEchoMode(QLineEdit.EchoMode.Password)
            return
    '''-------------------------------------------------------------------------
    helper function - populate password field with a random password
    ----------------------------------------------------------------------------'''
    def generatePassword(self):
        self.lineEdit_Password.setText(gen_password(self.pwdLength))
        return

    '''-------------------------------------------------------------------------
    function - called when user clicks on "Add Entry" button
    ----------------------------------------------------------------------------'''    
    def addEntry(self):
        self.newCred=''
        self.entry_UI()
        self.dateEdit_dateExp.setMinimumDate(QDate().currentDate())
        self.btn_Confirm.clicked.connect(self.confirmAddEntry)
        print("Add Entry")
        return

    '''-------------------------------------------------------------------------
    function - called when user clicks "Confirm" upon adding a new entry
    ----------------------------------------------------------------------------''' 
    def confirmAddEntry(self):
        self.newCred = {
            "title": self.lineEdit_Title.text(),
            "username": self.lineEdit_Username.text(),
            "password": self.lineEdit_Password.text(),
            "url": self.lineEdit_URL.text(),
            "remarks": self.textEdit_Remark.toPlainText(),
            "dateExp": QDate(self.dateEdit_dateExp.date()).toString("dd/MM/yyyy"),
            "dateMod": date.today().strftime("%d/%m/%Y")
        }
        if (len(self.lineEdit_Password.text()) < 8):
            info = QMessageBox(self)
            info.setIcon(QMessageBox.Icon.Information)
            info.setWindowTitle("Weak Password.")
            info.setText("Maybe considering using a stronger password or use the password generator after this.")
            info.setInformativeText("Password longer than 8 characters is recommended.")
            info.setStandardButtons(QMessageBox.StandardButton.Ok)
            info.exec()
            
        self.credList.append(self.newCred)
        self.populateCredentials()
        self.btn_Confirm.disconnect()
        self.btn_Confirm.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        return 

    '''-------------------------------------------------------------------------
    function - called when user clicks on "Edit Entry" button
    ----------------------------------------------------------------------------''' 
    def editEntry(self):
        try:
            print("Edit Entry")
            self.entry_UI()
            self.dateEdit_dateExp.setMinimumDate(QDate().currentDate())

            #initialize the "Confirm" button
            self.btn_Confirm.setEnabled(False)
            self.btn_Confirm.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB; border: 1px #2F528F; border-radius: 5px; font-size: 18px;}')
            self.btn_Confirm.setToolTip('No changes were made. Make some changes to enable this button.')
        
            #initialize the fields with the values of the selected credential/row
            self.lineEdit_Title.setText(self.credList[self.table_credentialList.currentRow()]['title'])
            self.lineEdit_Username.setText(self.credList[self.table_credentialList.currentRow()]['username'])
            self.lineEdit_Password.setText(self.credList[self.table_credentialList.currentRow()]['password'])
            self.lineEdit_URL.setText(self.credList[self.table_credentialList.currentRow()]['url'])
            self.dateEdit_dateExp.setDate(QDate.fromString(self.credList[self.table_credentialList.currentRow()]['dateExp'], "dd/MM/yyyy"))
            self.textEdit_Remark.setText(self.credList[self.table_credentialList.currentRow()]['remarks'])
            
            #connect the textChanged signal of the fields to the enableConfirm function
            # - ensures that the "Confirm" button is only enabled when there are changes made to the fields
            self.lineEdit_Title.textChanged.connect(self.enableConfirm)
            self.lineEdit_Username.textChanged.connect(self.enableConfirm)
            self.lineEdit_Password.textChanged.connect(self.enableConfirm)
            self.lineEdit_URL.textChanged.connect(self.enableConfirm)
            self.dateEdit_dateExp.dateChanged.connect(self.enableConfirm)
            self.textEdit_Remark.textChanged.connect(self.enableConfirm)
            self.btn_Confirm.clicked.connect(self.confirmEditEntry)
        except:
            print("Error: No entry selected.")
            QMessageBox.information(self, "Error", "The database is either blank or no entry is selected.")
            self.stackedWidget.setCurrentIndex(0)
            self.btn_Confirm.setEnabled(True)
            self.populateCredentials()
        # self.actionEdit_Entry.triggered.disconnect()
        # self.actionEdit_Entry.triggered.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        # self.actionEdit_Entry.triggered.connect(self.editEntry)
        return
    
    '''----------------------------------------------------------------------------------------------------------------------
    helper function - called when lineEdit fields are changed, ensure fields are changed prior to enabling "Confirm" button
    ------------------------------------------------------------------------------------------------------------------------'''
    def enableConfirm(self):
        #enables the "Confirm" button if there are changes made to the fields
        if((self.lineEdit_Title.text() != self.credList[self.table_credentialList.currentRow()]['title']) or 
            (self.lineEdit_Username.text() != self.credList[self.table_credentialList.currentRow()]['username']) or
            (self.lineEdit_Password.text() != self.credList[self.table_credentialList.currentRow()]['password']) or
            (self.lineEdit_URL.text() != self.credList[self.table_credentialList.currentRow()]['url']) or
            (QDate(self.dateEdit_dateExp.date()).toString("dd/MM/yyyy") != self.credList[self.table_credentialList.currentRow()]['dateExp']) or
            (self.textEdit_Remark.toPlainText() != self.credList[self.table_credentialList.currentRow()]['remarks'])):
            self.btn_Confirm.setEnabled(True)
            
            self.btn_Confirm.setStyleSheet('QPushButton {background-color: #5B9BD5; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px}')
            return
        
        #disables the "Confirm" button if there are no changes made to the fields
        self.btn_Confirm.setToolTip("")
        self.btn_Confirm.setEnabled(False)
        self.btn_Confirm.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB; border: 1px #2F528F; border-radius: 5px; font-size: 18px;}')

    '''-------------------------------------------------------------------------
    function - called when user clicks on "Confirm" during editing of an entry
    ----------------------------------------------------------------------------'''
    def confirmEditEntry(self):
        #update the selected credential with the entered new values
        self.credList[self.table_credentialList.currentRow()]['title'] = self.lineEdit_Title.text()
        self.credList[self.table_credentialList.currentRow()]['username'] = self.lineEdit_Username.text()
        self.credList[self.table_credentialList.currentRow()]['password'] = self.lineEdit_Password.text()
        self.credList[self.table_credentialList.currentRow()]['url'] = self.lineEdit_URL.text()
        self.credList[self.table_credentialList.currentRow()]['dateExp'] = QDate(self.dateEdit_dateExp.date()).toString("dd/MM/yyyy")
        self.credList[self.table_credentialList.currentRow()]['remarks'] = self.textEdit_Remark.toPlainText()
        self.credList[self.table_credentialList.currentRow()]['dateMod'] = date.today().strftime("%d/%m/%Y")

        self.btn_Confirm.disconnect()
        self.btn_Confirm.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.populateCredentials()
        return
    
    '''-------------------------------------------------------------------------
    function - called when user clicks on "Delete Entry" button
    ----------------------------------------------------------------------------'''
    def deleteEntry(self):
        try:
            self.deleteMsg = QMessageBox()
            self.deleteMsg.setIcon(QMessageBox.Icon.Warning)
            self.deleteMsg.setWindowIcon(QIcon(":Icons/Delete.svg"))
            self.deleteMsg.setWindowTitle("Delete Entry")
            self.deleteMsg.setText("Are you sure you want to delete this entry?\n Title: " + self.credList[self.table_credentialList.currentRow()]['title'] + "\n Username: " + self.credList[self.table_credentialList.currentRow()]['username'] +"\n Remarks: " + self.credList[self.table_credentialList.currentRow()]['remarks'])
            self.deleteMsg.setInformativeText("This action cannot be undone.")
            self.deleteMsg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            self.deleteMsg.button(QMessageBox.StandardButton.Yes).setStyleSheet("background-color: #961212; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px")
            self.deleteMsg.button(QMessageBox.StandardButton.No).setStyleSheet("background-color: #5B9BD5; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px")
            self.deleteMsg.setDefaultButton(QMessageBox.StandardButton.No)
            self.deleteMsg.buttonClicked.connect(self.deleteEntryConfirm)
            self.deleteMsg.exec()
        except:
            QMessageBox.information(self, "Error", "The database is either blank or no entry is selected.")
        return
    
    '''---------------------------------------------------------------------------------
    helper function - called when user clicks on "Yes" or "No" upon delete confirmation
    ------------------------------------------------------------------------------------'''
    def deleteEntryConfirm(self):
        if self.deleteMsg.clickedButton() == self.deleteMsg.button(QMessageBox.StandardButton.Yes):
            print("POP")
            self.credList.pop(self.table_credentialList.currentRow())
            self.populateCredentials()
        else:
            print("Cancel Delete")
        return
    
    '''-------------------------------------------------------------------------
    function - called when user clicks on the "Settings" button
    ----------------------------------------------------------------------------'''
    def settings(self):
        self.lbl_sliderPasswdLength.setText(str(self.pwdLength))
        self.slider_PasswordLength.setValue(self.pwdLength)
        self.btn_settingConfirm.setStyleSheet('QPushButton {background-color: #5B9BD5; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px}')
        self.btn_settingCancel.setStyleSheet('QPushButton {background-color: #40444B; color: #A6A6A6; border-radius: 5px; font-size: 18px}')
        print("Settings")
        return
    
    #called when the slider is moved to change the length of generated password
    def changePwdLength(self):
        self.lbl_sliderPasswdLength.setText(str(self.slider_PasswordLength.value()))
        return
    
    #confirmation of changing length of generated password
    def confirmSettings(self):
        self.passwordConfirm = QMessageBox()
        self.passwordConfirm.setIcon(QMessageBox.Icon.Question)
        self.passwordConfirm.setWindowIcon(QIcon(":Icons/Logo.svg"))
        self.passwordConfirm.setWindowTitle("Confirm Settings")
        self.passwordConfirm.setText("Changing default generated password length to: " + str(self.slider_PasswordLength.value()) + " characters")
        self.passwordConfirm.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.passwordConfirm.button(QMessageBox.StandardButton.Yes).setStyleSheet("background-color: #961212; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px")
        self.passwordConfirm.button(QMessageBox.StandardButton.No).setStyleSheet("background-color: #5B9BD5; color: #FFFFFF; border: 1px #2F528F; border-radius: 5px; font-size: 18px")
        self.passwordConfirm.buttonClicked.connect(self.completeSettings)
        self.passwordConfirm.exec()
        
        print("Confirm Settings")
        return

    #called when user clicks on "Yes" or "No" upon confirmation of changing length of generated password
    def completeSettings(self):
        if self.passwordConfirm.clickedButton() == self.passwordConfirm.button(QMessageBox.StandardButton.Yes):
            self.pwdLength = self.slider_PasswordLength.value()
            self.stackedWidget.setCurrentIndex(0)
            self.populateCredentials()
            return
        else:
            self.passwordConfirm.close()
        return