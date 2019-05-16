# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kilve\PycharmProjects\QSteamKeyManager\ui\AboutMe.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_me(object):
    def setupUi(self, about_me):
        about_me.setObjectName("about_me")
        about_me.resize(431, 307)
        self.verticalLayout = QtWidgets.QVBoxLayout(about_me)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gfx_logo = QtWidgets.QLabel(about_me)
        self.gfx_logo.setText("")
        self.gfx_logo.setPixmap(QtGui.QPixmap("res/QSKM_Logo_Long_400px.png"))
        self.gfx_logo.setObjectName("gfx_logo")
        self.verticalLayout.addWidget(self.gfx_logo)
        self.label_copyright = QtWidgets.QLabel(about_me)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_copyright.setFont(font)
        self.label_copyright.setObjectName("label_copyright")
        self.verticalLayout.addWidget(self.label_copyright)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.layout_bottom_button = QtWidgets.QHBoxLayout()
        self.layout_bottom_button.setObjectName("layout_bottom_button")
        self.pushButton_software = QtWidgets.QPushButton(about_me)
        self.pushButton_software.setObjectName("pushButton_software")
        self.layout_bottom_button.addWidget(self.pushButton_software)
        self.pushButton_license = QtWidgets.QPushButton(about_me)
        self.pushButton_license.setObjectName("pushButton_license")
        self.layout_bottom_button.addWidget(self.pushButton_license)
        self.pushButton_github = QtWidgets.QPushButton(about_me)
        self.pushButton_github.setObjectName("pushButton_github")
        self.layout_bottom_button.addWidget(self.pushButton_github)
        self.pushButton_close = QtWidgets.QPushButton(about_me)
        self.pushButton_close.setObjectName("pushButton_close")
        self.layout_bottom_button.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.layout_bottom_button)

        self.retranslateUi(about_me)
        QtCore.QMetaObject.connectSlotsByName(about_me)

    def retranslateUi(self, about_me):
        _translate = QtCore.QCoreApplication.translate
        about_me.setWindowTitle(_translate("about_me", "About QSteamKeyManager"))
        self.label_copyright.setText(_translate("about_me",
                                                "<html><head/><body><p><span style=\" font-weight:600;\">QSteamKeyManager (Alpha-0.0.6)</span><br/>Commit date: May 15, 2019</p><p><br/>Powered by open-source software (OSS).<br/></p><p>This software is distributed under GNU GPL v3 license.</p><p>Copyright © 2018-2019 <a href=\"https://github.com/l19980623/\"><span style=\" text-decoration: underline; color:#0000ff;\">Xuanli Lin</span></a>.</p></body></html>"))
        self.pushButton_software.setText(_translate("about_me", "OSS Used..."))
        self.pushButton_license.setText(_translate("about_me", "License..."))
        self.pushButton_github.setText(_translate("about_me", "View on Github..."))
        self.pushButton_close.setText(_translate("about_me", "Close"))
