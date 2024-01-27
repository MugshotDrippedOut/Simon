from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap, QIntValidator
from PyQt5.QtWidgets import QMessageBox

import sys
import os
import Stegano as stg


class Stenago(QtWidgets.QMainWindow):
    def __init__(self):
        super(Stenago,self).__init__()
        uic.loadUi("SteganoUI.ui",self)
        
        
        if not os.path.exists("Images"):
            os.makedirs("Images")


        #List of Images
        self.fillList(self.listWidgetSelectImageInput)
        self.fillList(self.listWidgetSelectImageOutput)
        
        getName = lambda: self.lineEditInputName.setText(self.listWidgetSelectImageInput.currentItem().text().split(".")[0])
        self.listWidgetSelectImageInput.itemClicked.connect(lambda:[self.selectImage(self.labelImageInput, self.listWidgetSelectImageInput), getName()])
        self.listWidgetSelectImageOutput.itemClicked.connect(lambda:self.selectImage(self.labelImageOutput, self.listWidgetSelectImageOutput))
        
        #Image Info
        self.pushButtonShowInfoInput.clicked.connect(lambda:self.imageInfo(self.listWidgetSelectImageInput.currentItem()))
        self.pushButtonShowInfoOutput.clicked.connect(lambda:self.imageInfo(self.listWidgetSelectImageOutput.currentItem()))
        
        #Create new Image
        validator = QIntValidator(1,255)
        self.lineEditHeight.setValidator(validator)
        self.lineEditWidth.setValidator(validator)
        
        self.horizontalSliderRed.valueChanged.connect(lambda: self.changeLabelColor())
        self.horizontalSliderGreen.valueChanged.connect(lambda: self.changeLabelColor())
        self.horizontalSliderBlue.valueChanged.connect(lambda: self.changeLabelColor())

        self.pushButtonNewImage.clicked.connect(lambda:self.newImage(self.checkBoxRandomize.isChecked()))
        
        #Add Image
        self.pushButtonAddImage.clicked.connect(lambda:self.addImage())
        
        #Hide Text
        self.pushButtonInput.clicked.connect(lambda:self.hideText())
        
        #Get Text
        self.pushButtonOutput.clicked.connect(lambda:self.getText())
        
        
    def fillList(self,listWidget):
        listWidget.clear()
        image_names = os.listdir("Images")
        for images_name in image_names:
            listWidget.addItem(images_name)


    def selectImage(self, labelImage, listWidget):
        try:
            currentItem = listWidget.currentItem()
            if currentItem is None:
                QMessageBox.critical(self, "Error", "No image selected.")
                return

            pixmap = QPixmap("Images/" + currentItem.text())
            labelImage.setPixmap(pixmap)
            labelImage.setScaledContents(True)

            if pixmap.width() > 255 or pixmap.height() > 255:
                # If the image is larger than 255x255, make it scalable
                labelImage.setFixedSize(255, 255)
            else:
                # Otherwise, set the size of the QLabel according to the QPixmap size
                labelImage.setFixedSize(pixmap.width(), pixmap.height())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to select image: {e}")
        
        
    def hideText(self):
        name = self.lineEditInputName.text()
        currentItem = self.listWidgetSelectImageInput.currentItem()
        try:
            if currentItem is None:
                QMessageBox.critical(self, "Error", "No image selected.")
                return
            if self.textEditInput.toPlainText() == "":
                QMessageBox.critical(self, "Error", "No text to hide.")
                return
            if name == "":
                QMessageBox.critical(self, "Error", "No name for the output image.")
                return
            stg.hide_text_in_image("Images/"+self.listWidgetSelectImageInput.currentItem().text(), self.textEditInput.toPlainText(), name+".png")
            self.fillList(self.listWidgetSelectImageInput)
            self.fillList(self.listWidgetSelectImageOutput)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to hide text: {e}")
            return
        
    def getText(self):
        if self.listWidgetSelectImageOutput.currentItem() is None:
            QMessageBox.critical(self, "Error", "No image selected.")
            return
        try:
            text_from_image = stg.get_text_from_image("Images/"+self.listWidgetSelectImageOutput.currentItem().text())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to get text from image: {e}")
            return
        self.textEditOutput.setText(text_from_image)

    
    def changeLabelColor(self):
        red = str(self.horizontalSliderRed.value())
        green = str(self.horizontalSliderGreen.value())
        blue = str(self.horizontalSliderBlue.value())
        self.labelPreview.setStyleSheet("QLabel { background-color : rgb("+red+","+green+","+blue+"); }")
        self.labelPreview.setText("rgb("+red+","+green+","+blue+")")
        
    def newImage(self, randomise):
        if self.lineEditName.text() == "":
            QMessageBox.critical(self, "Error", "No name for the output image.")
            return
        try:
            width = int(self.lineEditWidth.text())
            height = int(self.lineEditHeight.text())
            if randomise==False:
                color = [self.horizontalSliderRed.value(), self.horizontalSliderGreen.value(), self.horizontalSliderBlue.value()]
                stg.generate_image(width, height, True, color, self.lineEditName.text()+".png")
            else:
                stg.generate_image(width, height, False, [0, 0, 0], self.lineEditName.text()+".png")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate image: {e}")
            return
        self.fillList(self.listWidgetSelectImageInput)
        self.fillList(self.listWidgetSelectImageOutput)
        
    def addImage(self):
        try:
            os.startfile("Images")
            self.fillList(self.listWidgetSelectImageInput)
            self.fillList(self.listWidgetSelectImageOutput)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open folder: {e}")
        
    def imageInfo(self, selectedImage):
        try:
            if selectedImage is None:
                QMessageBox.critical(self, "Error", "No image selected.")
                return
            image_info = stg.get_image_info("Images/"+selectedImage.text())
            infoToShow = f"""Width: {image_info[0]}\nHeight: {image_info[1]}\nNumber of Pixels: {image_info[2]}\nColor: {image_info[3]}\nSize: {image_info[4]} bytes\nPath: {image_info[5]}"""
            QMessageBox.information(self, f"Image {selectedImage.text()} Info", infoToShow)    
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to get image info: {e}")
            return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Stenago()
    window.show()
    sys.exit(app.exec_())
        