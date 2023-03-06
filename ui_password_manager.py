# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_manager.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(833, 605)
        icon = QIcon()
        icon.addFile(u":/Icons/Logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionLock = QAction(MainWindow)
        self.actionLock.setObjectName(u"actionLock")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLock.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionAdd_Entry = QAction(MainWindow)
        self.actionAdd_Entry.setObjectName(u"actionAdd_Entry")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Entry.setIcon(icon3)
        self.actionEdit_Entry = QAction(MainWindow)
        self.actionEdit_Entry.setObjectName(u"actionEdit_Entry")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEdit_Entry.setIcon(icon4)
        self.actionDelete_Entry = QAction(MainWindow)
        self.actionDelete_Entry.setObjectName(u"actionDelete_Entry")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete_Entry.setIcon(icon5)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Gear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self._2 = QHBoxLayout(self.centralwidget)
        self._2.setSpacing(20)
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SetNoConstraint)
        self._2.setContentsMargins(20, 20, 20, 20)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_Manager = QWidget()
        self.page_Manager.setObjectName(u"page_Manager")
        self.horizontalLayout = QHBoxLayout(self.page_Manager)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_secTips = QFrame(self.page_Manager)
        self.frame_secTips.setObjectName(u"frame_secTips")
        self.frame_secTips.setFrameShape(QFrame.StyledPanel)
        self.frame_secTips.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_secTips)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_secTips)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_secTips)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_credList = QFrame(self.page_Manager)
        self.frame_credList.setObjectName(u"frame_credList")
        self.frame_credList.setFrameShape(QFrame.StyledPanel)
        self.frame_credList.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_credList)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_credentialList = QTableWidget(self.frame_credList)
        if (self.table_credentialList.columnCount() < 6):
            self.table_credentialList.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_credentialList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_credentialList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_credentialList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_credentialList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_credentialList.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_credentialList.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_credentialList.setObjectName(u"table_credentialList")
        font = QFont()
        font.setFamilies([u"HYWenHei"])
        self.table_credentialList.setFont(font)
        self.table_credentialList.setAutoFillBackground(True)
        self.table_credentialList.setStyleSheet(u"selection-background-color: #2B96CB;\n"
"background-color:#595959")
        self.table_credentialList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_credentialList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_credentialList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_credentialList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_credentialList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_credentialList.setShowGrid(False)
        self.table_credentialList.setSortingEnabled(False)
        self.table_credentialList.setWordWrap(False)
        self.table_credentialList.horizontalHeader().setCascadingSectionResizes(True)
        self.table_credentialList.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_credentialList.horizontalHeader().setStretchLastSection(True)
        self.table_credentialList.verticalHeader().setVisible(False)
        self.table_credentialList.verticalHeader().setHighlightSections(False)
        self.table_credentialList.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout.addWidget(self.table_credentialList)

        self.frame_credDetail = QFrame(self.frame_credList)
        self.frame_credDetail.setObjectName(u"frame_credDetail")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_credDetail.sizePolicy().hasHeightForWidth())
        self.frame_credDetail.setSizePolicy(sizePolicy1)
        self.frame_credDetail.setStyleSheet(u"#frame_bodyCredDetail { border: 1px solid #BFBFBF;}")
        self.frame_credDetail.setFrameShape(QFrame.StyledPanel)
        self.frame_credDetail.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_credDetail)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.frame_headerCredInfo = QFrame(self.frame_credDetail)
        self.frame_headerCredInfo.setObjectName(u"frame_headerCredInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_headerCredInfo.sizePolicy().hasHeightForWidth())
        self.frame_headerCredInfo.setSizePolicy(sizePolicy2)
        self.frame_headerCredInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_headerCredInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_headerCredInfo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.lbl_credIcon = QLabel(self.frame_headerCredInfo)
        self.lbl_credIcon.setObjectName(u"lbl_credIcon")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_credIcon.sizePolicy().hasHeightForWidth())
        self.lbl_credIcon.setSizePolicy(sizePolicy3)
        self.lbl_credIcon.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.lbl_credIcon)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lbl_credTitle = QLabel(self.frame_headerCredInfo)
        self.lbl_credTitle.setObjectName(u"lbl_credTitle")
        self.lbl_credTitle.setFont(font)

        self.horizontalLayout_3.addWidget(self.lbl_credTitle)

        self.btn_closeCredInfo = QPushButton(self.frame_headerCredInfo)
        self.btn_closeCredInfo.setObjectName(u"btn_closeCredInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_closeCredInfo.sizePolicy().hasHeightForWidth())
        self.btn_closeCredInfo.setSizePolicy(sizePolicy4)
        self.btn_closeCredInfo.setStyleSheet(u"border: 1px solid #BFBFBF;\n"
"border-radius: 5px;")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Cross.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeCredInfo.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.btn_closeCredInfo)


        self.verticalLayout_3.addWidget(self.frame_headerCredInfo)

        self.frame_bodyCredDetail = QFrame(self.frame_credDetail)
        self.frame_bodyCredDetail.setObjectName(u"frame_bodyCredDetail")
        self.frame_bodyCredDetail.setFrameShape(QFrame.StyledPanel)
        self.frame_bodyCredDetail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_bodyCredDetail)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.frame_leftCredDetail = QFrame(self.frame_bodyCredDetail)
        self.frame_leftCredDetail.setObjectName(u"frame_leftCredDetail")
        self.frame_leftCredDetail.setFrameShape(QFrame.StyledPanel)
        self.frame_leftCredDetail.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_leftCredDetail)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_4.setContentsMargins(-1, -1, 200, -1)
        self.lbl_Username = QLabel(self.frame_leftCredDetail)
        self.lbl_Username.setObjectName(u"lbl_Username")
        self.lbl_Username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.lbl_Username)

        self.lbl_Password = QLabel(self.frame_leftCredDetail)
        self.lbl_Password.setObjectName(u"lbl_Password")
        self.lbl_Password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.lbl_Password)

        self.lbl_Remarks = QLabel(self.frame_leftCredDetail)
        self.lbl_Remarks.setObjectName(u"lbl_Remarks")
        self.lbl_Remarks.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.lbl_Remarks)


        self.horizontalLayout_4.addWidget(self.frame_leftCredDetail)

        self.frame_rightCredInfo = QFrame(self.frame_bodyCredDetail)
        self.frame_rightCredInfo.setObjectName(u"frame_rightCredInfo")
        self.frame_rightCredInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_rightCredInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_rightCredInfo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 200, -1)
        self.lbl_URL = QLabel(self.frame_rightCredInfo)
        self.lbl_URL.setObjectName(u"lbl_URL")
        self.lbl_URL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lbl_URL)

        self.lbl_dateExp = QLabel(self.frame_rightCredInfo)
        self.lbl_dateExp.setObjectName(u"lbl_dateExp")
        self.lbl_dateExp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lbl_dateExp)


        self.horizontalLayout_4.addWidget(self.frame_rightCredInfo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.frame_bodyCredDetail)


        self.verticalLayout.addWidget(self.frame_credDetail)


        self.horizontalLayout.addWidget(self.frame_credList)

        self.stackedWidget.addWidget(self.page_Manager)
        self.page_addEntry = QWidget()
        self.page_addEntry.setObjectName(u"page_addEntry")
        self.verticalLayout_5 = QVBoxLayout(self.page_addEntry)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(25, -1, 25, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.label_3 = QLabel(self.page_addEntry)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_7 = QLabel(self.page_addEntry)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.page_addEntry)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)

        self.label_6 = QLabel(self.page_addEntry)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_addEntry)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page_addEntry)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 2, 1, 1)

        self.label_4 = QLabel(self.page_addEntry)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.textEdit = QTextEdit(self.page_addEntry)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.textEdit, 5, 2, 1, 2)

        self.label_2 = QLabel(self.page_addEntry)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_5 = QLabel(self.page_addEntry)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)

        self.lineEdit = QLineEdit(self.page_addEntry)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_addEntry)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)

        self.frame = QFrame(self.page_addEntry)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(500, -1, -1, -1)
        self.btn_Cancel = QPushButton(self.frame)
        self.btn_Cancel.setObjectName(u"btn_Cancel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_Cancel.sizePolicy().hasHeightForWidth())
        self.btn_Cancel.setSizePolicy(sizePolicy7)

        self.horizontalLayout_2.addWidget(self.btn_Cancel)

        self.btn_Confirm = QPushButton(self.frame)
        self.btn_Confirm.setObjectName(u"btn_Confirm")
        sizePolicy7.setHeightForWidth(self.btn_Confirm.sizePolicy().hasHeightForWidth())
        self.btn_Confirm.setSizePolicy(sizePolicy7)

        self.horizontalLayout_2.addWidget(self.btn_Confirm)


        self.gridLayout.addWidget(self.frame, 6, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page_addEntry)

        self._2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(50)
        sizePolicy8.setVerticalStretch(50)
        sizePolicy8.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy8)
        self.toolBar.setMinimumSize(QSize(0, 0))
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(60, 60))
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionLock)
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_Entry)
        self.toolBar.addAction(self.actionEdit_Entry)
        self.toolBar.addAction(self.actionDelete_Entry)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLock.setText(QCoreApplication.translate("MainWindow", u"Lock", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAdd_Entry.setText(QCoreApplication.translate("MainWindow", u"Add Entry", None))
        self.actionEdit_Entry.setText(QCoreApplication.translate("MainWindow", u"Edit Entry", None))
        self.actionDelete_Entry.setText(QCoreApplication.translate("MainWindow", u"Delete Entry", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<insert security tip here ", None))
        ___qtablewidgetitem = self.table_credentialList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Icon", None));
        ___qtablewidgetitem1 = self.table_credentialList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.table_credentialList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem3 = self.table_credentialList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtablewidgetitem4 = self.table_credentialList.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem5 = self.table_credentialList.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Modified", None));
        self.lbl_credIcon.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbl_credTitle.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_closeCredInfo.setText("")
        self.lbl_Username.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.lbl_Password.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.lbl_Remarks.setText(QCoreApplication.translate("MainWindow", u"remarks", None))
        self.lbl_URL.setText(QCoreApplication.translate("MainWindow", u"url", None))
        self.lbl_dateExp.setText(QCoreApplication.translate("MainWindow", u"expiry", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Remark:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Expiry Date:", None))
        self.btn_Cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_Confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

