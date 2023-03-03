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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStatusBar,
    QToolBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 608)
        self.actionLock = QAction(MainWindow)
        self.actionLock.setObjectName(u"actionLock")
        icon = QIcon()
        icon.addFile(u":/Icons/Lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLock.setIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionAdd_Entry = QAction(MainWindow)
        self.actionAdd_Entry.setObjectName(u"actionAdd_Entry")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Entry.setIcon(icon2)
        self.actionEdit_Entry = QAction(MainWindow)
        self.actionEdit_Entry.setObjectName(u"actionEdit_Entry")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEdit_Entry.setIcon(icon3)
        self.actionDelete_Entry = QAction(MainWindow)
        self.actionDelete_Entry.setObjectName(u"actionDelete_Entry")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete_Entry.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QSize(0, 0))
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(60, 60))
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionLock)
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLock.setText(QCoreApplication.translate("MainWindow", u"Lock", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAdd_Entry.setText(QCoreApplication.translate("MainWindow", u"Add Entry", None))
        self.actionEdit_Entry.setText(QCoreApplication.translate("MainWindow", u"Edit Entry", None))
        self.actionDelete_Entry.setText(QCoreApplication.translate("MainWindow", u"Delete Entry", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

