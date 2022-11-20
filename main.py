import sys
import random

from UI import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.draw = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
	
    def run(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if not self.draw:
            return None
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()
        self.draw = False

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randrange(255), random.randrange(255), random.randrange(255)))
        x, y = random.randrange(400), random.randrange(200)
        qp.drawEllipse(x, y, random.randrange(400 - x), random.randrange(200 - y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
