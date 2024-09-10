# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
from ui_mainWindow import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self,x=0,y=0,w=640,h=480):
       super (MyWindow,self).__ini__()
       self.setGeometry(x,y,w,h)
       self.setWindowTitle("Yolo")
       self.initUi()
    def initUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setuphUi(self)
        num_butt:QPushButton = getattr(self.ui,"Push Me")
        num_butt.clicked.connect(self.onClick)
    @Slot()
    def onClick():
       print("Hello Sailor")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()

    app.setActiveWindow(win)
    win.show()

    sys.exit(app.exec())
