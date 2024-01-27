from PyQt5 import uic, QtWidgets
import sys
import PlayFair as pf

        
class PlayFairUi(QtWidgets.QDialog):
    def __init__(self):
        super(PlayFairUi,self).__init__()
        uic.loadUi("PlayFairUI.ui",self)
        
        self.radioButtonCZ.setChecked(True)
        
        
                
        set_text_to_lineEdit(self.lineEditKlicZasifrovat, "Ahoj")
        set_text_to_textEdit(self.textEditOpenText, "Ahoj, jak se máš? Povinný paradox je paradox, který není paradoxem.")      

        
        click_zasifruj = lambda: [(set_text_to_textEdit(self.textEditZasifrovaneDvojice,
                                                       str(pf.playfair_sifra(get_text_from_lineEdit(self.lineEditKlicZasifrovat),
                                                                             pf.filtrovani_textu(get_text_from_textEdit(self.textEditOpenText),
                                                                                                 self.get_language()),True, self.get_language())))),
                                 set_text_to_textEdit(self.textEditZasifrovanyText, 
                                                      pf.rozdelit_po_piatich_znakoch(pf.premenit_dvojice_na_text(pf.playfair_sifra(get_text_from_lineEdit(self.lineEditKlicZasifrovat ),
                                                                                                                                   pf.filtrovani_textu(get_text_from_textEdit(self.textEditOpenText),
                                                                                                                                                       self.get_language()),True,self.get_language()),self.get_language()))),
                                 set_text_to_lineEdit(self.lineEditKlicDesifrovat, get_text_from_lineEdit(self.lineEditKlicZasifrovat)),
                                 set_text_to_textEdit(self.textEditZasNaDesText, get_text_from_textEdit(self.textEditZasifrovanyText))]
        
        click_desifruj = lambda: [(set_text_to_textEdit(self.textEditDesifrovanyText,
                                                       pf.premenit_dvojice_na_text(pf.playfair_sifra_desifrovat(get_text_from_lineEdit(self.lineEditKlicDesifrovat),
                                                                                                                pf.zjednotit_text(get_text_from_textEdit(self.textEditZasNaDesText)),self.get_language()),self.get_language())))]
        

        
        fill_tabulka = lambda:fill_table(self, pf.zmen_na_tabulku_5x5(pf.abeceda_plus_klic(pf.vytvorenie_abecedy(self.get_language()),pf.odstraneni_duplikatu_z_klice(get_text_from_lineEdit(self.lineEditKlicZasifrovat)))))
        
        create_table(self)
        
        self.btnZasifruj.clicked.connect(lambda: detect_key_lenght(self.lineEditKlicZasifrovat, click_zasifruj))
        self.pushButtonZobrazTabulku.clicked.connect(fill_tabulka)
        self.btnDesifruj.clicked.connect(lambda: detect_key_lenght(self.lineEditKlicDesifrovat, click_desifruj))
        self.show()
        
    
        def detect_key_lenght(widget, command):
            if len(widget.text()) < 3:
                set_text_to_textEdit(self.textEditChyby, "Klíč musí mít alespoň 3 znaky")
                return 
            if len(widget.text()) > 2:
                set_text_to_textEdit(self.textEditChyby, "")
                command()
        
    def get_language(self):
        if self.radioButtonCZ.isChecked():
            return "CZ"
        elif self.radioButtonEN.isChecked():
            return "EN"
        else:
            return "CZ"
        

def create_table(self):
    self.tableWidgetTabulka.setColumnCount(5)
    self.tableWidgetTabulka.setRowCount(5)
    for i in range(5):
        self.tableWidgetTabulka.setColumnWidth(i, 5)
        self.tableWidgetTabulka.setRowHeight(i, 5)


def fill_table(self, teble):
    for i in range(5):
        for j in range(5):
            self.tableWidgetTabulka.setItem(i, j, QtWidgets.QTableWidgetItem(teble[i][j]))

def get_text_from_textEdit(widget):
    return widget.toPlainText()

def set_text_to_textEdit(widget, new_text):
    widget.setPlainText(new_text)
    
def get_text_from_lineEdit(widget):
    return widget.text()

def set_text_to_lineEdit(widget, new_text):
    widget.setText(new_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = PlayFairUi()
    sys.exit(app.exec_())