from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from zipfile import ZipFile
from datetime import datetime

import hash_message as hm
import generate_keys as gk

import sys, os, glob


class Digital_Signature(QtWidgets.QMainWindow):
    def __init__(self):
        super(Digital_Signature,self).__init__()
        uic.loadUi("Digital_Signature.ui",self)
        
        self.setWindowTitle("Digital Signature")
        
        
        #Folder buttons
        self.pushButtonFolder.clicked.connect(lambda: self.select_folder(self.lineEditDigitalSignatureSign))
        self.pushButtonFolder_2.clicked.connect(lambda: self.select_folder(self.lineEditMessageSign))
        self.pushButtonFolder_3.clicked.connect(lambda: self.select_folder(self.lineEditPrivateKey))
        self.pushButtonFolder_4.clicked.connect(lambda: self.select_folder(self.lineEditSaveKeys))
        self.pushButtonFolder_5.clicked.connect(lambda: self.select_folder(self.lineEditSaveZip))
        self.pushButtonFolder_6.clicked.connect(lambda: self.select_folder(self.lineEditLoadZip))
        self.pushButtonFolder_7.clicked.connect(lambda: self.select_folder(self.lineEditSaveUnzip))
        self.pushButtonFolder_8.clicked.connect(lambda: self.select_folder(self.lineEditDigitalSignatureVerify))
        self.pushButtonFolder_10.clicked.connect(lambda: self.select_folder(self.lineEditPublicKey))
        
        
        #Info buttons
        self.pushButtonInfo.clicked.connect(lambda: self.get_info(self.lineEditDigitalSignatureSign.text(), ".sign"))
        self.pushButtonInfo_2.clicked.connect(lambda: self.get_info(self.lineEditMessageSign.text(), ".txt"))
        self.pushButtonInfo_3.clicked.connect(lambda: self.get_info(self.lineEditDigitalSignatureVerify.text(), ".sign"))
        
        
        #Generate keys
        self.pushButtonGenerateKeys.clicked.connect(lambda: self.gen_keys(self.lineEditSaveKeys.text()))
        
        
        #Zip keys
        self.pushButtonZip.clicked.connect(lambda: self.zip_keys(self.lineEditSaveZip.text()))
        
        
        #Unzip keys
        self.pushButtonUnzip.clicked.connect(lambda: self.unzip_keys(self.lineEditLoadZip.text(), self.lineEditSaveUnzip.text()))
        
        
        #Edit, Hash and sign
        self.pushButtonEditMessage.clicked.connect(lambda: os.startfile(self.find_file(self.lineEditMessageSign.text(), ".txt")))
        
        self.pushButtonHash.clicked.connect(lambda: self.create_hash(self.lineEditMessageSign.text(), self.lineEditDigitalSignatureSign.text()))
        
        self.pushButtonShowHash.clicked.connect(lambda: self.show_file(self.lineEditDigitalSignatureSign.text(), ".hash"))
        
        self.pushButtonLoadKey.clicked.connect(lambda: self.show_file(self.lineEditPrivateKey.text(), ".priv"))

        self.pushButtonSign.clicked.connect(lambda: self.sign(self.lineEditPrivateKey.text(), self.lineEditDigitalSignatureSign.text(), self.lineEditDigitalSignatureSign.text()))
        
        
        #Hash and verify
        self.pushButtonHash_2.clicked.connect(lambda: [self.unzip_files(self.lineEditDigitalSignatureVerify.text(), self.lineEditDigitalSignatureVerify.text(), "Signed.zip"),self.create_hash(self.lineEditDigitalSignatureVerify.text(), self.lineEditDigitalSignatureVerify.text(), ".sign", "Hash.hash")])
        
        self.pushButtonShowHash_2.clicked.connect(lambda: self.show_file(self.lineEditDigitalSignatureVerify.text(), ".hash"))

        self.pushButtonLoadKey_2.clicked.connect(lambda: self.show_file(self.lineEditPublicKey.text(), ".publ"))
        
        self.pushButtonVerify.clicked.connect(lambda: self.verify(self.lineEditPublicKey.text(), self.lineEditDigitalSignatureVerify.text()))

        #Color changing
        #1.bg_color, 2.text_color, 3.button_color, 4.button_hover_color, 5.button_pressed_color
        self.modes = [("255,255,255", "0,0,0", "255,255,255", "220,220,220", "150,150,150"),
                      ("0,0,0", "255,255,255", "0,0,0", "50,50,50", "100,100,100"),
                      ("50,50,50", "205,205,205", "50,50,50", "100,100,100", "150,150,150"),
                      ("87, 101, 116", "255,255,255", "87, 101, 116", "100,100,100", "150,150,150"),
                      ("136, 0, 21", "255,255,255", "136, 0, 21", "100,100,100", "150,150,150")]
        
        self.current_mode = 2

    def select_folder(self, lineEdit_to_fill, primary_folder=os.getcwd()):
        try:
            folder = QFileDialog.getExistingDirectory(self, "Select Folder", primary_folder, QFileDialog.ShowDirsOnly)
            if folder:
                lineEdit_to_fill.setText(folder)
        except Exception as e:
            QMessageBox.critical(self, "Error", "Error: " + str(e))
            return None


    def gen_keys(self, destination_folder="folder\Keys"):
        try:
            n, e, d = gk.generate_keys()
            if not os.path.exists("folder\Keys"):
                os.mkdir("folder\Keys")
            with open(destination_folder+"\Private_key.priv", "w") as file:
                file.write("RSA_SHA3-512 " + str(n))
                file.write("\n")
                file.write("RSA_SHA3-512 " + str(d))
            with open("folder\Keys\Public_key.publ", "w") as file:
                file.write("RSA_SHA3-512 " + str(n))
                file.write("\n")
                file.write("RSA_SHA3-512 " + str(e))
            QMessageBox.information(self, "Success", "Keys generated.")
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
      
      
    def find_file(self, directory, filename):
        try:
            pattern = os.path.join(directory, '**', '*' + filename)
            files = glob.glob(pattern, recursive=True)
            return files[0] if files else None
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
 
        
    def zip_keys(self, destination_folder):
        try:
            if not os.path.exists("folder\Keys"):
                os.mkdir("folder\Keys")
            private_key = self.find_file("folder\Keys", ".priv")
            public_key = self.find_file("folder\Keys", ".publ")
            if private_key is None or public_key is None:
                QMessageBox.critical(self, "Error", "Keys not found.")
                return None
            with ZipFile(destination_folder + "\Keys.zip", 'w') as zipf:
                zipf.write(private_key, arcname=os.path.basename(private_key))
                zipf.write(public_key, arcname=os.path.basename(public_key))
            self.remove_files("folder\Keys", ["Private_key.priv", "Public_key.publ"])
            QMessageBox.information(self, "Success", "Keys zipped.")
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None


    def unzip_keys(self, source_folder, destination_folder):
        try:
            if not os.path.exists("folder\Keys"):
                os.mkdir("folder\Keys")
            with ZipFile(source_folder + "\Keys.zip", 'r') as zipf:
                zipf.extractall(destination_folder)
            self.remove_files("folder\Zip", ["Keys.zip"])
            QMessageBox.information(self, "Success", "Keys unzipped.")
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None


    def load_key(self, source_folder, priv = True):
        try:
            if priv:
                key = self.find_file(source_folder, ".priv")
            else:
                key = self.find_file(source_folder, ".publ")
            if key is None:
                QMessageBox.critical(self, "Error", "Key not found.")
                return None
            with open(key, "r") as file:
                n = file.readline()
                e_d = file.readline()
            return n, e_d
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
        
        
    def create_hash(self, source_folder, destination_folder, message=".txt", hash_name="Hash.hash"):
        try:
            message = self.find_file(source_folder, message)
            message = hm.open_file(message)
            hash = hm.hash_function(message)
            with open(destination_folder + f"\{hash_name}", "w") as file:
                file.write("RSA_SHA3-512 " + hash)
            QMessageBox.information(self, "Success", "Hash created.")
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
        
    
    def show_file(self, directory, file):
        try:
            file = self.find_file(directory, file)
            with open(os.path.join(directory, file), "r") as f:
                QMessageBox.information(self, "Success", f.read())
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
        
        
    def get_info(self, directory, filename):
        try:
            file = self.find_file(directory, filename)
            if file is None:
                QMessageBox.critical(self, "Error", "File not found.")
                return None
            name = os.path.basename(file)
            path = os.path.dirname(file)
            size = os.path.getsize(file)
            file_type = os.path.splitext(file)[1]
            last_modified = os.path.getmtime(file)
            last_modified = datetime.fromtimestamp(last_modified).strftime("%d.%m.%Y %H:%M:%S")
            QMessageBox.information(self, "Success", f"Name: {name}\nPath: {path}\nSize: {size}\nType: {file_type}\nLast modified: {last_modified}")
            
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
        
    
    def zip_files(self, destination_folder, files, zip_name):
        try:
            with ZipFile(destination_folder + f"\{zip_name}", 'w') as zipf:
                for file in files:
                    zipf.write(file, arcname=os.path.basename(file))
            QMessageBox.information(self, "Success", "Files zipped.")
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
        
    
    def unzip_files(self, source_folder, destination_folder, zip_name):
        try:
            with ZipFile(source_folder + f"\{zip_name}", 'r') as zipf:
                zipf.extractall(destination_folder)
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
    
    
    def remove_files(self, directory, files):
        try:
            for file in files:
                os.remove(os.path.join(directory, file))
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
      
      
    def sign(self, key_path, hash_path, signature_path):
        try:
            key = self.load_key(key_path)
            if key is None:
                QMessageBox.critical(self, "Error", "Could not load key.")
                return None
            n, d = key
            if n[:2] == "\n":
                n = n[2:]
            n = n.replace("RSA_SHA3-512 ", "")
            d = d.replace("RSA_SHA3-512 ", "")
            hash_file = self.find_file(hash_path, ".hash")
            hash = hm.open_file(hash_file)
            signature = hm.encrypt(hash, n, d)
            with open(signature_path + "\Signature.sign", "w") as file:
                file.write("RSA_SHA3-512 " + signature)
            self.zip_files(signature_path, [self.find_file(signature_path, ".sign"), hash_file], "Signed.zip")
            self.remove_files(signature_path, ["Signature.sign", "Hash.hash"])
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Error: " + str(ex))
            return None
    
    
    def verify(self, key_path, signature_path):
        try:
            key = self.load_key(key_path, False)
            if key is None:
                QMessageBox.critical(self, "Error", "Could not load key.")
                return None
            n, e = key
            if n[:2] == "\n":
                n = n[2:]
            self.unzip_files(signature_path, signature_path, "Signed.zip")
            hash = self.find_file(signature_path, ".hash")
            hash = hm.open_file(hash)
            signature = self.find_file(signature_path, ".sign")
            signature = hm.open_file(signature)
            n = n.replace("RSA_SHA3-512 ", "")
            e = e.replace("RSA_SHA3-512 ", "")
            signature = signature.replace("RSA_SHA3-512 ", "")
            decrypted = hm.decrypt(signature, n, e)
            if decrypted == hash:
                QMessageBox.information(self, "Success", "Verified.")
            else:
                QMessageBox.critical(self, "Error", "Not verified.")
        except Exception as ex:
            QMessageBox.critical(self, "Error", "Verification failed\nError: " + str(ex))
            return None


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.toggleMode()


    def toggleMode(self):
        self.current_mode = (self.current_mode + 1) % len(self.modes)
        self.setMode(*self.modes[self.current_mode])


    def setMode(self, bg_color, text_color, button_color = None, button_hover_color = None, button_pressed_color = None):
        if button_color is None:
            button_color = bg_color
            button_hover_color = bg_color
            button_pressed_color = bg_color
        
        self.setStyleSheet(
            f"background-color: rgb({bg_color});"
            f"color: rgb({text_color});"
            """font:87 10pt "Arial Black";"""
        )
        
        button_stylesheet = (
            """QPushButton{
                background-color: rgb(""" + button_color + """);
                color: rgb(""" + text_color + """);
                font:87 10pt "Arial Black";}
                
                QPushButton:hover{
                background-color: rgb(""" + button_hover_color + """);
                color: rgb(""" + text_color + """);
                font:87 10pt "Arial Black";}
                
                QPushButton:pressed{
                background-color: rgb(""" + button_pressed_color + """);
                color: rgb(""" + text_color + """);
                font:87 10pt "Arial Black";}
            """
            )
        
        list_of_buttons = ("pushButtonHash", "pushButtonShowHash", "pushButtonLoadKey", "pushButtonSign", "pushButtonGenerateKeys", "pushButtonEditMessage",
                           "pushButtonZip", "pushButtonUnzip", "pushButtonHash_2", "pushButtonShowHash_2", "pushButtonLoadKey_2", "pushButtonVerify",)
        for button in list_of_buttons:
            getattr(self, button).setStyleSheet(button_stylesheet)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Digital_Signature()
    window.show()
    sys.exit(app.exec_())