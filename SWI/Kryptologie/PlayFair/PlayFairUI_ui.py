# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\bucka\Desktop\VS code\Python\Kryptologie\PlayFairUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1052, 511)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(97, 170, 198, 255), stop:1 rgba(0, 0, 83, 255));")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.textEditOpenText = QtWidgets.QTextEdit(Dialog)
        self.textEditOpenText.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.413, y1:1, x2:0.432836, y2:0.04, stop:0 rgba(34, 21, 113, 255), stop:1 rgba(141, 224, 255, 255));\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(0, 0, 0);")
        self.textEditOpenText.setObjectName("textEditOpenText")
        self.verticalLayout_2.addWidget(self.textEditOpenText)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditKlicZasifrovat = QtWidgets.QLineEdit(Dialog)
        self.lineEditKlicZasifrovat.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(60, 148, 242, 255), stop:1 rgba(255, 255, 255, 255));\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(0, 0, 0);")
        self.lineEditKlicZasifrovat.setText("")
        self.lineEditKlicZasifrovat.setObjectName("lineEditKlicZasifrovat")
        self.horizontalLayout.addWidget(self.lineEditKlicZasifrovat)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btnZasifruj = QtWidgets.QPushButton(Dialog)
        self.btnZasifruj.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(90, 156, 255);\n"
"font:87 12pt \"Arial Black\";\n"
"color:rgb(139, 255, 248)\n"
"")
        self.btnZasifruj.setObjectName("btnZasifruj")
        self.verticalLayout.addWidget(self.btnZasifruj)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.textEditZasifrovanyText = QtWidgets.QTextEdit(Dialog)
        self.textEditZasifrovanyText.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.413, y1:1, x2:0.432836, y2:0.04, stop:0 rgba(34, 21, 113, 255), stop:1 rgba(141, 224, 255, 255));\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(0, 0, 0);")
        self.textEditZasifrovanyText.setObjectName("textEditZasifrovanyText")
        self.verticalLayout_4.addWidget(self.textEditZasifrovanyText)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.textEditZasifrovaneDvojice = QtWidgets.QTextEdit(Dialog)
        self.textEditZasifrovaneDvojice.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.413, y1:1, x2:0.432836, y2:0.04, stop:0 rgba(34, 21, 113, 255), stop:1 rgba(141, 224, 255, 255));\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(0, 0, 0);")
        self.textEditZasifrovaneDvojice.setObjectName("textEditZasifrovaneDvojice")
        self.verticalLayout_3.addWidget(self.textEditZasifrovaneDvojice)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButtonCZ = QtWidgets.QRadioButton(Dialog)
        self.radioButtonCZ.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(90, 156, 255);\n"
"font:87 12pt \"Arial Black\";\n"
"color:rgb(139, 255, 248)\n"
"")
        self.radioButtonCZ.setObjectName("radioButtonCZ")
        self.horizontalLayout_5.addWidget(self.radioButtonCZ)
        self.radioButtonEN = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEN.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(90, 156, 255);\n"
"font:87 12pt \"Arial Black\";\n"
"color:rgb(139, 255, 248)\n"
"")
        self.radioButtonEN.setObjectName("radioButtonEN")
        self.horizontalLayout_5.addWidget(self.radioButtonEN)
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem1)
        self.tableWidgetTabulka = QtWidgets.QTableWidget(Dialog)
        self.tableWidgetTabulka.setStyleSheet("background-color: rgb(85, 255, 255);\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(0, 0, 0);")
        self.tableWidgetTabulka.setObjectName("tableWidgetTabulka")
        self.tableWidgetTabulka.setColumnCount(0)
        self.tableWidgetTabulka.setRowCount(0)
        self.verticalLayout_13.addWidget(self.tableWidgetTabulka)
        self.pushButtonZobrazTabulku = QtWidgets.QPushButton(Dialog)
        self.pushButtonZobrazTabulku.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(90, 156, 255);\n"
