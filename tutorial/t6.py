import sys
from PySide.QtGui import *
from PySide.QtCore import *


class LCDRange(QWidget):
    def __init__(self, parent=None):
        super(LCDRange, self).__init__(parent)
        lcd = QLCDNumber(2)
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 99)
        slider.setValue(0)
        slider.valueChanged.connect(lcd.display)

        layout = QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        quit = QPushButton("Quit")
        quit.clicked.connect(QApplication.quit)

        grid = QGridLayout()
        layout = QVBoxLayout()
        layout.addWidget(quit)
        layout.addLayout(grid)
        self.setLayout(layout)
        for row in range(3):
            for column in range(3):
                grid.addWidget(LCDRange(), row, column)

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
