import sys
from PySide.QtGui import *
from PySide.QtCore import *


app = QApplication(sys.argv)
label = QLabel("Hello World")
label.show()

app.exec_()
sys.exit()
