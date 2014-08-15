import sys
from PySide.QtGui import *
from PySide.QtCore import *

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        cb = QCheckBox("Show Title", self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QtGui.QCheckBox')

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle("Checked")
        else:
            self.setWindowTitle("")

app = QApplication(sys.argv)
widget = Example()
widget.show()
sys.exit(app.exec_())