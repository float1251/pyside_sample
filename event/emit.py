import sys
from PySide.QtCore import *
from PySide.QtGui import *


class Communicate(QObject):
    closeApp = Signal()


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')

    def mousePressEvent(self, e):
        self.c.closeApp.emit()


app = QApplication(sys.argv)
window = Example()
window.show()
sys.exit(app.exec_())