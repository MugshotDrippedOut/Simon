# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\bucka\Documents\GitHub\School\Simon\Kryptologie\Elektronicky_Podpis\Digital_Signature.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 511)
        MainWindow.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem = QtWidgets.QSpacerItem(116, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font:87 16pt \"Arial Black\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_14.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(116, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditSaveKeys = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSaveKeys.setObjectName("lineEditSaveKeys")
        self.horizontalLayout_4.addWidget(self.lineEditSaveKeys)
        self.pushButtonFolder_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\bucka\\Documents\\GitHub\\School\\Simon\\Kryptologie\\Elektronicky_Podpis\\folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonFolder_4.setIcon(icon)
        self.pushButtonFolder_4.setFlat(False)
        self.pushButtonFolder_4.setObjectName("pushButtonFolder_4")
        self.horizontalLayout_4.addWidget(self.pushButtonFolder_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButtonGenerateKeys = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGenerateKeys.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonGenerateKeys.setObjectName("pushButtonGenerateKeys")
        self.verticalLayout.addWidget(self.pushButtonGenerateKeys)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEditSaveZip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSaveZip.setObjectName("lineEditSaveZip")
        self.horizontalLayout_5.addWidget(self.lineEditSaveZip)
        self.pushButtonFolder_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder_5.setText("")
        self.pushButtonFolder_5.setIcon(icon)
        self.pushButtonFolder_5.setFlat(False)
        self.pushButtonFolder_5.setObjectName("pushButtonFolder_5")
        self.horizontalLayout_5.addWidget(self.pushButtonFolder_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.pushButtonZip = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonZip.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonZip.setObjectName("pushButtonZip")
        self.verticalLayout.addWidget(self.pushButtonZip)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEditLoadZip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLoadZip.setObjectName("lineEditLoadZip")
        self.horizontalLayout_6.addWidget(self.lineEditLoadZip)
        self.pushButtonFolder_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder_6.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder_6.setText("")
        self.pushButtonFolder_6.setIcon(icon)
        self.pushButtonFolder_6.setFlat(False)
        self.pushButtonFolder_6.setObjectName("pushButtonFolder_6")
        self.horizontalLayout_6.addWidget(self.pushButtonFolder_6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEditSaveUnzip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSaveUnzip.setObjectName("lineEditSaveUnzip")
        self.horizontalLayout_7.addWidget(self.lineEditSaveUnzip)
        self.pushButtonFolder_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder_7.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder_7.setText("")
        self.pushButtonFolder_7.setIcon(icon)
        self.pushButtonFolder_7.setFlat(False)
        self.pushButtonFolder_7.setObjectName("pushButtonFolder_7")
        self.horizontalLayout_7.addWidget(self.pushButtonFolder_7)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.pushButtonUnzip = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUnzip.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonUnzip.setObjectName("pushButtonUnzip")
        self.verticalLayout.addWidget(self.pushButtonUnzip)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(117, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font:87 16pt \"Arial Black\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditDigitalSignatureSign = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDigitalSignatureSign.setObjectName("lineEditDigitalSignatureSign")
        self.horizontalLayout_3.addWidget(self.lineEditDigitalSignatureSign)
        self.pushButtonFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder.setText("")
        self.pushButtonFolder.setIcon(icon)
        self.pushButtonFolder.setFlat(False)
        self.pushButtonFolder.setObjectName("pushButtonFolder")
        self.horizontalLayout_3.addWidget(self.pushButtonFolder)
        self.pushButtonInfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInfo.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonInfo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\bucka\\Documents\\GitHub\\School\\Simon\\Kryptologie\\Elektronicky_Podpis\\info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonInfo.setIcon(icon1)
        self.pushButtonInfo.setFlat(False)
        self.pushButtonInfo.setObjectName("pushButtonInfo")
        self.horizontalLayout_3.addWidget(self.pushButtonInfo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditMessageSign = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMessageSign.setObjectName("lineEditMessageSign")
        self.horizontalLayout_2.addWidget(self.lineEditMessageSign)
        self.pushButtonFolder_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder_2.setText("")
        self.pushButtonFolder_2.setIcon(icon)
        self.pushButtonFolder_2.setFlat(False)
        self.pushButtonFolder_2.setObjectName("pushButtonFolder_2")
        self.horizontalLayout_2.addWidget(self.pushButtonFolder_2)
        self.pushButtonInfo_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInfo_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonInfo_2.setText("")
        self.pushButtonInfo_2.setIcon(icon1)
        self.pushButtonInfo_2.setFlat(False)
        self.pushButtonInfo_2.setObjectName("pushButtonInfo_2")
        self.horizontalLayout_2.addWidget(self.pushButtonInfo_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButtonEditMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEditMessage.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonEditMessage.setObjectName("pushButtonEditMessage")
        self.verticalLayout_2.addWidget(self.pushButtonEditMessage)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButtonHash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHash.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonHash.setObjectName("pushButtonHash")
        self.horizontalLayout_8.addWidget(self.pushButtonHash)
        self.pushButtonShowHash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShowHash.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonShowHash.setObjectName("pushButtonShowHash")
        self.horizontalLayout_8.addWidget(self.pushButtonShowHash)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditPrivateKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPrivateKey.setObjectName("lineEditPrivateKey")
        self.horizontalLayout.addWidget(self.lineEditPrivateKey)
        self.pushButtonFolder_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder_3.setText("")
        self.pushButtonFolder_3.setIcon(icon)
        self.pushButtonFolder_3.setFlat(False)
        self.pushButtonFolder_3.setObjectName("pushButtonFolder_3")
        self.horizontalLayout.addWidget(self.pushButtonFolder_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButtonLoadKey = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoadKey.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonLoadKey.setObjectName("pushButtonLoadKey")
        self.verticalLayout_2.addWidget(self.pushButtonLoadKey)
        self.pushButtonSign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSign.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonSign.setObjectName("pushButtonSign")
        self.verticalLayout_2.addWidget(self.pushButtonSign)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem7 = QtWidgets.QSpacerItem(78, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font:87 16pt \"Arial Black\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_15.addWidget(self.label_3)
        spacerItem8 = QtWidgets.QSpacerItem(78, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEditDigitalSignatureVerify = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDigitalSignatureVerify.setObjectName("lineEditDigitalSignatureVerify")
        self.horizontalLayout_10.addWidget(self.lineEditDigitalSignatureVerify)
        self.pushButtonFolder_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder_8.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder_8.setText("")
        self.pushButtonFolder_8.setIcon(icon)
        self.pushButtonFolder_8.setFlat(False)
        self.pushButtonFolder_8.setObjectName("pushButtonFolder_8")
        self.horizontalLayout_10.addWidget(self.pushButtonFolder_8)
        self.pushButtonInfo_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInfo_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonInfo_3.setText("")
        self.pushButtonInfo_3.setIcon(icon1)
        self.pushButtonInfo_3.setFlat(False)
        self.pushButtonInfo_3.setObjectName("pushButtonInfo_3")
        self.horizontalLayout_10.addWidget(self.pushButtonInfo_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButtonHash_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHash_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonHash_2.setObjectName("pushButtonHash_2")
        self.horizontalLayout_12.addWidget(self.pushButtonHash_2)
        self.pushButtonShowHash_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShowHash_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonShowHash_2.setObjectName("pushButtonShowHash_2")
        self.horizontalLayout_12.addWidget(self.pushButtonShowHash_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lineEditPublicKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPublicKey.setObjectName("lineEditPublicKey")
        self.horizontalLayout_13.addWidget(self.lineEditPublicKey)
        self.pushButtonFolder_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFolder_10.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(155, 155, 155);\n"
"}\n"
"")
        self.pushButtonFolder_10.setText("")
        self.pushButtonFolder_10.setIcon(icon)
        self.pushButtonFolder_10.setFlat(False)
        self.pushButtonFolder_10.setObjectName("pushButtonFolder_10")
        self.horizontalLayout_13.addWidget(self.pushButtonFolder_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.pushButtonLoadKey_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoadKey_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonLoadKey_2.setObjectName("pushButtonLoadKey_2")
        self.verticalLayout_3.addWidget(self.pushButtonLoadKey_2)
        self.pushButtonVerify = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonVerify.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.pushButtonVerify.setObjectName("pushButtonVerify")
        self.verticalLayout_3.addWidget(self.pushButtonVerify)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 6, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Create keys"))
        self.label_7.setText(_translate("MainWindow", "Select path to save the keys"))
        self.lineEditSaveKeys.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Keys"))
        self.pushButtonGenerateKeys.setText(_translate("MainWindow", "Generate keys"))
        self.label_8.setText(_translate("MainWindow", "Select path to save the zip file"))
        self.lineEditSaveZip.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Zip"))
        self.pushButtonZip.setText(_translate("MainWindow", "Zip"))
        self.label_9.setText(_translate("MainWindow", "Select path to load the zip file"))
        self.lineEditLoadZip.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Zip"))
        self.label_10.setText(_translate("MainWindow", "Select path to save the unzipped file"))
        self.lineEditSaveUnzip.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Unzip"))
        self.pushButtonUnzip.setText(_translate("MainWindow", "Unzip"))
        self.label.setText(_translate("MainWindow", "Sign"))
        self.label_4.setText(_translate("MainWindow", "Select path for digital signature"))
        self.lineEditDigitalSignatureSign.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Signature"))
        self.label_5.setText(_translate("MainWindow", "Select path for message"))
        self.lineEditMessageSign.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Message"))
        self.pushButtonEditMessage.setText(_translate("MainWindow", "Edit Message"))
        self.pushButtonHash.setText(_translate("MainWindow", "Hash"))
        self.pushButtonShowHash.setText(_translate("MainWindow", "Show Hash"))
        self.label_6.setText(_translate("MainWindow", "Select path to load the private key"))
        self.lineEditPrivateKey.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Unzip"))
        self.pushButtonFolder_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#353535;\">Folder</span></p></body></html>"))
        self.pushButtonFolder_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Folder</p><p><br/></p></body></html>"))
        self.pushButtonLoadKey.setText(_translate("MainWindow", "Load key"))
        self.pushButtonSign.setText(_translate("MainWindow", "Sign"))
        self.label_3.setText(_translate("MainWindow", "Verify"))
        self.label_11.setText(_translate("MainWindow", "Select path to load digital signature"))
        self.lineEditDigitalSignatureVerify.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Signature"))
        self.pushButtonHash_2.setText(_translate("MainWindow", "Hash"))
        self.pushButtonShowHash_2.setText(_translate("MainWindow", "Show Hash"))
        self.label_13.setText(_translate("MainWindow", "Select path to load the public key"))
        self.lineEditPublicKey.setText(_translate("MainWindow", "C:/Users/bucka/Documents/GitHub/School/Simon/Kryptologie/Elektronicky_Podpis/folder/Unzip"))
        self.pushButtonLoadKey_2.setText(_translate("MainWindow", "Load key"))
        self.pushButtonVerify.setText(_translate("MainWindow", "Verify"))
