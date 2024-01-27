from PyQt5 import uic, QtWidgets
import sys
import ADFGVX as adf

class ADFGVXUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(ADFGVXUi,self).__init__()
        uic.loadUi("ADFGVX_UI.ui",self)
    
        
        #Defining inputs
        #self.lineEditPlainText.setText("UtokVPet")
        #self.lineEditKey.setText("Kolotoc")
        self.lineEditTableSeed.setText("Seed")
        
        #Getting inputs
        plainText = lambda: self.lineEditPlainText.text()
        key = lambda: self.lineEditKey.text()
        tableSeed = lambda: self.lineEditTableSeed.text()
        alphabet = lambda: adf.create_alphabet(table_size(self))
        s_alphabet = lambda: adf.alphabet_shuffle(alphabet(), tableSeed())
        table = lambda: adf.create_table(s_alphabet(), table_size(self))
         
         
        #Defining functions
        s_text = lambda: adf.sanitize_text(plainText(),alphabet(),table_size(self))
        s_text_lE = lambda: self.lineEditSanitizedText.setText(adf.list_to_str(s_text()))
        s_key = lambda: adf.sanitize_key(key())
        s_key_lE = lambda: self.lineEditSanitizedKey.setText(adf.list_to_str(s_key()))
        aitADFGVX = lambda: adf.all_indexes_to_ADFGVX(s_text(), table(), table_size(self))
        ttawk = lambda: adf.transposition_table_alphabeticly_with_key(aitADFGVX(),s_key())
        
        
        #Table
        fill_cipher_table(self, table())
        fill_tTable = lambda: fill_transposition_table(self, adf.transposition_table(aitADFGVX(),s_key()), s_key())
        fill_tTable_alphabetically = lambda: fill_transposition_table_alphabetically(self, ttawk(), s_key())
        
        
        # Defining buttons and line edits
        self.pushButtonRUN.clicked.connect(lambda: run())
        self.lineEditPlainText.textChanged.connect(lambda: run())
        self.lineEditKey.textChanged.connect(lambda: run())
        self.lineEditTableSeed.textChanged.connect(lambda: run())
        
        def encrypt():
            self.lineEditEncryptedText.setText(adf.space_based_on_ttawk(ttawk()))
        
        def decrypt():
            decrypted_text = adf.decrypt(adf.remove_spaces(self.lineEditEncryptedText.text()), key(), tableSeed(), table_size(self))
            self.lineEditDecryptedText.setText(adf.unfilter_spaces(adf.list_to_str(decrypted_text)))
            

        def run():
            if not check_error_key(self, key()) or key() == "":
                return
            check_error_key(self, key())
            if self.radioButtonEncrypt.isChecked():
                encrypt()
            elif self.radioButtonDecrypt.isChecked():
                if self.radioButton5x5.isChecked() and adf.check_for_not_ADFGX(adf.remove_spaces(self.lineEditEncryptedText.text())):
                    print(adf.check_for_not_ADFGX(adf.remove_spaces(self.lineEditEncryptedText.text())))
                    self.lineEditError.setText("Text can only contain letters A,D,F,G,X")
                    return
                elif self.radioButton6x6.isChecked() and adf.check_for_not_ADFGVX(adf.remove_spaces(self.lineEditEncryptedText.text())):
                    self.lineEditError.setText("Text can only contain letters A,D,F,G,V,X")
                    return
                elif len(adf.remove_spaces(self.lineEditEncryptedText.text())) % 2 != 0:
                    self.lineEditError.setText("Encrypted text lenght must be even")
                    return
                decrypt()
            s_text_lE()
            s_key_lE()
            fill_cipher_table(self, table())
            fill_tTable()
            fill_tTable_alphabetically()
        

         
def check_error_key(self, key):
    if len(key) < 5  :
        self.lineEditError.setText("Minumum key lenght is 5")
        return False
    else:
        self.lineEditError.setText("")
        return True


                
def table_size(self):
    if self.radioButton5x5.isChecked():
        return False
    elif self.radioButton6x6.isChecked():
        return True
    else:
        return True


def fill_cipher_table(self, table):
    headers = ["A","D","F","G","V","X"]
    if len(table) == 5:
        headers = ["A","D","F","G","X"]
        
    self.tableWidgetCipherTable.setRowCount(len(table))
    self.tableWidgetCipherTable.setColumnCount(len(table))
    self.tableWidgetCipherTable.setHorizontalHeaderLabels(headers)
    self.tableWidgetCipherTable.setVerticalHeaderLabels(headers)
    for i in range(len(table)):
        for j in range(len(table)):
            self.tableWidgetCipherTable.setItem(i,j,QtWidgets.QTableWidgetItem(table[i][j]))
        self.tableWidgetCipherTable.setRowHeight(i, 18)


def fill_transposition_table(self, table, key):
    self.tableWidgetTranspositionTable.setRowCount(len(table[0]))
    self.tableWidgetTranspositionTable.setColumnCount(len(table))
    self.tableWidgetTranspositionTable.setHorizontalHeaderLabels(key)

    for i in range(len(table)):
        for j in range(len(table[i])):
            self.tableWidgetTranspositionTable.setItem(j,i,QtWidgets.QTableWidgetItem(table[i][j]))
        self.tableWidgetTranspositionTable.setRowHeight(i, 18)
        

def fill_transposition_table_alphabetically(self, table, key):
    adf.sort_array(key)
    self.tableWidgetTranspositionTableAlphabetically.setRowCount(max(len(item) for item in table))
    self.tableWidgetTranspositionTableAlphabetically.setColumnCount(len(table))
    self.tableWidgetTranspositionTableAlphabetically.setHorizontalHeaderLabels(key)

    for i in range(len(table)):
        for j in range(len(table[i])):
            self.tableWidgetTranspositionTableAlphabetically.setItem(j,i,QtWidgets.QTableWidgetItem(table[i][j]))
        self.tableWidgetTranspositionTableAlphabetically.setRowHeight(i, 18)
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ADFGVXUi()
    window.show()
    sys.exit(app.exec_())