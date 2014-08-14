import sys
from PySide.QtGui import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Input", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.ie = QLineEdit(self)
        self.ie.move(130, 22)

        self.setWindowTitle("InputDialog")
        self.setGeometry(300, 300, 290, 150)

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "input dialog", "Enter your name")
        if ok:
            self.ie.setText(text)


app = QApplication(sys.argv)
widget = Example()
widget.show()
sys.exit(app.exec_())
