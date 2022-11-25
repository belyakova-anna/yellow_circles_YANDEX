import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow
import random


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Кружочки')
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
        self.screen_size = [700, 450]
        self.start = 0

    def paintEvent(self, event):
        if self.start:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            size = random.randint(0, self.screen_size[1])
            x = random.randint(0, self.screen_size[0] - size)
            y = random.randint(0, self.screen_size[1] - size)
            qp.drawEllipse(x, y, size, size)
            qp.end()

    def draw(self, qp):
        self.start = 1
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
