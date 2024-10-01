# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
from ui_mainwindow import Ui_MainWindow


class MyWindow(QMainWindow):
    result = 0;
    def __init__(self,x=0,y=0,w=281,h=121):
       super (MyWindow,self).__ini__()
       self.setGeometry(x,y,w,h)
       self.setWindowTitle("Calculatrice")
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


    sys.exit(app.exec())
