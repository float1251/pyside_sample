import sys
from PySide.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hBox = QHBoxLayout()
        hBox.addStretch(1)
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")

        hBox.addWidget(button1)
        hBox.addWidget(button2)

        # QMainWindowの場合、QWidgetにsetしてから出ないと表示されない
        widget = QWidget()
        widget.setLayout(hBox)
        self.setCentralWidget(widget)
        self.statusBar()

        button1.clicked.connect(self.onButtonClicked)
        button2.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage("{} was pressed".format(sender.text()))


app = QApplication(sys.argv)
window = Example()
window.show()
sys.exit(app.exec_())

