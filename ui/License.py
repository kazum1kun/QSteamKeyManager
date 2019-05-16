# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kilve\PycharmProjects\QSteamKeyManager\ui\License.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_License(object):
    def setupUi(self, License):
        License.setObjectName("License")
        License.resize(595, 583)
        self.verticalLayout = QtWidgets.QVBoxLayout(License)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_license = QtWidgets.QTextBrowser(License)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.textBrowser_license.setFont(font)
        self.textBrowser_license.setAcceptDrops(False)
        self.textBrowser_license.setSource(
            QtCore.QUrl("file:///C:/Users/kilve/PycharmProjects/QSteamKeyManager/res/GNU_GPL_v3.html"))
        self.textBrowser_license.setOpenExternalLinks(True)
        self.textBrowser_license.setObjectName("textBrowser_license")
        self.verticalLayout.addWidget(self.textBrowser_license)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton(License)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(License)
        self.pushButton_close.clicked.connect(License.close)
        QtCore.QMetaObject.connectSlotsByName(License)

    def retranslateUi(self, License):
        _translate = QtCore.QCoreApplication.translate
        License.setWindowTitle(_translate("License", "QSteamKeyManager License"))
        self.pushButton_close.setText(_translate("License", "Close"))
