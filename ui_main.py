# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainqZkFFT.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(576, 330)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_infos = QFrame(self.centralwidget)
        self.frame_infos.setObjectName(u"frame_infos")
        sizePolicy.setHeightForWidth(self.frame_infos.sizePolicy().hasHeightForWidth())
        self.frame_infos.setSizePolicy(sizePolicy)
        self.frame_infos.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_3 = QVBoxLayout(self.frame_infos)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_email = QFrame(self.frame_infos)
        self.frame_email.setObjectName(u"frame_email")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_email)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_email = QLabel(self.frame_email)
        self.label_email.setObjectName(u"label_email")
        font = QFont()
        font.setPointSize(14)
        self.label_email.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_email)

        self.lineEdit_email = QLineEdit(self.frame_email)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy1)
        self.lineEdit_email.setMinimumSize(QSize(250, 0))
        self.lineEdit_email.setStyleSheet(u"")
        self.lineEdit_email.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_email)


        self.verticalLayout_3.addWidget(self.frame_email)

        self.frame_name = QFrame(self.frame_infos)
        self.frame_name.setObjectName(u"frame_name")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_name)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_name = QLabel(self.frame_name)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.frame_name)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_name)


        self.verticalLayout_3.addWidget(self.frame_name)

        self.frame_password = QFrame(self.frame_infos)
        self.frame_password.setObjectName(u"frame_password")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_password = QLabel(self.frame_password)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.frame_password)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(250, 0))
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.lineEdit_password)


        self.verticalLayout_3.addWidget(self.frame_password)


        self.verticalLayout_4.addWidget(self.frame_infos)

        self.frame_btn = QFrame(self.centralwidget)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.frame_btn)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_generate = QPushButton(self.frame_btn)
        self.pushButton_generate.setObjectName(u"pushButton_generate")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_generate.sizePolicy().hasHeightForWidth())
        self.pushButton_generate.setSizePolicy(sizePolicy2)
        self.pushButton_generate.setMinimumSize(QSize(100, 50))
        self.pushButton_generate.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_generate)

        self.pushButton_train = QPushButton(self.frame_btn)
        self.pushButton_train.setObjectName(u"pushButton_train")
        sizePolicy2.setHeightForWidth(self.pushButton_train.sizePolicy().hasHeightForWidth())
        self.pushButton_train.setSizePolicy(sizePolicy2)
        self.pushButton_train.setMinimumSize(QSize(100, 50))
        self.pushButton_train.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_train)

        self.pushButton_recognize = QPushButton(self.frame_btn)
        self.pushButton_recognize.setObjectName(u"pushButton_recognize")
        sizePolicy2.setHeightForWidth(self.pushButton_recognize.sizePolicy().hasHeightForWidth())
        self.pushButton_recognize.setSizePolicy(sizePolicy2)
        self.pushButton_recognize.setMinimumSize(QSize(100, 50))
        self.pushButton_recognize.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_recognize)


        self.verticalLayout_4.addWidget(self.frame_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_btn.raise_()
        self.frame_infos.raise_()
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Face Recognition", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.pushButton_generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.pushButton_train.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.pushButton_recognize.setText(QCoreApplication.translate("MainWindow", u"Recognize", None))
    # retranslateUi

