import sys
from PySide.QtGui import *

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setFixedSize(200, 120)
        self.quit = QPushButton("Quit", self)
        self.quit.setGeometry(62, 40, 75, 30)
        self.quit.clicked.connect(QApplication.quit)

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())