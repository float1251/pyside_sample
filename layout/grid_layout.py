import sys
from PySide.QtCore import *
from PySide.QtGui import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
                 '4', '5', '6', '*', '1', '2', '3', '-',
                 '0', '.', '=', '+']
        grid = QGridLayout()

        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3 ),
               (4, 0), (4, 1), (4, 2), (4, 3)]

        for i in names:
            button = QPushButton(i)
            if j == 2:
                grid.addWidget(QLabel(""), 0, 2)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1

        self.setLayout(grid)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Calculator')


app = QApplication(sys.argv)
widget = Example()
widget.show()
sys.exit(app.exec_())
