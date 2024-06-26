# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\bucka\Documents\GitHub\School\Simon\Kryptologie\Steganografie\SteganoUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 654)
        MainWindow.setStyleSheet("background-color: rgb(23, 202, 118);\n"
"font:87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelSelectImage = QtWidgets.QLabel(self.centralwidget)
        self.labelSelectImage.setObjectName("labelSelectImage")
        self.verticalLayout.addWidget(self.labelSelectImage)
        self.listWidgetSelectImageInput = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetSelectImageInput.setMinimumSize(QtCore.QSize(0, 105))
        self.listWidgetSelectImageInput.setObjectName("listWidgetSelectImageInput")
        self.verticalLayout.addWidget(self.listWidgetSelectImageInput)
        self.labelImageInput = QtWidgets.QLabel(self.centralwidget)
        self.labelImageInput.setEnabled(True)
        self.labelImageInput.setMinimumSize(QtCore.QSize(256, 256))
        self.labelImageInput.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.labelImageInput.setText("")
        self.labelImageInput.setScaledContents(True)
        self.labelImageInput.setObjectName("labelImageInput")
        self.verticalLayout.addWidget(self.labelImageInput)
        self.pushButtonShowInfoInput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShowInfoInput.setStyleSheet("QPushButton{\n"
"background-color: rgb(23, 202, 118);\n"
"font:87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(23, 232, 118);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 170, 0);}")
        self.pushButtonShowInfoInput.setObjectName("pushButtonShowInfoInput")
        self.verticalLayout.addWidget(self.pushButtonShowInfoInput)
        self.textEditInput = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditInput.setObjectName("textEditInput")
        self.verticalLayout.addWidget(self.textEditInput)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelInputName = QtWidgets.QLabel(self.centralwidget)
        self.labelInputName.setObjectName("labelInputName")
        self.horizontalLayout_5.addWidget(self.labelInputName)
        self.lineEditInputName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInputName.setObjectName("lineEditInputName")
        self.horizontalLayout_5.addWidget(self.lineEditInputName)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.pushButtonInput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInput.setStyleSheet("QPushButton{\n"
"background-color: rgb(23, 202, 118);\n"
"font:87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(23, 232, 118);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 170, 0);}")
        self.pushButtonInput.setObjectName("pushButtonInput")
        self.verticalLayout.addWidget(self.pushButtonInput)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(256, 0))
        self.widget.setStyleSheet("background-color: rgb(23, 232, 118);\n"
"font:87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelNewImage = QtWidgets.QLabel(self.widget)
        self.labelNewImage.setObjectName("labelNewImage")
        self.gridLayout_2.addWidget(self.labelNewImage, 0, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelNewImageHeight = QtWidgets.QLabel(self.widget)
        self.labelNewImageHeight.setObjectName("labelNewImageHeight")
        self.verticalLayout_3.addWidget(self.labelNewImageHeight)
        self.labelNewImageHeight_2 = QtWidgets.QLabel(self.widget)
        self.labelNewImageHeight_2.setObjectName("labelNewImageHeight_2")
        self.verticalLayout_3.addWidget(self.labelNewImageHeight_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEditHeight = QtWidgets.QLineEdit(self.widget)
        self.lineEditHeight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditHeight.setInputMask("")
        self.lineEditHeight.setMaxLength(3)
        self.lineEditHeight.setObjectName("lineEditHeight")
        self.verticalLayout_4.addWidget(self.lineEditHeight)
        self.lineEditWidth = QtWidgets.QLineEdit(self.widget)
        self.lineEditWidth.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditWidth.setInputMask("")
        self.lineEditWidth.setMaxLength(3)
        self.lineEditWidth.setObjectName("lineEditWidth")
        self.verticalLayout_4.addWidget(self.lineEditWidth)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelRed = QtWidgets.QLabel(self.widget)
        self.labelRed.setObjectName("labelRed")
        self.verticalLayout_5.addWidget(self.labelRed)
        self.labelGreen = QtWidgets.QLabel(self.widget)
        self.labelGreen.setObjectName("labelGreen")
        self.verticalLayout_5.addWidget(self.labelGreen)
        self.labelBlue = QtWidgets.QLabel(self.widget)
        self.labelBlue.setObjectName("labelBlue")
        self.verticalLayout_5.addWidget(self.labelBlue)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalSliderRed = QtWidgets.QSlider(self.widget)
        self.horizontalSliderRed.setMaximum(255)
        self.horizontalSliderRed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRed.setObjectName("horizontalSliderRed")
        self.verticalLayout_6.addWidget(self.horizontalSliderRed)
        self.horizontalSliderGreen = QtWidgets.QSlider(self.widget)
        self.horizontalSliderGreen.setMaximum(255)
        self.horizontalSliderGreen.setPageStep(10)
        self.horizontalSliderGreen.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderGreen.setInvertedAppearance(False)
        self.horizontalSliderGreen.setObjectName("horizontalSliderGreen")
        self.verticalLayout_6.addWidget(self.horizontalSliderGreen)
        self.horizontalSliderBlue = QtWidgets.QSlider(self.widget)
        self.horizontalSliderBlue.setMaximum(255)
        self.horizontalSliderBlue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBlue.setObjectName("horizontalSliderBlue")
        self.verticalLayout_6.addWidget(self.horizontalSliderBlue)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.labelPreview = QtWidgets.QLabel(self.widget)
        self.labelPreview.setStyleSheet("")
        self.labelPreview.setText("")
        self.labelPreview.setObjectName("labelPreview")
        self.verticalLayout_7.addWidget(self.labelPreview)
        self.checkBoxRandomize = QtWidgets.QCheckBox(self.widget)
        self.checkBoxRandomize.setObjectName("checkBoxRandomize")
        self.verticalLayout_7.addWidget(self.checkBoxRandomize)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelName = QtWidgets.QLabel(self.widget)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout_3.addWidget(self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(self.widget)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout_3.addWidget(self.lineEditName)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.pushButtonNewImage = QtWidgets.QPushButton(self.widget)
        self.pushButtonNewImage.setStyleSheet("QPushButton{\n"
"font:87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(23, 202, 118);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 170, 0);}")
        self.pushButtonNewImage.setObjectName("pushButtonNewImage")
        self.verticalLayout_8.addWidget(self.pushButtonNewImage)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 2, 0, 1, 1)
        self.pushButtonAddImage = QtWidgets.QPushButton(self.widget)
        self.pushButtonAddImage.setStyleSheet("QPushButton{\n"
"font:87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(23, 202, 118);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 170, 0);}")
        self.pushButtonAddImage.setObjectName("pushButtonAddImage")
        self.gridLayout_2.addWidget(self.pushButtonAddImage, 3, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelSelectImage_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelSelectImage_2.setObjectName("labelSelectImage_2")
        self.verticalLayout_2.addWidget(self.labelSelectImage_2)
        self.listWidgetSelectImageOutput = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetSelectImageOutput.setObjectName("listWidgetSelectImageOutput")
        self.verticalLayout_2.addWidget(self.listWidgetSelectImageOutput)
        self.labelImageOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelImageOutput.setMinimumSize(QtCore.QSize(256, 256))
        self.labelImageOutput.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.labelImageOutput.setText("")
        self.labelImageOutput.setScaledContents(True)
        self.labelImageOutput.setObjectName("labelImageOutput")
        self.verticalLayout_2.addWidget(self.labelImageOutput)
        self.pushButtonShowInfoOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShowInfoOutput.setStyleSheet("QPushButton{\n"
"background-color: rgb(23, 202, 118);\n"
"font:87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(23, 232, 118);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 170, 0);}")
        self.pushButtonShowInfoOutput.setObjectName("pushButtonShowInfoOutput")
        self.verticalLayout_2.addWidget(self.pushButtonShowInfoOutput)
        self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditOutput.setObjectName("textEditOutput")
        self.verticalLayout_2.addWidget(self.textEditOutput)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.pushButtonOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOutput.setStyleSheet("QPushButton{\n"
"background-color: rgb(23, 202, 118);\n"
"font:87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(23, 232, 118);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 170, 0);}")
        self.pushButtonOutput.setObjectName("pushButtonOutput")
        self.verticalLayout_2.addWidget(self.pushButtonOutput)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSelectImage.setText(_translate("MainWindow", "Select Image to put text into"))
        self.pushButtonShowInfoInput.setText(_translate("MainWindow", "Show Info"))
        self.labelInputName.setText(_translate("MainWindow", "Name"))
        self.pushButtonInput.setText(_translate("MainWindow", "Hide text"))
        self.labelNewImage.setText(_translate("MainWindow", "Create new image"))
        self.labelNewImageHeight.setText(_translate("MainWindow", "Height"))
        self.labelNewImageHeight_2.setText(_translate("MainWindow", "Width"))
        self.lineEditHeight.setText(_translate("MainWindow", "255"))
        self.lineEditWidth.setText(_translate("MainWindow", "255"))
        self.labelRed.setText(_translate("MainWindow", "Red"))
        self.labelGreen.setText(_translate("MainWindow", "Green"))
        self.labelBlue.setText(_translate("MainWindow", "Blue"))
        self.checkBoxRandomize.setText(_translate("MainWindow", "Randomize"))
        self.labelName.setText(_translate("MainWindow", "Name"))
        self.pushButtonNewImage.setText(_translate("MainWindow", "New Image"))
        self.pushButtonAddImage.setText(_translate("MainWindow", "Add Image"))
        self.labelSelectImage_2.setText(_translate("MainWindow", "Select Image to get text from"))
        self.pushButtonShowInfoOutput.setText(_translate("MainWindow", "Show Info"))
        self.pushButtonOutput.setText(_translate("MainWindow", "Get text"))