"font:87 12pt \"Arial Black\";\n"
"color:rgb(139, 255, 248)\n"
"")
        self.pushButtonZobrazTabulku.setObjectName("pushButtonZobrazTabulku")
        self.verticalLayout_13.addWidget(self.pushButtonZobrazTabulku)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_14.addWidget(self.label_4)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_16.addWidget(self.label_12)
        self.textEditZasNaDesText = QtWidgets.QTextEdit(Dialog)
        self.textEditZasNaDesText.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.413, y1:1, x2:0.432836, y2:0.04, stop:0 rgba(34, 21, 113, 255), stop:1 rgba(141, 224, 255, 255));\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(0, 0, 0);")
        self.textEditZasNaDesText.setObjectName("textEditZasNaDesText")
        self.verticalLayout_16.addWidget(self.textEditZasNaDesText, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_15.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.lineEditKlicDesifrovat = QtWidgets.QLineEdit(Dialog)
        self.lineEditKlicDesifrovat.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(60, 148, 242, 255), stop:1 rgba(255, 255, 255, 255));\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(0, 0, 0);")
        self.lineEditKlicDesifrovat.setObjectName("lineEditKlicDesifrovat")
        self.horizontalLayout_4.addWidget(self.lineEditKlicDesifrovat)
        self.verticalLayout_17.addLayout(self.horizontalLayout_4)
        self.btnDesifruj = QtWidgets.QPushButton(Dialog)
        self.btnDesifruj.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(90, 156, 255);\n"
"font:87 12pt \"Arial Black\";\n"
"color:rgb(139, 255, 248)\n"
"")
        self.btnDesifruj.setObjectName("btnDesifruj")
        self.verticalLayout_17.addWidget(self.btnDesifruj)
        self.verticalLayout_15.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_18.addWidget(self.label_14)
        self.textEditDesifrovanyText = QtWidgets.QTextEdit(Dialog)
        self.textEditDesifrovanyText.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.413, y1:1, x2:0.432836, y2:0.04, stop:0 rgba(34, 21, 113, 255), stop:1 rgba(141, 224, 255, 255));\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(0, 0, 0);")
        self.textEditDesifrovanyText.setObjectName("textEditDesifrovanyText")
        self.verticalLayout_18.addWidget(self.textEditDesifrovanyText)
        self.verticalLayout_15.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_19.addWidget(self.label_15)
        self.textEditChyby = QtWidgets.QTextEdit(Dialog)
        self.textEditChyby.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.413, y1:1, x2:0.432836, y2:0.04, stop:0 rgba(34, 21, 113, 255), stop:1 rgba(141, 224, 255, 255));\n"
" font-family: \'Droid Sans\', sans-serif; font-size: 15px; font-weight: 500; line-height: 24px; color: rgb(255, 0, 0);")
        self.textEditChyby.setObjectName("textEditChyby")
        self.verticalLayout_19.addWidget(self.textEditChyby)
        self.verticalLayout_15.addLayout(self.verticalLayout_19)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PlaiFair"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#aaffff;\">Zašifrovat</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aaffff;\">Vložte text na zašifrovanie</span></p></body></html>"))
        self.textEditOpenText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans,sans-serif\'; font-size:15px; font-weight:496; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aaffff;\">Zadajte Kĺuč:</span></p></body></html>"))
        self.btnZasifruj.setText(_translate("Dialog", "Zašifruj"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aaffff;\">Zašifrovaný text:</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aaffff;\">Zašifrovaný text prevedený do dvojíc:</span></p></body></html>"))
        self.radioButtonCZ.setText(_translate("Dialog", "CZ"))
        self.radioButtonEN.setText(_translate("Dialog", "EN"))
        self.pushButtonZobrazTabulku.setText(_translate("Dialog", "Zobrazit Tabulku"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#aaffff;\">Dešifrovat</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aaffff;\">Vložte zašifrovaný text</span></p></body></html>"))
        self.textEditZasNaDesText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans,sans-serif\'; font-size:15px; font-weight:496; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aaffff;\">Zadajte Kĺuč:</span></p></body></html>"))
        self.btnDesifruj.setText(_translate("Dialog", "Dešifruj"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aaffff;\">Dešifrovaný text:</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aaffff;\">Detekce chyb:</span></p></body></html>"))