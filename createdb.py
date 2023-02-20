from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6 import uic

import sys

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
        self.lineEdit_MasterPasswd.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_MasterPasswd2.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_dbCreate.setStyleSheet('QPushButton {background-color: #BFBFBF; color: #2B96CB;}')
        self.show()
        print("Showing create DB menu")
        #solve how to make it show persistently until the operation is done
        # self.styleSheet('''
        #     QWidget {
        #         background-color: #40444B;
        #         font-size: 18px;  
        #     }
        #     QPushButton {
        #         font-size: 25px;
        #     }
        #     QLabel {
        #         color: #FFFFFF;
        #     }
        #     QToolButton{
        #         background-color: #BFBFBF;
        #         border-radius: 15px;
        #     }
        #     QTextEdit{
        #         background-color: #BFBFBF;
        #         border-radius: 15px;
        #     }    
        # ''')
    # def createDb_window():
    #     app = QApplication(sys.argv)
    #     window = CreateDb()
    #     sys.exit(app.exec())
class CreateDb_checkout(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('createdb.ui',self)
        self.setWindowTitle("Create Database")
        self.resize (640, 480)
        self.show()
        #solve how to make it show persistently until the operation is done
        self.styleSheet('''
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
    