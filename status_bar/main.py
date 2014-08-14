import sys
from PySide.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')


app = QApplication(sys.argv)
window = Example()
window.show()
sys.exit(app.exec_())
