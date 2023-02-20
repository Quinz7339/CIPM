# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createdb.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(700, 500)
        Form.setMinimumSize(QSize(700, 500))
        icon = QIcon()
        icon.addFile(u":/Icons/Logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_4)

        self.lbl_CreateDb = QLabel(Form)
        self.lbl_CreateDb.setObjectName(u"lbl_CreateDb")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_CreateDb.sizePolicy().hasHeightForWidth())
        self.lbl_CreateDb.setSizePolicy(sizePolicy)
        self.lbl_CreateDb.setMaximumSize(QSize(500, 40))
        font = QFont()
        font.setFamilies([u"HYWenHei"])
        self.lbl_CreateDb.setFont(font)
        self.lbl_CreateDb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.lbl_CreateDb)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addWidget(self.frame)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_MasterPasswd = QLineEdit(self.frame_2)
        self.lineEdit_MasterPasswd.setObjectName(u"lineEdit_MasterPasswd")

        self.horizontalLayout_2.addWidget(self.lineEdit_MasterPasswd)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit_MasterPasswd2 = QLineEdit(self.frame_5)
        self.lineEdit_MasterPasswd2.setObjectName(u"lineEdit_MasterPasswd2")
        self.lineEdit_MasterPasswd2.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_MasterPasswd2)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_dbCreate = QPushButton(self.frame_3)
        self.btn_dbCreate.setObjectName(u"btn_dbCreate")
        self.btn_dbCreate.setGeometry(QRect(490, 40, 161, 31))
        self.btn_dbCreate.setFont(font)
        self.btn_dbBack = QPushButton(self.frame_3)
        self.btn_dbBack.setObjectName(u"btn_dbBack")
        self.btn_dbBack.setGeometry(QRect(390, 40, 81, 31))
        self.btn_dbBack.setFont(font)

        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_CreateDb.setText(QCoreApplication.translate("Form", u"Input Database Information", None))
        self.label.setText(QCoreApplication.translate("Form", u"Please fill in the name for your newly created password database.", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password database name:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Enter the password to secure and unlock your passsword database.", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Master password:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Renter password:", None))
        self.btn_dbCreate.setText(QCoreApplication.translate("Form", u"Create database", None))
        self.btn_dbBack.setText(QCoreApplication.translate("Form", u"Back", None))
    # retranslateUi

