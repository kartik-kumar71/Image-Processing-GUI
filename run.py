import cv2
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Image(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Image Processing"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 580
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()



if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    ex = Image()
    sys.exit(myapp.exec_())
