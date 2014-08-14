import sys
from PySide.QtGui import *
from PySide.QtCore import *


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        ok = QPushButton("OK")
        cancel = QPushButton("Cancel")

        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(ok)
        hBox.addWidget(cancel)

        vBox = QVBoxLayout()
        vBox.addStretch(1)
        vBox.addLayout(hBox)

        self.setLayout(vBox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        # 常に前面に
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Example()
    widget.show()
    sys.exit(app.exec_())
