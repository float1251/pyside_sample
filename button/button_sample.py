
import sys
from PySide.QtGui import *

def say_hello():
    print("Hello World")

app = QApplication(sys.argv)
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()

app.exec_()
sys.exit()
