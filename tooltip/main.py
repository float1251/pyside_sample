import sys
from PySide.QtGui import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 10))

        self.setToolTip("This is a <b>QWidget</b> Widget")

        btn = QPushButton("Button", self)
        btn.clicked.connect(QApplication.quit)
        btn.setToolTip("This is a <b>QPushButton</b> Widget")
        btn.resize(150, 50)
        btn.move(50, 50)

        self.setWindowTitle("Tooltip")
        self.setGeometry(300, 300, 250, 150)

app = QApplication(sys.argv)
widget = Example()
widget.show()
sys.exit(app.exec_())
