import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QLabel, QDial, QComboBox, QPushButton
from PyQt5.QtGui import QPixmap, QImage
import cv2

class Image(QWidget):
    def __init__(self,image_path):
        super().__init__()
        self.title = "Image Processing"
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 250
        self.thresh_type = "cv2.THRESH_BINARY"
        self.image_path = image_path
        self.image = cv2.imread(self.image_path)
        self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.dial1 = QDial(self)
        self.dial2 = QDial(self)
        self.im_label = QLabel(self)
        self.cb1 = QComboBox(self)
        self.cb2 = QComboBox(self)
        self.reset_button = QPushButton("Revert changes",self)
        self.updateImage(self.image_gray)
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.dial1.setMinimum(0)
        self.dial1.setMaximum(255)
        self.dial2.setMinimum(0)
        self.dial2.setMaximum(255)
        self.dial1.move(20,130)
        self.dial2.move(120,130)
        self.dial1.valueChanged.connect(self.dial1_changed)
        self.dial2.valueChanged.connect(self.dial2_changed)

        self.cb1.addItems(["BINARY", "BINARY_INV","TRUNC","TOZERO","TOZERO_INV"])
        self.cb1.activated[str].connect(self.combo1_selection)
        self.cb1.move(40,50)
        self.cb2.move(280,50)

        self.reset_button.move(280,170)
        self.reset_button.clicked.connect(self.revert_button_pressed)
        
        
        self.show()
    def thresh(self):
        _, temp = cv2.threshold(self.image_gray,self.dial1.value(),self.dial2.value(),eval(self.thresh_type))
        self.updateImage(temp)

    def updateImage(self,gray):
        cv2.imshow('image',gray)


    def dial1_changed(self):
        self.thresh()
    def dial2_changed(self):
        self.thresh()
    def combo1_selection(self,text):
        self.thresh_type = "cv2.THRESH_" + text
        self.thresh()

    def revert_button_pressed(self):
        cv2.imshow('image',self.image_gray)
        self.dial1.setValue(0)
        self.dial2.setValue(0)
        






if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    ex = Image(sys.argv[1])
    sys.exit(myapp.exec_())
