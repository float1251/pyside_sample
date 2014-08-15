import sys
from PySide.QtGui import *
from PySide.QtCore import *


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')

    def showDate(self, date):
        self.lbl.setText(date.toString())

app = QApplication(sys.argv)
widget = Example()
widget.show()
sys.exit(app.exec_())