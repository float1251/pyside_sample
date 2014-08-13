import sys
from PySide.QtGui import *
from PySide.QtCore import *


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        quit = QPushButton("Quit")
        quit.clicked.connect(QApplication.quit)

        lcd = QLCDNumber(2)

        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 90)
        slider.setValue(0)

        slider.valueChanged.connect(lcd.display)

        layout = QVBoxLayout()
        layout.addWidget(quit)
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)


app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
