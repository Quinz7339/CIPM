# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unlockdb.ui'
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
        Form.resize(806, 546)
        icon = QIcon()
        icon.addFile(u":/Icons/Logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(175, 60, 100, 200)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.lbl_unlockFileName = QLabel(self.frame)
        self.lbl_unlockFileName.setObjectName(u"lbl_unlockFileName")
        font = QFont()
        font.setFamilies([u"HYWenHei"])
        self.lbl_unlockFileName.setFont(font)
        self.lbl_unlockFileName.setMargin(8)

        self.verticalLayout_2.addWidget(self.lbl_unlockFileName)

        self.lbl_unlockFileDir = QLabel(self.frame)
        self.lbl_unlockFileDir.setObjectName(u"lbl_unlockFileDir")
        self.lbl_unlockFileDir.setFont(font)
        self.lbl_unlockFileDir.setMargin(8)
        self.lbl_unlockFileDir.setIndent(0)

        self.verticalLayout_2.addWidget(self.lbl_unlockFileDir)

        self.frame_Fields = QFrame(self.frame)
        self.frame_Fields.setObjectName(u"frame_Fields")
        self.frame_Fields.setAutoFillBackground(False)
        self.frame_Fields.setFrameShape(QFrame.StyledPanel)
        self.frame_Fields.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_Fields)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 15, 15, -1)
        self.label_2 = QLabel(self.frame_Fields)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setMargin(0)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.lineEdit_MasterPasswd = QLineEdit(self.frame_Fields)
        self.lineEdit_MasterPasswd.setObjectName(u"lineEdit_MasterPasswd")

        self.verticalLayout_3.addWidget(self.lineEdit_MasterPasswd)

        self.frame_2 = QFrame(self.frame_Fields)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(150, 50, 0, -1)
        self.btn_unlockDb = QPushButton(self.frame_2)
        self.btn_unlockDb.setObjectName(u"btn_unlockDb")
        self.btn_unlockDb.setFont(font)

        self.horizontalLayout.addWidget(self.btn_unlockDb)

        self.btn_cancelUnlock = QPushButton(self.frame_2)
        self.btn_cancelUnlock.setObjectName(u"btn_cancelUnlock")
        self.btn_cancelUnlock.setFont(font)

        self.horizontalLayout.addWidget(self.btn_cancelUnlock)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame_Fields)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_unlockFileName.setText(QCoreApplication.translate("Form", u"Unlocking <filename> database:", None))
        self.lbl_unlockFileDir.setText(QCoreApplication.translate("Form", u"Location: <insert text here>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Kindly enter the master password:", None))
        self.btn_unlockDb.setText(QCoreApplication.translate("Form", u"Unlock", None))
        self.btn_cancelUnlock.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

