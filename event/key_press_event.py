import sys
from PySide.QtGui import *
from PySide.QtCore import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.resize(100, 100)
        self.setWindowTitle("KeyPressEvent")

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

app = QApplication(sys.argv)
widget = Example()
widget.show()
sys.exit(app.exec_())
