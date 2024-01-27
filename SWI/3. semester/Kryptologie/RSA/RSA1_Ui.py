from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from unidecode import unidecode

import RSA1 as rsa1
import sys

class RSA1_Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(RSA1_Ui,self).__init__()
        uic.loadUi("RSA1Ui.ui",self)
        
        self.setWindowTitle("RSA")
        self.fillKeys(self.genKeys())
        
        self.modes = [("255,255,255", "0,0,0"), ("0,0,0", "255,255,255"), ("50,50,50", "205,205,205"), ("78, 65, 135", "255, 255, 255")]  # Define modes
        self.current_mode = 0  # Define current_mode before connecting the signal
    
        #Buttons
        self.pushButtonGenerateKeys.clicked.connect(lambda:self.fillKeys(self.genKeys()))
        
        self.pushButtonEncrypt.clicked.connect(lambda: [self.encrypt(), self.fillTable()])
        
        self.pushButtonDecrypt.clicked.connect(lambda: self.decrypt())
        
        self.textEditTextToEncrypt.textChanged.connect(lambda: [self.fillTable(), self.encrypt(), self.decrypt()])
        

    def genKeys(self):
        try:
            return (rsa1.generate_keys(int(self.lineEditLenghtOfPrimeNumber.text())))
        except Exception as e:
            QMessageBox.critical(self, "Error", "Invalid number.\nError: " + str(e))
            return None
    
    
    def fillKeys(self, keys):
        try: 
            self.lineEditP.setText(str(keys[0]))
            self.lineEditQ.setText(str(keys[1]))
            self.lineEditPhi.setText(str(keys[2]))
            self.lineEditN.setText(str(keys[3]))
            self.lineEditE.setText(str(keys[4]))
            self.lineEditD.setText(str(keys[5]))
            
            self.lineEditNEncrypt.setText(str(keys[3]))
            self.lineEditEEncrypt.setText(str(keys[4]))
            
            self.lineEditNDecrypt.setText(str(keys[3]))
            self.lineEditDDecrypt.setText(str(keys[5]))
        except:
            return None
        
        
    def encrypt(self):
        if rsa1.check_e(int(self.lineEditEEncrypt.text()), int(self.lineEditPhi.text())): 
            pass
        else:
            QMessageBox.critical(self, "Error", "Invalid public key.\n e is not coprime with phi.\n1 < e < phi(n) is not satisfied.") 
            return None
        try:
            try:
                tNUM4 = rsa1.tNUM4(unidecode(self.textEditTextToEncrypt.toPlainText()))
                tNUM4 = rsa1.list_to_string(tNUM4)
                self.textEditNumeralRepresentation.setPlainText(str(tNUM4))
                self.textEditNumeralRepresentation_2.setPlainText(str(tNUM4))

                tNUM4 = rsa1.string_to_list(tNUM4)
                encrypted = rsa1.encryptNUM(tNUM4, int(self.lineEditNEncrypt.text()), int(self.lineEditEEncrypt.text()))
                encrypted = rsa1.list_to_string(encrypted)
                self.textEditEncrypted.setPlainText(str(encrypted))
                self.textEditEncrypted_2.setPlainText(str(encrypted))
            except Exception as e:
                QMessageBox.critical(self, "Error", "Error: " + str(e))
        except:
            QMessageBox.critical(self, "Error", "Invalid message.")
            return None
        
        
    def decrypt(self):
        try:
            if rsa1.check_d(int(self.lineEditDDecrypt.text()),int(self.lineEditE.text()), int(self.lineEditPhi.text())):
                pass
            else:
                QMessageBox.critical(self, "Error", "Invalid private key.\n d is not inverse of e.\ne*d mod phi(n) = 1 is not satisfied.")
                return None
            try:
                try:
                    encrypted = rsa1.string_to_list(self.textEditEncrypted_2.toPlainText())
                    decrypted = rsa1.decryptFINAL(encrypted, int(self.lineEditNDecrypt.text()), int(self.lineEditDDecrypt.text()))
                    self.textEditDecrypted.setPlainText(str(decrypted))
                except:
                    QMessageBox.critical(self, "Error", "Invalid private key.")
                    return None
            except:
                QMessageBox.critical(self, "Error", "Invalid message.")
                return None
        except Exception as e:
                QMessageBox.critical(self, "Error", "Error: " + str(e))
        
    
    def fillTable(self):
        text = unidecode(self.textEditTextToEncrypt.toPlainText())
        rows = len(text) 
        self.tableWidget.setRowCount(rows)
        for i in range(rows):
            try:
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(text[i])))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(ord(text[i]))))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(bin(ord(text[i])))[2:].zfill(8)))
                if i%4 == 0:
                    self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(rsa1.list_to_string(rsa1.tNUM4(text[i:i+4]))))
            except Exception as e:
                QMessageBox.critical(self, "Error", "Error: " + str(e))
                pass
            
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.toggleMode()


    def toggleMode(self):
        bg, text = self.modes[self.current_mode]
        self.setMode(bg, text)
        self.current_mode = (self.current_mode + 1) % len(self.modes)

            
        
    
    def setMode(self, bg, text):

        self.setStyleSheet("""background-color: rgb(""" + bg + """); color: rgb(""" + text + """); font:87 12pt "Arial Black"; """)
        self.tableWidget.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        self.pushButtonGenerateKeys.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        self.pushButtonEncrypt.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        self.pushButtonDecrypt.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        
        self.textEditTextToEncrypt.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        self.textEditNumeralRepresentation.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        self.textEditEncrypted.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        self.textEditDecrypted.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        self.textEditNumeralRepresentation_2.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        self.textEditEncrypted_2.setStyleSheet("background-color: rgb(" + bg + "); color: rgb(" + text + ");")
        
        self.tableWidget.setStyleSheet("""
        QHeaderView::section {
            background-color: rgb(""" + bg + """);
            color: rgb(""" + text + """); 
            font-weight: bold;
        }
        QHeaderView::section:horizontal {
            height: 18px;
        }
        QHeaderView::section {
            padding: 4px;
        }
        QTableWidget{
            font:87 12pt "Arial Black";
        }
        """)
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RSA1_Ui()
    window.show()
    sys.exit(app.exec_())
