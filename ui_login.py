# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QSizePolicy, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 586)
        Form.setMinimumSize(QSize(700, 500))
        icon = QIcon()
        icon.addFile(u":/Icons/Logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_Logo = QLabel(self.frame_3)
        self.lbl_Logo.setObjectName(u"lbl_Logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_Logo.sizePolicy().hasHeightForWidth())
        self.lbl_Logo.setSizePolicy(sizePolicy1)
        self.lbl_Logo.setMaximumSize(QSize(180, 180))
        self.lbl_Logo.setLayoutDirection(Qt.LeftToRight)
        self.lbl_Logo.setPixmap(QPixmap(u":/Icons/Logo.svg"))
        self.lbl_Logo.setScaledContents(True)
        self.lbl_Logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_Logo, 0, Qt.AlignHCenter)

        self.lbl_Welcome = QLabel(self.frame_3)
        self.lbl_Welcome.setObjectName(u"lbl_Welcome")
        font = QFont()
        font.setFamilies([u"HYWenHei"])
        self.lbl_Welcome.setFont(font)
        self.lbl_Welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_Welcome)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(500, 500))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_CreateDb = QToolButton(self.frame)
        self.btn_CreateDb.setObjectName(u"btn_CreateDb")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_CreateDb.sizePolicy().hasHeightForWidth())
        self.btn_CreateDb.setSizePolicy(sizePolicy2)
        self.btn_CreateDb.setMinimumSize(QSize(80, 80))
        self.btn_CreateDb.setMaximumSize(QSize(200, 200))
        self.btn_CreateDb.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_CreateDb.setIcon(icon1)
        self.btn_CreateDb.setIconSize(QSize(50, 50))
        self.btn_CreateDb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.btn_CreateDb, 0, Qt.AlignLeft)

        self.btn_OpenDb = QToolButton(self.frame)
        self.btn_OpenDb.setObjectName(u"btn_OpenDb")
        sizePolicy2.setHeightForWidth(self.btn_OpenDb.sizePolicy().hasHeightForWidth())
        self.btn_OpenDb.setSizePolicy(sizePolicy2)
        self.btn_OpenDb.setMinimumSize(QSize(80, 80))
        self.btn_OpenDb.setMaximumSize(QSize(200, 200))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_OpenDb.setIcon(icon2)
        self.btn_OpenDb.setIconSize(QSize(50, 50))
        self.btn_OpenDb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.btn_OpenDb, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 200))
        self.frame_2.setMaximumSize(QSize(500, 450))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_RecentFiles = QLabel(self.frame_2)
        self.lbl_RecentFiles.setObjectName(u"lbl_RecentFiles")
        self.lbl_RecentFiles.setFont(font)

        self.verticalLayout_2.addWidget(self.lbl_RecentFiles)

        self.txtEdit_RecentFiles = QTextEdit(self.frame_2)
        self.txtEdit_RecentFiles.setObjectName(u"txtEdit_RecentFiles")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txtEdit_RecentFiles.sizePolicy().hasHeightForWidth())
        self.txtEdit_RecentFiles.setSizePolicy(sizePolicy3)
        self.txtEdit_RecentFiles.setFont(font)
        self.txtEdit_RecentFiles.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.txtEdit_RecentFiles)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_Logo.setText("")
        self.lbl_Welcome.setText(QCoreApplication.translate("Form", u"Welcome to CIPM", None))
        self.btn_CreateDb.setText(QCoreApplication.translate("Form", u"Create New Database", None))
        self.btn_OpenDb.setText(QCoreApplication.translate("Form", u"Open Existing Database", None))
        self.lbl_RecentFiles.setText(QCoreApplication.translate("Form", u"Recent databases:", None))
    # retranslateUi

