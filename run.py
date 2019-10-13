import cv2
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QLabel, QDial
from PyQt5.QtGui import QPixmap


class Image(QWidget):
    def __init__(self,image_path):
        super().__init__()
        self.title = "Image Processing"
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 680
        self.image_path = image_path
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.im = QPixmap(self.image_path).scaled(260,260)
        self.im_label = QLabel(self)
        self.im_label.setPixmap(self.im)
        self.im_label.move(120,40)

        self.dial1 = QDial(self)
        self.dial2 = QDial(self)
        self.dial1.setMinimum(0)
        self.dial1.setMaximum(255)
        self.dial2.setMinimum(0)
        self.dial2.setMaximum(255)
        self.dial1.move(20,420)
        self.dial2.move(120,420)
        
        self.show()



if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    ex = Image(sys.argv[1])
    sys.exit(myapp.exec_())
