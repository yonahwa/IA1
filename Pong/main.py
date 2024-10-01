# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtCore import QTimer
from Game import Game

class Window(QWidget):
    def __init__(self,game):
        super().__init__()
        self.title = "PongPingPang"
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200

        self.init_ui()
        self.init_game(game)

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.show()

    def init_game(self,game):
        self.game = game
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)

    def pygame_loop(self):
        if self.game.loop():
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)
    app.exec()
    #...
    game.close()

